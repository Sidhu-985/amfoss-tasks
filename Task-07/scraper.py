import click
import requests
from bs4 import BeautifulSoup
import hashlib
import os

@click.command()
@click.argument('mp4_file', type=click.Path(exists=True))
@click.option('-l', '--language', default='eng', help='Filter subtitles by language (e.g., eng for English).')
@click.option('-o', '--output', default='./subtitles', help='Specify the output folder for the subtitles.')
@click.option('-s', '--file-size', type=int, help='Filter subtitles by movie file size in bytes.')
@click.option('-h', '--match-by-hash', is_flag=True, help='Match subtitles by movie hash.')
@click.option('-b', '--batch-download', is_flag=True, help='Enable batch mode to process all movies in a directory.')
def pirate_subtitles(mp4_file, language, output, file_size, match_by_hash, batch_download):
    """CLI app to fetch subtitles for a given MP4 file."""
    if batch_download:
        process_directory(mp4_file, language, output, file_size, match_by_hash)
    else:
        process_single_file(mp4_file, language, output, file_size, match_by_hash)

def process_single_file(mp4_file, language, output, file_size, match_by_hash):

    movie_hash = calculate_opensubtitles_hash(mp4_file) if match_by_hash else None
    size = os.path.getsize(mp4_file) if not file_size else file_size

    subtitles = scrape_subtitles(imdb_id, movie_hash, size, language)
    
    if subtitles:
        click.echo('Available subtitles:')
        for idx, subtitle in enumerate(subtitles):
            click.echo(f"{idx + 1}. {subtitle['name']} - Downloads: {subtitle['downloads']}")
        choice = click.prompt('Choose a subtitle to download', type=int, default=1)
        if 1 <= choice <= len(subtitles):
            download_subtitle(subtitles[choice - 1], output)
        else:
            click.echo('Invalid choice.')
    else:
        click.echo('No subtitles found.')

def process_directory(directory, language, output, file_size, match_by_hash):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.mp4'):
                click.echo(f"Processing file: {file}")
                process_single_file(os.path.join(root, file), language, output, file_size, match_by_hash)

def calculate_opensubtitles_hash(file_path):
    longlongformat = 'Q'  
    bytesize = struct.calcsize(longlongformat)
    filesize = os.path.getsize(file_path)
    hash = filesize

    with open(file_path, "rb") as f:
        if filesize < 65536 * 2:
            raise ValueError("File size too small for hash calculation")

        for x in range(65536 // bytesize):
            buffer = f.read(bytesize)
            (l_value,) = struct.unpack(longlongformat, buffer)
            hash += l_value
            hash = hash & 0xFFFFFFFFFFFFFFFF

        f.seek(max(0, filesize - 65536), 0)
        for x in range(65536 // bytesize):
            buffer = f.read(bytesize)
            (l_value,) = struct.unpack(longlongformat, buffer)
            hash += l_value
            hash = hash & 0xFFFFFFFFFFFFFFFF

    return "%016x" % hash

def scrape_subtitles(imdb_id, movie_hash, file_size, language):
    url = f"https://www.opensubtitles.org/en/search2/sublanguageid-{language}/imdbid-{imdb_id}"
    if movie_hash:
        url += f"/moviehash-{movie_hash}"
    if file_size:
        url += f"/moviesize-{file_size}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        subtitles = []
        for subtitle in soup.find_all('tr', class_='subtitle-row'):
            name = subtitle.find('a', class_='bnone').text.strip()
            downloads = int(subtitle.find('td', class_='text-muted').text.strip())
            download_url = subtitle.find('a', class_='bnone')['href']
            subtitles.append({'name': name, 'downloads': downloads, 'url': download_url})
        return subtitles
    except requests.RequestException as e:
        click.echo(f"Error fetching subtitles: {e}")
        return []

def download_subtitle(subtitle, output_dir):
    subtitle_url = f"https://www.opensubtitles.org{subtitle['url']}"
    try:
        response = requests.get(subtitle_url)
        response.raise_for_status()

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        subtitle_file = os.path.join(output_dir, f"{subtitle['name']}.srt")
        with open(subtitle_file, 'wb') as f:
            f.write(response.content)
        
        click.echo(f"Subtitle downloaded to {subtitle_file}")
    except requests.RequestException as e:
        click.echo(f"Error downloading subtitle: {e}")

if __name__ == '__main__':
    pirate_subtitles()

import requests
from bs4 import BeautifulSoup

def get_live_scores():
    res = requests.get('https://www.espncricinfo.com/live-cricket-score')

    if res.status_code == 200:
        soup = BeautifulSoup(res.text, 'html.parser')
        
        match_statuses = soup.find_all(class_='ds-text-tight-s ds-font-regular ds-truncate ds-text-typo')
        teams = soup.find_all(class_='ci-team-score ds-flex ds-justify-between ds-items-center ds-text-typo ds-my-1')
        
        if len(teams) > 0:
            team_1 = teams[0].get_text(strip=True)
            team_2 = teams[1].get_text(strip=True)
            match_status = match_statuses[0].get_text(strip=True)
            
            return team_1, team_2, match_status

    print("Error: Unable to fetch data {}.".format(res.status_code))
    return None, None, None
team_1, team_2, match_status = get_live_scores()
print(team_1, team_2, match_status)


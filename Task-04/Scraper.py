import requests
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
import csv

GOOGLE_BOOKS_API_KEY = "AIzaSyAqzlo7oiqxuteU3Tj2W7PjmQDV9pRouz8"

user_reading_list = {}

async def get_book(ctx: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = ctx.message.chat.id
    query = ' '.join(ctx.message.text.split()[1:])
    
    if not query:
        await ctx.message.reply_text("Please provide a search query.")
        return
    
    response = requests.get(f'https://www.googleapis.com/books/v1/volumes?q={query}&key={GOOGLE_BOOKS_API_KEY}')
    data = response.json()
    
    if response.status_code != 200:
        await ctx.message.reply_text("Failed to retrieve books. Please try again later.")
        return

    if 'items' not in data:
        await ctx.message.reply_text("No books found.")
        return

    with open("Book.csv", "w", newline='') as op:
        headers = ['Title', 'Authors', 'Description', 'Published Year']
        data1 = csv.DictWriter(op, delimiter=',', fieldnames=headers)
        data1.writeheader() 

        for i in range(min(6, len(data['items']))): 
            book = data['items'][i]['volumeInfo']
            title = book.get('title', 'No title')
            authors = ', '.join(book.get('authors', [])) if book.get('authors') else 'No authors'
            description = book.get('description', 'No description')
            year_published = book.get('publishedDate', 'No publishedDate')

            data1.writerow({
                'Title': title,
                'Authors': authors,
                'Description': description,
                'Published Year': year_published
            })

    with open('Book.csv', 'rb') as file:
        await context.bot.send_document(chat_id=chat_id, document=file)

async def get_preview(msg: Update, context: ContextTypes.DEFAULT_TYPE):
    query1 = ' '.join(msg.message.text.split()[1:])

    if not query1:
        await msg.message.reply_text("Please provide a search query.")
        return
    
    response = requests.get(f'https://www.googleapis.com/books/v1/volumes?q={query1}&key={GOOGLE_BOOKS_API_KEY}')
    data1 = response.json()

    book = data1['items'][0]['volumeInfo']
    info_link = book.get('infoLink', 'No link available')

    reply = f"**Link:** {info_link}"
    await msg.message.reply_text(reply)

async def add_book(ctx: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = ctx.message.chat_id
    book_title = context.user_data.get('pending_book')
    response = requests.get(f'https://www.googleapis.com/books/v1/volumes?q={book_title}&key={GOOGLE_BOOKS_API_KEY}')
    data = response.json()

    if not book_title:
        await ctx.message.reply_text("No book title was provided.")
        return
    
    book = data['items'][0]['volumeInfo']
    title = book.get('title','No title')

    if chat_id not in user_reading_list:
        user_reading_list[chat_id] = []
    
    elif title != book_title:
        await ctx.message.reply_text("The Book name is wrong")
        await ctx.message.reply_text(f"Did u mean {title}")

    elif title in user_reading_list[chat_id]:
        await ctx.message.reply_text(f"{title} is already added to your library")

    else:
        user_reading_list[chat_id].append(title)
        await ctx.message.reply_text(f"'{title}' has been added to your reading list.")

async def delete_book(ctx: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = ctx.message.chat_id
    book_title = context.user_data.get('pending_book')


    if not book_title:
        await ctx.message.reply_text("No book title was provided.")
        return

    if chat_id in user_reading_list and book_title in user_reading_list[chat_id]:
        user_reading_list[chat_id].remove(book_title)
        await ctx.message.reply_text(f"'{book_title}' has been removed from your reading list.")
    else:
        await ctx.message.reply_text(f"'{book_title}' is not in your reading list.")

async def view_list(ctx: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = ctx.message.chat_id
    books = user_reading_list.get(chat_id, [])

    if not books:
        await ctx.message.reply_text("Your reading list is empty.")
    else:
        book_list = "\n".join(books)
        await ctx.message.reply_text(f"Your reading list:\n{book_list}\n")

async def button_handler(ctx: Update, context: ContextTypes.DEFAULT_TYPE):
    query = ctx.callback_query
    await query.answer()

    if query.data == 'add_book':
        await add_book(query, context)
    elif query.data == 'delete_book':
        await delete_book(query, context)
    elif query.data == 'view_list':
        await view_list(query, context)

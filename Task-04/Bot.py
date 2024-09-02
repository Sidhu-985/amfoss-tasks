import datetime
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, ContextTypes, MessageHandler, CommandHandler, filters, CallbackQueryHandler
from Scraper import get_book, get_preview, add_book, button_handler

Token = "7466430293:AAH6pPZYS5d0bfEsBQ4MSKE3-eNBunCe9mE"
bot_username = "@dsfhv_bot"

async def start(msg: Update, context: ContextTypes.DEFAULT_TYPE):
    await msg.message.reply_text(f"Hello {msg.message.chat.username} and WELCOME TO MY BOOK KINGDOM!")

async def help(msg: Update, context: ContextTypes.DEFAULT_TYPE):
    await msg.message.reply_text(
        "Here are all the commands!\n"
        "/start - Receive Welcome message\n"
        "/book - To search books by its genre\n"
        "/preview - Previews the details of books\n"
        "/list - Add or delete a book from your library\n"
        "/reading_list - Displays buttons to manage your reading list"
    )

async def book(msg: Update, context: ContextTypes.DEFAULT_TYPE):
    await get_book(msg, context)

async def preview(msg: Update, context: ContextTypes.DEFAULT_TYPE):
    await get_preview(msg, context)

async def list(msg: Update, context: ContextTypes.DEFAULT_TYPE):
    book_title = ' '.join(msg.message.text.split()[1:])

    if not book_title:
        await msg.message.reply_text("Please provide the title of the book you want to add or delete along with /list.")
        return

    context.user_data['pending_book'] = book_title
    await msg.message.reply_text(
        f"You've entered: {book_title}\n"
        "Use /reading_list to manage your library."
    )

async def reading_list(msg: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("Add Book", callback_data='add_book'),
            InlineKeyboardButton("Delete Book", callback_data='delete_book'),
            InlineKeyboardButton("View Reading List", callback_data='view_list')
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await msg.message.reply_text("Choose an option:", reply_markup=reply_markup)

def handle_response(text: str) -> str:
    if 'hello' in text.lower():
        return "Hello there! Welcome to my store. How may I help you?"
    if 'how are you' in text.lower():
        return "I am fine!"
    if 'i want a book' in text.lower():
        return 'Sure! You can start by typing /help'
    return "I don't understand what u r saying just type /help to start"

async def handle_message(ctx: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = ctx.message.chat.type
    text: str = ctx.message.text

    print(f'User {ctx.message.chat.id} is logged in')

    if message_type == 'group':
        if bot_username in text:
            new_text: str = text.replace(bot_username, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    print('Bot: ', response)
    await ctx.message.reply_text(response)

if __name__ == '__main__':
    print("Starting bot")
    app = Application.builder().token(Token).build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('help', help))
    app.add_handler(CommandHandler('book', book))
    app.add_handler(CommandHandler('preview', preview))
    app.add_handler(CommandHandler('list', list))
    app.add_handler(CommandHandler('reading_list', reading_list))
    
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, add_book))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("Polling...")
    app.run_polling(poll_interval=3)

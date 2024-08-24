# 📝 Blog Burst 📝

## Task: Gopal and his PagePal

> # Introduction
> The task is about building a Telegram Book [Bot](https://core.telegram.org/bots) for our good old Pal Gopal.
> This Bot should have the ability to provide all the info about any book query provided by the user from [GOOGLE BOOKS API](https://developers.google.com/books/docs/v1/using).
> Whether it may be its title,description,Published Year,Price etc.

> # Technical Details
> - First I created a new bot and received its token from **BotFather**. Then I needed an API key which allows me to access all the books details from Googl Books.
> - After that I started to write the script in new virtual environment. I pip installed these commands below which are necessary to edit the bot script:
>   
>   ```
>   telegram bot
>   requests
>   ```
> - I started to create the commands which are required for the bot like /start,/help,/book input,/list input etc and other commands. This was somewhat hard especially for commands like book where I have to retrieve a list of books and its detail based on genre from Books JSON place and return it in the form of csv file. I tried to think of many ways to do this, but still managed to do so. And whats this is all about : | .
> - After creating all the commands I decided to create my own response handling as if the user is typing something else atleasts some response will occur from the bot' side. I managed the message handling and runned the bot using the Bot token. I referred these docs/videos below to complete it:
> - [Bot Demo](https://www.youtube.com/watch?v=vZtm1wuA2yc)
> - [Bot Features](https://core.telegram.org/bots/features)
> - Then after almost a week it was finally done.

> # My Thoughts and Experience
> I felt like this was a fatastic task. I really enjoyed doing this even if it took a sufficient amount of time. And that's what creating a program is about. At first you may feel like you can't do this at all and give up instantenously. But if you try your hardest then it will defenitely pay off in the end. And that's what I felt,
> Also I deployed my Bot and it can accessed officially.
> - Name: Book Bot
> - Username: @dsfhv_bot

> # Technical Difficulties
> Like I said ```when you are trying to up the mountain you may sometimes slip or fall off```. Similar situation I have faced many times during type casting.
> Every 

# lichessko

## Getting started

1. Create a `.env` file in the project root with your Telegram token:

   ```bash
   echo "TELEGRAM_BOT_TOKEN=xxxxxxxxxx" > .env
   ```

   The application reads this file automatically, so you no longer need the `poetry-dotenv-plugin`.

2. Install dependencies and run the bot:

   ```bash
   poetry install
   poetry run python -m bot.main
   ```

Environment variables defined outside the `.env` file always take precedence, so you can override the token without editing the file when deploying.

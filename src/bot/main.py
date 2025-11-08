import os
import logging

from telegram import Update
from telegram.ext import Application, ApplicationBuilder, CommandHandler, ContextTypes

from utils.env import load_env_file

logging.getLogger("httpx").setLevel(logging.WARNING)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)

def build_application() -> Application:
    token = os.getenv("TELEGRAM_TOKEN")
    if not token:
        raise RuntimeError(
            f"Missing Telegram Token; set it in your environment or .env file."
        )

    application = ApplicationBuilder().token(token).build()
    application.add_handler(CommandHandler("hello", hello))

    application.add_handler(CommandHandler("echo", echo))


    return application

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"Hello {update.effective_user.first_name}")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(update.message.text)

def main() -> None:
    load_env_file()
    build_application().run_polling()


if __name__ == "__main__":
    main()

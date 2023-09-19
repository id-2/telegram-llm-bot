import logging

from telegram import Update
from telegram.ext import ContextTypes

from telegram_smart_bots.bots.voice_journal.services.text import add_text
from telegram_smart_bots.shared.utils import async_typing

logger = logging.getLogger(__name__)


@async_typing
async def modify_text_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    msg_date = int(update.message.reply_to_message.text.split(":=")[0].strip())
    new_text = update.message.text.split(":=")[-1].strip()
    reply_msg = await add_text(user_id, msg_date, new_text)

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=reply_msg,
        reply_to_message_id=update.message.id,
    )


@async_typing
async def text_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_date = update.message.date
    forward_date = update.message.forward_date
    user_id = update.message.from_user.id
    msg_date = message_date if forward_date is None else forward_date
    msg_date = int(msg_date.timestamp())
    text = update.message.text

    reply_msg = await add_text(user_id, msg_date, text)

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=reply_msg,
        reply_to_message_id=update.message.id,
    )

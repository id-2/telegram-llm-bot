import datetime
import logging
import os

from langchain.schema import HumanMessage

from telegram_smart_bots.shared.history.history import MongoDBChatMessageHistory

logger = logging.getLogger(__name__)


async def add_location(
    user_id: int, msg_date: datetime.datetime, latitude: float, longitude: float
):
    try:
        loc_history = MongoDBChatMessageHistory(
            os.getenv("BOT_NAME"), user_id, str(msg_date.date())
        )

        await loc_history.add_message(
            HumanMessage(
                content=f"{latitude}, {longitude}",
                additional_kwargs={
                    "timestamp": int(msg_date.timestamp()),
                    "type": "location",
                },
            )
        )

        reply_msg = "😄"
    except Exception as ex:
        logger.error(ex)
        reply_msg = "😢"
    return reply_msg

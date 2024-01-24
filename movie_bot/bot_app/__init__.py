import logging
from .app import dp,bot,user_chat_router
from .command_list import private
from .user_group import user_group_router


logging.basicConfig(level=logging.INFO)
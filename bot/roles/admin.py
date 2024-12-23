import logging

from telegram import  Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.constants import ParseMode
from telegram.ext import CallbackContext

# Pre-assign menu text
FIRST_MENU_MARKUP = None
FIRST_MENU = "<b>Админ Панель</b>\n\nХуй"
SECOND_MENU = "<b>Menu 2</b>\n\nЗалупа"

# Pre-assign button text
NEXT_BUTTON = "Next"
BACK_BUTTON = "Back"
TUTORIAL_BUTTON = "Tutorial"

# Build keyboards
def build_menu_keyboard():
    buttons = []
    return InlineKeyboardMarkup(buttons)


class Admin:
    def __init__(self):
        pass

    async def menu(update: Update, context: CallbackContext) -> None:
        """
        This handler sends a menu with the inline buttons we pre-assigned above
        """
        # logging.getLogger(__name__).info(f'{update.message.from_user.id} use {update.message.text}')

        await context.bot.send_message(
            update.message.from_user.id,
            FIRST_MENU,
            parse_mode=ParseMode.HTML,
            reply_markup=FIRST_MENU_MARKUP
        )

    async def on_button_tap(update: Update, context: CallbackContext) -> None:
        """
        This handler processes the inline buttons on the menu
        """

        data = update.callback_query.data
        text = ''
        markup = None

        if data == NEXT_BUTTON:
            text = SECOND_MENU
            markup = SECOND_MENU_MARKUP
        elif data == BACK_BUTTON:
            text = FIRST_MENU
            markup = FIRST_MENU_MARKUP

        # Close the query to end the client-side loading animation
        await update.callback_query.answer()

        # Update message content with corresponding menu section
        await update.callback_query.edit_message_text(
            text,
            ParseMode.HTML,
            reply_markup=markup
        )

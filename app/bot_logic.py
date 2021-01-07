from telegram.ext import MessageHandler, Filters, InlineQueryHandler, CommandHandler, CallbackContext, Updater
from telegram import InlineQueryResultArticle, InlineQueryResultCachedGif, InputTextMessageContent, ParseMode, Update
from telegram.utils.helpers import escape_markdown
from app.crypto import render_crypto_results
from uuid import uuid4
import telegram
import logging
from config import auth

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s -%(message)s',level=logging.INFO
)

logger = logging.getLogger(__name__)

updater = Updater(token=auth['telegram_bot_token'], use_context=True)
dispatcher = updater.dispatcher

def inlinequery(update: Update, context: CallbackContext) -> None:

    query = update.inline_query.query

    if not query:
        return

    current_prices = render_crypto_results()

    results = [

        InlineQueryResultArticle(
            id=str(uuid4()),
            title="BTC",
            input_message_content=InputTextMessageContent(
                f"Current Price:\n_*BTC: ${current_prices['btc']}*_", parse_mode=ParseMode.MARKDOWN_V2
            ),
            thumb_url='https://pbs.twimg.com/profile_images/826820245134258176/XMOBC_oB_400x400.jpg',
            thumb_width=30,
            thumb_height=30

        ),

        InlineQueryResultArticle(
            id=str(uuid4()),
            title="ETH",
            input_message_content=InputTextMessageContent(
                f"Current Price:\n_*ETH: ${current_prices['eth']}*_", parse_mode=telegram.ParseMode.MARKDOWN_V2
            ),
            thumb_url='https://img.block123.com/nav/images/cea0d6c1-fefc-52fc-aca3-21c31fdd239b_2ReDnBD.jpg',
            thumb_width=30,
            thumb_height=30

        ),

        InlineQueryResultArticle(
            id=str(uuid4()),
            title="LTC",
            input_message_content=InputTextMessageContent(
                f"Current Price:\n_*LTC: ${current_prices['ltc']}*_", parse_mode=telegram.ParseMode.MARKDOWN_V2
            )
        ),

        InlineQueryResultArticle(
            id=str(uuid4()),
            title="UNI",
            input_message_content=InputTextMessageContent(
                f"Current Price:\n_*UNI: ${current_prices['uni']}*_", parse_mode=telegram.ParseMode.MARKDOWN_V2
            )
        ),

        InlineQueryResultArticle(
            id=str(uuid4()),
            title="COMP",
            input_message_content=InputTextMessageContent(
                f"Current Price:\n_*COMP: ${current_prices['comp']}*_", parse_mode=telegram.ParseMode.MARKDOWN_V2
            )
        ),
        InlineQueryResultArticle(
            id=str(uuid4()),
            title="NXM",
            input_message_content=InputTextMessageContent(
                f"Current Price:\n_*NXM: ${current_prices['nxm']}*_", parse_mode=telegram.ParseMode.MARKDOWN_V2
            )
        ),

        InlineQueryResultArticle(
            id=str(uuid4()),
            title="ATOM",
            input_message_content=InputTextMessageContent(
                f"Current Price:\n_*ATOM: ${current_prices['atom']}*_", parse_mode=telegram.ParseMode.MARKDOWN_V2
            )
        ),

        InlineQueryResultArticle(
            id=str(uuid4()),
            title="REN",
            input_message_content=InputTextMessageContent(
                f"Current Price:\n_*REN: ${current_prices['ren']}*_", parse_mode=telegram.ParseMode.MARKDOWN_V2
            ),
            thumb_url='https://64.media.tumblr.com/avatar_b4e09377302e_128.pnj',
            thumb_width=30,
            thumb_height=30
        ),

        InlineQueryResultArticle(
            id=str(uuid4()),
            title="MKR",
            input_message_content=InputTextMessageContent(
                f"Current Price:\n_*MKR: ${current_prices['mkr']}*_", parse_mode=telegram.ParseMode.MARKDOWN_V2
            )
        ),

        InlineQueryResultArticle(
            id=str(uuid4()),
            title="YFI",
            input_message_content=InputTextMessageContent(
                f"Current Price:\n_*YFI: ${current_prices['yfi']}*_", parse_mode=telegram.ParseMode.MARKDOWN_V2
            )
        ),

        InlineQueryResultArticle(
            id=str(uuid4()),
            title="AAVE",
            input_message_content=InputTextMessageContent(
                f"Current Price:\n_*AAVE: ${current_prices['aave']}*_", parse_mode=telegram.ParseMode.MARKDOWN_V2
            )
        ),

        InlineQueryResultArticle(
            id=str(uuid4()),
            title="SUSHI",
            input_message_content=InputTextMessageContent(
                f"Current Price:\n_*SUSHI: ${current_prices['sushi']}*_", parse_mode=telegram.ParseMode.MARKDOWN_V2
            ),
            thumb_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS671T5rBIRNGvv3C7g8FbR8aH9ccwGiMS3kQ&usqp=CAU',
            thumb_width=30,
            thumb_height=30
        ),

        InlineQueryResultArticle(
            id=str(uuid4()),
            title="XRP",
            input_message_content=InputTextMessageContent(
                f"Current Price:\n_*XRP: ${current_prices['xrp']}*_", parse_mode=telegram.ParseMode.MARKDOWN_V2
            )
        ),

        InlineQueryResultArticle(
            id=str(uuid4()),
            title="ADA",
            input_message_content=InputTextMessageContent(
                f"Current Price:\n_*ADA: ${current_prices['ada']}*_", parse_mode=telegram.ParseMode.MARKDOWN_V2
            )
        ),

    ]

    update.inline_query.answer(results)

dispatcher.add_handler(InlineQueryHandler(inlinequery))

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет, I'm Plutus, your personal crypto connoseiur")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="If you need help ask Ben!")

help_handler = CommandHandler('help', help)
dispatcher.add_handler(help_handler)

def stop_bot(update, context):

    context.bot.send_message(chat_id=update.effective_chat.id, text="Shutting Down! Прощай!")
    stopBot()

dispatcher.add_handler(CommandHandler('stopbot', stop_bot))

def btcPrice(update, context):

    current_prices = render_crypto_results()
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Current Price:\n_*BTC: ${current_prices['btc']}*_", parse_mode=telegram.ParseMode.MARKDOWN_V2)

btc_price_handler = CommandHandler('btc', btcPrice)
dispatcher.add_handler(btc_price_handler)

def ethPrice(update, context):

    current_prices = render_crypto_results()
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Current Price:\n_*ETH: ${current_prices['eth']}*_", parse_mode=telegram.ParseMode.MARKDOWN_V2)

eth_price_handler = CommandHandler('eth', ethPrice)
dispatcher.add_handler(eth_price_handler)

def usdtPrice(update, context):

    current_prices = render_crypto_results()
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Current Price:\n_*USDt: ${current_prices['usdt']}*_", parse_mode=telegram.ParseMode.MARKDOWN_V2)

usdt_price_handler = CommandHandler('tether', usdtPrice)
dispatcher.add_handler(usdt_price_handler)

def xrpPrice(update, context):

    current_prices = render_crypto_results()
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Current Price:\n_*XRP: ${current_prices['xrp']}*_", parse_mode=telegram.ParseMode.MARKDOWN_V2)

xrp_price_handler = CommandHandler('xrp', xrpPrice)
dispatcher.add_handler(xrp_price_handler)

def ltcPrice(update, context):

    current_prices = render_crypto_results()
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Current Price:\n_*LTC: ${current_prices['ltc']}*_", parse_mode=telegram.ParseMode.MARKDOWN_V2)

ltc_price_handler = CommandHandler('ltc', ltcPrice)
dispatcher.add_handler(ltc_price_handler)

def adaPrice(update, context):

    current_prices = render_crypto_results()
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Current Price:\n_*ADA: ${current_prices['ada']}*_", parse_mode=telegram.ParseMode.MARKDOWN_V2)

ada_price_handler = CommandHandler('ada', adaPrice)
dispatcher.add_handler(ada_price_handler)

def uniPrice(update, context):

    current_prices = render_crypto_results()
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Current Price:\n_*UNI: ${current_prices['uni']}*_", parse_mode=telegram.ParseMode.MARKDOWN_V2)

uni_price_handler = CommandHandler('uni', uniPrice)
dispatcher.add_handler(uni_price_handler)

def compPrice(update, context):

    current_prices = render_crypto_results()
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Current Price:\n_*COMP: ${current_prices['comp']}*_", parse_mode=telegram.ParseMode.MARKDOWN_V2)

comp_price_handler = CommandHandler('comp', compPrice)
dispatcher.add_handler(comp_price_handler)

def nxmPrice(update, context):

    current_prices = render_crypto_results()
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Current Price:\n_*NXM: ${current_prices['nxm']}*_", parse_mode=telegram.ParseMode.MARKDOWN_V2)

nxm_price_handler = CommandHandler('nxm', nxmPrice)
dispatcher.add_handler(nxm_price_handler)

def atomPrice(update, context):

    current_prices = render_crypto_results()
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Current Price:\n_*ATOM: ${current_prices['atom']}*_", parse_mode=telegram.ParseMode.MARKDOWN_V2)

atom_price_handler = CommandHandler('atom', atomPrice)
dispatcher.add_handler(atom_price_handler)

def renPrice(update, context):

    current_prices = render_crypto_results()
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Current Price:\n_*REN: ${current_prices['ren']}*_", parse_mode=telegram.ParseMode.MARKDOWN_V2)

ren_price_handler = CommandHandler('ren', renPrice)
dispatcher.add_handler(ren_price_handler)

def mkrPrice(update, context):

    current_prices = render_crypto_results()
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Current Price:\n_*MKR: ${current_prices['mkr']}*_", parse_mode=telegram.ParseMode.MARKDOWN_V2)

mkr_price_handler = CommandHandler('mkr', mkrPrice)
dispatcher.add_handler(mkr_price_handler)

def yfiPrice(update, context):

    current_prices = render_crypto_results()
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Current Price:\n_*YFI: ${current_prices['yfi']}*_", parse_mode=telegram.ParseMode.MARKDOWN_V2)

yfi_price_handler = CommandHandler('yfi', yfiPrice)
dispatcher.add_handler(yfi_price_handler)

def aavePrice(update, context):

    current_prices = render_crypto_results()
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Current Price:\n_*AAVE: ${current_prices['aave']}*_", parse_mode=telegram.ParseMode.MARKDOWN_V2)

aave_price_handler = CommandHandler('aave', aavePrice)
dispatcher.add_handler(aave_price_handler)

def sushiPrice(update, context):

    current_prices = render_crypto_results()
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Current Price:\n_*SUSHI: ${current_prices['sushi']}*_", parse_mode=telegram.ParseMode.MARKDOWN_V2)

sushi_price_handler = CommandHandler('sushi', sushiPrice)
dispatcher.add_handler(sushi_price_handler)

def allPrice(update, context):

    current_prices = render_crypto_results()
    template ="".join([f"\n_*{token.upper()}: ${current_prices[token]}*_" for token in current_prices.keys() if int(current_prices[token])!=0])
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"*Current Crypto Prices*:\n{template}", parse_mode=telegram.ParseMode.MARKDOWN_V2)

all_price_handler = CommandHandler('all', allPrice)
dispatcher.add_handler(all_price_handler)




def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I did not understand that command.")


unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)



def startBot():
    updater.start_polling()



def stopBot():
    updater.stop()

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

# تعریف دکمه‌ها و ویدیوها
VIDEOS = {
    "موضوع 1": "https://example.com/video1.mp4",
    "موضوع 2": "https://example.com/video2.mp4",
    "موضوع 3": "https://example.com/video3.mp4"
}

# تابع شروع
def start(update: Update, context):
    keyboard = [[InlineKeyboardButton(topic, callback_data=topic)] for topic in VIDEOS]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("موضوع موردنظر را انتخاب کنید:", reply_markup=reply_markup)

# هندلر دکمه‌ها
def button_handler(update: Update, context):
    query = update.callback_query
    query.answer()
    topic = query.data
    video_url = VIDEOS[topic]
    query.message.reply_text(f"ویدیو مربوط به {topic}:", disable_web_page_preview=True)
    query.message.reply_video(video=video_url)

# تنظیمات اصلی
def main():
    # توکن ربات
    TOKEN = "توکن شما"
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # افزودن هندلرها
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CallbackQueryHandler(button_handler))

    # اجرای ربات
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()

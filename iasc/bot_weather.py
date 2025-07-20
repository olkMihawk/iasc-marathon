import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

BOT_TOKEN = '7683840094:AAG9wTRrJ0LwAH_nofSofyl7JQp6qJQZm3w'
WEATHER_API_KEY = '79dc4b1d52f4b7c38a3a4231535c83b5'

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привіт! Напиши місто, і я скажу погоду ☀️")

# Функція для отримання погоди
def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric&lang=ua"
    res = requests.get(url).json()
    if res.get("cod") != 200:
        return "Місто не знайдено 😕"
    temp = res["main"]["temp"]
    desc = res["weather"][0]["description"]
    return f"У місті {city} зараз {desc}, температура {temp}°C"

# Обробка повідомлень
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    city = update.message.text
    result = get_weather(city)
    await update.message.reply_text(result)

# Запуск бота
app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.run_polling()

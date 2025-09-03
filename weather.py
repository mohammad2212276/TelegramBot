import telebot, requests
import os

bot_token = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(bot_token)

channel_id = os.environ.get("CHANNEL_ID")

api_key = os.environ.get("API_KEY")



provinces = {
    "تهران": (35.6892, 51.3890),
    "البرز": (35.8400, 50.9391),
    "اصفهان": (32.6539, 51.6660),
    "آذربایجان شرقی": (38.0667, 46.2993),
    "آذربایجان غربی": (37.5527, 45.0760),
    "اردبیل": (38.2498, 48.2933),
    "ایلام": (33.6374, 46.4227),
    "بوشهر": (28.9234, 50.8203),
    "چهارمحال و بختیاری": (32.3267, 50.8645),
    "خراسان جنوبی": (32.8663, 59.2211),
    "خراسان رضوی": (36.2972, 59.6067),
    "خراسان شمالی": (37.4718, 57.1011),
    "خوزستان": (31.3203, 48.6692),
    "زنجان": (36.6736, 48.4787),
    "سمنان": (35.5729, 53.3973),
    "سیستان و بلوچستان": (29.4963, 60.8629),
    "فارس": (29.5918, 52.5836),
    "قزوین": (36.2730, 50.0041),
    "قم": (34.6401, 50.8764),
    "کردستان": (35.3219, 46.9862),
    "کرمان": (30.2839, 57.0834),
    "کرمانشاه": (34.3142, 47.0650),
    "کهگیلویه و بویراحمد": (30.6680, 51.5876),
    "گلستان": (36.8416, 54.4438),
    "گیلان": (37.2808, 49.5832),
    "لرستان": (33.4667, 48.3569),
    "مازندران": (36.5659, 53.0586),
    "مرکزی": (34.0842, 49.6983),
    "هرمزگان": (27.1832, 56.2666),
    "همدان": (34.7992, 48.5146),
    "یزد": (31.8974, 54.3675)
}
for province, (lat, lon) in provinces.items():

    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric&lang=fa"
    response = requests.get(url)
    data = response.json()

    if "main" in data:
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        
        message += f"⛅ {province}: {temp}°C ({description})\n⛅ رطوبت: {humidity}%\n⛅ باد: {wind_speed} m/s\n\n"
    
    else:
        message += f"{province} NOT FOUND\n\n"
    


bot.send_message(channel_id, message)

bot.infinity_polling()

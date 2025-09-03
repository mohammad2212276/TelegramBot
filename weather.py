import telebot, requests
import os

bot_token = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(bot_token)

channel_id = os.environ.get("CHANNEL_ID")


provinces = {
	"Tehran": {"lat":35.6892, "lon":51.3890},
	"Alborz": {"lat":35.9400, "lon":50.9600},
	"Isfahan": {"lat":32.6546, "lon":51.6680},
	"Fars": {"lat":29.5918, "lon":52.5836},
	"Khorasan Razavi": {"lat":36.2969, "lon":59.6069},
	"Mazandaran": {"lat":36.5656, "lon":53.0589},
	"Gilan": {"lat":37.2800, "lon":49.5920},
	"Kerman": {"lat":30.2830, "lon":57.0834},
	"Hormozgan": {"lat":27.1830, "lon":56.2660},
	"Khuzestan": {"lat":31.3270, "lon":48.6940},
	"West Azarbaijan": {"lat":37.5560, "lon":45.0725},
	"East Azarbaijan": {"lat":38.0810, "lon":46.2919},
	"Lorestan": {"lat":33.4878, "lon":48.6940},
	"Markazi": {"lat":34.6401, "lon":50.8759},
	"Qazvin": {"lat":36.2688, "lon":50.0041},
	"Golestan": {"lat":36.8383, "lon":54.4439},
	"Ardabil": {"lat":38.2510, "lon":48.2970},
	"Yazd": {"lat":31.8974, "lon":54.3569},
	"Kohgiluyeh and Boyer-Ahmad": {"lat":30.8370, "lon":50.5800},
	"Sistan and Baluchestan": {"lat":29.4950, "lon":60.8720},
	"Kermanshah": {"lat":34.3142, "lon":47.0650},
	"Hamedan": {"lat":34.7986, "lon":48.5146},
	"Chaharmahal and Bakhtiari": {"lat":32.2476, "lon":50.8495},
	"Bushehr": {"lat":28.9234, "lon":50.8203},
	"Zanjan": {"lat":36.6746, "lon":48.4787},
	"Semnan": {"lat":35.5729, "lon":53.3965},
	"North Khorasan": {"lat":37.4713, "lon":57.3306},
	"South Khorasan": {"lat":32.8663, "lon":59.2211},
	"Qom": {"lat":34.6399, "lon":50.8759},
	"Ilam": {"lat":33.6373, "lon":46.4220},
	"Kurdistan": {"lat":35.3140, "lon":47.0610}
}

api_key = os.environ.get("API_KEY")


for province, coords in provinces.items():

	lat = ["lat"]
	lon = ["lon"]

	url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric&lang=fa"

	response = requests.get(url)

	if response.status_code == "200":
		data = response.json()
		temp = data['main']['temp']
		humidity = data['main']['humidity']
		desc = data['main'][0]['description']
		wind = data['wind']['speed']

		msg += f"⛅{province}:{temp}C\n⛅رطوبت:{humidity}%\n⛅هوا:{desc}\n⛅سرعت وزش باد:{wind}ms\n\n"
    else:
		msg += f"{province}:not Found\n\n"


bot.send_message(channel_id, msg)
bot.infinity_polling()

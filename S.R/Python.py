import eel
import pyowm

owm = pyowm.OWM('0be0de8b3dfcdecb0d25517208677e8d')


@eel.expose
def get_weather(place):
	observation = owm.weather_at_place(place)

	w = observation.get_weather()

	temp = w.get_temperature("celsius")["temp"]

	return "В городе " + place + " сейчас " + str(temp) + " градусов"

	




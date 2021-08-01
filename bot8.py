import telebot # importamos la libreria de telebot

# token = os.getenv['TOKEN']
bot = telebot.TeleBot('1746473976:AAEnVcmQzO-hZmaMrG1c-6Vqc1zG9Qo6Qxg') #anadimos el token
updates = bot.get_updates()
message = updates[0].message
from_user = message.from_user
id = from_user.id
get_me = bot.get_me()

@bot.message_handler(commands=['info','hola']) #definimos el comando
def hola(mensaje):
    bot.send_chat_action(id, 'typing')
    bot.send_message(id, "Envia 1 o Celsius par ver Formula Grados Celsius a Grados Kelvin \n Envia 2 o Kelvin  para ver Formula Grados Kelvin a Grados Celsius..")
    print("Mandaron info")

@bot.message_handler(commands=['1','Celsius']) 
def celsius(mensaje):
    bot.send_chat_action(id, 'typing')
    bot.send_message(id, "0 °C + 273.15 = 273.15 K")
    print("Mandaron 1")

@bot.message_handler(commands=['2','Kelvin'])
def kelvin(mensaje):
    bot.send_chat_action(id, 'typing')
    bot.send_message(id, "0 K − 273.15 = -273.1 °C")
    print("Mandaron 2")

bot.polling()
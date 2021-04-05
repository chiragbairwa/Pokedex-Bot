github
#
import pokebase as pb
from telegram.ext import *
import telegram
import json

API_KEY = "1694781352:AAF9iSKRof6Z6pO6YSHyM-JTG9lP0TcbssQ"

""" SEARCH """
def search(pokemon_text):
    with open('pokedex.json') as f:
        data = json.load(f)
        data = data['pokemon']
    """
    Output: "id": 1,
        "num": "001",
        "name": "Bulbasaur",
        "img": "http://www.serebii.net/pokemongo/pokemon/001.png",
        "type": [
          "Grass",
          "Poison"
        ],
        "height": "0.71 m",
        "weight": "6.9 kg",
        "candy": "Bulbasaur Candy",
        "candy_count": 25,
        "egg": "2 km",
        "spawn_chance": 0.69,
        "avg_spawns": 69,
        "spawn_time": "20:00",
        "multipliers": [1.58],
        "weaknesses": [
          "Fire",
          "Ice",
          "Flying",
          "Psychic"
        ],
        "next_evolution": [{
          "num": "002",
          "name": "Ivysaur"
        }, {
          "num": "003",
          "name": "Venusaur"
    """
    
    #Try searching with ID
    try:        
        for i in data:
            if i['id'] == int(pokemon_text):                
                return i
    
    #If Failed Searching with Name
    except:
        for i in data:
            if i['name'].lower() == (pokemon_text.lstrip(' ')):
                return i
               
    return 0

""" Responses """

def start_command(update, context):
    update.message.reply_text('Welcome')

def search_command(update, context):
    #update.message.reply_text('Search')
    #Receiving Pokemon Name
    search_text = str(update.message.text).lower()
    pokemon_text = search_text.lstrip("/search")
    
    #Checking ID or NAME
    result = search(pokemon_text) 
    send_message = f"#{result['id']} {result['name']}\nType: {result['type']}\nWeakness: {result['weaknesses']}"
    if result != 0:
        update.message.reply_text( result['img'] )
        update.message.reply_text( send_message )
    else:
        update.message.reply_text( 'Try Again')

def sample_response(input_text):
    user_msg = str(input_text).lower()

    if user_msg in ("hello"):
        return "Hey"

    return "Say that again"


""" Main """

print("BoT Started....")

def handler_message(update, context):
    #Receive
    text = str(update.message.text).lower()
    #Proccess
    response = sample_response(text)


    update.message.reply_text(response)

#def error(update,context):
#    print(f"UPdater {update} caused error {content.error}")

def main():
    updater = Updater(API_KEY, use_context = True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command) )
    dp.add_handler(CommandHandler("search", search_command) )

    dp.add_handler(MessageHandler(Filters.text, handler_message) )

    #dp.add_error_handler(error)
    
    updater.start_polling()
    updater.idle()


main()

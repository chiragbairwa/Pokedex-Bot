from telegram.ext import Updater , CommandHandler , MessageHandler , Filters
import json
""" API """

API = {}
with open('API.json','r') as f:
	data = json.load(f)

API_KEY = data['API_KEY']
"""
    Json Output: 
    {
    "abilities": [
      "Overgrow"
    ],
    "detailPageURL": "/us/pokedex/bulbasaur",
    "weight": 15.2,
    "weakness": [
      "Fire",
      "Flying",
      "Ice",
      "Psychic"
    ],
    "number": "001",
    "height": 28,
    "collectibles_slug": "bulbasaur",
    "featured": "true",
    "slug": "bulbasaur",
    "name": "Bulbasaur",
    "ThumbnailAltText": "Bulbasaur",
    "ThumbnailImage": "https://assets.pokemon.com/assets/cms2/img/pokedex/detail/001.png",
    "id": 1,
    "type": [
      "grass",
      "poison"
    ]
  },
"""

""" SEARCH """
def search(pokemon_text):
    with open('pokedex.json') as f:
        data = json.load(f)    
    
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

def handler_message(update, context):

	if str(update.message.text).lower() in ('hello' , 'hey', 'hi'):
		update.message.reply_text( 'Hey !!' )
	else:
		#Receiving Pokemon Name
		pokemon_text = str(update.message.text).lower()
		#Checking ID or NAME
		result = search(pokemon_text)
		if result == 0:
			update.message.reply_text('Try Again Pls')
		else:
			send_message = f"#{result['id']} {result['name']}\nType: {result['type']}\nHeight: {result['height']}\nWeight: {result['weight']}\nWeakness: {result['weakness']}\n{result['ThumbnailImage']}"
			update.message.reply_text(send_message)    


""" Main """

print("BoT Started....")

def main():
    updater = Updater(API_KEY, use_context = True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(MessageHandler(Filters.text, handler_message))

    #dp.add_error_handler(error)
    
    updater.start_polling()
    updater.idle()

main()

""" Error Handle 
def error(update,context):
    print(f"UPdater {update} caused error {content.error}")
"""

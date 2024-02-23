#!/usr/bin/env python3

# AwACAgIAAxkBAAO9ZbLQ9JPaoYMjZ1yKUaIeRiqucIAAAnw8AAKjFplJ_redyLP7r5s0BA - гс основа

import telebot
from telebot import types

# Замените 'YOUR_BOT_TOKEN' на токен вашего бота
API_TOKEN = '6502294895:AAHr4Uyv2t96a4ausDedNO8KxC7V-bWY_0I'

bot = telebot.TeleBot(API_TOKEN)
snippet = 'main.opus'

@bot.message_handler(commands=['start'])
def handle_start(message):
	# Создаем клавиатуру с inline-кнопкой "Войти в сеть"
	markup = types.InlineKeyboardMarkup()
	login_button = types.InlineKeyboardButton("в̤́͝ой͍̍ͅт̻̑͒и̡̬̅ в с͜етͣь̤̕", callback_data='login')
	markup.add(login_button)
	
	# Отправляем сообщение с клавиатурой
	bot.send_message(message.chat.id, "при̼ве͐т̷͒̔!͓ͣ \n\nдаͧвно н͑͒еͥ в̓̑и̲ͯд̼е̽͘л̣̔̑иͯсь̛,͍͙̋ п̪ог̞̗о̬в̱͔̕ори̛_с̆о̣ͩ мной͔ п̾̓ͪо̮ж͂̈́а͇͉ͬл̮у͠й͌̍ст̾̀а̨̹̹", reply_markup=markup)
	
#@bot.message_handler(content_types=['voice'])
#def handle_voice(message):
#	# Получаем объект голосового сообщения
#	voice = message.voice
#	
#	# Отправляем ID файла в ответ
#	bot.send_message(message.chat.id, f'ID файла голосового сообщения: {voice.file_id}')
#
#@bot.message_handler(content_types=['photo'])
#def get_photo_id(message):
#	# Проверяем, что в сообщении есть фото
#	photo = message.photo[-1]
#	bot.send_message(message.chat.id, f'ID файла: {photo.file_id}')
	
@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
	if call.data == 'login':
		markup = types.InlineKeyboardMarkup()
		message_button = types.InlineKeyboardButton("с͕͆͢оо̵̪̿б͘щ̲е̌н̈́͋̍и̟е", callback_data='message')
		markup.add(message_button)
		bot.edit_message_text("в̙̈ т͝в̇̎ӧ͠е̤м͚ п̡͌о̄ч̗т͔̲о̫͛в̡ͤом̦ я͙̈щ̉́ик̈̕е͍̑ *н̉о̪̘в̌ое̋ с̀о̵ͮоб̘щ͂̌е̃нͅӥ͡ё̩*\n\nп͠ͅр͎о͙слуͫ̌ш̯̀а͡й͝ е͡г̃́о", call.message.chat.id, call.message.message_id, reply_markup=markup, parse_mode='MarkdownV2')
		
	elif call.data == 'message':
		bot.answer_callback_query(call.id, "з̴̝͗..̷͕̏з̟̽.ͫ̎зз. з̭аг̾̑рͮузк̣̮а̞͔ͣ")
		try:
			markup2 = types.InlineKeyboardMarkup()
			reply_button = types.InlineKeyboardButton("о̞̟ͪт̺̈́в̳̐е̏т̿", callback_data='reply')
			markup2.add(reply_button)
			bot.send_voice(call.message.chat.id, voice='AwACAgIAAxkBAAO9ZbLQ9JPaoYMjZ1yKUaIeRiqucIAAAnw8AAKjFplJ_redyLP7r5s0BA', reply_markup=markup2)
		except telebot.apihelper.ApiException as e:
			if e.error_code == 400:
				bot.send_message(call.message.chat.id, "п̓ͩо͙̥ж̶͑алͭу̪͛й̫͍ст͙ͭа̗̥̋ в͖̝̅клю̗ч̋и ѓ̼̀оͤ̋л̔осͧо͚̩в̠̪ͧые͕̲ с͇ͦо̂оͤбͩ͐̀щ̴͋̊е̢͍͗н̧̝и͊̆̈я̟̬ͯ в̝̃ настр̺͑о̯̪й̎к̙̼͑а̙͢х̧͋̈́ п̗ͥ̏ри̫͋̃вͮ͋а̯̐͗т͉ͮͬн̓̎о̗͇ͨс͖т̴̦ͣи̦ ѝ͛ поͭпр̲̊о̉͢͟буͩ͘й͢ сͯн̃о̝в̤ͦа̲̔")
			else:
				bot.send_message(call.message.chat.id, "п̉͊р̏оͧ̐͝иͣз̮̏о̦шл̴̾͘а̮ оши̧бͥ̽̕к̲͑ͯа п͡р̣и о̠̑̚тп̛р̾̎ͭа̡в̻́кӗ̪̏ г͈̫о͈̿ло̪́с̫͟о̲ͩвог̫о соо̘͒бͨщ̶̱̦ен͖͂и̗я̾")
				# Выводим информацию об ошибке в консоль
				print(f"Error: {e}")    
	elif call.data == 'reply':
		bot.send_message(call.message.chat.id, 'л̾э͉̎и̖͔̪н̗̿ эͣ͘т̧ӧ̈ к̭̀то̛?ͅ')
		@bot.message_handler(func=lambda message: True)
		def handle_message(message):
			if message.text.lower() == "это я" or message.text.lower() == "я":
				bot.send_photo(message.chat.id, photo='AgACAgIAAxkBAAIC5WXNwf9tFQ5jVPnmGejEsaVqAAFp1AAC7N0xG689cEovhnPI_fOdUwEAAwIAA3gAAzQE')
			else:
				markup2 = types.InlineKeyboardMarkup()
				reply_button = types.InlineKeyboardButton("о̨̛т͚͍̎в̉ͅе̻͈т̩", callback_data='reply')
				markup2.add(reply_button)
				bot.send_message(message.chat.id, 'от̽в̢е̗т_ не͜в̯͂ернͫы̹̭̄й̼̄,͂ под͖ум͓ͣ͡а̦й̞̬ͧ е͚щ̛́ͤё̷͝ и̙͍̐ в̛̛о̢ͯз̩͙͑в͉ͪрͫащ͢а͍͙ͯй̸̨͋с̿яͨ̕,ͅͅ кͪ͘огд̍а̯̿̅ б͂͝уͤ̄ͣд̊̓͆еш̰̒̚ь̸͔ г̳̇ͦо͟тͤ͗͝о̋вͧ.̠̯̒..̠̓', reply_markup=markup2)
				
		
				
if __name__ == '__main__':
	bot.polling(none_stop=True)
	
	
	
	
	
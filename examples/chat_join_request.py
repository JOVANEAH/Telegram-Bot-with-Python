import telebot


bot = telebot.TeleBot('5459926076:AAGSREDwwBYPt8Gx4v3njA6dhnWnQoFgO_w')

@bot.chat_join_request_handler()
def make_some(message: telebot.types.ChatJoinRequest):
    bot.send_message(message.chat.id, 'I accepted a new user!')
    bot.approve_chat_join_request(message.chat.id, message.from_user.id)

bot.infinity_polling(allowed_updates=telebot.util.update_types)
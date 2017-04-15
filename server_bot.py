import telebot
import config as cfg


def get_response(message):
    return "Привет?"


bot = telebot.TeleBot(cfg.token)

'''

class WebhookServer(object):
    @cherrypy.expose
    def index(self):
        if 'content-length' in cherrypy.request.headers and \
                        'content-type' in cherrypy.request.headers and \
                        cherrypy.request.headers['content-type'] == 'application/json':
            length = int(cherrypy.request.headers['content-length'])
            json_string = cherrypy.request.body.read(length).decode("utf-8")
            update = telebot.types.Update.de_json(json_string)
            # Эта функция обеспечивает проверку входящего сообщения (скорее всего это так)
            bot.process_new_updates([update])
            return ''
        else:
            raise cherrypy.HTTPError(403)
'''


@bot.message_handler(content_types=['text'])
def respond(message):
    response = get_response(message)
    markup = 0
    if response.type == "get_confirmation":
        markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.add('Да', 'Нет')
    bot.send_message(message.chat.id, response.text, reply_markup=markup)

'''
bot.remove_webhook()

bot.set_webhook(url=cfg.WEBHOOK_URL_BASE + cfg.WEBHOOK_URL_PATH, certificate=open(cfg.WEBHOOK_SSL_CERT, 'r'))

cherrypy.config.update({
    'server.socket_host': cfg.WEBHOOK_LISTEN,
    'server.socket_port': cfg.WEBHOOK_PORT,
    'server.ssl_module': 'builtin',
    'server.ssl_certificate': cfg.WEBHOOK_SSL_CERT,
    'server.ssl_private_key': cfg.WEBHOOK_SSL_PRIV
})

cherrypy.quickstart(WebhookServer(), cfg.WEBHOOK_URL_PATH, {'/': {}})
'''

if __name__ == '__main__':
    bot.polling(none_stop=True)

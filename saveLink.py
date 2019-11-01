#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Este es un proyecto de prueba para un bot de telegram con la funcionalidad de guardar todos los
# links de un chat. Puede utilizarse en un grupo de Telegram.
# Este es un proyecto de aprendizaje para aprender sobre python.

# Modulos de telegram-python-bot
import telegram.ext
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Modulo para acceder al token
from tokenReader import access_token
# Modulo para manejar fecha y hora
from datetime import datetime
# Modulo para extraer links
from urlextract import URLExtract
# Modulo para el manejo de la base de datos
import sqlite3

# Logging del bot
TOKEN = access_token()
updater = Updater(token = TOKEN, use_context=True)

dispatcher = updater.dispatcher

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

# Funciones para comandos del bot
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
    text="Hola, estoy listo!")

def description(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Este bot es una prueba de contexto. Guardo todos los links de este chat')

# Las funciones pasan al manejador

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

description_handler = CommandHandler('descripcion', description)
dispatcher.add_handler(description_handler)

# Defino la funcion para captar el mensaje

def captar_mensaje(update, context):
    fecha = update.message.date.strftime("%d-%b-%Y (%H:%M:%S)")
    first_name = str(update.message.from_user.first_name)
    last_name = str(update.message.from_user.last_name)
    emisor = first_name + last_name
    mensaje = update.message.text
    vals = (fecha, emisor, mensaje)
    return vals


# Defino una funcion para pasar los links a start_polling

def link2string(l):
    w =  '**'.join(l)
    return w

# Defino la funcion para guardar los mensajes (creo que es mejor una funcion)
# y filtrar el link. Solo caso afirmativo debe guardarlo
extractor = URLExtract()

def guardar_mensaje(update,context):
    vals = captar_mensaje(update, context)
    men = vals[2]
    if extractor.has_urls(men):
        urls = extractor.find_urls(men)
        urls_string = link2string(urls)
        conn = sqlite3.connect('save_message_db.sqlite')
        cur = conn.cursor()
        stmt = 'insert into links (date, user, link) values (?, ?, ?)'
        vals2 = (vals[0],vals[1],urls_string)
        cur.execute(stmt, vals2)
        conn.commit()
        cur.close()
    else:
        pass


dispatcher.add_handler(MessageHandler(Filters.text, guardar_mensaje))
# Start the Bot

updater.start_polling()

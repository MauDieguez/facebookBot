# Facebook ChatBot Version 1.2 - Created by Mau:)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

import time


# Note: You need to train your ChatterRobot first:
# Go to line 61 and delete the (#)
# Once you trained for the first time, comment the block of code again (#)


class Bot:
    def __init__(self, email, password, name): # Constructor
        self.bot = driver.get("https://www.facebook.com/")
        self.email = email
        self.password = password
        self.name = name

    def login(self):  # Login in facebook
        email_login = driver.find_element_by_id("email")
        email_login.send_keys(self.email)
        email_password = driver.find_element_by_id("pass")
        email_password.send_keys(self.password)
        email_password.send_keys(Keys.RETURN)

    def buscar_persona(self):  # Search the given name of the person
        search = driver.find_element_by_class_name("_58al")
        search.send_keys(self.name)
        time.sleep(2)
        search_aux = driver.find_element_by_class_name("_58al")
        search_aux.send_keys(Keys.RETURN)

    def hablar_persona(self, dato):  # Send message
        chat = driver.find_element_by_class_name("_1p1t")
        chat.send_keys(dato + Keys.ENTER)

    def leerTexto(self):  # Read input
        texto = driver.find_elements_by_class_name("_5yl5")
        aux2 = texto[-1].text
        print(f"Input: {aux2}")
        return aux2



chatbot = ChatBot(
    "Robot"
)

# Read Data
Email = input()
Password = input()
Name = input()

# Main
driver = webdriver.Safari()  # Change this is you want to use it with Chrome, Firefox, etc.
driver.maximize_window()    # Note: You need to install drivers first!!!
bot = Bot(Email, Password, Name)  # Your email, password and name of the person you want to talk with

# Training
# trainer = ChatterCorpusTrainer(bot)
# trainer.train(
# "chatterbot.corpus.english"
# )


bot.login()
time.sleep(20)
bot.buscar_persona()
time.sleep(3)
bot.hablar_persona("Hi, I'm a robot")

size0 = driver.find_elements_by_class_name("_5yl5")
size_base = len(size0)

while True:
    size0 = driver.find_elements_by_class_name("_5yl5")
    size = len(size0)

    if size > size_base:
        Dato = bot.leerTexto()
        respuesta = chatbot.get_response(Dato)
        f = str(respuesta)
        print(f"Expected Output: {f}")
        bot.hablar_persona(f)
        size_base = size+1
    time.sleep(5)






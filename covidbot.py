import logging  
import os 

#from Adafruit_IO import Data 
#YOUR_AIO_USERNAME=os.getenv('YOUR_AIO_USERNAME') #ADAFRUIT_IO_USERNAME 
#YOUR_AIO_KEY = os.getenv('YOUR_AIO_KEY') #ADAFRUIT_IO_KEY
#from Adafruit_IO import Client, Feed
#aio = Client(YOUR_AIO_USERNAME,YOUR_AIO_KEY) 
  
#creating feed 
#new= Feed(name='covidfeed1')  
#result= aio.create_feed(new)    

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters 
 
def start(bot,update): 
 
    chat_id = bot.message.chat_id     
    bot.message.reply_text("HI, I'M COVID-19 BOT")
    bot.message.reply_text("type /covid_info to know about the virus")
    bot.message.reply_text("type /symptom to know about the symptoms")
   # bot.message.reply_text("type /check for temperature check")
    bot.message.reply_text("type /cases_statistics to know about the cases worlwide")
    bot.message.reply_text("type /precautions to know about the precationary measures")
    bot.message.reply_text("type /shopping to shop medical items")
    bot.message.reply_text("type /message to view message to the public")

def covid_info(bot,update):

    chat_id = bot.message.chat_id 
    bot.message.reply_text(text="COVID-19 is a disease caused by a new strain of coronavirus. CO stands for corona, VI for virus, and D for disease. Formerly, this disease was referred to as 2019 novel coronavirus or 2019-nCoV")
    update.bot.sendPhoto(chat_id=chat_id,photo='https://www.gavi.org/sites/default/files/thumbnail/cdc-w9KEokhajKw-unsplash_h2.jpg')

    bot.message.reply_text(text="type /covid_info to know about the virus")
    bot.message.reply_text(text="type /symptom to know about the symptoms")
   # bot.message.reply_text(text="type /check for temperature check")
    bot.message.reply_text(text="type /cases_statistics to know about the cases worlwide")
    bot.message.reply_text(text="type /precautions to know about the precationary measures")
    bot.message.reply_text(text="type /shopping to shop medical items")
    bot.message.reply_text(text="type /message to view message to the public")
    
def symptom(bot,update):

    chat_id = bot.message.chat_id
    bot.message.reply_text(text="Most common symptoms:\n1.fever\n2.dry cough\n3.tiredness\n")
    bot.message.reply_text(text="Less common symptoms:\n1.aches, pains\n2.sore throat\n3.diarrhoea\n4.conjunctivitis\n5.headache\n6.loss of taste/smell\n7.discolouration of fingers")
    bot.message.reply_text(text="If you come across any such above mentioned symptoms, please consult the doctor and get yourselves tested.")

    bot.message.reply_text(text="type /covid_info to know about the virus")
    bot.message.reply_text(text="type /symptom to know about the symptoms")
   # bot.message.reply_text(text="type /check for temperature check")
    bot.message.reply_text(text="type /cases_statistics to know about the cases worlwide")
    bot.message.reply_text(text="type /precautions to know about the precationary measures")
    bot.message.reply_text(text="type /shopping to shop medical items")
    bot.message.reply_text(text="type /message to view message to the public")
    

'''def check(bot,update): 

    chat_id = bot.message.chat_id
    bot.message.reply_text(text="What's your body temperature?")
    bot.message.reply_text(text="Select /normal_temp if temperature <= 98.6 degree Celsius") 
    bot.message.reply_text(text="Select /fever_temp if temperature >= 99 degree Celsius")

def normal_temp(bot,update): 

    value = Data(value=1)
    value_send = aio.create_data('covidfeed',value)
    chat_id = bot.message.chat_id
    bot.message.reply_text(text="Your body temperature is ideal, please eat healthy food")

    bot.message.reply_text(text="type /covid_info to know about the virus")
    bot.message.reply_text(text="type /symptom to know about the symptoms")
   # bot.message.reply_text(text="type /check for temperature check")
    bot.message.reply_text(text="type /cases_statistics to know about the cases worlwide")
    bot.message.reply_text(text="type /precautions to know about the precationary measures")
    bot.message.reply_text(text="type /shopping to shop medical items")
    bot.message.reply_text(text="type /message to view message to the public")
    

def fever_temp(bot,update):

    value = Data(value=0)
    value_send = aio.create_data('covidfeed',value)
    chat_id = bot.message.chat_id
    bot.message.reply_text(text="You are most likely to have fever, Please be cautious")

    bot.message.reply_text(text="type /covid_info to know about the virus")
    bot.message.reply_text(text="type /symptom to know about the symptoms")
    #bot.message.reply_text(text="type /check for temperature check")
    bot.message.reply_text(text="type /cases_statistics to know about the cases worlwide")
    bot.message.reply_text(text="type /precautions to know about the precationary measures")
    bot.message.reply_text(text="type /shopping to shop medical items")
    bot.message.reply_text(text="type /message to view message to the public")
'''
def cases_statistics(bot,update):
    
    chat_id = bot.message.chat_id
    bot.message.reply_text(text="Select the below link to view the statistics of Covid-19")
    bot.message.reply_text(text="https://covid19.who.int")

    bot.message.reply_text(text="type /covid_info to know about the virus")
    bot.message.reply_text(text="type /symptom to know about the symptoms")
    #bot.message.reply_text(text="type /check for temperature check")
    bot.message.reply_text(text="type /cases_statistics to know about the cases worlwide")
    bot.message.reply_text(text="type /precautions to know about the precationary measures")
    bot.message.reply_text(text="type /shopping to shop medical items")
    bot.message.reply_text(text="type /message to view message to the public")
    

def precautions(bot,update):
    
    chat_id = bot.message.chat_id
    update.bot.sendPhoto(chat_id=chat_id, photo="https://i.pinimg.com/originals/f3/98/37/f39837e2c85756f8b7a2bd39bd9c3024.jpg",caption="Please wear a mask while you step out!\n")
    bot.message.reply_text(text="To prevent the spread of COVID-19:\n*Clean your hands often\n Use soap and water, or an alcohol-based hand rub.\n*Maintain a safe distance from anyone who is coughing or sneezing.\n*Wear a mask when physical distancing is not possible.\n*Don’t touch your eyes, nose or mouth.\n*Cover your nose and mouth with your bent elbow or a tissue when you cough or sneeze.\n*Stay home when you feel unwell.\n*If you have a fever, cough and difficulty breathing, seek medical attention.")

    bot.message.reply_text(text="type /covid_info to know about the virus")
    bot.message.reply_text(text="type /symptom to know about the symptoms")
    #bot.message.reply_text(text="type /check for temperature check")
    bot.message.reply_text(text="type /cases_statistics to know about the cases worlwide")
    bot.message.reply_text(text="type /precautions to know about the precationary measures")
    bot.message.reply_text(text="type /shopping to shop medical items")
    bot.message.reply_text(text="type /message to view message to the public")
    
    
def shopping(bot,update): 

    chat_id = bot.message.chat_id
    bot.message.reply_text(text="You can shop for mask, gloves and sanitizers online")
    bot.message.reply_text("choose options below to shop them")
    bot.message.reply_text("type /mask to shop masks")
    bot.message.reply_text("type /sanitizer to shop sanitizer")
    bot.message.reply_text("type /gloves to shop gloves")

def mask(bot,update):

    chat_id = bot.message.chat_id
    update.bot.sendPhoto(chat_id=chat_id,photo="https://keepwomenhealthy.com/wp-content/uploads/2020/07/masks_ranked_1024.jpg")
    bot.message.reply_text("click below to shop")
    bot.message.reply_text(text="https://www.amazon.in/Masks-Respirators/b?ie=UTF8&node=8452605031")
    bot.message.reply_text("type /mask to shop masks")
    bot.message.reply_text("type /sanitizer to shop sanitizer")
    bot.message.reply_text("type /gloves to shop gloves")
    bot.message.reply_text(text="type /message to view message to the public")

def sanitizer(bot,update):

    chat_id = bot.message.chat_id
    update.bot.sendPhoto(chat_id=chat_id,photo="https://media1.fdncms.com/rochester/imager/u/original/11617421/sanitizer.jpg")
    bot.message.reply_text("click below to shop")
    bot.message.reply_text(text= "https://www.amazon.in/sanitizer/s?k=sanitizer")
    bot.message.reply_text("type /mask to shop masks")
    bot.message.reply_text("type /sanitizer to shop sanitizer")
    bot.message.reply_text("type /gloves to shop gloves")
    bot.message.reply_text(text="type /message to view message to the public")

def gloves(bot,update):

    chat_id = bot.message.chat_id
    update.bot.sendPhoto(chat_id=chat_id,photo="https://cdn.shopify.com/s/files/1/0971/2990/products/Screenshot_20200329-173805_AliExpress_large.jpg?v=1585481715")
    bot.message.reply_text("click below to shop")
    bot.message.reply_text(text= "https://www.amazon.in/hand-gloves/s?k=hand+gloves")
    bot.message.reply_text("type /mask to shop masks")
    bot.message.reply_text("type /sanitizer to shop sanitizer")
    bot.message.reply_text("type /gloves to shop gloves")
    bot.message.reply_text(text="type /message to view message to the public")

def message(bot,update):

    chat_id = bot.message.chat_id
    bot.message.reply_text(text= "The COVID-19 pandemic has demonstrated the interconnected nature of our world – and that no one is safe until everyone is safe. Only by acting in solidarity can communities save lives and overcome the devastating socio-economic impacts of the virus.")
    bot.message.reply_text(text= "STAY HOME STAY SAFE,\nDON'T STEP OUT IF NOT NECESSARY!")

def main(): #mainfunction

  BOT_TOKEN= os.getenv("BOT_TOKEN")
  u = Updater(BOT_TOKEN, use_context=True)
  dp = u.dispatcher
  dp.add_handler(CommandHandler('start',start))
  dp.add_handler(CommandHandler('covid_info',covid_info))
  dp.add_handler(CommandHandler('symptom',symptom))
  dp.add_handler(CommandHandler('cases_statistics',cases_statistics))
  dp.add_handler(CommandHandler('precautions',precautions))
  dp.add_handler(CommandHandler('shopping',shopping))
  dp.add_handler(CommandHandler('mask',mask))
  dp.add_handler(CommandHandler('sanitizer',sanitizer))
  dp.add_handler(CommandHandler('gloves',gloves))
  '''dp.add_handler(CommandHandler('check',check))
  dp.add_handler(CommandHandler('normal_temp',normal_temp))
  dp.add_handler(CommandHandler('fever_temp',fever_temp))'''
  dp.add_handler(CommandHandler('message',message))

  u.start_polling()
  u.idle()

if __name__ == '__main__':
    main()
  

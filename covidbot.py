import logging  
import os  

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters 
 
def start(bot,update): 
  
    chat_id = bot.message.chat_id     
    bot.message.reply_text("HI, I'M COVID BOT")
    bot.message.reply_text("type /covid_info to know about the virus and variants")
    bot.message.reply_text("type /symptom to know about the symptoms")
    bot.message.reply_text("type /cases_statistics to know about the cases worlwide")
    bot.message.reply_text("type /precautions to know about the precationary measures")
    bot.message.reply_text("type /mental_health to check upon your well being")
    bot.message.reply_text("type /shopping to shop medical items")
    bot.message.reply_text("type /message to view message to the public")

def covid_info(bot,update):

    chat_id = bot.message.chat_id 
    bot.message.reply_text(text="COVID-19 is a disease caused by a new strain of coronavirus. CO stands for corona, VI for virus, and D for disease. Formerly, this disease was referred to as 2019 novel coronavirus or 2019-nCoV")
    update.bot.sendPhoto(chat_id=chat_id,photo='https://www.gavi.org/sites/default/files/thumbnail/cdc-w9KEokhajKw-unsplash_h2.jpg')
    bot.message.reply_text(text="If you wish to know about other strains click on the variant you want to know about\n/Alpha\n/Beta\n/Gama\n/Delta\n/Mu\n/Omicron") 
    bot.message.reply_text(text="Are you curious to know how variants happen? Then select /Mutation")
    
def Alpha(bot,update):
    chat_id = bot.message.chat_id 
    bot.message.reply_text(text="In late 2020, experts noted gene mutations in COVID-19 cases seen in people in southeastern England. This variant has since been reported in other countries, including the U.S. Scientists estimate that these mutations could make the virus up to 70% more transmissible, meaning it could spread more easily. Some research has linked this variant to a higher risk of death, but the evidence isn't strong.The mutation on the Alpha variant is on the spike protein, which helps the virus infect its host.")
    bot.message.reply_text("WHO Designation :	Alpha\nLineage :	B1.1.1.7\nFirst detected : United Kingdom\nDate reported : November 2020")
    bot.message.reply_text(text="Do you want to continue texting with me?\n/yes or /no")
def Beta(bot,update):
    chat_id = bot.message.chat_id
    bot.message.reply_text(text="The Beta variant appears to spread more easily than the original virus but doesn't seem to cause worse illness.")
    bot.message.reply_text("WHO Designation :	Beta\nLineage :	B.1.351\nFirst detected :	Nelson Mandela Bay, South Africa\nDate reported :	July 2020")
    bot.message.reply_text(text="Do you want to continue texting with me?\n/yes or /no")
def Gama(bot,update):
    chat_id = bot.message.chat_id
    bot.message.reply_text(text="In January 2021, experts spotted this COVID-19 variant in people from Brazil who'd traveled to Japan. By the end of that month, it was showing up in the U.S.The Gamma variant appears to be more contagious than earlier strains of the virus. And it may be able to infect people who've already had COVID-19. A report from Brazil confirms that a 29-year-old woman came down with this variant after an earlier coronavirus infection a few months before.")
    bot.message.reply_text("WHO Designation :	Gamma\nLineage :	P.1\nOther Names : 20J/501Y.V3, Variant of Concern 202101/02 (VOC-202101/02), Brazilian variant or Brazil variant\nFirst detected	: Tokyo, Japan\nDate reported	: January 2021")
    bot.message.reply_text(text="Do you want to continue texting with me?\n/yes or /no")
def Delta(bot,update):
    chat_id = bot.message.chat_id
    bot.message.reply_text(text="This variant was spotted in India in December 2020. It caused a huge surge in cases in mid-April 2021. This highly contagious variant is now found in 178 countries including the U.S., the U.K., Australia, and all of Europe. It's the dominant strain in the U.S. and the U.K.The variant is thought to be partly responsible for India's deadly second wave of the pandemic beginning in February 2021")
    bot.message.reply_text("WHO Designation :	Delta\nLineage : B.1.617.2\nFirst detected : India\nDate reported	: December 2020")
    bot.message.reply_text(text="Do you want to continue texting with me?\n/yes or /no")
def Mu(bot,update):
    chat_id = bot.message.chat_id
    bot.message.reply_text(text="Experts first spotted this COVID-19 variant (pronounced m'yoo) in Colombia in January 2021. Since then, countries in South America and Europe have reported outbreaks of Mu. In the U.S., the CDC says Mu reached a peak in June 2021, when it made up less than 5% of variants going around the country. As of early September, it had been steadily declining. Still, scientists continue to track Mu.")
    bot.message.reply_text("WHO Designation :	Mu variant\nLineage :B.1.621 or VUI-21JUL-1\nFirst detected : Colombia\nDate reported : January 2021")
    bot.message.reply_text(text="Do you want to continue texting with me?\n/yes or /no")
def Omicron(bot,update):
    chat_id = bot.message.chat_id
    bot.message.reply_text(text="Experts in South Africa first reported the Omicron variant to the World Health Organization (WHO) on Nov. 24, 2021. They discovered the variant after COVID-19 infections suddenly began to go up.The WHO grouped Omicron as a Variant of Concern. This category means the variant might have a higher transmissibility, cause more intense disease, and may be less likely to respond to vaccines or treatments.") 
    bot.message.reply_text("WHO Designation :	Omicron\nLineage :	B1.1.529\nFirst detected : South Africa\nDate reported : November 2021")
    bot.message.reply_text(text="Do you want to continue texting with me?\n/yes or /no")
def Mutation(bot,update):
    chat_id = bot.message.chat_id
    bot.message.reply_text(text="Coronaviruses have all their genetic material in something called RNA (ribonucleic acid). RNA has some similarities to DNA, but they aren't the same. When viruses infect you, they attach to your cells, get inside them, and make copies of their RNA, which helps them spread. If there's a copying mistake, the RNA gets changed. Scientists call those changes mutations.These changes happen randomly and by accident. It's a normal part of what happens to viruses as they multiply and spread.Because the changes are random, they may make little to no difference in a person's health. Other times, they may cause disease. For example, one reason you need a flu shot every year is because influenza viruses change from year to year. This year's flu virus probably isn't the exact same one that circulated last year. If a virus has a random change that makes it easier to infect people and it spreads, that variant will become more common. The bottom line is that all viruses, including coronaviruses, can change over time.")      
    bot.message.reply_text(text="Do you want to continue texting with me?\n/yes or /no")      
          
def yes(bot,update):
    chat_id = bot.message.chat_id 
    bot.message.reply_text("HI, I'M COVID BOT")
    bot.message.reply_text("type /covid_info to know about the virus and variants")
    bot.message.reply_text("type /symptom to know about the symptoms")
    bot.message.reply_text("type /cases_statistics to know about the cases worlwide")
    bot.message.reply_text("type /precautions to know about the precationary measures")
    bot.message.reply_text("type /mental_health to check upon your well being")
    bot.message.reply_text("type /shopping to shop medical items")
    bot.message.reply_text("type /message to view message to the public")    
    
def no(bot,update):
     chat_id = bot.message.chat_id 
     bot.message.reply_text("Thank you for chatting along with me\nHope you have a great day!")
     bot.message.reply_text("If you wish your change your mind and want to continue texting please type /start\nI'll be available anytime to reply to your text")
    
def symptom(bot,update):
    chat_id = bot.message.chat_id
    bot.message.reply_text(text="Most common symptoms:\n1.fever\n2.dry cough\n3.tiredness\n")
    bot.message.reply_text(text="Less common symptoms:\n1.aches, pains\n2.sore throat\n3.diarrhoea\n4.conjunctivitis\n5.headache\n6.loss of taste/smell\n7.discolouration of fingers")
    bot.message.reply_text(text="If you come across any such above mentioned symptoms, please consult the doctor and get yourselves tested.")
    bot.message.reply_text(text="Do you want to continue texting with me?\n/yes or /no")
    
def cases_statistics(bot,update):
    chat_id = bot.message.chat_id
    bot.message.reply_text(text="Select the below link to view the statistics of Covid-19")
    bot.message.reply_text(text="https://covid19.who.int")
    bot.message.reply_text(text="Do you want to continue texting with me?\n/yes or /no")
   
def precautions(bot,update):
    chat_id = bot.message.chat_id
    update.bot.sendPhoto(chat_id=chat_id, photo="https://i.pinimg.com/originals/f3/98/37/f39837e2c85756f8b7a2bd39bd9c3024.jpg",caption="Please wear a mask while you step out!\n")
    bot.message.reply_text(text="To prevent the spread of COVID-19:\n*Clean your hands often\n Use soap and water, or an alcohol-based hand rub.\n*Maintain distance from anyone who is coughing or sneezing.\n*Wear a mask when physical distancing is not possible.\n*Don’t touch your eyes, nose or mouth.\n*Stay home when you feel unwell.\n*If you have a fever, cough and difficulty breathing, seek medical attention.")
    bot.message.reply_text(text="Do you want to continue texting with me?\n/yes or /no")
def vaccine(bot,update):
    chat_id = bot.message.chat_id
    bot.message.reply_text(text="Arm yourself against covid-19, please get your dose of vaccination\nclick below to know about the various vaccines developed for the covid-19")
    bot.message.reply_text("https://covid19.trackvaccines.org/agency/who/")
   
def mental_health(bot,update):
    chat_id = bot.message.chat_id
    bot.message.reply_text(text="select your suitable mood right now")
    bot.message.reply_text("/happy")
    bot.message.reply_text("/sad")
    bot.message.reply_text("/bored")
    bot.message.reply_text("/sleep_deprived")
    bot.message.reply_text("/angry")
    bot.message.reply_text("/nervous")
    
def happy(bot,update):
    chat_id = bot.message.chat_id
    update.bot.sendPhoto(chat_id=chat_id,photo="https://cdn.w600.comps.canstockphoto.com/be-happy-smiley-clipart_csp10100718.jpg")
    bot.message.reply_text("It's good to know that you are in a happy state of mind")
    bot.message.reply_text(text="Happiness is always a choice, so choose to be happy, keep smiling!")
    bot.message.reply_text(text="Do you want to continue texting with me?\n/yes or /no")

def sad(bot,update):
    chat_id = bot.message.chat_id
    bot.message.reply_text("Some scenarios make us feel bad, many people are sailing in the same boat, you are not alone")
    bot.message.reply_text("Everything changes with time, Nothing is permanent but your willpower matters")
    bot.message.reply_text("Remember that GOOD MENTAL HEALTH IMPROVES THE OVERALL QUALITY OF LIFE")
    bot.message.reply_text("IT IS OK TO TALK IT OUT")
    bot.message.reply_text("If you are feeling depressed, please feel free to contact any of the below mentioned contacts for personalized support")
    bot.message.reply_text("Parivarthan:- 080 65333323")
    bot.message.reply_text("NIMHANS:- 080 46110007")
    bot.message.reply_text("Roshni Trust:- 4066202000/2001")
    bot.message.reply_text("Asra:- 9820466726")
    bot.message.reply_text(text="Do you want to continue texting with me?\n/yes or /no")

def bored(bot,update):
    chat_id = bot.message.chat_id
    bot.message.reply_text("I would like to suggest you some activities to get rid of your boredom.")
    #bot.message.reply_text("Reading is important. If you know how to read, then the whole world opens up to you – Barack Obama")
    #bot.message.reply_text("Read a good book.....A word after a word after a word is power. It has the power to make your mind and heart free")
    bot.message.reply_text("Watch TED Talks and you will get inspired by those real life experiences")
    bot.message.reply_text("Learn a new language, its fun")
    bot.message.reply_text("Spend your time embracing the nature")
    bot.message.reply_text("Write in your journal. It’s a wonderful way to document your life.")
    bot.message.reply_text("Have a power nap, so you'll feel charged up.")
    bot.message.reply_text(text="Do you want to continue texting with me?\n/yes or /no")
   
def sleep_deprived(bot,update):
    chat_id = bot.message.chat_id
    #update.bot.sendPhoto(chat_id=chat_id,photo="")
    bot.message.reply_text("Try going to bed and waking up at the same times every day")
    bot.message.reply_text("Turn off electronic devices and keep them away")
    bot.message.reply_text("Avoiding eating 2–3 hours before bedtime")
    bot.message.reply_text("Practice Meditation, mindfulness training, breathing exercises, yoga and acupressure")
    #bot.message.reply_text("Turmeric milk will help")
    bot.message.reply_text(text="Do you want to continue texting with me?\n/yes or /no")

def angry(bot,update):
    chat_id = bot.message.chat_id
    #update.bot.sendPhoto(chat_id=chat_id,photo="")
    bot.message.reply_text("Anger is a weakness. When anger is recurrent and unmanaged, it can lead to physical effects.")
    bot.message.reply_text("Think before you speak")
    bot.message.reply_text("Use humor to release tension")
    bot.message.reply_text("Get some exercise")
    bot.message.reply_text("Don't hold a grudge. Identify possible solutions.")
    bot.message.reply_text(text="Do you want to continue texting with me?\n/yes or /no")

def nervous(bot,update):
    chat_id = bot.message.chat_id
    update.bot.sendPhoto(chat_id=chat_id,photo="")
    bot.message.reply_text("Choose courage over nervousness. Emotions are never permanent") 
    bot.message.reply_text("Change your focus")
    bot.message.reply_text("Relax your body")
    bot.message.reply_text("Get some fresh air, think you can do it!")
    bot.message.reply_text("Fuel your body with some positivity. You can defnitely overcome fear and complete any given task.")
    #bot.message.reply_text("Identify pressure points to calm anger and anxiety")
    bot.message.reply_text(text="Do you want to continue texting with me?\n/yes or /no")
    
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
    bot.message.reply_text(text="Do you want to continue texting with me? /yes or /no")
    
def sanitizer(bot,update):
    chat_id = bot.message.chat_id
    update.bot.sendPhoto(chat_id=chat_id,photo="https://media1.fdncms.com/rochester/imager/u/original/11617421/sanitizer.jpg")
    bot.message.reply_text("click below to shop")
    bot.message.reply_text(text= "https://www.amazon.in/sanitizer/s?k=sanitizer")
    bot.message.reply_text(text="Do you want to continue texting with me?\n/yes or /no")
      
def gloves(bot,update):
    chat_id = bot.message.chat_id
    update.bot.sendPhoto(chat_id=chat_id,photo="https://cdn.shopify.com/s/files/1/0971/2990/products/Screenshot_20200329-173805_AliExpress_large.jpg?v=1585481715")
    bot.message.reply_text("click below to shop")
    bot.message.reply_text(text= "https://www.amazon.in/hand-gloves/s?k=hand+gloves")
    bot.message.reply_text(text="Do you want to continue texting with me?\n/yes or /no")


def main(): #mainfunction

  BOT_TOKEN= os.getenv("BOT_TOKEN")
  u = Updater(BOT_TOKEN, use_context=True)
  dp = u.dispatcher
  dp.add_handler(CommandHandler('start',start))
  dp.add_handler(CommandHandler('covid_info',covid_info))
  dp.add_handler(CommandHandler('yes',yes))
  dp.add_handler(CommandHandler('no',no))
  dp.add_handler(CommandHandler('mental_health',mental_health))
  dp.add_handler(CommandHandler('happy',happy))
  dp.add_handler(CommandHandler('sad',sad))
  dp.add_handler(CommandHandler('nervous',nervous))
  dp.add_handler(CommandHandler('angry',angry))
  dp.add_handler(CommandHandler('bored',bored))
  dp.add_handler(CommandHandler('sleep_deprived',sleep_deprived))
  dp.add_handler(CommandHandler('Alpha',Alpha))
  dp.add_handler(CommandHandler('Beta',Beta))
  dp.add_handler(CommandHandler('Gama',Gama))
  dp.add_handler(CommandHandler('Delta',Delta))
  dp.add_handler(CommandHandler('Mu',Mu))
  dp.add_handler(CommandHandler('Omicron',Omicron))
  dp.add_handler(CommandHandler('Mutation',Mutation))
  dp.add_handler(CommandHandler('symptom',symptom))
  dp.add_handler(CommandHandler('cases_statistics',cases_statistics))
  dp.add_handler(CommandHandler('precautions',precautions))
  dp.add_handler(CommandHandler('shopping',shopping))
  dp.add_handler(CommandHandler('mask',mask))
  dp.add_handler(CommandHandler('sanitizer',sanitizer))
  dp.add_handler(CommandHandler('gloves',gloves))


  u.start_polling()
  u.idle()

if __name__ == '__main__':
    main()
  

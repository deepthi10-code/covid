import logging  
import os  

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters 
 
def start(bot,update): 
 
    chat_id = bot.message.chat_id     
    bot.message.reply_text("HI, I'M COVID BOT")
    bot.message.reply_text("type /covid_info to know about the virus")
    bot.message.reply_text("type /symptom to know about the symptoms")
    bot.message.reply_text("type /cases_statistics to know about the cases worlwide")
    bot.message.reply_text("type /precautions to know about the precationary measures")
    bot.message.reply_text("type /shopping to shop medical items")
    bot.message.reply_text("type /mental_health to view message to the public")
    bot.message.reply_text("type /message to view message to the public")

def covid_info(bot,update):

    chat_id = bot.message.chat_id 
    bot.message.reply_text(text="COVID-19 is a disease caused by a new strain of coronavirus. CO stands for corona, VI for virus, and D for disease. Formerly, this disease was referred to as 2019 novel coronavirus or 2019-nCoV")
    update.bot.sendPhoto(chat_id=chat_id,photo='https://www.gavi.org/sites/default/files/thumbnail/cdc-w9KEokhajKw-unsplash_h2.jpg')

    bot.message.reply_text(text="type /covid_info to know about the virus")
    bot.message.reply_text(text="type /symptom to know about the symptoms")
    bot.message.reply_text(text="type /cases_statistics to know about the cases worlwide")
    bot.message.reply_text(text="type /precautions to know about the precationary measures")
    bot.message.reply_text(text="type /shopping to shop medical items")
    bot.message.reply_text(text="type /message to view message to the public")
    bot.message.reply_text(text="Do you want to continue texting with me? /yes or /no")
    
def yes(bot,update):
    chat_id = bot.message.chat_id 
    bot.message.reply_text("HI, I'M COVID BOT")
    bot.message.reply_text("type /covid_info to know about the virus")
    bot.message.reply_text("type /symptom to know about the symptoms")
    bot.message.reply_text("type /cases_statistics to know about the cases worlwide")
    bot.message.reply_text("type /precautions to know about the precationary measures")
    bot.message.reply_text("type /shopping to shop medical items")
    bot.message.reply_text("type /message to view message to the public")    
    
    
def no(bot,update):
     chat_id = bot.message.chat_id 
    bot.message.reply_text("Thank you for chatting along with me\nHope you have a great day!")
    
    
def symptom(bot,update):

    chat_id = bot.message.chat_id
    bot.message.reply_text(text="Most common symptoms:\n1.fever\n2.dry cough\n3.tiredness\n")
    bot.message.reply_text(text="Less common symptoms:\n1.aches, pains\n2.sore throat\n3.diarrhoea\n4.conjunctivitis\n5.headache\n6.loss of taste/smell\n7.discolouration of fingers")
    bot.message.reply_text(text="If you come across any such above mentioned symptoms, please consult the doctor and get yourselves tested.")
    bot.message.reply_text(text="Do you want to continue texting with me? /yes or /no")
    
def cases_statistics(bot,update):
    
    chat_id = bot.message.chat_id
    bot.message.reply_text(text="Select the below link to view the statistics of Covid-19")
    bot.message.reply_text(text="https://covid19.who.int")
    bot.message.reply_text(text="Do you want to continue texting with me? /yes or /no")
    

def precautions(bot,update):
    
    chat_id = bot.message.chat_id
    update.bot.sendPhoto(chat_id=chat_id, photo="https://i.pinimg.com/originals/f3/98/37/f39837e2c85756f8b7a2bd39bd9c3024.jpg",caption="Please wear a mask while you step out!\n")
    bot.message.reply_text(text="To prevent the spread of COVID-19:\n*Clean your hands often\n Use soap and water, or an alcohol-based hand rub.\n*Maintain distance from anyone who is coughing or sneezing.\n*Wear a mask when physical distancing is not possible.\n*Don’t touch your eyes, nose or mouth.\n*Stay home when you feel unwell.\n*If you have a fever, cough and difficulty breathing, seek medical attention.")
    bot.message.reply_text(text="Do you want to continue texting with me? /yes or /no")
   

def mental_health(bot,update):
    
    chat_id = bot.message.chat_id
    bot.message.reply_text(text="select your suitable mood right now")
    bot.message.reply_text("/happy")
   ''' bot.message.reply_text("/sad")
    bot.message.reply_text("/bored")
    bot.message.reply_text("/sleep deprived")
    bot.message.reply_text("/angry")
    bot.message.reply_text("/nervous")
    '''
 
def happy(bot,update):
    chat_id = bot.message.chat_id
    update.bot.sendPhoto(chat_id=chat_id,photo="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxASEBAQDw8VEBUVFRYVFRUVEA8PDxUPFRUWFhUSFRUYHSggGBolGxUWITEhJSkrLi4uFx8zODMtNygtLisBCgoKDg0OGhAQGi0lHyUtLS0tLS0tLS0tLS0tLS0tLS0tKy0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLf/AABEIAOEA4QMBIgACEQEDEQH/xAAcAAEAAgMBAQEAAAAAAAAAAAAAAQIDBQYEBwj/xABAEAACAQIDBAcEBwcDBQAAAAAAAQIDEQQFIRIxQVEGByJhcYGRE1KhwRQyQrHR4fAjM1NykpOyYtLxQ1RzosL/xAAbAQABBQEBAAAAAAAAAAAAAAAAAQIDBAUGB//EADcRAAIBAwEEBwcCBgMAAAAAAAABAgMEETEFEiFRQWFxgZGh0QYTIjKxwfAjQhQzUmJykhWi4f/aAAwDAQACEQMRAD8A+3N8iyQSJAAAAAAAABDJAAUCLWJAAAAAAEXDDAkEFd4uGA3lwBAAAAAAAAFZFgAFCYk2JAAAAAAAAAAAAAAAAAAAIZ4q+PS0j2n6L8ytc3dG2hv1pYXm+pLV/mR0YuTwj2SdtWeWrjoLd2vA11WtKX1ncxHKXftRN8LeOFzlxfhp9SzG2X7me2eYSe5JfEwSxM3vl8vuMIMGttS7rfPUl44XgsLyJlTgtEWcnzK7IBQfHiyQsnYvGvNbpGIEkK06fGEmux4+gjSep64Y+a3u/kvkeinmMftXXxNYDUt9u31H9+8v7vi89fMjlRg+g31OaeqdzIc/GTTunY9tHMGtJ69/H0OksfaShV+Gutx89Y+q7+HWV527WnE2YMcJpq6dzIdImmsrQrgACgAAAAAAAAAAAAAAAAAMdaooq7diuIrKEbv04s0tas5u8vJcEY21drwso7q4zei5db9NX2cSalSc+wzYnFynpuXL8TzgHn1zc1bmo6lV5f5wXJdSLsYqKwgASQDiAAGAAAAAAAAAAAAAADJSqyi7xf5m0wuKU9Nz5GnCbTunZo2NmbYq2clHWHTH05PyfSRVKSn2nRA8eCxe3o9Gj2HodvcU69NVKbyn+eK6ShKLi8MAAmEAAAAAAAAq2EwAsY6k1FNt2SMhpMzxO1LZW5fFlDaV9GzoOo9dEub9FqySlTc5YMWIrucrvTkuRRIpEyI8yr1pVZupN5b4tmlhRWEAARZEBIA+EU8tiNggkgbJ5fAUAAQAAWSvoKll4QhUGVRXBN997FZLl+a7iWVvKKz6+nHuyIpFAAQjgGAAFbtO6dmbnBYnbj3revmaeQoVnCSkvNc+42tj7TdnVxL5H83qutea68DKtLfjw1OjKuRSE1KKa1TLRiejJprKM0siQBQAAACgLWJADx5jiNiGm96I0UT05pW2qjS3R/Tf65HmieebdvHcXTivlhwX3fj9EadvT3Idv4jLEsUgXMFj5AkgkdFJ6jQc9026W0cuoe0qL2lSV1TpJ2lNq1239mKurvvS4nQH516eZ7HE5xKVXtUaNWNFR4OhSnapu4Se2/Bo2djWKvrjdn8kVlryS7/sRVZ7keGp1GSdcFf28FjsPTjQm9JU41IzhFu232m1NLja25+B9ijJNJp3T1TWqae5o+M9afTLBY/AYelQpRVSnUjsbOz2KWxKMopJaRfY07kfQerXFurlOCk9XGn7P+1KVNfCKNH2i2ZQoQhVox3VndaWnNPj2MjoVG20zpQAcmWgWg7NMqShYycGpLoExngcZ026Z1cLUWGwmH9tV2dZys6EHL6sGlJNvc33Nc9MfRDrDpYut9Fr7EKzbUHFtU6jhFbSs9YSvtWV3dRfdf5z0K6VUKOdYjHYvtxk68qd3ZRqymtmSvutDaXmeDrH6Q0cTmMcbgkqUrQcnH+PCTcal/ets/0o9G/4O3dt7rdxJr5unOMd6WnZ18Sh76W9k/RYPB0fzJYrC4fEpW9rTjNrlNrtR8ndeR7zzqcJQk4y1XB9qL6eeIAAwUMwszMxSJqcVqxUzYZTX19m/FePFfM25y0aji1Jb0dLSqKSTXFXO79nr331B0paw0/xenhp2YKVzT3Zb3P6mQAHQlYAAABhxNTZjKXJfHgZjW53O1PZ5v4L9IrXtb3FvOryT8ejzwPpx3pKJpE+e8yIxIyI8sZsMywLlIsuRtETAAEyIRJ2TfcfkSrUc5Sk9XJtvxbufr0/K3SbLXhMZicM1ZwqSiv/ABt3g13OLi/M6/2Tkt6tHpe6+5Z9Spc9BrFLZ3b+L4eB+lOrDCunlOCi1bahKp5VJymvhJH5+6MZHUxuKpYamnecu07aQprWc34L42XE/UmEoRpwhTprZjCMYRS3KEUoxXokT+1VeKp06PS3vPsSaXjl+AlsuLZkBJBxJcBKIJDIH5NzzDOlicRRat7OrUh/TNr5Hhir6I+k9c/R2VLG/S4RvTxFrvhHERVpRfK6Sl/VyPnMnbReb+S7j1izuY3NvCqnqvPpXiZko7raP0T1PTbyjDp/ZlWS8PayfzOzOd6vMrlhsswlGaansOck9GpVJOpsvvW0l5HRHme0Zqd1VktHKWPE0KfyoAApjxIwsySMchy4j4mORuslq3g4+789fxNMz15NUtUtzT9Vr+Jt7Cr+6vYcpZi+/TzSGXEc031cToAAeiGUAAAA0mfS7UFyTfr/AMG7Ofzt/tPCPzMbb8sWMutxXnn7Fm1Waq7zwoyRMReLPPWjTkZYsyoxIvFkbImWAA0aDmel3QbB5i4zrKdOpFWVSm4xm4e7K6akvijpgTULipQnv0pNPmhrimsM0fRbolhMvhKOGg9qX16k2pVZW3JtJJLuSSN4ANrValabnUbbfSxUkuCAAIxQAAA8uaZdRxNGdDEU1VpzVpRd/JprVNb01qjkMp6qcuoV1X/a1tl7UadWUJUlK91dKKcrd7tzudySWqF9cUIuFObinqk+4Y4Rby0ACCqPAAYAVkYmWkykmPiiRFJMzYGdqtN96Xrp8zAy1GVpRfevvLVtPcqwlyafg0OksxaOsAB6q9TEAAEAHPZz+9fgvkdCc/na7afOPzZi7finZvPRKPoWbR/qdzPASmVRKOAm09DVwazpB0pweB9n9Lq7DnfZShOpJpWu7RWi1W89GQ9I8HjIuWErxq2+tHWNSPDtQklJLvtY5zrK6JvH4eMqNvb0dp003ZThK21TvuTeyrN8Vwvc4DqXpSjmlSMk4yjQqqSaakpKdNNNPc7mzS2fa1tnzrxk9+HzLhjq4dfbzKU6k41FFrgz70mCkWXRz+M8ESMAy2XLzv8AcROPl8fQnlbSSzkbvGMAFYcAAKBJAAZAkAD4xjjMhrJKgDW8scDzZhjaVGnKrXqRpQjvlOSjFeb49x6Gz5v15q+XUXyxUPL9lWV/X7y1Y0FXuIUpPCk8CTe7FyRvct6fZbiK8cPRxO1ObtG9KtCMpclKUbep0UmfHuqPobUdSGY4hbMI3dCL+tOb09q+UVrbm9dy1+xRjfw3vwL+07ShRuFRt23jg8vPHuS0WotCUnHekYyYb14r7zMkvd8m3dlaUO3C25y8+9FaFvJSjx1a59Lx0/nMm300zqgAeovUxAABAKbzUZ/T+pJd6+f4m6PBnFLapS7rP03/AAuZ+1KPvrSpDqz4cfsS0JbtSLOeJRRFkzzg2iyPn+d4mGWZ1Txs4pUMbT9lVnb93Vi43nfgrKm2uPafA780vTLIY47B1cPop/XpSf2a0fq68E7uL7pMtWFWFOtir8kluy7H09zw+4grQbjw1XFHQRlxWv3GWEuJ8h6semrpSWWY5uEoN06U5abM4u3sJvhZ6J+XI+tJjL6xq2Vbcl2p9DXNfnAZCaqRyj1+Gq8bbysnw7l+JgizImV53GcpLGfzq+4m5gAArCgAAAJIJHRS1YjBAIbCUt58RUiSrYcijYiQ5INnzvrGx8cXXw2S0bSnVqQnXe90qUe15S2by8Le8bTp/wBNaeApbEGp4ma/Zw3qKentanKPJcX3Xa0fVLkdTZq5niryrYi+w5X2vZN3lUf8zWnclbRm7YW38PSd9U4Y/lr+qXQ+yOvXjxinLfl7td/YfRIQUYqMVZJKKS3KKVkvQyU5LVPc0Y2Q2ZUJOL3i3u5WDM1xfdre+7kuZmy/tVodzcn9/wCB4mbTIKd5TlysvN6v7via2zs17unDHDOX3fF1cu0hrfBTbN6AD0IyAAAAFJxumnuenkXAdoHIVqbjKUXw0Kpm0z7D2aqLjo/Hg/1yNUea39q7a4lS6Fp2PT07UbdGfvIKRZEkJgotZJD5t1q9DJVlLHYSN6iX7eCXaqQS/ex5ySWq4rw103QLrMlRUcPj3KpSSSjVScqsEve4zj8V3rRfYz5d1hdXO25YvL42nrKpRWm097nS5S5x48NdH0Wzr6hcUlZ3vy/tly6s9HU9Oh8MFGtRlGXvKfej6lg8XTqwjUo1I1ISV4yjJSi13NGdM/MmQ9IcZgqjeGqOm7/tKUlenJrR7UHuemu5rmfUuj3W3hatoYyDw0923G9TDt/5R9Gu8r3vs9cUW3S+OPVr4dPdnmFO5jLXgz6YpE7R4MBmFGvHboVoVo+9CcZrztuZ6rmBKLTw0TpZ4mXaJuYbltobgN0yXI2jHci4YDdLuRVspOaScpNJLVtuyS5tnHZ91l5dhrqFX6VP3aNpQv31Pq+jb7izb2lWvLdpRcn1eui7xJSjH5mdnc+edOOsyjhlKjgnHEVtzlfao0nr/XLuWi4vg/nXSvrCxuNUqe19HovR06baclyqT3y8NF3Ho6C9AK2NlGtXUqWGX2t06v8App93OW7lfh01tsOlaw/iL+Swv2rTsfPsX0Ksq7m92mjJ0H6MVs0xMsVjJSlRUtqrOTalWqfwk+W69ty0VtD7pGKSSSSSVkkrJJbkkYsHhKdGnClRgqcIK0YpWSRmbMjaW0JXtXexiK4RXJevl0LQtUaKprrDZAKmfgsEM6XKaGxSjfe9X57vhY0eBw/tKkY8OPgjqUdZ7N2jzO4kv7V9X9l4lC9qaQ7yQAdWZ4AAAAAAGHEUlOLi9zX6ZytWm4ycZb07fmdgarOMFtLbiu0t/evxMLbmz/4il7yC+KPmuXatV3rpLVrW3Jbr0f1NGRcqixwzNYsLlS1xMCHL9Leg+Fxyc2vYV7aVoLV8lUj9tbuT7z4/0l6E43B3lUpbdNf9WkpTpW5y0vB+KSP0QLmtY7auLXEfmhyfR2PVea6itVtYz4rgz8q4bFVKctulUlTkvtQlKEvVanT5b1jZrSslinVS4VYQqq3Nya2vifXc76B5dirynh1Sm/t0n7GV3xaXZb8Uzjcz6nnr9Fxia4RrQad++cL/AOJ0MdsbPul+vHH+UU/B8X9Owpu2qw+XyPDh+uTGrSph8PU70q1N+faZ6l101eOAh/fn/tNFX6qszj9WNKp/LWS/zSPE+rnNv+zf97Df7wVtsWfFOH+2PLeQm9XXPwOkrdc2Kafs8JRi+G1KpNeisajGdaWaVdI1adBcfZ0Y7vGe015GLD9WGay30IU/5q1L/wCWzd4DqgxMre3xVKmuVOM60n3u6ivvFS2LQ4/pv/v6h+vLn9Dgs0zjE4h3r4irW1v26kpq/NRbsvIyZTkeJxktnC0ZVH9qy7Ee9zekV4s+zZP1XZdRalUjPEyX8RpQv/JGyfg7nZYehCnBQpQjTit0YxUIpdyWiK9f2ko047ttDPbwXhq/IkhZyfzM+e9EuqyjR2auPccRNaqkr/R0/wDVfWo/RdzPoySSSSsloktElyBDZzF1d1rqe/WlnlyXYugvU6UYLEUS2RchsFYlwQSD35Tg9uW1JdmL9XyLNrbTuaqpw1flzfd/5qMqTUI7zNjlGE2IbTXalr4LgjZAHpFvQhQpxpw0X5nv1fWYk5OUnJgAEw0AAAAKBMALgAANBm2X7LdSC0f1kuH5GqR2bNDmeWON501db3Hj5dxye2NjvLr0Fw1lFfVfdd6NG2uuG5PuZrLgpcm5yxfJLIqiWx6isZkNedES2uAuQCN8XkdgtcXKom4mALXIK3LU43aQsYuTSQj4LIIuZtvc7qKe5bPDmUqrjazvZ23c1YnlQwsp/nj9UsriNUsspcqLkNkA8kko2evA4KVV8o8X+t7JqFCdaoqdNZb/ADw5sSclFZk+AwGElVlZaRW9/ridNSpqKUYqyRWhRjCKjFWS/V2Zjvdm7NhZ0+cnq/supeer6sevWdV9RDZVy5EyfARiaZASiQAAAAAKNE2LAAAAAAAAA1ePypTvKHZl8H+BoqtCUXsyWy/16nYmCtQjNWklJd5iX2xKNd78Phl5PtS07V35LVG6lDg+K8zkmyLm4xWSPfTl5P5M1dfDzhpOOz93qcnd2NxbvNWOFzXGPj64fUaNKtTn8r9SiZNyAUusmLXIuQBAwTcmE7NMpYkVNrihMZM7lHhLTXg7pPejFUqX3fqysihMItu0U2+VrsmdaUvhS15Z8uLG7iXEgJX0WvxZssLk85az7C9X6G4wuBhT+rHXm9WadpsK5rcZrcj16/66+OCvUu4R04v86TV4DJ27Sq6L3efjyN5CCSSSslw4FwdfaWNG1ju012t6vt9FhGbUqyqPMmCspFiEi4RkRiWAAAAAAAAAAAAAAAAAAAAAAAVkk9GiwADw1ssoy+xbvWh5KmRx+zUcfFKX4G5BSq7NtavGdNd3B+KwyWNepHSTOflkU+FRPysVeSVPej6v8DogU3sGy/pf+0vUk/jKvPyRzyyOfvRXr+BmhkXvVP8A1/M3YHw2HZRedzPa5eoju6r6TW08opLfG/i/kj206UYq0Uku5Iygv0bajR/lwUexYIZTlL5nkAAnGgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAf//Z")
    bot.message.reply_text("It's good to know that you are in a happy state of mind")
    bot.message.reply_text(text="Happiness is always a choice, so choose to be happy, keep smiling!")
    bot.message.reply_text(text="Do you want to continue texting with me? /yes or /no")
    
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
    bot.message.reply_text(text="Do you want to continue texting with me? /yes or /no")
      
def gloves(bot,update):

    chat_id = bot.message.chat_id
    update.bot.sendPhoto(chat_id=chat_id,photo="https://cdn.shopify.com/s/files/1/0971/2990/products/Screenshot_20200329-173805_AliExpress_large.jpg?v=1585481715")
    bot.message.reply_text("click below to shop")
    bot.message.reply_text(text= "https://www.amazon.in/hand-gloves/s?k=hand+gloves")
    bot.message.reply_text(text="Do you want to continue texting with me? /yes or /no")

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
  dp.add_handler(CommandHandler('yes',yes))
  dp.add_handler(CommandHandler('no',no))
  dp.add_handler(CommandHandler('mental_health',mental_health))
  dp.add_handler(CommandHandler('happy',happy))
  #dp.add_handler(CommandHandler('covid_info',covid_info))
  #dp.add_handler(CommandHandler('covid_info',covid_info))
  #dp.add_handler(CommandHandler('covid_info',covid_info))
  dp.add_handler(CommandHandler('symptom',symptom))
  dp.add_handler(CommandHandler('cases_statistics',cases_statistics))
  dp.add_handler(CommandHandler('precautions',precautions))
  dp.add_handler(CommandHandler('shopping',shopping))
  dp.add_handler(CommandHandler('mask',mask))
  dp.add_handler(CommandHandler('sanitizer',sanitizer))
  dp.add_handler(CommandHandler('gloves',gloves))
  dp.add_handler(CommandHandler('message',message))

  u.start_polling()
  u.idle()

if __name__ == '__main__':
    main()
  

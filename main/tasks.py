from celery import shared_task
from .models import EntryModel,OldEntryModel
import smtplib
from bs4 import BeautifulSoup
import requests
from datetime import datetime

def send_mail(email, url, price):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('smartdiscount.ltd@gmail.com', 'xixrwxqlsaovqmxm')

    subject = 'Price fell down'
    body = f'''
    Url: {url}
    Price : {price}

    If our website helped you save money, if you are willing to fund us with even $1, because we could offer better opportunities. SmartDiscount wishes you a good purchase.

    Best regards,

    SmartDiscount Administration.
    '''

    msg = f'Subject: {subject}\n\n{body}'

    server.sendmail(
        'smartdiscount.ltd@gmail.com',
        email,
        msg
    )
    server.quit()

@shared_task
def check():
    entries = EntryModel.objects.all()
    for entry in entries:
        wanted_price = entry.price
        function_text = entry.site.price_function
        
        exec(function_text,globals())

        current_price = float(f(entry.url))
        if current_price < wanted_price:
            send_mail(entry.email, entry.url, current_price)
            print("sending mail to: " +entry.email)
            entry.delete()

    print("checked | "+datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

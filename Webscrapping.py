import requests
from bs4 import BeautifulSoup
import html5lib
import smtplib
import time

def userInput():
    global flipkartProductURL
    global amazonProductURL
    global RDProductURL
    flipkartProductURL=input('enter the flipkart url:')
    amazonProductURL=input('enter the amazon url:')
    RDProductURL=input('enter the RD url:')


def trackPrices():
    
    headers={'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
    if flipkartProductURL and amazonProductURL and RDProductURL:
        flipkartResponse=requests.get(flipkartProductURL,headers=headers)
        amazonResponse=requests.get(amazonProductURL,headers=headers)
        RDResponse=requests.get(RDProductURL,headers=headers)
        flipkartSoup=BeautifulSoup(flipkartResponse.content,'html5lib')
        amazonSoup=BeautifulSoup(amazonResponse.content,'html5lib')
        RDSoup=BeautifulSoup(RDResponse.content,'html5lib')
        flipkartProductPrice=float(flipkartSoup.find('div',attrs='_30jeq3 _16Jk6d').text.replace(',','')[1:])
        amazonProductPrice=float(amazonSoup.find('span',attrs='a-price-whole').text.replace(',','')[0:])
        RDProductPrice=float(RDSoup.find('span',attrs='pdp__offerPrice').text.replace(',','')[1:])
        print('Flipkart product is',str(flipkartProductPrice))
        print('Amazon product is',str(amazonProductPrice))
        print('Reliance Digital product is',str(RDProductPrice))
        sendEmail(amazonProductPrice,flipkartProductPrice,RDProductPrice)


def sendEmail(amazonPrice,flipkartPrice,RDPrice):
    message='pk'
    
    if (flipkartPrice < amazonPrice) and (flipkartPrice < RDPrice):
        message="Flipkart Price is low.Price is Rs "+str(flipkartPrice)
    elif (amazonPrice < flipkartPrice) and (amazonPrice < RDPrice):
        message="Amazon Price is low.Price is Rs "+str(amazonPrice)
        
    else:
        message="Reliance Digital Price is low.Price is RS "+str(RDPrice)
    
    fromEmail="pikachupi142@gmail.com"
    toEmail='priyadurgam2825@gmail.com'
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(fromEmail,'ndyjgcrkdjatuiqf')    
    server.sendmail(fromEmail,toEmail,message)
    print('mail send successfully')
    server.quit()
userInput()
while True:
    trackPrices()
    time.sleep(43200)

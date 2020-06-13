# Libraries
import requests
import time
import json
import argparse
from datetime import datetime
from requests import Request, Session
from tqdm import tqdm


# COINMARKET-API-URL
COINMARKET_URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

#IFTTT URL:
WEBHOOKS_TELEGRAM_URL = "https://maker.ifttt.com/trigger/bitcoinTelegram1/with/key/g2fW8tTnrigBgQ67BktfNdINEslhjApQsujQIx-eHKF"
WEBHOOKS_SMS_URL = "https://maker.ifttt.com/trigger/bitcoinSMS/with/key/g2fW8tTnrigBgQ67BktfNdINEslhjApQsujQIx-eHKF"
WEBHOOKS_PUSH_URL = "https://maker.ifttt.com/trigger/bitcoinPush/with/key/g2fW8tTnrigBgQ67BktfNdINEslhjApQsujQIx-eHKF"
WEBHOOKS_TWITTER_URL = "https://maker.ifttt.com/trigger/bitcoinTwitter/with/key/g2fW8tTnrigBgQ67BktfNdINEslhjApQsujQIx-eHKF"


# PARAMETERS
# https://coinmarketcap.com/api/documentation/v1/#section/Quick-Start-Guide -->Find python code from here
parameters = {
    'start': '1',
    'limit': '1',
    'convert': 'INR'
}
#HEADERS
headers = {
    'Accepts': 'application/json',

    # coinmarketcap individual key
    'X-CMC_PRO_API_KEY': '0701a1d6-a389-48c3-8311-0ef834939015',
}

# ---------------------------------------------------FETCH BITCOIN DATA------------------------------------------------------------------
# @ GET
# FETCH BITCOIN PRICE FROM COINMARKET
def fetchBitcoin():
    print('The Bitcoin Price is Being Fetched(^_^).')
    
    session = requests.Session()
    print('Breathe in .')
    print('Breathe Out .')
    session.headers.update(headers)
    response = session.get(COINMARKET_URL, params=parameters)
    data = json.loads(response.text)
    x = 1
    for i in tqdm(range(0,100000)):
        for x in range(0,1000):
            x*=4
    price = float(data['data'][0]['quote']['INR']['price'])
    return round(price)
# ----------------------------------------------------------BEAUTIFY/FORMAT BITCOIN DATA  --------------------------------------------
# FORMAT TELEGRAM MESSAGE
def telegramMessage(bitcoin_data):
    print('Beautifying your Message')
    x = 1
    for i in tqdm(range(0,100000)):
        for x in range(0,1000):
            x*=4    
    rows = []
    for bitcoin_value in bitcoin_data:
        date = bitcoin_value['date'].strftime('%d.%m.%Y %H:%M')
        value = bitcoin_value['bitcoin_current_amount']
        row = '{}: ₹ <b>{}</b>'.format(date, value)
        rows.append(row)
    return '<br>'.join(rows)

# FORMAT SMS MESSAGE
def smsMessage(bitcoin_log):
    rows = []
    for bitcoin_value in bitcoin_log:
        date = bitcoin_value['date'].strftime('%d.%m.%Y %H:%M')
        value = bitcoin_value['bitcoin_current_amount']
        row = '\nDate {}: is Rs: {}'.format(date, value)
        rows.append(row)
    return '\n'.join(rows)

# -------------------------------------------------------POST BITCOIN DATA-------------------------------------------------------------------------
# @ POST  -->PUSH NOTIFICATION
# SEND BITCOIN PRICE AS PUSH NOTIFICATION
def postPushFunc(event, value):
    data = {'value1': value}
    post_event = WEBHOOKS_PUSH_URL.format(event)
    requests.post(post_event, json=data)
    print('Please Check Notification(*_*) ')

# @ POST  --> TELEGRAM MESSAGE
# SEND BITCOIN PRICE AS TELEGRAM MESSAGE
def postTelegramFunc(event, value):
    data = {'value1': value}
    post_event = WEBHOOKS_TELEGRAM_URL.format(event)
    requests.post(post_event, json=data)
    print('Please Check Telegram Channel (*_*) ')
    print("https://t.me/piyushBitcoin")


# @ POST --> TWITTER ACCOUNT
# SEND BITCOIN PRICE TO TWITTER ACCOUNT
def postTwitterFunc(event, value):
    data = {'value1': value}
    post_event = WEBHOOKS_TWITTER_URL.format(event)
    requests.post(post_event, json=data)
    print('Please Check Twitter ==> https://twitter.com/piyushcodes ')
    print("https://twitter.com/piyushcodes")

# @ POST --> SMS TO ANDROID PHONE:
# SEND BITCOIN PRICE AS SMS TO ANDROID PHONE:
def postSMSFunc(event, value, phone):
    data = {'value1': value, 'value2': phone}
    post_event = WEBHOOKS_SMS_URL.format(event)
    requests.post(post_event, json=data)
    #ANIMATION
    print('SMS has been Sent')
    animation = "|/-\\"
    idx = 0
    while True:
      print(animation[idx % len(animation)], end="\r")
      idx += 1
      time.sleep(0.1)    
# -------------------------------------------------------------------X--------------------------------------------------------
# PUSH IFTTT MASTER DRIVER THAT FETCHES THE DATA AND POST TO APP
def ifttt_master_driver(alert, time_interval, bitcoin_limit):
    print("Welcome :) ")
    bitcoin_data = [] 
    BITCOIN_ALERT_LIMIT = float(alert[0])
    TIME_INTERVAL = float(time_interval[0])
    while True:
        bitcoin_current_amount = fetchBitcoin()
        date = datetime.now()
        bitcoin_data.append(
            {'date': date, 'bitcoin_current_amount': bitcoin_current_amount})
        if bitcoin_current_amount < BITCOIN_ALERT_LIMIT:
            postPushFunc(
                'bitcoin_price_emergency_alert', bitcoin_current_amount)
        if len(bitcoin_data) == bitcoin_limit[0]:
            postPushFunc('bitcoin_price_update',
                                         telegramMessage(bitcoin_data))
            bitcoin_data = []
        time.sleep(TIME_INTERVAL*60)


# TELEGRAM MASTER DRIVER THAT FETCHES THE DATA AND POST TO TELEGRAM
def telegram_master_driver(alert, time_interval, bitcoin_limit):
    print("Welcome :) ")
    bitcoin_data = []
    BITCOIN_ALERT_LIMIT = float(alert[0])
    TIME_INTERVAL = float(time_interval[0])
    while True:
        bitcoin_current_amount = fetchBitcoin()
        date = datetime.now()
        bitcoin_data.append(
            {'date': date, 'bitcoin_current_amount': bitcoin_current_amount})
        if bitcoin_current_amount < BITCOIN_ALERT_LIMIT:
            postTelegramFunc(
                'bitcoin_price_emergency_alert', bitcoin_current_amount)
        if len(bitcoin_data) == bitcoin_limit[0]:
            postTelegramFunc('bitcoin_price_update',
                                telegramMessage(bitcoin_data))
            bitcoin_data = []
        time.sleep(TIME_INTERVAL*60)

# TWITTER MASTER DRIVER THAT FETCHES THE DATA AND POST TO TWITTER
def twitter_master_driver(alert, time_interval, bitcoin_limit):
    print("Welcome :) ")
    bitcoin_data = []
    BITCOIN_ALERT_LIMIT = float(alert[0])
    TIME_INTERVAL = float(time_interval[0])
    while True:
        bitcoin_current_amount = fetchBitcoin()
        date = datetime.now()
        bitcoin_data.append(
            {'date': date, 'bitcoin_current_amount': bitcoin_current_amount})
        if bitcoin_current_amount < BITCOIN_ALERT_LIMIT:
            postTwitterFunc(
                'bitcoin_price_emergency_alert', bitcoin_current_amount)
        if len(bitcoin_data) == bitcoin_limit[0]:
            postTwitterFunc('bitcoin_price_update',
                                telegramMessage(bitcoin_data))
            bitcoin_data = []
        time.sleep(TIME_INTERVAL*60)

# SMS MASTER DRIVER THAT FETCHES THE DATA AND POST TO ANDROID PHONE
def sms_master_driver(alert, time_interval, bitcoin_limit):
    print('Welcome :)')
    phoneNumber = input(
        'Enter the Phone Number with ISD Code Ex: 918074220270==> ')
    bitcoin_log = []
    BITCOIN_ALERT_LIMIT = float(alert[0])
    TIME_INTERVAL = float(time_interval[0])
    while True:
        bitcoin_current_amount = fetchBitcoin()
        date = datetime.now()
        bitcoin_log.append(
            {'date': date, 'bitcoin_current_amount': bitcoin_current_amount})

        if bitcoin_current_amount < BITCOIN_ALERT_LIMIT:
            postSMSFunc(
                'bitcoin_price_emergency_alert', bitcoin_current_amount, phoneNumber)

        if len(bitcoin_log) == bitcoin_limit[0]:
            postSMSFunc('bitcoin_price_update',
                                   smsMessage(bitcoin_log), phoneNumber)
            bitcoin_log = []

        time.sleep(TIME_INTERVAL*60)

# THIS IS THE MATRIX OF THIS APP,WHICH TAKES THE INPUT THROUGH CLI AND PASSES IT DOWN.
def mainControlFunc():
    input = argparse.ArgumentParser(
        description='Bitcoin Price Alert App.', epilog='This Script helps in sharing Real-Time Bitcoin Prices to Appropriate Services')

    input.add_argument('-a', '--alert_amount', type=int, nargs=1, default=[
                           10000], metavar='alert_amount', help='The price of 1 bitcoin when an emergency alert will be sent. Default is 10000 USD')

    input.add_argument('-t', '--time_interval', type=int, nargs=1, default=[
                           5], metavar='time_interval', help='The Frequency at which the the Bitcoin value is going to be Fetched from Server')

    input.add_argument('-l', '--logLength', type=int, nargs=1, default=[
                           2], metavar='logLength', help='The number of Entries you would like to Send,the default is #2 Entries')

    input.add_argument('-d', '--destination_app', metavar='destination_app',
                           help='The Messaging Service Destiation 1. Telegram  2. SMS  3. Twitter 4. IFTTT', required=True)

    args = input.parse_args()

    # this is the switch control this will call only that function that is mentioned
    # by user and transfer the control to it.
    if(args.destination_app == 'telegram'):
        print('Join this Channel https://t.me/piyushBitcoin .')
        telegram_master_driver(
            args.alert_amount, args.time_interval, args.logLength)
    if(args.destination_app == 'ifttt'):
        print('To Receive a Push Notification in IFTTT App')
        ifttt_master_driver(args.alert_amount,
                            args.time_interval, args.logLength)
    if(args.destination_app == 'sms'):
        print('You will Receive a Text-Message from this Number +91 8074220270')
        sms_master_driver(args.alert_amount,
                            args.time_interval, args.logLength)
    if(args.destination_app == 'twitter'):
        print('Follow this Account https://twitter.com/piyushcodes .')

        twitter_master_driver(args.alert_amount,
                            args.time_interval, args.logLength)


if __name__ == '__main__':

    # MASTER FUNCTION
    mainControlFunc()

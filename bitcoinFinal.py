

import requests
import time
import json
import argparse
from datetime import datetime
from requests import Request, Session

# COINMARKET-API-URL
COINMARKET_URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
# IFTTT WEBHOOKS-TELEGRAM-URL
WEBHOOKS_TELEGRAM_URL = "https://maker.ifttt.com/trigger/bitcoinTelegram1/with/key/g2fW8tTnrigBgQ67BktfNdINEslhjApQsujQIx-eHKF"


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
# ifttt webhook-ifttt notification applet url to send notofications on ifttt app
# IFTTT_WEBHOOK_PUSH_NOTIFICATION = "https://maker.ifttt.com/trigger/bitcoin_price_emergency_alert/with/key/ndVpfq0Cj212OhPhvOuYtHCV6IBK_0ZOWQl1oWqjqkv"




# @ GET
# FETCH BITCOIN PRICE FROM COINMARKET
def fetchBitcoin():
    print(' The Bitcoin Price is Being Fetched (^_^).')
    session = requests.Session()
    print('Breathe in .')
    print(' Breathe Out .')
    session.headers.update(headers)

    response = session.get(COINMARKET_URL, params=parameters)
    data = json.loads(response.text)
    print(' . . . . . We are Almost There!. . . . .')

    price = float(data['data'][0]['quote']['INR']['price'])
    

    return round(price)

# @ POST 
# SEND BITCOIN PRICE AS PUSH NOTIFICATION
def postPushFunc(event, value):
    print('postPushFunc()')
    data = {'value1': value}

    post_event = IFTTT_WEBHOOK_PUSH_NOTIFICATION.format(event)

    requests.post(post_event, json=data)
    print('THANKS FOR YOUR PATIENCE (T_T)')

    print('Please Check Notification(*_*) ')

# @ POST 
# SEND BITCOIN PRICE AS TELEGRAM NOTIFICATION
def postTelegramFunc(event, value):
    data = {'value1': value}

    post_event = WEBHOOKS_TELEGRAM_URL.format(event)

    requests.post(post_event, json=data)

    print('Please Check Telegram Channel (*_*) ')
    print("https://t.me/piyushBitcoin")

# FORMAT TELEGRAM MESSAGE
def telegramMessage(bitcoin_data):
    print('Beautifying your Telegram Message (#_#)')
    rows = []
    for bitcoin_value in bitcoin_data:
        date = bitcoin_value['date'].strftime('%d.%m.%Y %H:%M')
        value = bitcoin_value['bitcoin_current_amount']
        row = '{}: ₹ <b>{}</b>'.format(date, value)
        rows.append(row)
    return '<br>'.join(rows)



# ifttt push notification master driver function that runs to fetch BTC value and send a push notification
def ifttt_master_driver(alert, time_interval, bitcoin_limit):
    print('Please wait from sometime the app is running you will be prompted when the notification is sent')
    bitcoin_data = []  ##containing the msg
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


# THIS IS THE MATRIX OF THIS APP,WHICH TAKES THE INPUT THROUGH CLI AND PASSES IT DOWN.
def mainControlFunc():
    input = argparse.ArgumentParser(
        description='Bitcoin Price Alert App.', epilog='This app gives the value of 1 BTC in INR')

    input.add_argument('-a', '--alert_amount', type=int, nargs=1, default=[
                           10000], metavar='alert_amount', help='The price of 1 bitcoin when an emergency alert will be sent. Default is 10000 USD')

    input.add_argument('-t', '--time_interval', type=int, nargs=1, default=[
                           5], metavar='time_interval', help='The time interval in minutes after which the lastest value of bitcoin will be fetched. Defalut is 5 minutes')

    input.add_argument('-l', '--log_lenght', type=int, nargs=1, default=[
                           2], metavar='log_lenght', help='The number of records/entries you want example 5 entries at 5 minutes interval. Default length is 2')

    input.add_argument('-d', '--destination_app', metavar='destination_app',
                           help='The mobile application on which you want to recive alert. Destination app options are (1) IFTTT app, (2) Telegram App, (3) Email', required=True)

    args = input.parse_args()

    print('Bitcoin App started with time interval of ',
          args.time_interval[0], ' and threshold = $',  args.alert_amount[0], 'for destination ', args.destination_app)

    # this is the switch control this will call only that function that is mentioned
    # by user and transfer the control to it.
    if(args.destination_app == 'telegram'):
        print('Join this Channel https://t.me/piyushBitcoin .')
        telegram_master_driver(
            args.alert_amount, args.time_interval, args.log_lenght)
    if(args.destination_app == 'ifttt'):
        ifttt_master_driver(args.alert_amount,
                            args.time_interval, args.log_lenght)


if __name__ == '__main__':

    # calling the master control to start the app.
    mainControlFunc()
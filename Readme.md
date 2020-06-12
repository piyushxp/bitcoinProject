[![js-standard-style](https://img.shields.io/badge/code%20style-standard-brightgreen.svg?style=flat)](https://github.com/feross/standard)

![#f03c15](https://via.placeholder.com/15/f03c15/000000?text=+) ![#c5f015](https://via.placeholder.com/15/c5f015/000000?text=+) ![#1589F0](https://via.placeholder.com/15/1589F0/000000?text=+)

# Bitcoin Alert [![Twitter Follow](https://img.shields.io/twitter/follow/piyushcodes?style=social)](https://twitter.com/piyushcodes)

##### What is Bitcoin?

> Bitcoin offers an efficient means of transferring money over the internet and is controlled by a decentralized network with a transparent set of rules, thus presenting an alternative to central bank-controlled fiat money.

##### Advantage of Bitcoin:

>     By using a cryptocurrency, users are able to exchange value digitally without third party oversight

##### Problem Faced by Users:

> The main Issue with Bitcoin is that it is "FICKLE THING" and its value changes every minute.

## BITCOIN-ALERT PROJECT:

> #### This Project consistes of a "Bitcoin-Notification Messaging Service" that can be used to send Real-Time Bitcoin Prices to target Messaging Service like Telegram,Twitter,Phone SMS and Push Notification(IFTTT App)

# Installation Guide:

> step by step series of examples and explanations about how to get your development env running :)

##### Step 1

- Either Download the Repo,Which you will find at the top right of [Repo link](https://github.com/piyush-mahapatra-au6/bitcoinProject) or clone it in your Local Machine.
  ```sh
  git clone https://github.com/piyush-mahapatra-au6/bitcoinProject.git
  ```

##### Step 2

- Go into the Folder containing the Project Files
  ```sh
  cd bitcoinProject
  ```

##### Step 3

- Make Sure that your Machine has Python 3.6+
- Run the follwing Command
  ```python
  $ python3 bitcoinAlert.py --help
  ```

##### Step 4

- Then,you will see the following options

  ```sh
  -h, --help           -- Help with this Application
  -a alertPrice
                        The price of 1 bitcoin when an emergency alert will be
                        sent. Default is 10000 USD
  -t timeFrequency
                        The Frequency at which the the Bitcoin value is going
                        to be Fetched from Server
  -l logLength
                        The number of Entries you would like to Send,the
                        default is #2 Entries
  -d destination_app
                        The Messaging Service Destiation 1. Telegram
                        2. SMS
                        3. Twitter
                        4. IFTTT

  -c currency        INR
  ```

## Visual Guide for Command Line:

> Run the below mentioned appropriate commands for the Target Applications,in the Terminal.
> ![](images/proof.png)

## Target Applications:

|         Telegram          |         Twitter          |         SMS          |
| :-----------------------: | :----------------------: | :------------------: |
| ![](images/telegrams.jpg) | ![](images/twitters.jpg) | ![](images/smss.jpg) |

## Python Packages & Libraries Used

- Request
- time
- Argparser
- Tqdm (For Progress bar)

## Technologies Used:

- Python 3.8
- HTTPS
- Webhooks
- Messaging Platforms Available:
  - Telegram
  - IFTTT App
  - Twitter
  - Android SMS

## API Reference

- [CineMarket Docs](https://coinmarketcap.com/api/documentation/v1/)
- [IFTTT API reference](https://platform.ifttt.com/docs/api_reference)

## Future Scope:

- Build a GUI for this project
- Expand the Messaging Platforms
- Include other Cryptocurrency for this Project.

## Contribute

BicoinAlert is built on with Python 3.6 and IFTTT service. If you are new to this ,head over to this page
[IFTTT docs and Integration](https://platform.ifttt.com/docs)

## Credits [![Twitter Follow](https://img.shields.io/twitter/follow/piyushcodes?style=social)](https://twitter.com/piyushcodes)

- Medium Articles
- Stackoverflow
- RealPython

## License

MIT © [piyush Mahapatra]()
![](images/bitcoin50.jpg) [![Windows Build Status](https://ci.appveyor.com/api/projects/status/github/akashnimare/foco?branch=master&svg=true)](https://github.com/piyush-mahapatra-au6)

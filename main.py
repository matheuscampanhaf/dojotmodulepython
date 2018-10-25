from dojotmodulepython import config
from dojotmodulepython.kafka import Consumer
from dojotmodulepython.kafka import TopicManager
from dojotmodulepython.kafka import Producer
from dojotmodulepython import auth
from dojotmodulepython import Messenger

def main():
    print(config.dojot['subjects']['tenancy'])
    messenger = Messenger("Matheus")
    messenger.init()

if __name__=="__main__":
    main()
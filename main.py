from dojotmodulepython import config
from dojotmodulepython.kafka import Consumer
from dojotmodulepython.kafka import TopicManager
from dojotmodulepython.kafka import Producer
from dojotmodulepython import auth
from dojotmodulepython import Messenger

def main():
    messenger = Messenger("Matheus",None)
    messenger.init()

if __name__=="__main__":
    main()
from dojotmodulepython import config
from dojotmodulepython.kafka import Consumer
from dojotmodulepython.kafka import TopicManager
from dojotmodulepython.kafka import Producer

def main():
    prod = Producer()
    prod.send_msg("admin",config.dojot['subjects']['devices'],"data")

if __name__=="__main__":
    main()
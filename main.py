from dojotmodulepython import config
from dojotmodulepython.kafka import Consumer
from dojotmodulepython.kafka import TopicManager
from dojotmodulepython.kafka import Producer
from dojotmodulepython import auth


def main():
    tenants = auth.get_tenants()
    print(tenants)
if __name__=="__main__":
    main()
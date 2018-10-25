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
    print("\n")
    messenger.create_channel(config.dojot['subjects']['device_data'], "w")
    messenger.publish(config.dojot['subjects']['device_data'], "admin", {
        "metadata": {
            "deviceid": "c6ea4b",
            "tenant": "admin",
            "timestamp": 1528226137452,
            "templates": [2, 3]
        },
        "attrs": {
            "humidity": 60
        }
    })


if __name__ == "__main__":
    main()

from dojotmodulepython import config
from dojotmodulepython.kafka import Consumer
from dojotmodulepython.kafka import TopicManager
from dojotmodulepython.kafka import Producer
from dojotmodulepython import auth
from dojotmodulepython import Messenger
import time


def does_nothing(tenant,data):
    print("[SUCCESS] received message!!! tenant: %s, data: %s" % (tenant,data))

def main():
    print(config.dojot['subjects']['tenancy'])
    messenger = Messenger("Matheus")
    messenger.init()
    print("\n")
    messenger.create_channel(config.dojot['subjects']['device_data'], "rw")
    messenger.on("device-data","message",does_nothing,True)
    time.sleep(1)
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
    time.sleep(1)
    print("\n")
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
    time.sleep(1)
    print("\n")
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
    print("\n")

    messenger.publish(config.dojot['subjects']['tenancy'], config.dojot['management_service'], {"tenant":"matheus"})
    messenger.create_channel(config.dojot['subjects']['device_data'], "r")
    messenger.on(config.dojot['subjects']['devices'], "message", does_nothing)
    time.sleep(2)
    print("\n")
    messenger.create_channel(config.dojot['subjects']['tenancy'],"rw")
    messenger.publish(config.dojot['subjects']['tenancy'], config.dojot['management_service'], {"tenant":"matheus"})
    print("Please send that there is a new tenant")
    print("WANNA PUBLISH ON NEW TENANT")
    print("\n")
    messenger.publish(config.dojot['subjects']['device_data'], "matheus", {
        "metadata": {
            "deviceid": "c6ea4b",
            "tenant": "matheus",
            "timestamp": 1528226137452,
            "templates": [2, 3]
        },
        "attrs": {
            "humidity": 60
        }
    })


if __name__ == "__main__":
    main()

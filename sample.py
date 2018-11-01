from dojotmodulepython import Messenger, config
import time
from dojotmodulepython.Logger import Log


LOGGER = Log().color_log()
def rcv_msg(tenant,data):
    LOGGER.critical("rcvd msg from tenant: %s -> %s" % (tenant,data))


def main():
    messenger = Messenger("Dojot-Snoop")
    messenger.init()
    messenger.create_channel(config.dojot['subjects']['device_data'], "rw")
    messenger.create_channel(config.dojot['subjects']['tenancy'], "rw")
    messenger.create_channel(config.dojot['subjects']['devices'], "rw")

    messenger.on(config.dojot['subjects']['device_data'], "message", rcv_msg)
    messenger.on(config.dojot['subjects']['tenancy'], "message", rcv_msg)
    messenger.on(config.dojot['subjects']['devices'], "message", rcv_msg)

if __name__=="__main__":
    main()
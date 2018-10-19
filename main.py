from dojotmodulepython import config
from dojotmodulepython.kafka import Consumer

def main():
    print(config.data_broker['host'])
    cons = Consumer()

if __name__=="__main__":
    main()
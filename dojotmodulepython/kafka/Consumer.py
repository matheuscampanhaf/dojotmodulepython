from kafka import KafkaConsumer
from kafka.errors import KafkaTimeoutError
from ..Config import config
from .TopicManager import TopicManager
import json
import time

class Consumer:

    def __init__(self, topic, callback, group_id, name=None):
        
        self.topic = topic
        self.broker = [config.kafka['host']]
        self.group_id = group_id
        self.consumer = None
        self.callback = callback

    def wait_init(self):
        init = False
        while not init:
            try:
                self.consumer.poll()
                self.consumer.seek_to_end()
                init = True
            except AssertionError as error:
                print("Ignoring assertion error %s %s" % (self.topic,error))
                time.sleep()

    def run(self):
        print("Creating consumer on %s on group %s and topic %s" % (self.broker, self.group_id, self.topic))
        self.consumer = KafkaConsumer(bootstrap_servers=self.broker, group_id=self.group_id)
        self.consumer.subscribe(topics=[self.topic])
        self.wait_init()
        print("Consumer created %s" % self.topic)

        for msg in self.consumer:
            print("Got new kafka event %s %s" % (self.topic, msg))
            try:
                self.callback(msg)
            except Exception as error:
                print("Data handler raised an unknown exception. Ignoring: %s" % error)


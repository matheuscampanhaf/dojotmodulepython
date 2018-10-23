from kafka import KafkaProducer
from kafka.errors import KafkaTimeoutError
from ..Config import config
from .TopicManager import TopicManager
import json


class Producer:

    def __init__(self):
        self.broker = [config.kafka['host']]
        self.topic_manager = TopicManager()

    def init(self):
        try:
            self.producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('utf-8'),
                                          bootstrap_servers=self.broker)
            return 1
        except AssertionError as error:
            print("Ignoring assertion error on kafka producer %s" % error)
            return 0

    def send_msg(self, tenant, subject, data):
        try:
            topic = self.topic_manager.get_topic(
                tenant, subject, config.data_broker['host'])
            print("topic for %s is %s" %
                  (config.dojot['subjects']['devices'], topic))

            if topic is None:
                print(" Failed to retrieve named topic to publish to")

            self.producer.send(topic, data)
            self.producer.flush()
        except KafkaTimeoutError:
            print("Kafka timed out")

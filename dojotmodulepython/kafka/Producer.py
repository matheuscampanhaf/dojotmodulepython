from kafka import KafkaProducer
from kafka import KafkaConsumer
from kafka.errors import KafkaTimeoutError
from ..Config import config
from .TopicManager import TopicManager
import json

class DeviceEvent:
    create = "create"
    update = "update"
    remove = "remove"
    configure = "configure"
    template = "template.update"



kafka_address = config.kafka['host'] + ":" + config.kafka['port']

topic_manager = TopicManager()
producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('utf-8'),
                             bootstrap_servers=kafka_address)

def send_msg(tenant, data):
    try:
        topic = topic_manager.get_topic(tenant, config.dojot['subjects']['devices'], config.data_broker['host'])
        print("topic for %s is %s" % (config.dojot['subjects']['devices'], topic))

        if topic is None:
            print(" Failed to retrieve named topic to publish to")

        producer.send(topic, data)
        producer.flush()
    except KafkaTimeoutError:
        print("Kafka timed out")



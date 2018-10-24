import json
import uuid
from .kafka import Producer
from .kafka import TopicManager
from .kafka import Consumer
from .Config import config
from .Auth import auth


class Messenger():

    def __init__(self, name, config=None):
        self.topic_manager = TopicManager()
        self.event_callbacks = dict()
        self.tenants = []
        self.subjects = dict()
        self.topics = []
        self.producer_topics = dict()
        self.global_subjects = dict()
        self.queued_messages = []
        self.instance_id = name + str(uuid.uuid4())
        self.config = config

        producer = Producer()
        ret = producer.init()

        if ret:
            print("Producer for module %s is ready" % self.instance_id)
            print("Sending pending messages")
            for msg in self.queued_messages:
                self.publish(msg['subject'], msg['tenant'], msg['message'])
            queued_messages = []
        else:
            print("Could not create producer")
            # TODO: process.exit()

        #self.create_channel(self.config.dojot['subjects']['tenancy'], "r", True)



    def init(self):
        """
        Initializes the messenger and sets with all tenants
        """
        self.on(config.dojot['subjects']['tenancy'],
                "message", self.process_new_tenant)
        try:
            ret_tenants = auth.get_tenants()
            print("Retrieved list of tenants")
            for ten in ret_tenants:
                print("Bootstraping tenant: %s" % ten)
                self.process_new_tenant(config.dojot['management_service'], json.dumps({"tenant": ten}))
                print("%s bootstrapped." % ten)
                print("tenants: %s" % self.tenants)
            print("Finished tenant boostrapping")
        except Exception as error:
            print("Could not get list of tenants: %s" % error)
        # TODO: try again



    def process_new_tenant(self, tenant, msg):
        """
            Process new tenant: bootstrap it for all subjects registered
            and emit an event
        """
        print("Received message in tenanct subject.")
        print("Tenant is: %s" % tenant)
        print("Message is: %s" % msg)
        try:
            data = json.loads(msg)

        except Exception as error:
            print("Data is not a valid JSON. Bailing out.")
            print("Error is: %s" % error)
            return

        if("tenant" not in data):
            print("Received message is invalid. Bailing out.")
            return

        if(data['tenant'] in self.tenants):
            print("This tenant was already registered. Bailing out.")
            return

        self.tenants.append(data['tenant'])
        for sub in self.subjects:
            a="a"
            # self.bootstrap_tenant(sub, tenant, self.subjects[sub]['mode'])
        self.emit(config.dojot['subjects']['tenancy'], config.dojot['management_service'], "new-tenant", data['tenant'])



    def emit(self, subject, tenant, event, data):
        """
            Executes all callbacks related to that subject@event
        """
        print("Emitting new event %s for subject %s@%s" %
              (event, subject, tenant))
        if(subject not in self.event_callbacks):
            print("No on is listening to subject %s events" % subject)
            return
        if(event not in self.event_callbacks[subject]):
            print("No one is listening to subject %s %s events" %
                  (subject, event))
            return
        for callback in self.event_callbacks[subject][event]:
            callback(tenant, data)



    def on(self, subject, event, callback):
        """
            Register new callbacks to be invoked when something happens to a subject
            The callback should have two parameters: tenant, data
        """
        print("Registering new callback for subject %s and event %s" % (subject, event))

        if (subject not in self.event_callbacks):
            self.event_callbacks[subject] = dict()

        if (event not in self.event_callbacks[subject]):
            self.event_callbacks[subject][event] = []

        self.event_callbacks[subject][event].append(callback)

        if(subject not in self.subjects and subject not in self.global_subjects):
            self.create_channel(subject)

    

    def create_channel(self, subject, mode="r", is_global=False):
        """
            Creates a new channel tha is related to tenants, subjects, and kafka
            topics.
        """

        print("Creating channel for subject: %s" % subject)

        associated_tenants = []

        if(is_global == True):
            associated_tenants = [config.dojot['management_service']]
        else:
            associated_tenants = self.tenants
            self.tenants[subject] = {"mode": mode}
        
        for tenant in associated_tenants:
            self.__bootstrap_tenants(subject, tenant, mode, is_global)

    

    def __bootstrap_tenants(self, subject, tenant, mode, is_global=False):
        """
            TODO: write something
        """

        print("Bootstraping tenant %s for subject %s" % (tenant,subject))
        print("Global: %s, mode: %s" % (is_global, mode))

        print("Requesting topic for %s@%s" % (subject,tenant))

        try:
            ret_topic = self.topic_manager.get_topic(tenant, subject, config.data_broker['host'], is_global)
            
            if (ret_topic in self.topics):
                print("Already have a topic for %s@%s" % (subject,tenant))
                return

            print("Got topic for subject %s and tenant %s: %s" % (subject,tenant,ret_topic))
            self.topics.append(ret_topic)

            if ("r" in mode):
                self.consumer.subscribe(topic, callback)

            if("w" in mode):
                print("Adding a producer topic.")
                if (subject not in self.producer_topics):
                    self.producer_topics[subject] = dict()
                self.producer_topics[subject][tenant] = ret_topic
        except Exception as error:
            print("Could not get topic: %s" % error)

    def __process_kafka_messages(self, subject, tenant, messages):
        print("Received messages: %s" %s messages)
        self.emit(subject, tenantm "message", messages['value'].encode('utf-8'))



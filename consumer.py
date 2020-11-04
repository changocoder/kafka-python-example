from kafka import KafkaConsumer
import json
import sys

bootstrap_servers = ['xxxxxxxxxxxxxx:9092']

topicName = 'sample'

consumer = KafkaConsumer(topicName, group_id='group1',
                         bootstrap_servers=bootstrap_servers)

for msg in consumer:
    print(json.loads(msg.value))

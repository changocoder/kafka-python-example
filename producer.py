from kafka import KafkaProducer
import json
producer = KafkaProducer(bootstrap_servers='xxxxxxxxxxxxxx:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))
message = {
    'msg': 'hola mundo'
}
for x in range(100):
    producer.send('sample', json.dumps(message))
    #producer.send('Cameras', key=b'message-two', value=b'This is Kafka-Python')
    print("send", message)

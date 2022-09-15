### Overview



1) In the root directory, run ````docker-compose up````
2) Enter the listener container with ```docker-compose exec listener-service bash```
3) And run the python script to start seeing the messages as they are being published to the events topic in the Kafka container ````python3 kafka_consumer.py````

The messages published to the events topic in Kafka mimic real time messages that are constantly being generated as a result of our activity on websites and apps.
These messages are then buffered into the Kafka cluster waiting for a consumer that 'subscribes' to the topic. The consumer will get every single message
published into the topic it subscribed to so as long as the subscription remains active. If another consumer subscribes to the same topic, each consumer will get a copy of each message, therefore 
enabling one-to-one, one-to-many, many-to-one and many-to-many patterns.





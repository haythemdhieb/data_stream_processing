### Overview



1) In the root directory, run ````docker-compose up````
2) Enter the listener container with ```docker-compose exec processing-service ./launch.sh```
3) And run the python script to start seeing the messages as they are being published to the events topic in the Kafka container ````python3 kafka_consumer.py````





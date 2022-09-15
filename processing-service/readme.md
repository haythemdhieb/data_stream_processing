### Overview

This ETL pipeline was built as part of a series of interviews for a senior data engineer role in which I had to build
a data system that would process real time messages from a Kafka topic.

I show an example of how such streaming workflow could be set up in a scalable, robust and easy-to-integrate manner. 
Structured Streaming is a module of Apache Spark that can ingest and process
a huge volume of incoming files in almost real time. It integrates seamlessly with real-time data ingestion platforms (Kafka, Kinesis) and it provides a bunch
of connectors for SQL and NoSQL databases (MySQL, Mongo), data lakes (S3, GCS, etc.), and data warehouses (Redshift, BigQuery).

This project requires Docker and Docker Compose installed on your local machine (the Docker images were specified for the M1 chip on Mac):

1) In the root directory, run ````docker-compose up````
2) Enter the listener container with ```docker-compose exec listener-service bash```
3) And run the python script to start seeing the messages as they are being published to the events topic in the Kafka container ````python3 kafka_consumer.py````

The messages published to the events topic in Kafka mimic real time messages that are constantly being generated as a result of our activity on websites and apps.
These messages are then buffered into the Kafka cluster waiting for a consumer that 'subscribes' to the topic. The consumer will get every single message
published into the topic it subscribed to so as long as the subscription remains active. If another consumer subscribes to the same topic, each consumer will get a copy of each message, therefore 
enabling one-to-one, one-to-many, many-to-one and many-to-many patterns.

Please build a data system that ingests, processes and stores these processed messages. Bear in mind that the proposed data system needs to be scalable, and suitable for analytical workloads.




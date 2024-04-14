# DataStream-SQLServer

DataStream-SQLServer provides real-time data streaming from SQL Server using Zookeeper, Kafka, and Debezium. This repository contains the necessary configurations, Docker setups, and sample code to get you started.

# Table of Contents

- Requirements
- Setting Up
- Commands and Usage
- Managing Kafka Cluster
- Customization
- License

# Before you start, ensure you have the following installed:

Docker
Docker Compose
Kafka Manager (optional)
Setting Up

# Enable CDC on SQL Server
Run the SQL commands in commands/cdc-enable.sql to enable Change Data Capture (CDC) on your SQL Server database and table.

sql

-- Enable CDC on the database
EXEC sys.sp_cdc_enable_db;

-- Enable CDC on the table
EXEC sys.sp_cdc_enable_table 
@source_schema = N'dbo', 
@source_name = N'customers', 
@role_name = NULL;

# Configuration
Adjust docker-workspace/config.json to suit your SQL Server and Kafka configurations. This file is used by Debezium to connect to your SQL Server database and Kafka cluster.

json

{
    "name": "demo-db-cdc",
    "config": {
        ...
    }
}

# Commands and Usage

# Bring Up Containers
bash

docker-compose -f zookeeper-kafka.yml up -d
Kafka Topics and Management
bash

# Create a topic
kafka-topics --create --topic test-topic --bootstrap-server localhost:9092 --partitions 10 --replication-factor 1

# List topics
kafka-topics --list --bootstrap-server localhost:9092

# Delete a topic
kafka-topics --delete --topic test-topic --bootstrap-server localhost:9092
Debezium Configuration
Post your Debezium connector configuration using:

# bash

curl -X POST -H "Content-Type: application/json" --data @config.json localhost:8083/connectors/
Kafka Manager
Use Kafka Manager to manage your Kafka cluster, topics, and consumers:

Access via http://localhost:9000/
Zookeeper hosts: zookeeper:2181

# Customization

Feel free to modify configurations, add more tables, or adjust Kafka settings to suit your requirements. Remember to adjust the consumer.py script to handle new schemas or tables.


# License

This project is licensed under the MIT License - see the LICENSE.md file for details.
# DataStream-SQLServer

To stream real time data from sql server, using Zookeeper, kafka and debezium on docker desktop.

# Requirements

You have to enable the CDC on your database and table, to capture the changes.

# Kafka-Manager

You can use kafka manager to manage kafka cluster, topic, consumer through ui.
Also you can monitor the data stream.

- use below url
http://localhost:9000/

# To Capture Changes

You can adjust the config.json file or create multiple configs based on your usage.

- use below command to config the capture.
curl -X POST -H "Content-Type: application/json" --data @config.json localhost:8083/connectors/
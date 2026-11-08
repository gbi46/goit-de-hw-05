import json

from kafka import KafkaConsumer

from configs import kafka_config

consumer = KafkaConsumer(
    "temperature_alerts",
    "humidity_alerts",
    bootstrap_servers=kafka_config["bootstrap_servers"],
    security_protocol=kafka_config["security_protocol"],
    sasl_mechanism=kafka_config["sasl_mechanism"],
    sasl_plain_username=kafka_config["username"],
    sasl_plain_password=kafka_config["password"],
    group_id="alert_reader",
    auto_offset_reset="earliest",
    value_deserializer=lambda value: json.loads(value.decode("utf-8")),
)

try:
    for record in consumer:
        print(f"[{record.topic}] {record.value}")
except KeyboardInterrupt:
    pass
finally:
    consumer.close()

import json

from kafka import KafkaConsumer, KafkaProducer

from configs import kafka_config

connection = {
    "bootstrap_servers": kafka_config["bootstrap_servers"],
    "security_protocol": kafka_config["security_protocol"],
    "sasl_mechanism": kafka_config["sasl_mechanism"],
    "sasl_plain_username": kafka_config["username"],
    "sasl_plain_password": kafka_config["password"],
}

consumer = KafkaConsumer(
    "building_sensors",
    **connection,
    group_id="sensor_alerts",
    auto_offset_reset="earliest",
    value_deserializer=lambda value: json.loads(value.decode("utf-8")),
)
producer = KafkaProducer(
    **connection,
    value_serializer=lambda value: json.dumps(value).encode("utf-8"),
)

try:
    for record in consumer:
        data = record.value
        alerts = []

        if data["temperature"] > 40:
            alerts.append(("temperature_alerts", "temperature перевищує 40°C"))
        if data["humidity"] > 80 or data["humidity"] < 20:
            alerts.append(("humidity_alerts", "вологість поза межами 20–80%"))

        for topic, message in alerts:
            alert = {**data, "message": message}
            producer.send(topic, alert).get(timeout=10)
            print(alert)
except KeyboardInterrupt:
    pass
finally:
    consumer.close()
    producer.close()

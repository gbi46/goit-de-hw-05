from kafka.admin import KafkaAdminClient, NewTopic
from configs import kafka_config

TOPICS_NAME = "IoT_Topic_ivcoder"
topics_names = []
ids = ['building_sensors', 'temperature_alerts', 'humidity_alerts']

for topic_id in ids:
    topics_names.append(f"{TOPICS_NAME}_{topic_id}")

# define new topics
new_topics = [
    NewTopic(
        name=name, 
        num_partitions=2, 
        replication_factor=1
    )
    for name in topics_names
]



# create Kafka client
admin_client = KafkaAdminClient(
    bootstrap_servers=kafka_config['bootstrap_servers'],
    security_protocol=kafka_config['security_protocol'],
    sasl_mechanism=kafka_config['sasl_mechanism'],
    sasl_plain_username=kafka_config['username'],
    sasl_plain_password=kafka_config['password']
)


# create new topics
try:
    admin_client.create_topics(new_topics=new_topics, validate_only=False)
    print(f"Topics {', '.join(topics_names)} created successfully.")
except Exception as e:
    print(f"An error occurred: {e}")

# get topics list
topics = sorted(admin_client.list_topics())
print("All topics in Kafka:")
for topic in topics:
    print(f"- {topic}")

# close connection
admin_client.close()

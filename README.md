# goit-de-hw-05

Навчальний проєкт для роботи з Apache Kafka за допомогою `kafka-python`.

## Встановлення

Потрібні Python 3, `pip` і Bash. Рекомендовано створити віртуальне середовище та встановити залежності:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Скопіюйте `.env.example` у `.env` і вкажіть у ньому Kafka-облікові дані. Файл `.env` ігнорується Git.

## Запуск скриптів

Передайте `run.sh` назву потрібного скрипту без розширення:

```bash
./run.sh create_topics
./run.sh produce_sensors
./run.sh consume_sensors
./run.sh read_alerts
```

Якщо файл `run.sh` не має права на запуск, виконайте `chmod +x run.sh` або запускайте так: `bash run.sh produce_sensors`.

- `create_topics` створює Kafka-топіки.
- `produce_sensors` надсилає показники датчика в `building_sensors`.
- `consume_sensors` читає показники та надсилає сповіщення в топіки тривог.
- `read_alerts` виводить сповіщення з `temperature_alerts` і `humidity_alerts`.

Для повного сценарію спочатку створіть топіки, потім запустіть `consume_sensors` і `read_alerts` у двох окремих терміналах, а в третьому — `produce_sensors`. Скрипти-консьюмери зупиняються через `Ctrl+C`.

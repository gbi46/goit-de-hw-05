#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Usage: ./run.sh {create_topics|produce_sensors|consume_sensors|read_alerts}"
    exit 1
fi

case "$1" in
    create_topics|produce_sensors|consume_sensors|read_alerts)
        exec python3 "$1.py"
        ;;
    *)
        echo "Unknown command: $1"
        echo "Usage: ./run.sh {create_topics|produce_sensors|consume_sensors|read_alerts}"
        exit 1
        ;;
esac

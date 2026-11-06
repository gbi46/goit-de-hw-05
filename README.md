# goit-de-hw-05

Навчальний проєкт із залежністю `kafka-python`.

## Вимоги

- Python 3
- `pip`
- Bash

## Встановлення залежностей

Усі Python-залежності перелічені у файлі `requirements.txt`. Скрипт `run.sh` встановлює їх командою `pip install -r requirements.txt`.

Рекомендовано створити та активувати віртуальне середовище:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Після цього запустіть скрипт із кореневої папки проєкту:

```bash
chmod +x run.sh
./run.sh
```

Якщо файл уже має дозвіл на виконання, крок із `chmod` можна пропустити. Також можна запустити скрипт через Bash без зміни дозволів:

```bash
bash run.sh
```

Поточний `requirements.txt` встановлює `kafka-python` версії `3.0.13`. Після завершення встановлення можна перевірити пакет командою:

```bash
python -m pip show kafka-python
```

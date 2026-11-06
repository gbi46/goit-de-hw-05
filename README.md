# goit-de-hw-05

An educational project that uses the `kafka-python` dependency.

## Requirements

- Python 3
- `pip`
- Bash

## Installing dependencies

All Python dependencies are listed in `requirements.txt`. The `run.sh` script installs them with `pip install -r requirements.txt`.

We recommend creating and activating a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Then run the script from the project root:

```bash
chmod +x run.sh
./run.sh
```

If the file is already executable, you can skip the `chmod` step. You can also run the script with Bash without changing its permissions:

```bash
bash run.sh
```

The current `requirements.txt` installs `kafka-python` version `3.0.13`. After installation, you can verify the package with:

```bash
python -m pip show kafka-python
```

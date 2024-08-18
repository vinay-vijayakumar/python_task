# Python Task

    1. load_data.py - Script to read an excel file, perform aggregation and load data to sqlite3 db.
    2. main.py - Basic flask API server with 1 API endpoint.
        /data - Fetch data from the db and return if it exists.

## 1. Create virtual environment.

python3 -m venv .venv

## 2. Activate virtual environment.

source .venv/bin/activate

## 3. Install requirements.

pip install -r requirements.txt

## 4. Run the script.

python main.py

import pandas as pd
import sqlite3

from flask import Flask, request

connection = sqlite3.connect("well.db", check_same_thread=False)

app = Flask(__name__)

def read_from_db(connection, well):
    '''
        Read well data from the DB.
    '''
    return pd.read_sql(f'select * from annual_data where "API WELL  NUMBER" = {well}', connection)


@app.route("/data")
def data():
    '''
        Fetch well data from the database.
    '''
    well = request.args.get('well')
    if well and well.isnumeric():
        result = read_from_db(connection=connection, well=well)
        if len(result):
            return {
                "oil": int(result["OIL"][0]),
                "gas": int(result["GAS"][0]),
                "brine": int(result["BRINE"][0])
            }, 200
        return "No data", 404
    return "Bad Request", 400

if __name__ == "__main__":
    app.run(debug=True, port=8080)
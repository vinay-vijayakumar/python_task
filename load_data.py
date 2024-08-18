import pandas as pd
import sqlite3

def read_xls_file(file_path):
    '''
        Read the excel file 
    '''
    try:
        df = pd.read_excel(file_path)
        print(df)
        return df
    except Exception as e:
        print(e)
        return None

def calculate_annual_data(df):
    '''
        Calculate annual data for OIL, GAS, BRINE in each well.
    '''
    grouped = df.groupby(["API WELL  NUMBER", "Production Year"]).agg( 
        OIL=pd.NamedAgg(column="OIL", aggfunc="sum"),
        GAS=pd.NamedAgg(column="GAS", aggfunc="sum"),
        BRINE=pd.NamedAgg(column="BRINE", aggfunc="sum")
    )
    # print(pd.DataFrame(grouped))
    return grouped

def write_to_db(connection, data):
    '''
        Write data to the DB.
    '''
    try:
        return data.to_sql(name='annual_data', con=connection)
    except Exception as e:
        print(e)
        return False

def read_from_db(connection):
    return pd.read_sql('select * from annual_data', connection)


def main():
    connection = sqlite3.connect("well.db")
    file_path = '20210309_2020_1 - 4.xls' # Replace with file path
    if file_path:
        df = read_xls_file(file_path=file_path)
        if len(df):
            total_df = calculate_annual_data(df)
            result = write_to_db(connection=connection, data=total_df)
            if result:
                print("Data loaded to DB.")
            else:
                print('Data load failed!')
    connection.close()

if __name__ == "__main__":
    main()
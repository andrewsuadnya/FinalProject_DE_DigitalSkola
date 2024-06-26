from sqlalchemy import create_engine


def load(data, table_name):
    user = 'airflow'
    passwd = 'airflow'
    hostname = 'localhost'
    database = 'data_warehouse'

    conn_string = f'postgresql://{user}:{passwd}@{hostname}:5432/{database}'

    db = create_engine(conn_string)
    conn = db.connect()

    data.to_sql(table_name, con=conn, if_exists='append',
                index=False)

    print("Successfully loaded to postgres")

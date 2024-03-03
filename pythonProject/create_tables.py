import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def drop_tables(cur, conn):
    for query in drop_table_queries:
        try:
            cur.execute(query)
            conn.commit()
        except Exception as e:
            print(f"Failed to execute query: {query}", e)

def create_tables(cur, conn):
    for query in create_table_queries:
        try:
            cur.execute(query)
            conn.commit()
        except Exception as e:
            print(f"Failed to execute query: {query}", e)


def main():
    config = configparser.ConfigParser()
    config.read('dwh.cfg')
    try:
        conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
        print("Connected to the database")

        cur = conn.cursor()
        drop_tables(cur, conn)
        print("Tables dropped")
        create_tables(cur, conn)
        print("Tables created")


    except Exception as e:
        print("An error occurred while connecting to the database: ", e)
    finally:
        cur.close()
        conn.close()
        print("Database connection closed")



if __name__ == "__main__":
    main()
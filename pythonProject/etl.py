import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries


def load_staging_tables(cur, conn):
    """
    Loads data into staging tables based on SQL queries defined in the copy_table_queries.

    Args:
        cur: a database cursor reference, used to perform database operations
        conn: a database connection reference

    Raises:
        Exception: if unable to execute SQL query
    """
    for query in copy_table_queries:
        try:
            cur.execute(query)
            conn.commit()
        except Exception as e:
            print(f"Failed to execute query: {query}", e)


def insert_tables(cur, conn):
    """
    Inserts data into tables defined in the database based on the SQL queries defined in the insert_table_queries.

    Args:
        cur: a database cursor reference, used to perform database operations.
        conn: a database connection reference.

    Raises:
        Exception: if unable to execute SQL query.
    """
    for query in insert_table_queries:
        try:
            cur.execute(query)
            conn.commit()
        except Exception as e:
            print(f"Failed to execute query: {query}", e)


def main():
    """
    Connects to a PostgreSQL database, loads data into staging tables, and then inserts data into final tables.
    Reads database config details from a config file 'dwh.cfg'
    """
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()

    print('Loading staging tables...')
    load_staging_tables(cur, conn)
    print('inserting tables...')
    insert_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()
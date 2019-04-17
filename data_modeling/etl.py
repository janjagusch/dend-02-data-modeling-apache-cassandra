"""
This module provides methods to load the raw data, prepare it and
store it in the data warehouse.
"""
import logging

import cql_queries
from db import create_session, insert
from etl_steps.prepare import PreparerQuery1, PreparerQuery2, \
    PreparerQuery3
from utils import read_file


logging.basicConfig(filename='etl.log',level=logging.DEBUG)


def process_query_1(session, filepath):
    """
    Prepares data for table query_1.
    """
    preparer = PreparerQuery1()
    values = read_file(filepath)
    prepared_values = preparer.transform(values)
    insert(cql_queries.QUERY_1_TABLE_INSERT, prepared_values, session)


def process_query_2(session, filepath):
    """
    Prepares data for table query_2.
    """
    preparer = PreparerQuery2()
    values = read_file(filepath)
    prepared_values = preparer.transform(values)
    insert(cql_queries.QUERY_2_TABLE_INSERT, prepared_values, session)


def process_query_3(session, filepath):
    """
    Prepares data for table query3.
    """
    preparer = PreparerQuery3()
    values = read_file(filepath)
    prepared_values = preparer.transform(values)
    insert(cql_queries.QUERY_3_TABLE_INSERT, prepared_values, session)


def process_data(session, filepath, funcs):
    """
    Generic method to process data.
    Args:
        cur: a database cursor.
        conn: a database connection.
        filepath: a string filepath.
        func: a function that processes the filepath.
    """
    for func in funcs:
        func(session, filepath)


def main():
    """
    Creates the connection to the database, creates the cursor,
    and processes song- and log files.
    """
    funcs = [process_query_1, process_query_2, process_query_3]
    print("Creating connection...")
    cluster, session = create_session()
    session.set_keyspace('sparkifydb')
    print("Inserting data...")
    process_data(session, "../data/event_data_new.csv", funcs)
    print("Closing connection...")
    session.shutdown()
    cluster.shutdown()
    print("Done.")


if __name__ == "__main__":
    main()

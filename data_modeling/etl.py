"""
This module provides methods to load the raw data, prepare it and
store it in the data warehouse.
"""
from tqdm import tqdm

import cql_queries
from db import create_session, insert
from etl_steps.prepare import PreparerQuery1, PreparerQuery2, \
    PreparerQuery3
from etl_steps.read import get_files, read_file


def process_query_1(session, filepath):
    preparer = PreparerQuery1()
    values = read_file(filepath)
    prepared_values = preparer.transform(values)
    insert(cql_queries.QUERY_1_TABLE_INSERT, prepared_values, session)


def process_query_2(session, filepath):
    preparer = PreparerQuery2()
    values = read_file(filepath)
    prepared_values = preparer.transform(values)
    insert(cql_queries.QUERY_2_TABLE_INSERT, prepared_values, session)


def process_query_3(session, filepath):
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
    # get all files matching extension from directory
    all_files = get_files(filepath)

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for datafile in tqdm(all_files):
        for func in funcs:
            func(session, datafile)


def main():
    """
    Creates the connection to the database, creates the cursor,
    and processes song- and log files.
    """
    funcs = [process_query_1, process_query_2, process_query_3]
    cluster, session = create_session()
    session.set_keyspace('sparkifydb')

    process_data(session, "../data/event_data", funcs)

    session.shutdown()
    cluster.shutdown()


if __name__ == "__main__":
    main()

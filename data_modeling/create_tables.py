"""
This module provides methods to drop and re-create all tables.
"""
from db import create_session
import cql_queries


def create_database():
    """
    Creates the database and establishes the connection.
    """
    # connect to default database
    cluster, session = create_session()

    # create sparkify database with UTF8 encoding
    session.execute(cql_queries.KEYSPACE_DROP)
    session.execute(cql_queries.KEYSPACE_CREATE)

    session.set_keyspace('sparkifydb')

    return cluster, session


def drop_tables(session):
    """
    Drops all tables.
    """
    for query in cql_queries.DROP_TABLE_QUERIES:
        session.execute(query)


def create_tables(session):
    """
    Creates all tables.
    """
    for query in cql_queries.CREATE_TABLE_QUERIES:
        session.execute(query)


def main():
    """
    First, creates databse and establishes connection.
    Then, drops all tables and re-creates them.
    """
    cluster, session = create_database()

    drop_tables(session)
    create_tables(session)

    session.shutdown()
    cluster.shutdown()

if __name__ == "__main__":
    main()

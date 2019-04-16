"""
This module provides methods to interact with Cassandra.
"""
import json
import logging

from cassandra.cluster import Cluster
from cassandra import InvalidRequest


def create_session():
    """
    Creates a session with a local cluster.
    """
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect()
    return cluster, session


def insert(query, records, session):
    """
    Inserts all records with query in cursor.
    """
    for record in records:
        try:
            session.execute(query, record)
        except InvalidRequest as e:
            logging.exception(json.dumps(record))

from db import create_session
import cql_queries


def main():
    cluster, session = create_session()
    session.set_keyspace("sparkifydb")
    for i, query in enumerate(cql_queries.SELECT_TABLE_QUERIES):
        rows = session.execute(query)
        print("Query {}:".format(i + 1))
        for row in rows:
            print(" {}".format(row))
        print("")
    session.shutdown()
    cluster.shutdown()


if __name__ == "__main__":
    main()

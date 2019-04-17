"""
Answers the questions stated in the project description.
"""
from tabulate import tabulate
import pandas as pd

from db import create_session
import cql_queries


def get_answers():
    """
    Executes all SELECT_TABLE_QUERIES, stores them in pandas dataframes
    and return all in a list.
    """
    answers = []
    print("Creating connection...")
    cluster, session = create_session()
    session.set_keyspace("sparkifydb")
    print("Executing queries...")
    for i, query in enumerate(cql_queries.SELECT_TABLE_QUERIES):
        answers.append(pd.DataFrame(list(session.execute(query))))
    print("Closing connection...")
    session.shutdown()
    cluster.shutdown()
    print("Done.")
    return answers


def main():
    """
    Answers all questions and writes them into markdown.
    """
    answers = get_answers()
    for i, answer in enumerate(answers, 1):
        with open("../answers/query_{}.txt".format(i), "w") as file_pointer:
            file_pointer.write(tabulate(answer, tablefmt="pipe", headers="keys"))
    return answers

if __name__ == "__main__":
    main()

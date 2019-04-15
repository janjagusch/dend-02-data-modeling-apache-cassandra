# KEYSPACE QUERIES
KEYSPACE_CREATE = ("""
CREATE KEYSPACE IF NOT EXISTS sparkifydb
  WITH REPLICATION =
{'class' : 'SimpleStrategy', 'replication_factor' : 3}"""
                   )

KEYSPACE_DROP = ("""
DROP KEYSPACE IF EXISTS sparkifydb;
""")


# DROP QUERIES
QUERY_1_TABLE_DROP = """DROP TABLE IF EXISTS query_1;"""

QUERY_2_TABLE_DROP = """DROP TABLE IF EXISTS query_2;"""

QUERY_3_TABLE_DROP = """DROP TABLE IF EXISTS query_3;"""


# CREATE QUERIES
QUERY_1_TABLE_CREATE = (
"""
CREATE TABLE IF NOT EXISTS query_1 (artist_name VARCHAR,
                                    song_title VARCHAR,
                                    song_duration DECIMAL,
                                    session_id INT,
                                    item_in_session INT,
                                    PRIMARY KEY(session_id,
                                                item_in_session)
                                    );
""")

QUERY_2_TABLE_CREATE = (
"""
CREATE TABLE IF NOT EXISTS query_2 (artist_name VARCHAR,
                                    song_title VARCHAR,
                                    user_first_name VARCHAR,
                                    user_last_name VARCHAR,
                                    user_id INT,
                                    session_id INT,
                                    item_in_session INT,
                                    PRIMARY KEY(user_id,
                                                session_id,
                                                item_in_session)
                                    );
""")

QUERY_3_TABLE_CREATE = (
"""
CREATE TABLE IF NOT EXISTS query_3 (song_title VARCHAR,
                                    user_first_name VARCHAR,
                                    user_last_name VARCHAR,
                                    user_id INT,
                                    PRIMARY KEY(song_title,
                                                user_id
                                                )
                                    );
""")


# INSERT QUERIES
QUERY_1_TABLE_INSERT = ("""
INSERT INTO query_1 (artist_name,
                     song_title,
                     song_duration,
                     session_id,
                     item_in_session)
VALUES (%(artist_name)s,
        %(song_title)s,
        %(song_duration)s,
        %(session_id)s,
        %(item_in_session)s);
""")

QUERY_2_TABLE_INSERT = ("""
INSERT INTO query_2 (artist_name,
                     song_title,
                     user_first_name,
                     user_last_name,
                     user_id,
                     session_id,
                     item_in_session)
VALUES (%(artist_name)s,
        %(song_title)s,
        %(user_first_name)s,
        %(user_last_name)s,
        %(user_id)s,
        %(session_id)s,
        %(item_in_session)s);
""")

QUERY_3_TABLE_INSERT = ("""
INSERT INTO query_3 (song_title,
                     user_first_name,
                     user_last_name,
                     user_id)
VALUES (%(song_title)s,
        %(user_first_name)s,
        %(user_last_name)s,
        %(user_id)s);
""")


# SELECT QUERIES
QUERY_1_SELECT = ("""
SELECT artist_name,
       song_title,
       song_duration
  FROM query_1
 WHERE session_id=338
   AND item_in_session=4;
""")

QUERY_2_SELECT = ("""
SELECT artist_name,
       song_title,
       user_first_name,
       user_last_name
  FROM query_2
 WHERE user_id=10
   AND session_id=182;
""")

QUERY_3_SELECT = ("""
SELECT user_first_name,
       user_last_name
  FROM query_3
 WHERE song_title = 'All Hands Against His Own';
""")


DROP_TABLE_QUERIES = [QUERY_1_TABLE_DROP, QUERY_2_TABLE_DROP,
                      QUERY_3_TABLE_DROP]

CREATE_TABLE_QUERIES = [QUERY_1_TABLE_CREATE, QUERY_2_TABLE_CREATE,
                        QUERY_3_TABLE_CREATE]

SELECT_TABLE_QUERIES = [QUERY_1_SELECT, QUERY_2_SELECT, QUERY_3_SELECT]

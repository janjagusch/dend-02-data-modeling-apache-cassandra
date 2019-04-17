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
QUERY_1_TABLE_DROP = """DROP TABLE IF EXISTS song_in_session;"""

QUERY_2_TABLE_DROP = """DROP TABLE IF EXISTS song_in_user;"""

QUERY_3_TABLE_DROP = """DROP TABLE IF EXISTS user_in_song;"""


# CREATE QUERIES
QUERY_1_TABLE_CREATE = (
"""
CREATE TABLE IF NOT EXISTS song_in_session (
                                    session_id INT,
                                    item_in_session INT,
                                    artist_name VARCHAR,
                                    song_title VARCHAR,
                                    song_duration DECIMAL,
                                    PRIMARY KEY(session_id,
                                                item_in_session)
                                    );
""")

QUERY_2_TABLE_CREATE = (
"""
CREATE TABLE IF NOT EXISTS song_in_user (
                                    user_id INT,
                                    session_id INT,
                                    item_in_session INT,
                                    artist_name VARCHAR,
                                    song_title VARCHAR,
                                    user_first_name VARCHAR,
                                    user_last_name VARCHAR,
                                    PRIMARY KEY(user_id,
                                                session_id,
                                                item_in_session)
                                    );
""")

QUERY_3_TABLE_CREATE = (
"""
CREATE TABLE IF NOT EXISTS user_in_song (
                                    song_title VARCHAR,
                                    user_id INT,
                                    user_first_name VARCHAR,
                                    user_last_name VARCHAR,
                                    PRIMARY KEY(song_title,
                                                user_id)
                                    );
""")


# INSERT QUERIES
QUERY_1_TABLE_INSERT = ("""
INSERT INTO song_in_session (
                     session_id,
                     item_in_session,
                     artist_name,
                     song_title,
                     song_duration)
VALUES (
        %(session_id)s,
        %(item_in_session)s,
        %(artist_name)s,
        %(song_title)s,
        %(song_duration)s
        );
""")

QUERY_2_TABLE_INSERT = ("""
INSERT INTO song_in_user (
                     user_id,
                     session_id,
                     item_in_session,
                     artist_name,
                     song_title,
                     user_first_name,
                     user_last_name)
VALUES (
        %(user_id)s,
        %(session_id)s,
        %(item_in_session)s,
        %(artist_name)s,
        %(song_title)s,
        %(user_first_name)s,
        %(user_last_name)s
        );
""")

QUERY_3_TABLE_INSERT = ("""
INSERT INTO user_in_song (
                     song_title,
                     user_id,
                     user_first_name,
                     user_last_name)
VALUES (
        %(song_title)s,
        %(user_id)s,
        %(user_first_name)s,
        %(user_last_name)s
        );
""")


# SELECT QUERIES
QUERY_1_SELECT = ("""
SELECT artist_name,
       song_title,
       song_duration
  FROM song_in_session
 WHERE session_id=338
   AND item_in_session=4;
""")

QUERY_2_SELECT = ("""
SELECT artist_name,
       song_title,
       user_first_name,
       user_last_name
  FROM song_in_user
 WHERE user_id=10
   AND session_id=182;
""")

QUERY_3_SELECT = ("""
SELECT user_first_name,
       user_last_name
  FROM user_in_song
 WHERE song_title = 'All Hands Against His Own';
""")


DROP_TABLE_QUERIES = [QUERY_1_TABLE_DROP, QUERY_2_TABLE_DROP,
                      QUERY_3_TABLE_DROP]

CREATE_TABLE_QUERIES = [QUERY_1_TABLE_CREATE, QUERY_2_TABLE_CREATE,
                        QUERY_3_TABLE_CREATE]

SELECT_TABLE_QUERIES = [QUERY_1_SELECT, QUERY_2_SELECT, QUERY_3_SELECT]

INSERT_TABLE_QUERIES = [QUERY_1_TABLE_INSERT, QUERY_2_TABLE_INSERT, QUERY_3_TABLE_INSERT]

# Apache Cassandra Data Modeling Project
My solution for the data modeling with Apache Cassandra project in the Data Engineering Nanodegree on Udacity.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. The following steps are tested only for Ubuntu 18.04.

### Docker

This project comes with a docker container with Apache Cassandra and the necessary database (sparkifydb). To get the container up and running, please execute:

```
docker-compose up
```

### Virtual Environment

All necessary packages are listed in the ```requirements.txt``` file and can be installed by executing:

```
bin/setup
```

This will create a virutal environment ```env``` in your root folder.

### Running the ETL Process

To create and populate the database, execute the following commands:

```
source env/bin/activate   # activate the virtual environment
cd data_modeling          # move into the source folder
python create_tables.py   # create database and empty tables
python etl.py             # populate tables
python answer.py          # execute project queries and writes response into answers/
```

<!-- ### Testing

You can validate that everything went well with the following commands:
```
cd ..                    # move back to the root folder
bin/pytest               # test that all tables have been populated properly.
``` -->

## Answers to the Questions

### Question 1
Give me the artist, song title and song's length in the music app history that was heard during sessionId = 338, and itemInSession = 4.
```
SELECT artist_name,
       song_title,
       song_duration
  FROM query_1
 WHERE session_id=338
   AND item_in_session=4;
```

|    | artist_name   | song_title                      |   song_duration |
|---:|:--------------|:--------------------------------|----------------:|
|  0 | Faithless     | Music Matters (Mark Knight Dub) |         495.307 |

### Question 2
Give me only the following: name of artist, song (sorted by itemInSession) and user (first and last name) for userid = 10, sessionid = 182.
```
SELECT artist_name,
       song_title,
       user_first_name,
       user_last_name
  FROM query_2
 WHERE user_id=10
   AND session_id=182;
```

|    | artist_name       | song_title                                           | user_first_name   | user_last_name   |
|---:|:------------------|:-----------------------------------------------------|:------------------|:-----------------|
|  0 | Down To The Bone  | Keep On Keepin' On                                   | Sylvie            | Cruz             |
|  1 | Three Drives      | Greece 2000                                          | Sylvie            | Cruz             |
|  2 | Sebastien Tellier | Kilometer                                            | Sylvie            | Cruz             |
|  3 | Lonnie Gordon     | Catch You Baby (Steve Pitron & Max Sanna Radio Edit) | Sylvie            | Cruz             |

### Question 3
Give me every user name (first and last) in my music app history who listened to the song 'All Hands Against His Own'.
```
SELECT user_first_name,
       user_last_name
  FROM query_3
 WHERE song_title = 'All Hands Against His Own';
```

|    | user_first_name   | user_last_name   |
|---:|:------------------|:-----------------|
|  0 | Jacqueline        | Lynch            |
|  1 | Tegan             | Levine           |
|  2 | Sara              | Johnson          |

## Authors

* **Jan-Benedikt Jagusch** - *Initial work* - [jbj2505](https://github.com/jbj2505)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

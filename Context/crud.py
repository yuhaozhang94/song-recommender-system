import sqlite3
from sqlite3 import Error
import pandas as pd


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def get_tables(conn):
    table = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table';", conn)
    return table


def get_records(conn, table_name, limit=None):
    query = "SELECT * FROM " + table_name
    if limit!=None:
        query += " LIMIT " + str(limit)
    table = pd.read_sql_query(query, conn)
    return table


def create_audio_analysis(conn, record):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO audio_analysis(uri, duration, loudness, tempo, tempo_confidence,
                               time_signature, time_signature_confidence, key,
                                key_confidence, mode, mode_confidence)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    return cur.lastrowid


def create_audio_feature(conn, record):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO audio_analysis(uri, danceability, energy, key, loudness, mode, 
                               speechiness, acousticness, instrumentalness, 
                               liveness, valence, tempo)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    return cur.lastrowid
from distutils.debug import DEBUG
import sqlite3
from db.run_sql import run_sql

from models.artist import Artist
from models.album import Album


def save(artist):
    sql = "INSERT INTO artists (name) VALUES (%s) RETURNING * "
    values = [artist.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    artist.id = id
    return artist

def delete_all():
    sql = """
        DELETE FROM artists
    """
    run_sql(sql)

def select(id):
    artist = None
    sql = "SELECT * FROM artists WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        artist = Artist(result['name'], result['id'])
    return artist

def select_all():
    artists = []
    sql = "SELECT * FROM artists"
    result = run_sql(sql)

    for row in result:
        artist = Artist(row['name'], row['id'])
        artists.append(artist)
    return artists

def update(artist):
    sql = """
        UPDATE artists
        SET name = %s
        WHERE id = %s
    """
    values = [artist.name, artist.id]
    run_sql(sql, values)

def delete(id):
    sql = """
    DELETE FROM artists
    WHERE id = %s
    """
    values = [id]
    run_sql(sql, values)
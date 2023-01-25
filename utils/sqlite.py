import sqlite3
import logging

logger = logging.getLogger(__file__)


def connect():
    return sqlite3.connect("pokemon_wiki.db")


def exec(conn, stmt, args=None, fetch=True, commit=True):
    cursor = conn.cursor()
    try:
        if args:
            cursor.execute(stmt, args)
        else:
            cursor.execute(stmt)
        if commit:
            conn.commit()
        return cursor.fetchall() if fetch else None
    except:
        logger.exception("Error executing stmt: %s. args: %s", stmt, args)
        if commit:
            conn.rollback()
        raise


def exec_one(conn, stmt, args=None, fetch=True, commit=True):
    cursor = conn.cursor()
    try:
        if args:
            cursor.execute(stmt, args)
        else:
            cursor.execute(stmt)
        if commit:
            conn.commit()
        return cursor.fetchone() if fetch else None
    except:
        logger.exception("Error executing stmt: %s. args: %s", stmt, args)
        if commit:
            conn.rollback()
        raise


def insert(conn, stmt, args=None, commit=True):
    cursor = conn.cursor()
    try:
        if args:
            cursor.execute(stmt, args)
        else:
            cursor.execute(stmt)
        if commit:
            conn.commit()
        return cursor.lastrowid
    except:
        logger.exception("Error executing stmt: %s. args: %s", stmt, args)
        if commit:
            conn.rollback()
        raise

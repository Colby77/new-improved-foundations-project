"""
This file is for resetting the database for development purposes

Run with 'python reset.py'
"""


import models, database


def reset_db():
    models.Base.metadata.drop_all(
        bind=database.engine, tables=[models.User.__table__, models.Character.__table__]
        )


if __name__ == '__main__':
    reset_db()
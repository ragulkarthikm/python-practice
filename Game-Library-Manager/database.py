import sqlite3
from tabulate import tabulate
import data_models as dm


class DBManager:

    def __init__(self, DBPath):

        print("Connecting to SQLite")
        self.con = sqlite3.connect(DBPath)

        self.cur = self.con.cursor()

        self.cur.execute(
            """ CREATE TABLE IF NOT EXISTS games (
                g_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                platform TEXT,
                genre TEXT,
                release_year INTEGER,
                developer TEXT,
                storefront TEXT,
                status TEXT,
                playtime REAL,
                personal_rating INTEGER
            ); """
        )
        self.con.commit()
        print("Connected to SQLite")

    def addgame(
        self,
        name,
        platform,
        genre,
        release_year,
        developer,
        storefront,
        status,
        playtime,
        personal_rating,
    ):
        print("adding game ..../")
        self.cur.execute(
            "INSERT INTO games (name, platform, genre, release_year, developer, storefront, status, playtime, personal_rating) VALUES (?,?,?,?,?,?,?,?,?);",
            (
                name,
                platform,
                genre,
                release_year,
                developer,
                storefront,
                status,
                playtime,
                personal_rating,
            ),
        )
        self.con.commit()
        print("Game Added...")

    def allgames(self):
        print("-----------------All Games--------------------\n")
        self.cur.execute("SELECT * FROM games")
        data = self.cur.fetchall()
        print(
            tabulate(
                data,
                headers=[
                    "ID",
                    "Title",
                    "Platform",
                    "Genre",
                    "Release Year",
                    "Developer Name",
                    "Store",
                    "Status",
                    "Playtime(h)",
                    "Rating(1 to 10)",
                ],
                tablefmt="fancy_grid",
            )
        )
        print("\n")
        print("*************************************************")

    def updategame(
        self,
        name,
        platform,
        genre,
        release_year,
        developer,
        storefront,
        status,
        playtime,
        personal_rating,
        g_id,
    ):
        print("Updating Your game data............/")
        self.cur.execute(
            "UPDATE games set name=?, platform=?, genre=?, release_year=?, developer=?, storefront=?, status=?, playtime=?, personal_rating=? WHERE g_id=?;",
            (
                name,
                platform,
                genre,
                release_year,
                developer,
                storefront,
                status,
                playtime,
                personal_rating,
                g_id,
            ),
        )
        self.con.commit()
        print("Game Data Updated....")

    def deletegame(self, g_id):
        print("Deleting the game data............/")
        self.cur.execute("DELETE FROM games WHERE g_id=?;", (g_id,))
        self.con.commit()
        print("Game Deleted..")

    def DBclose(self):
        print("Disconnecting from SQLite")
        self.con.close()
        print("Disconnected from SQLite")

    def mini_stat(self):
        print(
            """
=================================
       LIBRARY DASHBOARD
=================================
"""
        )

        self.cur.execute("SELECT count(name) FROM games;")
        mstat_game_owned = self.cur.fetchone()[0]
        mstat_game_owned = mstat_game_owned or 0
        print("Total Games Owned:   ", mstat_game_owned)

        self.cur.execute("SELECT sum(playtime) FROM games;")
        mstat_pt = self.cur.fetchone()[0]
        mstat_pt = mstat_pt or 0
        print("Total Hours Played:  ", mstat_pt)

        self.cur.execute("SELECT avg(personal_rating) FROM games;")
        mstat_rating = self.cur.fetchone()[0]
        mstat_rating = mstat_rating or 0
        print("Average Game Rating: ", mstat_rating)

        self.cur.execute("SELECT COUNT(status) FROM games WHERE status = 'Completed';")
        mstat_comp = self.cur.fetchone()[0]
        print("Games Completed:     ", mstat_comp)

        print("=================================")

    def search_game(self, search_fat, keyword):

        qru = f"SELECT * FROM games WHERE {search_fat} LIKE ?"
        sf_keyword = f"%{keyword}%"
        self.cur.execute(qru, (sf_keyword,))
        s_result = self.cur.fetchall()
        print(
            tabulate(
                s_result,
                headers=[
                    "ID",
                    "Title",
                    "Platform",
                    "Genre",
                    "Release Year",
                    "Developer Name",
                    "Store",
                    "Status",
                    "Playtime(h)",
                    "Rating(1 to 10)",
                ],
                tablefmt="fancy_grid",
            )
        )

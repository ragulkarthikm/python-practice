import sqlite3


class DBManager:

    def __init__(self, DBPath):
        self.con = sqlite3.connect(DBPath)

        self.cur = self.con.cursor()

        self.cur.execute(
            """
            CREATE TABLE IF NOT EXISTS games (
                "id" INTEGER,
                "name" TEXT,
                "platform" TEXT,
                "genre" TEXT,
                "status" TEXT,
                PRIMARY KEY("id" AUTOINCREMENT)
            );"""
        )
        self.con.commit()

    def addgame(self, name, platform, genre, status):
        print("adding game ..../")
        self.cur.execute(
            "INSERT INTO games (name, platform, genre, status) VALUES (?, ?, ?, ?);",
            (name, platform, genre, status),
        )
        self.con.commit()
        print("Game Added...")

    def allgames(self):
        print("-----------------All Games--------------------")
        data = self.cur.execute("SELECT * FROM games")
        for item in data:
            print(item)

    def updategame(self, name, platform, genre, status, id):
        print("Updating Your game data............/")
        self.cur.execute(
            "UPDATE games set name=?, platform=?, genre=?, status=? WHERE id=?;",
            (name, platform, genre, status, id),
        )
        self.con.commit()
        print("Game Data Updated....")

    def deletegame(self, id):
        print("Deleting the game data............/")
        self.cur.execute("DELETE FROM games WHERE id=?;", (id,))
        self.con.commit()
        print("Game Deleted..")


db = DBManager(r"C:\Users\ASUS\OneDrive\Desktop\gamelib.db")

while True:
    print(
        """
        1 Add game
        2 View all games
        3 Update a game
        4 Delete a game
        5 Exit

        """
    )
    ch = int(input("Enter the Number : "))

    if ch == 1:
        print("Add Game")
        name = input("Enter the game name: ")
        platform = input("Enter the game platform: ")
        genre = input("Enter the game genre: ")
        status = input("Enter the game status: ")
        db.addgame(name, platform, genre, status)

    elif ch == 2:
        db.allgames()

    elif ch == 3:
        print("Update Game Data")
        id = int(input("Enter the Game data ID: "))
        name = input("Enter the game name: ")
        platform = input("Enter the game platform: ")
        genre = input("Enter the game genre: ")
        status = input("Enter the game status: ")
        db.updategame(name, platform, genre, status, id)

    elif ch == 4:
        print("Delete Game Data")
        id = int(input("Enter the Game data ID: "))
        db.deletegame(id)

    elif ch == 5:
        print(".....................Thank You.....................")
        break

    else:
        print("Invalid Number")

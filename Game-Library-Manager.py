import sqlite3


class gamedata:
    def get_g_id(self):
        while True:
            try:
                self.g_id = int(input("Enter the Game data ID: "))
            except ValueError:
                print("Please use numerical value, (Game ID : 325)")
                print("...........................................")
            else:
                break
        return self.g_id


class DBManager:

    def __init__(self, DBPath):
        self.con = sqlite3.connect(DBPath)

        self.cur = self.con.cursor()

        self.cur.execute(
            """
            CREATE TABLE IF NOT EXISTS games (
                "g_id" INTEGER,
                "name" TEXT,
                "platform" TEXT,
                "genre" TEXT,
                "status" TEXT,
                PRIMARY KEY("g_id" AUTOINCREMENT)
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
        print("-----------------All Games--------------------\n")
        data = self.cur.execute("SELECT * FROM games")
        for item in data:
            print(item)
        print("\n")
        print("*************************************************")

    def updategame(self, name, platform, genre, status, g_id):
        print("Updating Your game data............/")
        self.cur.execute(
            "UPDATE games set name=?, platform=?, genre=?, status=? WHERE g_id=?;",
            (name, platform, genre, status, g_id),
        )
        self.con.commit()
        print("Game Data Updated....")

    def deletegame(self, g_id):
        print("Deleting the game data............/")
        self.cur.execute("DELETE FROM games WHERE g_id=?;", (g_id,))
        self.con.commit()
        print("Game Deleted..")

    def DBclose(self):
        self.con.close()


db = DBManager(r"gamelib.db")
game = gamedata()

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
    try:
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
            u_g_id = game.get_g_id()
            name = input("Enter the game name: ")
            platform = input("Enter the game platform: ")
            genre = input("Enter the game genre: ")
            status = input("Enter the game status: ")
            db.updategame(name, platform, genre, status, u_g_id)

        elif ch == 4:
            print("Delete Game Data")
            u_g_id = game.get_g_id()
            db.deletegame(u_g_id)

        elif ch == 5:
            print(".....................Thank You.....................")
            break

        else:
            print("Invalid Number. Select number between 1 to 5")

    except ValueError:
        print("Please use the menu number below (1 to 5)")


db.DBclose()

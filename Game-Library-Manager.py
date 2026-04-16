import sqlite3
from tabulate import tabulate

stores_list = [
    "Steam",
    "Epic Games Store",
    "GOG",
    "Microsoft Store",
    "Xbox Store",
    "PlayStation Store",
    "Nintendo eShop",
    "Amazon Games",
    "itch.io",
    "Humble Store",
    "Ubisoft Connect",
    "EA App",
    "Battle.net",
    "Rockstar Games Launcher",
    "Green Man Gaming",
    "Fanatical",
    "Google Play Store",
]

platforms_list = [
    "Windows",
    "macOS",
    "Linux",
    "PlayStation 5",
    "PlayStation 4",
    "PlayStation 3",
    "Xbox Series X/S",
    "Xbox One",
    "Xbox 360",
    "Nintendo Switch",
    "Nintendo Wii U",
    "Nintendo Wii",
    "iOS",
    "Android",
    "Web Browser",
    "Steam Deck",
]

genres_list = [
    "Action",
    "Adventure",
    "Action-Adventure",
    "Role-Playing (RPG)",
    "JRPG",
    "Strategy",
    "Real-Time Strategy (RTS)",
    "Turn-Based Strategy (TBS)",
    "Simulation",
    "Sports",
    "Racing",
    "Fighting",
    "Shooter",
    "First-Person Shooter (FPS)",
    "Third-Person Shooter (TPS)",
    "Platformer",
    "Puzzle",
    "Survival",
    "Horror",
    "Stealth",
    "Sandbox",
    "Open World",
    "Roguelike",
    "Roguelite",
    "Metroidvania",
    "Battle Royale",
    "MMO",
    "MMORPG",
    "MOBA",
    "Card Game",
    "Board Game",
    "Visual Novel",
    "Interactive Fiction",
    "Party",
    "Music/Rhythm",
    "Educational",
    "Idle/Incremental",
]

statu_list = [
    "Not Started",
    "Playing",
    "Completed",
    "100% Completed",
    "On Hold",
    "Dropped",
    "Wishlist",
    "Backlog",
    "Replaying",
]


class gamedata:
    def get_g_id(self):
        while True:
            try:
                self.g_id = int(input("Enter the Game data ID: "))
            except ValueError:
                print("Please use numerical value, eg : (Game ID : 325)")
                print("...........................................")
            else:
                break
        return self.g_id

    def get_from_list(self, ch_list, dis_txt):
        print(dis_txt)
        for i, n in enumerate(ch_list, start=1):
            print(i, n)
        while True:
            try:
                ch = int(input("Choose a number: "))
            except ValueError:
                print("Invalid choice")
            else:
                if ch < 1 or ch > len(ch_list):
                    print("Invalid choice")
                else:
                    ch_list_num = ch - 1
                    ch_list_item = ch_list[ch_list_num]
                    print("Selected option is ", ch_list_item)
                    return ch_list_item
                    break


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


db = DBManager(r"C:\Users\ASUS\OneDrive\Desktop\gamelib.db")
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
            platform = game.get_from_list(platforms_list, "Platforms")
            genre = game.get_from_list(genres_list, "Genres")
            release_year = input("Enter the release year (eg : 2000) : ")
            developer = input("Enter the developer Name: ")
            storefront = game.get_from_list(stores_list, "Stores")
            status = game.get_from_list(statu_list, "Status")
            playtime = input("Enter the game play time")
            personal_rating = input("Enter the Game rating")
            db.addgame(
                name,
                platform,
                genre,
                release_year,
                developer,
                storefront,
                status,
                playtime,
                personal_rating,
            )

        elif ch == 2:
            db.allgames()

        elif ch == 3:
            print("Update Game Data")
            u_g_id = game.get_g_id()
            name = input("Enter the game name: ")
            platform = game.get_from_list(platforms_list, "Platforms")
            genre = game.get_from_list(genres_list, "Genres")
            release_year = input("Enter the release year (eg : 2000) : ")
            developer = input("Enter the developer Name: ")
            storefront = game.get_from_list(stores_list, "Stores")
            status = game.get_from_list(statu_list, "Status")
            playtime = input("Enter the game play time")
            personal_rating = input("Enter the Game rating")
            db.updategame(
                name,
                platform,
                genre,
                release_year,
                developer,
                storefront,
                status,
                playtime,
                personal_rating,
                u_g_id,
            )

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

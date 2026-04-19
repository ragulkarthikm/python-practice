import data_models as dm
import database as mdb


db = mdb.DBManager(r"gamelib.db")
game = dm.gamedata()

db.mini_stat()

while True:
    print(
        """
        1 Add game
        2 View all games
        3 Update a game
        4 Delete a game
        5 Search the Game
        6 Export to CSV
        7 Exit

        """
    )
    try:
        ch = int(input("Enter the Number : "))

        if ch == 1:
            print("Add Game")
            name = input("Enter the game name: ")
            platform = game.get_from_list(dm.platforms_list, "Platforms")
            genre = game.get_from_list(dm.genres_list, "Genres")
            release_year = input("Enter the release year (eg : 2000) : ")
            developer = input("Enter the developer Name: ")
            storefront = game.get_from_list(dm.stores_list, "Stores")
            status = game.get_from_list(dm.statu_list, "Status")
            playtime = input("Enter the game play time: ")
            personal_rating = input("Enter the Game rating: ")
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
            platform = game.get_from_list(dm.platforms_list, "Platforms")
            genre = game.get_from_list(dm.genres_list, "Genres")
            release_year = input("Enter the release year (eg : 2000) : ")
            developer = input("Enter the developer Name: ")
            storefront = game.get_from_list(dm.stores_list, "Stores")
            status = game.get_from_list(dm.statu_list, "Status")
            playtime = input("Enter the game play time: ")
            personal_rating = input("Enter the Game rating: ")
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
            print("=================================")
            print("      Search for Games")
            print("=================================")
            print(
                """
                1  ID
                2  Name
                3  Platform
                4  Genre
                5  Release Year
                6  Developer
                7  Storefront
                8  Status
                9  Playtime
                10 Personal Rating
                """
            )
            search_fat = game.search_type()
            keyword = input("Enter the Game search value: ")
            db.search_game(search_fat, keyword)

        elif ch == 6:
            print("Exporting Your data as CSV file")
            db.export_to_csv()
            print("Data Exported")

        elif ch == 7:
            print(".....................Thank You.....................")
            break

        else:
            print("Invalid Number. Select number between 1 to 7")

    except ValueError:
        print("Please use the menu number below (1 to 7)")


db.DBclose()

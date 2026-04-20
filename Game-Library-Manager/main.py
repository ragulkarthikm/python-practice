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
            new_game_data = game.get_all_data()
            db.addgame(new_game_data)

        elif ch == 2:
            db.allgames()

        elif ch == 3:
            print("Update Game Data")
            u_g_id = game.get_g_id()
            update_game_data = game.get_all_data()
            db.updategame(
                update_game_data,
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

import database as mdb
import requests

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

    def get_all_data(self):
        name = input("Enter the game name: ")
        platform = self.get_from_list(platforms_list, "Platforms")
        genre = self.get_from_list(genres_list, "Genres")
        release_year = self.get_num_data("Enter the release year (eg : 2010) : ")
        developer = input("Enter the developer Name: ")
        storefront = self.get_from_list(stores_list, "Stores")
        status = self.get_from_list(statu_list, "Status")
        playtime = self.get_num_data("Enter the game play time: ")
        personal_rating = self.get_rating_data()
        return (
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

    def search_type(self):
        while True:
            try:
                search_fat = int(input("Select the Game search factor: "))

            except ValueError:
                print("Invalid choice. Select number between 1 to 10")

            else:
                if search_fat == 1:
                    return f"g_id"
                elif search_fat == 2:
                    return f"name"
                elif search_fat == 3:
                    return f"platform"
                elif search_fat == 4:
                    return f"genre"
                elif search_fat == 5:
                    return f"release_year"
                elif search_fat == 6:
                    return f"developer"
                elif search_fat == 7:
                    return f"storefront"
                elif search_fat == 8:
                    return f"status"
                elif search_fat == 9:
                    return f"playtime"
                elif search_fat == 10:
                    return f"personal_rating"
                else:
                    print("Invalid Number. Select number between 1 to 10")
                return search_fat
                break

    def get_num_data(self, print_data):
        print(print_data)
        while True:
            try:
                self.g_num_data = int(input("Enter the Value: "))
            except ValueError:
                print("Please use numerical value")
                print("...........................................")
            else:
                break
        return self.g_num_data

    def get_rating_data(self):
        print("Rate you game from 1 to 10 (0 for no rating)")
        while True:
            try:
                rate = int(input("Enter the Game rating: "))
            except ValueError:
                print("Invalid choice. Select number between 0 to 10")
            else:
                if rate < 0 or rate > 10:
                    print("Invalid choice. Select number between 0 to 10")
                else:
                    return rate
                    break

    def get_api_data(self):

        api_key = "_api_key_"

        ser_c = input("Enter the game name: ")
        url = f"https://api.rawg.io/api/games?key={api_key}&search={ser_c}"

        api_resp = requests.get(url)
        data = api_resp.json()

        gamelist = data["results"]

        gamelist = data.get("results", [])

        for i, game in enumerate(gamelist[:10], start=1):
            id = game.get("id", "N/A")
            name = game.get("name", "N/A")
            released = game.get("released", "N/A")
            print(i, id, name, released)

        print("")
        game_chr = int(input("enter the game: "))
        print("")
        user_game_chr = game_chr - 1

        gid = gamelist[user_game_chr]["id"]

        url2 = f"https://api.rawg.io/api/games/{gid}?key={api_key}"

        resp2 = requests.get(url2)
        data2 = resp2.json()

        developer_name = data2.get("developers", [])

        print(data2.get("name"))
        print(developer_name[0].get("name"))
        print("")
        print(data2.get("description_raw"))

        # display "WIP"
        print("")
        print("***********************")
        print("feat - Work in progress..")
        print("***********************")
        print("")

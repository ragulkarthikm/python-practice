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

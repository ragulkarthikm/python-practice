import sqlite3

con = sqlite3.connect(r"gamelib.db")

con.execute(
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
con.commit()


def addgame():
    print("Add Game...")
    name = input("Enter the Game Title: ")
    platform = input("Enter the Game Platform: ")
    genre = input("Enter the Game Genre: ")
    status = input("Enter the Game status: ")
    con.execute(
        "INSERT INTO games (name, platform, genre, status) VALUES (?, ?, ?, ?);",
        (name, platform, genre, status),
    )
    con.commit()
    print("Game Added..")


def viewallgames():
    print("Game List..")
    result = con.execute("SELECT * FROM games")
    for item in result:
        print(item)


def updategame():
    print("Update Game Details..")
    id = int(input("Enter the Entry ID: "))
    name = input("Enter the Game Title: ")
    platform = input("Enter the Game Platform: ")
    genre = input("Enter the Game Genre: ")
    status = input("Enter the Game status: ")
    con.execute(
        "UPDATE games set name=?, platform=?, genre=?, status=? WHERE id=?;",
        (name, platform, genre, status, id),
    )
    con.commit()
    print("Game data updated..")


def deletegame():
    print("Delete Game..")
    id = int(input("Enter the Entry ID: "))
    con.execute("DELETE FROM games WHERE id=?;", (id,))
    con.commit()


while True:
    print(
        """
            1. Add Game 
            2. View Library 
            3. Update Game Status 
            4. Remove Game 
            5. Exit
           """
    )
    c = int(input("Select Your Choice : "))
    if c == 1:
        addgame()

    elif c == 2:
        viewallgames()

    elif c == 3:
        updategame()

    elif c == 4:
        deletegame()

    elif c == 5:
        print("Thank You..")
        break

    else:
        print("Invalid Selection")

con.close()

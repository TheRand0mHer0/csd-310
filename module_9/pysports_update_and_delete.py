# Anthony Murdock
# Pysports Updates & Deletes

import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "root",
    "password": "1moref##k",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True

}

get_player_records_command = "SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id"
# a 2d nested array of commands needed for the assignment
# index 0 is the cursor command and index 1 is the print statement
cursor_commands = [
        [
            "INSERT INTO player (first_name, last_name, team_id) VALUES('Smeagol', 'Shire Folk', 1)",
            " -- DISPLAYING PLAYER RECORDS AFTER INSERT -- "
        ],
        [
            "UPDATE player set team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol' ",
            " -- DISPLAYING PLAYER RECORDS AFTER UPDATE -- "
        ],
        [
            "DELETE FROM player WHERE first_name = 'Gollum' ",
            " -- DISPLAYING PLAYER RECORDS AFTER DELETE -- "
        ]
    ]

def print_player_records(players):
    for player in players:
        player_id = player[0]
        first_name = player[1]
        last_name = player[2]
        team_id = player[3]
        print(f'Player ID: {player_id}\nFirst Name: {first_name}\nLast Name: {last_name}\nTeam Name: {team_id}\n\n')

try:
    db = mysql.connector.connect(**config)

    print("\n Database user {} connected to MySQL on host {} with database {}" .format(config["user"], config["host"], config["database"]))

    input("\n\n Press any key to continue. . ." )
    cursor = db.cursor()
    # loop over cursor commands to execute
    for command in cursor_commands:
        cursor.execute(command[0])
        print(command[1])
        cursor.execute(get_player_records_command)
        players = cursor.fetchall(); 
        print_player_records(players)


except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")
    
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")
    
    else:
        print(err)

finally:
    db.close()
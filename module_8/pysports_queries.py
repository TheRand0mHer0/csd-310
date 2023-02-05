import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "root",
    "password": "1moref##k",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True

}

try:
    db = mysql.connector.connect(**config)

    print("\n Database user {} connected to MySQL on host {} with database {}" .format(config["user"], config["host"], config["database"]))

    input("\n\n Press any key to continue. . ." )
    cursor = db.cursor()

    cursor.execute("SELECT team_id, team_name, mascot FROM team")

    teams = cursor.fetchall()
    print(" -- DISPLAYING TEAM RECORDS -- ")
    for team in teams:
        team_id = team[0]
        team_name = team[1]
        mascot = team[2]
        print(f'Team ID: {team_id}\nTeam Name: {team_name}\nMascot: {mascot}\n\n')

    cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")
    players = cursor.fetchall()
    print(" -- DISPLAYING PLAYER RECORDS -- ")

    for player in players:
        player_id = player[0]
        first_name = player[1]
        last_name = player[2]
        team_id = player[3]
        print(f'Player ID: {player_id}\nFirst Name: {first_name}\nLast Name: {last_name}\nTeam ID: {team_id}\n\n')


except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")
    
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")
    
    else:
        print(err)

finally:
    db.close()


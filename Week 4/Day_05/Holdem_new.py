import psycopg2
from psycopg2 import sql

# Connect to your postgres DB
conn = psycopg2.connect(
    dbname="Poker", 
    user="postgres", 
    password="####",
    host="localhost",
    port="5432"
)

# Open a cursor to perform database operations
cur = conn.cursor()

while True:
    hand = input("Enter your starting hand\nFor example: if Ace-King Suited, type AKs \n If not, AKo: ")

    # Query database to get hand details
    cur.execute(sql.SQL("SELECT * FROM public.poker_hands WHERE hand = %s"), [hand])
    hand_details = cur.fetchone()

    if not hand_details:
        print("Hand not found in the database. Try again.")
        continue

    if hand_details[-1]:  # check if encouraged_to_be_played is True
        print("Very good hand!")
    else:
        print("Proceed with caution!")

    while True:
        num_players = input("Enter the number of players at the table (between 2 and 9): ")

        try:
            num_players = int(num_players)
        except ValueError:
            print("Invalid input. Please enter a number between 2 and 9.")
            continue

        if 2 <= num_players <= 9:
            break
        else:
            print("Invalid input. Please enter a number between 2 and 9.")

    # Extract the corresponding probability from the database
    prob = hand_details[num_players - 1]  # Adjusting index to match player count
    print(f"The probability of this hand winning with {num_players} players at the table is {prob}")

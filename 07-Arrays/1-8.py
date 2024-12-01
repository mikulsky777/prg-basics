computer_games = [
   "Minecraft", "Fortnite", "Cyberpunk 2077", "The Witcher 3",
   "League of Legends", "Valorant", "Grand Theft Auto V", 
   "Elden Ring", "Apex Legends", "Call of Duty: Warzone"
]

computer_games = sorted(computer_games)

counter = 1

while counter <= len(computer_games):
    print(f'{counter}. {computer_games[counter-1]}')
    counter += 1
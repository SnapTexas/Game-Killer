import time 
from game_manager import *
from meme_rendering import render_gif
import datetime
games={"DarkAndDarker":"Tavern.exe"}
game="DarkAndDarker"
time_data=datetime.datetime.now()
date=str(time_data.date())
print(type(date),date)
memes_path=[i for i in os.listdir("memes")]
print(memes_path)


def main():
    while True:    
        game_running=find_game(game_name=games[game])
        result=None
        if game_running:
            result=does_record_exits(date=date,game_name=game)
        if result is not None:
            
            update_game_data(date=date,total_usage=) 

            pass
        time.sleep(60)
        

main()      
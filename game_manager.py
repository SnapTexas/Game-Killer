import psutil
import os 
import signal
import time
import datetime
from db_handeling import (is_overplaying,
                          get_game_limit,
                          create_game_record,
                          find_record,
                          update_game_data)


def kill_game(game_id):
    try:
        os.kill(game_id, signal.SIGTERM)
    except ProcessLookupError:
        print("Game is not running")
    except PermissionError:
        print("Permission denied")
#Working
def find_game(game_name:str)->int|None:
    for process in psutil.process_iter():
        id=process.pid
        name=process.name()
        if name==game_name:
            return id
    return None

def get_runtime(game_id:int)->int:
    p=psutil.Process(game_id)
    start_time=datetime.fromtimestamp(p.create_time())
    run_time=datetime.now() - start_time
    return int(run_time.total_seconds()//60)

def punish(actual_time_played, game_limit):
    time_limit_1=game_limit
    time_limit_2=game_limit+(game_limit//3)
    time_limit_3=game_limit+(game_limit//2)
    if actual_time_played > time_limit_1 :
        print("Level 1")
        print("meme spam")
    if actual_time_played > time_limit_2:
        print("Level 2")
        print("messing controls")
    if actual_time_played > time_limit_3:
        print("Level 3")
        print("sms Ammi")
    
def main():
    list_of_games={"DarkAndDarker":"Tavern.exe"}
    game_name="DarkAndDarker"
    game_id=find_game(game_name,list_of_games)
    print("Game id is ",game_id)
    
if __name__=='__main__':
    main()
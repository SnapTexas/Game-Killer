import psutil
import os 
import signal
import time
from db_handeling import ()


def kill_game(game_id):
    try:
        os.kill(game_id, signal.SIGTERM)
    except ProcessLookupError:
        print("Game is not running")
    except PermissionError:
        print("Permission denied")
#Working
def find_game(game_name):
    for process in psutil.process_iter():
        id=process.pid
        name=process.name()
        if name==game_name:
            return id
    return None



def main():
    list_of_games={"DarkAndDarker":"Tavern.exe"}
    game_name="DarkAndDarker"
    game_id=find_game(game_name,list_of_games)
    print("Game id is ",game_id)
    
if __name__=='__main__':
    main()
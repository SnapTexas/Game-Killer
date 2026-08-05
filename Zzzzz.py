import psutil
import os 
import signal
import time 
from db_handeling import update_game_data
from meme_rendering import render_gif
games=["Tavern.exe"]
def kill_game(name,id,game):
    if name in games:
        print(f"Found name:{name} ,process_id:{id}")
        print("Now killing the game! UwU ")
        print("Killing in ",end="")
        for i in range(5,0,-1):
            time.sleep(1)
            print(i,end=" ",flush=True)
        print()
        os.kill(id,signal.SIGTERM)

memes_path=[i for i in os.listdir("memes")]
print(memes_path)
def main():
    while True:    
        for process in psutil.process_iter():
            id=process.pid
            name=process.name()
            #print(f"pid : {id} - name :{name}")
            kill_game(name=name,id=id,game=games)
            break   
                
                
                    
        print("Sleeping")
        time.sleep(1)
        

main()      
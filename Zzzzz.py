import psutil
import os 
import signal
import time 
game="Tavern.exe"
while True:
    
    
    for process in psutil.process_iter():
        id=process.pid
        name=process.name()
        #print(f"pid : {id} - name :{name}")

        if name==game:
            print(f"Found name:{name} ,process_id:{id}")
            print("Now killing the game! UwU ")
            print("Killing in ",end="")
            for i in range(5,0,-1):
                time.sleep(1)
                print(i,end=" ",flush=True)
            print()

            
            os.kill(id,signal.SIGTERM)
            print("Killed Game!")

            print("Get A JOBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB")
            print("FAaaaaaaaah")
            break
    print("Sleeping")
    time.sleep(15)
    
 
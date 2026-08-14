import time 
from game_manager import *
from meme_rendering import render_gif
import datetime
games={"DarkAndDarker":"Tavern.exe"}

time_data=datetime.datetime.now()
date=str(time_data.date())
print(type(date),date)
memes_path=[i for i in os.listdir("memes")]
print(memes_path)

def main():
    try:
        while True:    
            game_id=find_game(game_name=games["DarkAndDarker"])
            runtime=None
            result=None
            total_time_played=None
            game_limit=get_game_limit(game_name=games["DarkAndDarker"])
            if game_id is not None:
                runtime=get_runtime(game_id=game_id)
                game_data = find_record(date=date,game_name=games["DarkAndDarker"])
                
            else:
                if runtime is not None:
                    total_time_played=total_time_played+runtime
                    update_game_data(date=date,
                                    total_usage=total_time_played,
                                    last_played=time_data.now())
                    time.sleep(60)
            if game_data:
                # print(record)
                # day,
                # game_name,
                # date,
                # total_time_played,
                # last_played
                total_time_played=game_data[3]
                actual_time_played=total_time_played+runtime
                if  actual_time_played > game_limit:
                    #time limit check
                    punishment()
            
                
            else:
                result=create_game_record(day=time_data.day(),
                                        game_name=games["DarkAndDarker"],
                                        date=date,
                                        time=time_data.now()
                                        )
                if result:
                    print("Record Created Successfully")
                else:
                    print("Record not Created!!")


    except Exception as e:
        print(e)
        

main()      
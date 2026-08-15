import time 
from game_manager import *
import datetime
import asyncio
games={"DarkAndDarker":"Tavern.exe"}





async def main():
    try:
        runtime=None
        result=None
        total_time_played=None
        while True:    
            time_data=datetime.datetime.now()
            date=str(time_data.date())

            game_id=find_game(game_name=games["DarkAndDarker"])

            game_limit=get_game_limit(game_name=games["DarkAndDarker"])
            game_data = find_record(date=date,game_name=games["DarkAndDarker"])
            if game_id is not None:
                runtime=get_runtime(game_id=game_id)
                print("Getting runtime")
            else:


                if runtime is not None :
                    total_time_played=total_time_played+runtime
                    update_game_data(date=date,
                                    total_usage=total_time_played,
                                    last_played=time_data.now())
                    runtime=None
                    time.sleep(60)
                else:
                    
            if game_data:
                # game_data:
                # 0 -> day
                # 1 -> game_name
                # 2 -> date
                # 3 -> total_time_played
                # 4 -> last_played
                total_time_played=game_data[3]
                print(f"Total time played {total_time_played}")
                print(f"Runtime {runtime}")
                if runtime is not None:
                    
                    actual_time_played=total_time_played+runtime
                
                    

                if  actual_time_played > game_limit:
                    #time limit check
                    await punish(actual_time_played=actual_time_played,
                           game_limit=game_limit)
            
                
            else:
                print("Hello")
                day = time_data.strftime("%A")
                result=create_game_record(day=day,
                                        game_name=games["DarkAndDarker"],
                                        date=date,
                                        time=time_data
                                        )
                print("Hi")
                print(game_data)
                if result:
                    print("Record Created Successfully")
                else:
                    print("Record not Created!!")

            time.sleep(2)
    except Exception as e:
        print(e)
        

asyncio.run(main())      
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
        actual_time_played=None
        while True:    
            time_data=datetime.datetime.now()
            date=str(time_data.date())

            game_id=find_game(game_name=games["DarkAndDarker"])

            game_limit=get_game_limit(game_name=games["DarkAndDarker"])
            game_data = find_record(date=date,game_name=games["DarkAndDarker"])
            if game_id is not None:
                runtime=get_runtime(game_id=game_id)
                print("Getting runtime")
            elif game_id is None and actual_time_played is not None:
                print(f"Game Stopped and Runtime {runtime}")
                result=update_game_data(date=date,
                                        game_name=games['DarkAndDarker'],
                                        total_usage=actual_time_played,
                                        last_played=time_data)
                
                if result:
                    print("Updated SuccessFully game time played")
                    actual_time_played=None
                else:
                    print("Failed to update game runtime ")
                runtime=None
                    
                
                    
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
                    print("actual time played:",actual_time_played)
                    

                    if  actual_time_played > game_limit :
                        #time limit check
                        await punish(actual_time_played=actual_time_played,
                            game_limit=game_limit)
            
                
            if game_data is None and game_id is not None:
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

            await asyncio.sleep(60)
    except Exception as e:
        print(e)
        

asyncio.run(main())      
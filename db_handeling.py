import sqlite3
import datetime

db_name="game_usage.db"
connection=sqlite3.connect(db_name)

cursor=connection.cursor()
time_data=datetime.datetime.now()
date=time_data.date()
games_table_name="GAMES_DATA"
game_limits="game_time_limits"
game_name="DarkAndDarker"


def handel_sqlite_exception(func):
    def wrapper(*args,**kwargs):
        try:
            result =func(*args,**kwargs)
            print(result)
            return result
        except sqlite3.Error as e:
            print(e)
    return wrapper

@handel_sqlite_exception
def update_game_data(date,total_usage,last_played):
        global games_table_name
    
        
        update_query = f"""
                UPDATE {games_table_name}
                SET total_time_played = ?,
                        last_played = ?
                WHERE date = ? AND game_name = ?
                """
        result = cursor.execute(update_query,(total_usage,
                                    last_played,
                                    date,
                                    game_name))
        connection.commit()
        return result 

@handel_sqlite_exception
def find_record(date:str,game_name:str)->tuple|None:
    global games_table_name
    serach_query=f"""SELECT * FROM {games_table_name} WHERE game_name = ? AND date= ?"""
    cursor.execute(serach_query,(game_name,date))
    result=cursor.fetchone()
    if result is not None:
        return result
    return None   

#Working
@handel_sqlite_exception
def create_game_record(day,game_name,date,time,total_time_played=0):
        global games_table_name
        
        create_query=f"""INSERT INTO {games_table_name} (day,
                                                game_name,
                                                date,
                                                total_time_played,
                                                last_played) 
                                                VALUES (?,?,?,?,?)"""

        
        cursor.execute(create_query,(day,game_name,date,total_time_played,time))
        
        connection.commit()
        return True

#Working

@handel_sqlite_exception
def get_game_limit(game_name:str)->int|None:
    global game_limits
    cursor.execute(f"""SELECT time_limit FROM {game_limits} WHERE game_name = ?""",(game_name,))
    result=cursor.fetchone()
    if result:
         return result[0]
    else:
         raise Exception(f"game limit of {game_name} doesn't exist!!")
    

#Working
@handel_sqlite_exception
def is_overplaying(game_name,games_table_name,date):
    game_limit=get_game_limit(game_name=game_name,game_limits=game_limits)
    cursor.execute(f"""SELECT total_time_played FROM {games_table_name} WHERE game_name = ? AND date = ?""",(game_name,date))
    total_time_played_today=cursor.fetchone()
    total_time_played_today=total_time_played_today[0]
    print(total_time_played_today)
    print(type(total_time_played_today))
    if total_time_played_today >= game_limit:
        return True
    return False
    

def main():

    create_table=f"""CREATE TABLE IF NOT EXISTS {games_table_name}(day STRING,
                                                        game_name STRING,
                                                        date  STRING PRIMARY KEY, 
                                                        total_time_played INTEGER,  
                                                        last_played STRING );"""
    #cursor.execute(create_table)
    #connection.commit()
    print(create_game_record(day=str(time_data.strftime("%A")),
                            game_name="DarkAndDarker",
                            date=str(time_data.date()),
                            time=(time_data.hour*60+time_data.minute)))

    print(type(time_data.day),time_data.day)
    print(time_data.strftime("%A"))

    cursor.execute(f"""SELECT * FROM {games_table_name}""")
    result=cursor.fetchall()
    print(result)

    #cursor.execute(f"DELETE FROM {games_table_name}")
    connection.commit()

if __name__=='__main__':
     main()
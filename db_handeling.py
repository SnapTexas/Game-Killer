import sqlite3
import datetime

db_name="game_usage.db"
connection=sqlite3.connect(db_name)

cursor=connection.cursor()




create_table="""CREATE TABLE IF NOT EXISTS DarkAndDarker(day STRING, 
                                                date  STRING PRIMARY KEY, 
                                                total_usage INTEGER, 
                                                start_time STRING, 
                                                last_played STRING );"""

def update_game_data(table_name,total_usage,last_played):
    now = datetime.datetime.now()
    date=str(now.date())
    print(date) #Debug
    update_query=f"""UPDATE {table_name} SET total_usage = ?,
                                        last_played = ? ,
                                        WHERE date = ? """
    cursor.execute(update_query,(total_usage,
                                 last_played,
                                 date))
    connection.commit()


#cursor.execute(create_table)
#connection.commit()
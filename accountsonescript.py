


import sqlite3
import time
global sql




db = sqlite3.connect('Account.db')
sql = db.cursor()



sql.execute("""CREATE TABLE IF NOT EXISTS Account (
    ID INTEGER PRIMARY KEY,
    NAME TEXT,
    PASS TEXT
    
)""")


    
    
 
db.commit()   
 






def accountonescript():
      
  
  x = 1
  
  while(True):
    
    
    if x <= 4: # кол аккаунтов
      
      
      
      sql.execute(f"SELECT NAME FROM Account WHERE ID = '{x}'") #имя аккаунта по id
      namelog = str(sql.fetchone()[0])
      print(namelog)# имя акканта x
  
      sql.execute(f"SELECT PASS FROM Account WHERE ID = '{x}'") #пароль аккаунта по id
  
      passlog = str(sql.fetchone()[0])
      print(passlog) # пароль аккаунта x
      
      print('аккаунт' x)
      x += 1
      

    else:
      
    
      print('Цикл окончен, x =', x)
      time.sleep(4)
      accountonescript()
        
        
        
      
  

accountonescript()

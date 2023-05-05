import sqlite3
from pathlib import Path

DB_FILE_PATH = Path(__file__).parent / 'Firma_hochbau_wbs_python.db'

# 1. Create connection
db = sqlite3.connect(DB_FILE_PATH)

#2 Create a cursor

mycursor = db.cursor()

#3 define SQL statement

## 1-Variante 
sql_statement1 = 'INSERT INTO abteilung VALUES (102,"MongoDB");'


## 2-Variante 
id = 200
vorname = 'Kassandra'
nachname = 'bear'
FK_abt_id = 102
sql_statement2 = f'INSERT INTO mitarbeitende VALUES ({id},"{vorname}","{nachname}",{FK_abt_id});'

## 3-Variante
sql_statement3= "INSERT INTO abteilung VALUES (?,?);"
data = (3343,'welt')

#4 Execute SQL statement
#mycursor.execute(sql_statement2)

## Execution of variante 3
mycursor.execute(sql_statement3,data)

#5. Commit the changes
db.commit()

#6 Display Data
mycursor.execute('SELECT * FROM abteilung;')
for row in mycursor:
    print(row)
# Display alternative
mycursor.execute('SELECT * FROM abteilung;')
result = mycursor.fetchall()
print(result)
#6 close the connection
db.close()
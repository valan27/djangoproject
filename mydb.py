import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Valan@27',
    
    
)

cursorObject = dataBase.cursor()

cursorObject.execute("CRETE DATABASE test")
print("all done!")
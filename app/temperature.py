import sqlite3
import csv
database_file = "nycInfo.db"
connection = sqlite3.connect(database_file, check_same_thread=False)
#create temperature table
connection.execute("CREATE TABLE IF NOT EXISTS" +
                " temperature (" +
                "AirTemp INTEGER, " +
                "Day TEXT, " +
                "Hour INTEGER, " +
                "Latitude FLOAT, " +
                "Longitude FLOAT, " +
                "Year TEXT, " +
                "Install_Type TEXT" +
                ")")
print("temperature table created")
connection.commit()
def create_temperature(cursor, data):
    query = "INSERT INTO temperature (AirTemp, Day, Hour, Latitude, Longitude, Year, Install_Type) VALUES "
    TEXT_indices = list(range(1,8))
    for r in range(min(len(data)-1,1000)):
        query += "("
        for c in range(min(len(data[r]),1000)):
            if len(data[r][c]) < 1:
                query += "NULL" + ", "
            elif c in TEXT_indices:
                query += "'" + data[r][c] + "', "
            #else:
                #query += data[r][c] + ", "
        query = query[:len(query)-2] + "),"
    query = query[:len(query)-2] + ");"
    print(query)
    cursor.execute(query)
    cursor.connection.commit()


with open("Hyperlocal_Temperature_Monitoring.csv", "r") as file:
    dataList = file.read().split("\n")
    for r in range(len(dataList)):
        dataList[r] = dataList[r].split(",")

    create_temperature(cursor=connection.cursor(), data=dataList[1:])
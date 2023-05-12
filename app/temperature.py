import sqlite3
import csv
database_file = "nycInfo.db"
connection = sqlite3.connect(database_file, check_same_thread=False)
#create temperature table
connection.execute("CREATE TABLE IF NOT EXISTS" +
                " temperature (" +
                "Sensor.ID TEXT, " +
                "AirTemp INTEGER, " +
                "Day TEXT, " +
                "Hour INTEGER, " +
                "Latitude FLOAT, " +
                "Longitude FLOAT, " +
                "Year TEXT, " +
                "Install.Type TEXT, " +
                "Borough TEXT, " +
                "ntacode TEXT" +
                ")")
print("temperature table created")
connection.commit()
def create_temperature(cursor, data):
    query = "INSERT INTO temperature (Sensor.ID, AirTemp, Day, Hour, Latitude, Longitude, Year, Install.Type, Borough, ntacode) VALUES "
    TEXT_indices = list(range(1,11))
    for r in range(len(data)-1):
        query += "("
        for c in range(len(data[r])):
            if len(data[r][c]) < 1:
                query += "NULL" + ", "
            elif c in TEXT_indices:
                query += "'" + data[r][c] + "', "
            else:
                query += data[r][c] + ", "
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
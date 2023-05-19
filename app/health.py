import sqlite3
import csv
database_file = "nycInfo.db"
connection = sqlite3.connect(database_file, check_same_thread=False)
#create health table
connection.execute("CREATE TABLE IF NOT EXISTS" +
                " health (" +
                "Facility_Type TEXT, " +
                "Borough TEXT, " +
                "Facility_Name TEXT, " +
                "Cross_Streets TEXT, " +
                "Phone TEXT, " +
                "Location1 TEXT, " +
                "Postcode INTEGER, " +
                "Latitude FLOAT, " +
                "Longitude FLOAT, " +
                "Community_Board INTEGER, " +
                "Council_District INTEGER, " +
                "Census_Tract INTEGER, " +
                "BIN INTEGER, " +
                "BBL INTEGER, " +
                "NTA INTEGER" +
                ")")
print("health table created")
connection.commit()
def create_health(cursor, data):
    query = "INSERT INTO health (Facility, Borough, Facility_Name, Cross_Streets, Phone, Location1, Postcode, Latitude, Longitude, Community_Board, Council_District, Census_Tract, BIN, BBL, NTA) VALUES "
    TEXT_indices = [0,1,2,3,4,5]
    for r in range(len(data)-1):
        query += "("
        for c in range(len(data[r])):
            if len(data[r][c]) < 1:
                query += "NULL" + ", "
            elif c in TEXT_indices:
                if c == 5:
                    data[r][c] = data[r][c][1:]
                query += "'" + data[r][c] + "', "
            else:
                query += data[r][c] + ", "
        query = query[:len(query)-2] + "),"
    query = query[:len(query)-2] + ");"
    print(query)
    cursor.execute(query)
    cursor.connection.commit()

with open("health.csv", "r") as file:
    dataList = file.read().split("\n")
    for r in range(len(dataList)):
        dataList[r] = dataList[r].split(",")

    create_health(cursor=connection.cursor(), data=dataList[1:])
'''
with open("View_of_NYC_Health___Hospitals_patient_care_locations___2011__Map_.csv", "r") as file:
    dataList = file.read().split("\n")
    for r in range(len(dataList)):
        dataList[r] = dataList[r].split(",")

    create_health(cursor=connection.cursor(), data=dataList[1:])'''
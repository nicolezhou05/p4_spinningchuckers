import sqlite3
import csv
database_file = "nycInfo.db"
connection = sqlite3.connect(database_file, check_same_thread=False)
#create buildings table
connection.execute("CREATE TABLE IF NOT EXISTS" +
                " buildings (" +
                "CountedRentalUnits INTEGER, " +
                "CountedHomeownershipUnits INTEGER, " +
                "AllCountedUnits INTEGER, " +
                "TotalBuildingUnits INTEGER, " +
                "BaseSquareFootage INTEGER," +
                "Stories INTEGER," +
                "Latitude FLOAT," +
                "Longitude FLOAT" +
                ")")
print("buildings table created")
connection.commit()
def create_buildings(cursor, data):
    query = "INSERT INTO buildings (CountedRentalUnits, CountedHomeownershipUnits, AllCountedUnits, TotalBuildingUnits, BaseSquareFootage, Stories, Latitude, Longitude) VALUES "
    TEXT_indices = [9,10,11,12,13,14,20,21]
    for r in range(len(data)-1):
        query += "("
        for c in range(len(data[r])):
            if len(data[r][c]) < 1 and c in TEXT_indices:
                query += "'NULL'" + ", "
            elif c in TEXT_indices:
                query += "'" + data[r][c] + "', "
            #else:
                #break
                #query += data[r][c] + ", "
        query = query[:len(query)-2] + "),"
    query = query[:len(query)-2] + ");"
    print(query)
    cursor.execute(query)
    cursor.connection.commit()


with open("buildings.csv", "r") as file:
    dataList = file.read().split("\n")
    for r in range(len(dataList)):
        dataList[r] = dataList[r].split(",")

    create_buildings(cursor=connection.cursor(), data=dataList[1:])
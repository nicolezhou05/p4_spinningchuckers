import sqlite3
import csv
database_file = "nycInfo.db"
connection = sqlite3.connect(database_file, check_same_thread=False)
#create energy table
connection.execute("CREATE TABLE IF NOT EXISTS" +
                " energy (" +
                "Property_ID INTEGER, " +
                "Property_Name TEXT, " +
                "Parent_Property_ID TEXT, " +
                "Parent_Property_Name TEXT, " +
                "Month TEXT, " +
                "Electricity_Use TEXT, " +
                "Natural_Gas_Use TEXT" +
                ")")
print("energy table created")
connection.commit()
def create_energy(cursor, data):
    query = "INSERT INTO energy (Property_ID, Property_Name, Parent_Property_ID, Parent_Property_Name, Month, Electricity_Use, Natural_Gas_Use) VALUES "
    TEXT_indices = list(range(1,8))
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


with open("Local_Law_84_2021__Monthly_Data_for_Calendar_Year_2020_.csv", "r") as file:
    dataList = file.read().split("\n")
    for r in range(len(dataList)):
        dataList[r] = dataList[r].split(",")

    create_energy(cursor=connection.cursor(), data=dataList[1:])
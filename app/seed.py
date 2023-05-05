import sqlite3
database_file = "nycInfo.db"
connection = sqlite3.connect(database_file, check_same_thread=False)

# #create transportation table
# connection.execute("CREATE TABLE IF NOT EXISTS" +
#                 " transportation (" +
#                 "VMS INTEGER, " +
#                 "main_roadway TEXT, " +
#                 "direction TEXT, " +
#                 "cross_street TEXT, " +
#                 "borough TEXT, " +
#                 "barcode INTEGER, " +
#                 "borocd INTEGER, " +
#                 "coun_dist INTEGER, " +
#                 "assem_dist INTEGER, " +
#                 "st_sen_dist INTEGER, " +
#                 "cong_dist INTEGER, " +
#                 "type TEXT, " +
#                 "owner TEXT, " +
#                 "FEMAFldz TEXT, " +
#                 "FEMAFldT TEXT, " +
#                 "HrcEvac INTEGER, " +
#                 "latitude REAL, " +
#                 "longitude REAL, " +
#                 "the_geom TEXT"
#                 ")")
# print("transportation table created")
# connection.commit()
def create(cursor):
    query = "INSERT INTO transportation VALUES("
    for r in dataList:
        query += 

with open("Overhead_Electronic_Signs.csv", "r") as file:
    dataList = file.read().split("\n")
    for r in range(len(dataList)):
        dataList[r] = dataList[r].split(",")
    print(dataList)

    headings = dataList[0]
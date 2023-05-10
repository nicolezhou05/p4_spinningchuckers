import sqlite3
database_file = "nycInfo.db"
connection = sqlite3.connect(database_file, check_same_thread=False)

# #create buildings table
# connection.execute("CREATE TABLE IF NOT EXISTS" +
#                 " buildings (" +
#                 "Block INTEGER, " +
#                 "Lot INTEGER, " +
#                 "SchoolDist INTEGER, " +
#                 "Council INTEGER, " +
#                 "ZipCode INTEGER, " +
#                 "FireComp TEXT, " +
#                 "PolicePrct INTEGER, " +
#                 "HealthArea INTEGER" +
#                 "LandUse INTEGER"+
#                 ")")
# print("buildings table created")
# connection.commit()
def create(cursor):
    query = "INSERT INTO buildings VALUES("
    for r in dataList:
        query += 


"""
with open("US_Crime_Data.csv", "r") as file:
    dataList = file.read().split("\n")
    for r in range(len(dataList)):
        dataList[r] = dataList[r].split(",")
    print(dataList)

    headings = dataList[0]
"""
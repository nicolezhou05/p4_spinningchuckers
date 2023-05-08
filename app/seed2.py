import sqlite3
database_file = "nycInfo.db"
connection = sqlite3.connect(database_file, check_same_thread=False)

# #create crime table
# connection.execute("CREATE TABLE IF NOT EXISTS" +
#                 " crime (" +
#                 "Date TEXT, " +
#                 "Title TEXT, " +
#                 "Organization TEXT, " +
#                 "cross_street TEXT, " +
#                 "City TEXT, " +
#                 "State TEXT, " +
#                 "URL TEXT, " +
#                 "Keyword TEXT, " +
#                 "Summary TEXT" +
#                 ")")
# print("crime table created")
# connection.commit()
def create(cursor):
    query = "INSERT INTO crime VALUES("
    for r in dataList:
        query += 

with open("US_Crime_Data.csv", "r") as file:
    dataList = file.read().split("\n")
    for r in range(len(dataList)):
        dataList[r] = dataList[r].split(",")
    print(dataList)

    headings = dataList[0]
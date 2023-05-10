import sqlite3
database_file = "nycInfo.db"
connection = sqlite3.connect(database_file, check_same_thread=False)

#create health table
connection.execute("CREATE TABLE IF NOT EXISTS" +
                " transportation (" +
                "facility_type TEXT, " +
                "borough TEXT, " +
                "facility_name TEXT, " +
                "cross_streets TEXT, " +
                "phone TEXT, " +
                "location1 INTEGER, " +
                "postcode INTEGER, " +
                "latitude REAL, " +
                "longitude REAL, " +
                "community_board INTEGER, " +
                "council_district INTEGER, " +
                "census_tract INT, " +
                "BIN INT, " +
                "BBL INT, " +
                "NTA TEXT, " +
                ")")
print("health table created")
connection.commit()

def createTransport(cursor, data):
    query = "INSERT INTO health (facility_type, borough, facility_name, cross_streets, phone, location1, postcode, latitude, longitude, community_board, council_district, census_tract, BIN, BBL, NTA) VALUES "
    TEXT_indeces = [0, 1, 2, 3, 4, 14]
    for r in range(len(data)-1):
        query += "("
        for c in range(len(data[r])):
            if len(data[r][c]) < 1:
                query += "NULL" + ", "
            elif c in TEXT_indeces:
                query += "'" + data[r][c] + "', "
            else:
                query += data[r][c] + ", "
        query = query[0:len(query)-2] + "),"
    query = query[0:len(query)-2] + ");"
    print(query)
    cursor.execute(query)
    cursor.connection.commit()

with open("health.csv", "r") as file:
    dataList = file.read().split("\n")
    for r in range(len(dataList)):
        dataList[r] = dataList[r].split(",")

    createhealth(cursor=connection.cursor(), data=dataList[1:])
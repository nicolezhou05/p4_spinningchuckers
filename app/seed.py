import sqlite3
database_file = "nycInfo.db"
connection = sqlite3.connect(database_file, check_same_thread=False)

#create transportation table
connection.execute("CREATE TABLE IF NOT EXISTS" +
                " transportation (" +
                "VMS INTEGER, " +
                "main_roadway TEXT, " +
                "direction TEXT, " +
                "cross_street TEXT, " +
                "borough TEXT, " +
                "barcode INTEGER, " +
                "borocd INTEGER, " +
                "coun_dist INTEGER, " +
                "assem_dist INTEGER, " +
                "st_sen_dist INTEGER, " +
                "cong_dist INTEGER, " +
                "type TEXT, " +
                "owner TEXT, " +
                "FEMAFldz TEXT, " +
                "FEMAFldT TEXT, " +
                "HrcEvac INTEGER, " +
                "latitude REAL, " +
                "longitude REAL, " +
                "the_geom TEXT"
                ")")
print("transportation table created")
connection.commit()

def create(cursor, data):
    query = "INSERT INTO transportation (VMS, main_roadway, direction, cross_street, borough, barcode, borocd, coun_dist, assem_dist, st_sen_dist, cong_dist, type, owner, FEMAFldz, FEMAFldT, HrcEvac, latitude, longitude, the_geom) VALUES ("
    TEXT_indeces = [1, 2, 3, 4, 11, 12, 13, 14, 18]
    for r in range(len(data)):
        for c in range(len(data[r])):
            if c in TEXT_indeces:
                query += "'" + data[r][c] + "',"
            else:
                query += data[r][c] + ", "
        print("This is row " + str(r))
    query += ")"
    print(query)
    cursor.execute(query)
    cursor.connection.commit()

with open("Overhead_Electronic_Signs.csv", "r") as file:
    dataList = file.read().split("\n")
    for r in range(len(dataList)):
        dataList[r] = dataList[r].split(",")

    create(cursor=connection.cursor(), data=dataList[1:])

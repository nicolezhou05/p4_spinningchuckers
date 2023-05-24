import sqlite3
import csv
database_file = "nycInfo.db"
connection = sqlite3.connect(database_file, check_same_thread=False)
#create energy table
connection.execute("CREATE TABLE IF NOT EXISTS" +
                " jobs (" +
                "job_id INTEGER, " +
                "agency TEXT, " +
                "posting_type TEXT, " +
                "num_of_positions INTEGER, " +
                "business_title TEXT, " +
                "civic_service_title TEXT, " +
                "title_code_no TEXT, " +
                "level TEXT, " +
                "job_category TEXT, " +
                "full_part_time_indicator TEXT, " +
                "salary_range_from FLOAT, " +
                "salary_range_to FLOAT, " +
                "salary_freq TEXT, " +
                "work_location TEXT, " +
                "division_work_unit TEXT, " +
                "job_description TEXT, " +
                "minimum_qual_reqs TEXT, " +
                "pref_skills TEXT, " +
                "additional_info TEXT, " +
                "to_apply TEXT, " +
                "hours_shift TEXT, " +
                "work_location1 TEXT, " +
                "recruitment_contact TEXT, " +
                "residency_req TEXT, " +
                "posting_date TEXT, " +
                "post_until TEXT, " +
                "posting_updated TEXT, " +
                "process_date TEXT"
                ")")
print("jobs table created")
connection.commit()
def create_jobs(cursor, data):
    query = "INSERT INTO jobs (job_id, agency, posting_type, num_of_positions, business_title, civic_service_title, title_code_no, level, job_category, full_part_time_indicator, salary_range_from, salary_range_to, salary_freq, work_location, division_work_unit, job_description, minimum_qual_reqs, pref_skills, additional_info, to_apply, hours_shift, work_location1, recruitment_contact, residency_req, posting_date, post_until, posting_updated, process_date) VALUES "
    TEXT_indices = [1, 2, 4, 5, 6, 7, 8, 9, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]
    for r in range(len(data)-1):
        query += "("
        for c in range(len(data[r])):
            if len(data[r][c]) < 1:
                query += "NULL" + ", "
            elif c in TEXT_indices:
                query += "'" + data[r][c].replace('"',"").replace("'","") + "', "
            else:
                query += data[r][c].replace('"',"") + ", "
        query = query[:len(query)-2] + "),"
    query = query[:len(query)-2] + ");"
    print(query)
    cursor.execute(query)
    cursor.connection.commit()


with open("nyc-jobs.csv", "r", encoding="utf-8") as file:
    dataList = file.read().split("\n")
    for i in range(len(dataList)):
        dataList[i] = dataList[i][:300].replace(", ","; ") + dataList[i][300:-96].replace(", ","; ").replace(",1","1").replace(",2","2").replace(",3","3").replace(",4","4").replace(",5","5").replace(",6","6").replace(",7","7").replace(",8","8").replace(",9","9").replace(",0","0") + dataList[i][-96:]

    for r in range(len(dataList)):
        dataList[r] = dataList[r].split(",")

    create_jobs(cursor=connection.cursor(), data=dataList[1:50])
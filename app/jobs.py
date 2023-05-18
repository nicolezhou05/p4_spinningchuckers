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
                "salary_range_from INTEGER, " +
                "salary_range_to INTEGER, " +
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
    query = "INSERT INTO jobs (agency, posting_type, num_of_positions, business_title, civic_service_title, title_code_no, level, job_category, full_part_time_indicator, salary_range_from, salary_range_to, salary_freq, work_location, division_work_unit, job_description, minimum_qual_reqs, pref_skills, additional_info, to_apply, hours_shift, work_location1, recruitment_contact, residency_req, posting_date, post_until, posting_updated, process_date) VALUES "
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


with open("nyc-jobs.csv", "r", encoding="utf-8") as file:
    dataList = file.read().split("\n")
    for r in range(len(dataList)):
        dataList[r] = dataList[r].split(",")

    create_jobs(cursor=connection.cursor(), data=dataList[1:])
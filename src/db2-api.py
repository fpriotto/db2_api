import ibm_db
import ibm_db_dbi
import pandas as pd

# confident info
dsn_hostname = ""
dsn_uid = ""
dsn_pwd = ""

dsn_driver = "{IBM DB2 ODBC DRIVER}"
dsn_database = "bludb"
dsn_port = ""
dsn_protocol = "TCPIP"
dsn_security = "SSL"


dsn = (
    "DRIVER={0};"
    "DATABASE={1};"
    "HOSTNAME={2};"
    "PORT={3};"
    "PROTOCOL={4};"
    "UID={5};"
    "PWD={6};"
    "SECURITY={7};").format(dsn_driver, dsn_database, dsn_hostname, dsn_port, dsn_protocol, dsn_uid, dsn_pwd,dsn_security)

# print the connection string to check correct values are specified
print(dsn)

# Create database connection
try:
    #Create connection object
    conn = ibm_db.connect(dsn, "", "")
    print ("Connected to database: ", dsn_database, "as user: ", dsn_uid, "on host: ", dsn_hostname, "\n")

except:
    print ("Unable to connect: ", ibm_db.conn_errormsg(), "\n")

pconn = ibm_db_dbi.Connection(conn)

# Checks metadata
print("\n\nMETADATA FROM TABLE CREATION:\n")
df = pd.read_sql(("select TABSCHEMA, TABNAME, CREATE_TIME from SYSCAT.TABLES where TABSCHEMA='{0}'").format((dsn_uid.upper())), pconn)
print(df)

# Checks number of cols
print("\n\nMETADATA FROM TABLE SCHOOLS:\n")
df = pd.read_sql("select count(*) as number_of_columns from SYSCAT.COLUMNS where TABNAME = 'SCHOOLS'", pconn)
print(df)

# Checks cols info
print("\n\nMETADATA FROM TABLE SCHOOLS:\n")
df = pd.read_sql("select distinct(NAME), COLTYPE, LENGTH from SYSIBM.SYSCOLUMNS where TBNAME = 'SCHOOLS'", pconn)
print(df)

# A few problems are selected using data provided and sql statements are written to solve them

print("\n\nProblem 1: How many Elementary Schools are in the dataset?\n")
df = pd.read_sql("select count(*) as number_of_elementary_schools from SCHOOLS where \"Elementary, Middle, or High School\" = 'ES'", pconn)
print(df)

print("\n\nProblem 2: What is the highest Safety Score?\n")
df = pd.read_sql("select MAX(SAFETY_SCORE) as MAX_SAFETY_SCORE from SCHOOLS", pconn)
print(df)

print("\n\nProblem 3: Which schools have highest Safety Score?\n")
df = pd.read_sql("select Name_of_School, Safety_Score from SCHOOLS where Safety_Score = (select MAX(SAFETY_SCORE) as MAX_SAFETY_SCORE from SCHOOLS)", pconn)
print(df)

print("\n\nProblem 4: What are the top 10 schools with the highest \"Average Student Attendance\"?\n")
df = pd.read_sql("select NAME_OF_SCHOOL, AVERAGE_STUDENT_ATTENDANCE from SCHOOLS order by AVERAGE_STUDENT_ATTENDANCE desc NULLS LAST limit 10", pconn)
print(df)

print("\n\nProblem 5: Retrieve the list of 5 Schools with the lowest Average Student Attendance sorted in ascending order based on attendance\n")
df = pd.read_sql("select NAME_OF_SCHOOL, AVERAGE_STUDENT_ATTENDANCE from SCHOOLS order by AVERAGE_STUDENT_ATTENDANCE asc limit 5", pconn)
print(df)

print("\n\nProblem 6: Now remove the '%' sign from the above result set for Average Student Attendance column\n")
df = pd.read_sql("select NAME_OF_SCHOOL, replace(AVERAGE_STUDENT_ATTENDANCE, '%', '') as average_student_attendance \
     from SCHOOLS order by AVERAGE_STUDENT_ATTENDANCE asc limit 5", pconn)
print(df)

print("\n\nProblem 7: Which Schools have Average Student Attendance lower than 70%?\n")
df = pd.read_sql("select Name_of_School, Average_Student_Attendance  \
     from SCHOOLS \
     where CAST ( REPLACE(Average_Student_Attendance, '%', '') AS DOUBLE ) < 70 \
     order by Average_Student_Attendance", pconn)
print(df)

print("\n\nProblem 8: Get the total College Enrollment for each Community Area\n")
df = pd.read_sql("select COMMUNITY_AREA_NAME, SUM(COLLEGE_ENROLLMENT) as total_college_enrollment from SCHOOLS group by COMMUNITY_AREA_NAME", pconn)
print(df)

print("\n\nProblem 9: Get the 5 Community Areas with the least total College Enrollment sorted in ascending order\n")
df = pd.read_sql("select COMMUNITY_AREA_NAME, total_college_enrollment \
    from (select COMMUNITY_AREA_NAME, SUM(COLLEGE_ENROLLMENT) as total_college_enrollment from SCHOOLS group by COMMUNITY_AREA_NAME) \
    order by total_college_enrollment limit 5", pconn)
print(df)

print("\n\nProblem 10: List 5 schools with lowest safety score\n")
df = pd.read_sql("select NAME_OF_SCHOOL, SAFETY_SCORE from SCHOOLS order by SAFETY_SCORE LIMIT 5", pconn)
print(df)

print("\n\nProblem 11: Get the hardship index for the community area which has College Enrollment of 871\n")
df = pd.read_sql("select CSD.HARDSHIP_INDEX, CSD.COMMUNITY_AREA_NAME, SCH.COLLEGE_ENROLLMENT \
from CHICAGO_SOCIOECONOMIC_DATA CSD, SCHOOLS SCH where CSD.CA = SCH.COMMUNITY_AREA_NUMBER \
and SCH.COLLEGE_ENROLLMENT = 871", pconn)
print(df)

print("\n\nProblem 12: Get the hardship index for the community area which has the school with the highest enrollment\n")
df = pd.read_sql("select CSD.HARDSHIP_INDEX, CSD.COMMUNITY_AREA_NAME, SCH.COLLEGE_ENROLLMENT from \
CHICAGO_SOCIOECONOMIC_DATA CSD, SCHOOLS SCH where CSD.CA = SCH.COMMUNITY_AREA_NUMBER \
and SCH.COLLEGE_ENROLLMENT = (select max(COLLEGE_ENROLLMENT) from SCHOOLS)", pconn)
print(df)

ibm_db.close(conn)
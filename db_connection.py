import sqlite3

# db_name = 'sql11481732'
# db_name = "e_health"
db_name = "db.sqlite3"

# password = 'IxcCRn59jy'
password = ''

# user = 'sql11481732'
user = 'root'

# host = 'sql11.freesqldatabase.com'
host = 'localhost'


# connection = pymysql.connect(host=host, user=user, passwd=password, database=db_name)
connection = sqlite3.connect(db_name)
cursor = connection.cursor()

# cursor.execute(f'''
#     SELECT *
#     FROM {db_name}.users
# ''')
#
# print(cursor.fetchone())


import serial
import time
import db_connection as db
import datetime


# make sure the 'COM#' is set according the Windows Device Manager
ser = serial.Serial('COM6', 9600, timeout=1)
time.sleep(2)

# connecting to database
#connection = pymysql.connect(host="e-health.cr9kejwuec2v.us-east-2.rds.amazonaws.com", user="admin", passwd="salah_abdellah.2022", database="e-health")
#cursor = connection.cursor()
### khdm b  db.connection o db.cursor

while True:
    card_uid = ser.readline().decode().strip('\n')   # read a byte
    if card_uid:
        timestamp = datetime.datetime.now()
        date = timestamp.strftime("%m-%d-%Y")
        time = timestamp.strftime("%H:%M:%S")
        # print(card_uid)
        cursor.execute(f'''
            SELECT nom, prenom, dateNaissance, age, sexe, ville 
            FROM `e-health`.users
            WHERE uid = {card_uid}
        ''')

        user_informations = cursor.fetchone()

        print(user_informations)
        # break
#
# connection.close()
# ser.close()

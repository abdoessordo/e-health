import serial
from time import sleep
import db_connection as db


def read_card_uid():
    ser = serial.Serial('/dev/tty/ACM0', 9600, timeout=1)
    sleep(1)

    while True:
        card_uid = ser.readline().decode().strip('\n')   # read a byte
        if card_uid:

            db.cursor.execute(f'''
                SELECT * 
                FROM {db.db_name}.users
                WHERE card_id = {card_uid}
            ''')
            ser.close()
            return db.cursor.fetchone()


def add_visit(user_id, medecin_id):
    db.cursor.execute(f'''
                    INSERT INTO {db.db_name}.visites (patient_id, medecin_id)
                    VALUES ('{user_id}', '{medecin_id}')
                ''')
    db.connection.commit()


if __name__ == '__main__':
    # print(read_card_uid())

    add_visit()
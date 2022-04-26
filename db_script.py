from med.models import Meds
import sqlite3
import os
import sys
def main():
	"""Run administrative tasks."""
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ehealth.settings')
	db=sqlite3.connect("meds.db")
	cur=sqlite3.cursor()
	sql="SELECT * FROM Meds"
	res=cur.execute(sql)
	for x in res:
		Meds.objects.create(x)    

if __name__ == '__main__':
	main()


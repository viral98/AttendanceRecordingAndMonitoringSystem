import serial
import MySQLdb
import time
import datetime
db = MySQLdb.connect("DESKTOP-7PF3GNC", "viral", "viral", "student")
ldb= MySQLdb.connect("localhost", "classroom", "password", "timetable")
print "Connected"
CDay =datetime.date.today().strftime("%A");
curs=db.cursor()
curs2= ldb.cursor()
curs.execute("Select COUNT(*) from attendance")
srno = curs.fetchone()
sr_no = int(srno[0])
ser = serial.Serial('/dev/ttyUSB0',2400)
ser.baudrate = 9600

while True:
	curs.execute("Select sub_code from timetable where Tday = %s and Stime < NOW() AND Etime > NOW()",(CDay))
	SubCode= curs.fetchone()
	int1 = SubCode[0]
	string = ser.readline(12)
	print "start"
	if len(string) == 0:
		print "Insert a tag"
	else:
		string = string[1:11]
		if string == '5003BD0FE5':
			curs.execute("Select lecture from subject where sub_code = %s",(int1))
			lectno= curs.fetchone()
			lect = lectno[0]
			lect = lect + 1
			curs.execute("""UPDATE student.subject set lecture = %s where sub_code = %s""",(lect,int1))
			print "Welcome Teacher XYZ"
			db.commit()
			
			curs.execute("""UPDATE student.attendance SET datetime= NOW(), attend_sub_code = %s, status = 0 WHERE status IS null""",(int1))
			query = "SELECT stud_id,rfid FROM student"
			curs.execute(query)
			for stud_id,rfid in curs.fetchall():
			    curs.execute("INSERT into attendance(sr_num,attend_stud_id,attend_rfid_id) values ({0},{1},'{2}')".format(sr_no, stud_id,rfid))
			
			    print(stud_id, rfid)
			    sr_no = sr_no + 1
			db.commit()

		curs.execute("""UPDATE student.attendance SET datetime= NOW(), attend_sub_code = %s, status = 1 WHERE attend_rfid_id = %s AND status IS null""",(int1,string))
		print string 
		print SubCode
			
import smtplib
import time

server = smtplib.SMTP( "mail.gmx.com", 25 )
server.starttls()
server.login( 'hellofriendhello@gmx.com', 'A12345t!' )
#server.login( 'youhavebeenscrubbedscrub@gmail.com', 'a123456t' )

print server

numsent = 0 
retry = 0
smsgdict = {"verizon" : "vtext.com", "virgin" : "vmobl.com", "tmobile" : "tmomail.com", "att" : "txt.att.net", "sprint" : "messaging.sprintpcs.com"}
phonenum = raw_input("num> ")
carrier = raw_input("carrier> ")
haha = raw_input("mesg> ")
num = raw_input("number of messages> ")
smsgate = smsgdict[carrier]

while (numsent < num):
	try:
#		server.sendmail( 'The Scrub Ravager', '5099429080@tmomail.net', haha )
#		server.sendmail( 'The Scrub Ravager', '3603592082@vtext.com', haha )
#		server.sendmail( 'The Scrub Ravager', '5413902024@vmobl.com', haha )
#		server.sendmail( 'The Scrub Ravager', '3605812008@vtext.com', haha )
		time.sleep(2)
		print phonenum
		print smsgate
		print haha
		server.sendmail( 'hellofriendhello@gmx.com', phonenum + "@" + smsgate, haha )	
		numsent += 1
		print numsent
	except Exception as e:
		print e
		print "An error ocurred, retrying..."
		server.quit()
		print "waiting 10 seconds..."
		time.sleep(10)
		server.connect()
		retry += 1
		if (retry > 3):
			break
		if (numsent == 0):
			print "Most likely not a correct number/carrier"
			break

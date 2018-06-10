from time import sleep     # Import time library
import RPi.GPIO as GPIO    # Import RPi Library
import smtplib 
import sys
GPIO.setmode(GPIO.BOARD)   # Specify We Want to reference Physical pins

cable=12  # Descriptive Variable for pin 12 
GPIO.setup(cable,GPIO.IN,pull_up_down=GPIO.PUD_UP) # Set cable as input and Activate pull up resistor 

pull_up_down=GPIO.PUD_UP

while(1): # Create an infinite loop
	if GPIO.input(cable)==0: # cable will report 0 if it is pressed
		print ("water detected")
		content = 'Warnning! water has been detected, Kindly check!'
		mail = smtplib.SMTP('smtp.gmail.com', 587)
		mail.ehlo()
		mail.starttls()
		mail.login('waterdetectionsystem@gmail.com', '199419941994')
		mail.sendmail('waterdetectionsystem@gmail.com', 'yourEmail@gmail.com', content)
		mail.close()
		sleep(.1)   # delay
		sys.exit()   
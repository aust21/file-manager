import sys, time, os

def type_writer(message):
    for i in message:
    	sys.stdout.write(i)
    	sys.stdout.flush()
    	time.sleep(.05)

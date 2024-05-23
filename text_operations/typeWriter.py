import sys, time, os
sys.path.append(os.getcwd())

def type_writer(message):
    for i in message:
    	sys.stdout.write(i)
    	sys.stdout.flush()
    	time.sleep(.05)

for x in range (1,61):
	print (x)


import time,os
while True:
	t=time.localtime()
	os.system("cls")
	print(str(t[3])+":"+str(t[4])+":"+str(t[5]))
	time.sleep(0.5)


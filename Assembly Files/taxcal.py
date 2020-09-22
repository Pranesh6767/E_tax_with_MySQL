import time
area=float(input("Enter Area In square meter:\n\n"))
print("Choose The type of Building\n\n1.Hut or mud Building\n2.Stone or Brick Building Built in clay \n 3.Stone, bricks Building built in lime or cement.\n 4.RCC Building ")
ch1=int(input())
if  ch1 == 1:
	taxrate=0.30
	maxtaxrate=0.75
	redirec=5320
elif ch1==2:
	taxrate=0.60
	maxtaxrate=0.120
	redirec=9120
elif  ch1 == 3:
	taxrate=0.75
	maxtaxrate=0.150
	redirec=12920
elif ch1==4:
	taxrate=0.120
	maxtaxrate=0.200
	redirec=15200
print("What is the use of Building\n\n\n\n1.Residential Use\n2.Industrial Use \n3.Commertial Use")
ch2=int(input())
if  ch2==1:
	bhtax=1
elif ch2==2:
	bhtax=1.20
elif ch2==3:
	taxrate=1.25
print("What is the age of Building..... in years")
age=int(input())
if age <= 2:
	drate=1
	maxdrate=1
elif age>2 and age<=5:
	drate=0.95
	maxdrate=0.95
elif age>5 and age<=10:
	drate=0.85
	maxdrate=0.9
elif age>10 and age<=20:
	drate=0.75
	maxdrate=0.8
elif age>20 and age<=30:
	drate=0.60
	maxdrate=0.7
elif age>30 and age<=40:
	drate=0.45
	maxdrate=0.6
elif age>40 and age<=50:
	drate=0.30
	maxdrate=0.5
elif age>50 and age<=60:
	drate=0.20
	maxdrate=0.4
elif age>60:
	drate=0.15
	maxdrate=0.3


taxa1=area*1130

taxb1=area*redirec*drate*bhtax
taxc1=(taxa1+taxb1)/1000
tax1=taxc1*taxrate

maxtaxb1=area*redirec*maxdrate*bhtax
maxtaxc1=(taxa1+maxtaxb1)/1000
maxtax1=maxtaxc1*maxtaxrate
print("Building Tax is from ",tax1,"To",maxtax1)
time.sleep(10)



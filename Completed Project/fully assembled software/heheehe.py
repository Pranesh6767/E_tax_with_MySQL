s=str("12:05:45AM")
h=s[0:2]
hi=int(h)
if s[8]=="P" and hi!=12:
    hi=hi+12
elif s[8]=="A" and hi==12:
	hi=0
h=str(hi)
print(h+s[2:8])
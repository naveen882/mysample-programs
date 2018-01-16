import pandas as pd

a1=pd.DataFrame({'a':[1.11,2.22,3.33],'b':[4.44,5.55,6.66]})
a2=pd.DataFrame({'a':[1.1,2.2,3.3],'b':[4.4,5.5,6.6]})
print a1
print a2
#print a1+a2
print "======"
#c= pd.concat([a1,a2],axis=1)
#print c
#c= pd.merge(a1,a2,on=["a"])
#c=a1.join(a2)
#print type(c)
#c.loc[:,'diff']= a1-a2
#print c
c=pd.DataFrame()
for i in a1:
	print "===="
	print a1[i]
	print a2[i]
	#c['a1'+i]=a1[i]
	#c['a2'+i]=a2[i]
	#c['diff'+i] = a1[i]-a2[i]
	c[i+"_dev"]=a1[i]
	c[i+"base"]=a2[i]
	c[i+"_"] = a1[i]-a2[i]

print c


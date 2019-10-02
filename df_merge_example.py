import pandas as pd


a=pd.DataFrame({'a':[1,2,3,4,5],'b':[6,7,8,9,10],'c':[11,12,13,14,15]})
b=pd.DataFrame({'a':[1,2,3,4,5],'b':[6,7,8,9,10],'c':[11,12,13,14,15]})
print a
print b

df1=pd.merge(a,b,on=['a','b'],how="outer")
print df1
"""
   a   b   c
0  1   6  11
1  2   7  12
2  3   8  13
3  4   9  14
4  5  10  15
   a   b   c
0  1   6  11
1  2   7  12
2  3   8  13
3  4   9  14
4  5  10  15
   a   b  c_x  c_y
0  1   6   11   11
1  2   7   12   12
2  3   8   13   13
3  4   9   14   14
4  5  10   15   15
"""


print "==================="
a=pd.DataFrame({'a':[1,2,3,4,5],'b':[6,7,8,99,10],'c':[11,12,13,14,15]})
b=pd.DataFrame({'a':[1,2,3,4,5],'b':[6,7,8,9,10],'c':[11,12,13,14,15]})
print a
print b

df1=pd.merge(a,b,on=['a','b'],how="outer")
print df1
print df1.columns.tolist()

"""
   a   b   c
0  1   6  11
1  2   7  12
2  3   8  13
3  4  99  14
4  5  10  15
   a   b   c
0  1   6  11
1  2   7  12
2  3   8  13
3  4   9  14
4  5  10  15
   a   b   c_x   c_y
0  1   6  11.0  11.0
1  2   7  12.0  12.0
2  3   8  13.0  13.0
3  4  99  14.0   NaN
4  5  10  15.0  15.0
5  4   9   NaN  14.0
['a', 'b', 'c_x', 'c_y']

"""
print "==================1"
a=pd.DataFrame({'a':[1,2,3,4,5],'b':[6,7,8,99,10],'c':[11,12,13,14,15]})
b=pd.DataFrame({'a':[1,2,3,4,5],'b':[6,7,8,9,10],'c':[11,12,13,14,15]})
print a
print b
#print a['a'].sum()
print "========="
df=pd.concat([a,b])
print df
df = df.reset_index(drop=True)
print df
df_gpby=df.groupby(list(df.columns))
idx = [x[0] for x in df_gpby.groups.values() if len(x)==1]	
print df.reindex(idx)
print "=========="
df1 = pd.DataFrame([[1, 'a'], [2, 'b'], [3, 'c']], columns=['num', 'name'])
df1 = df1.set_index('name')
df2 = pd.DataFrame([[1, 'a'], [2, 'b'], [3, 'c']], columns=['num', 'another_name'])
df2 = df2.set_index('another_name')
print df1
print df2
print df1.equals(df2)
#True

print df1.index.names == df2.index.names
#False
print "============="
a=pd.DataFrame({'a':[1,2,3,4,5],'b':[6,7,8,99,10],'c':[11,12,13,14,15]})
b=pd.DataFrame({'a':[1,2,3,4,5],'b':[6,7,8,9,10],'c':[11,12,13,14,15]})
df = pd.merge(a,b,on=['a','b'],how="outer",suffixes=('_1','_2'))
print df
print "============="
def fn(x):
	#print x
	return x[0]+x[1]+x[2]
	
a=pd.DataFrame({'a':[1,2,3,4,5],'b':[6,7,8,99,10],'c':[11,12,13,14,15]})
b=pd.DataFrame({'a':[1,2,3,4,5],'b':[6,7,8,9,10],'c':[11,12,13,14,15]})
print a
print b
print "============="
df = pd.merge(a,b,on=['a','b'],how="outer",suffixes=('_1','_2'))
a= df.apply(fn,axis=1)
print type(a)
print a
print "============="
pd.set_option('display.precision',1000)
a=pd.DataFrame({'a':[1,2,3,4,5],'b':[6,7,8,99,10],'c':[11,12,13,14,15]})
b=pd.DataFrame({'a':[1,2,3,4,5],'b':[6,7,8,9,10],'c':[11,12,13,14,15]})
df = pd.merge(a,b,on=['a','b'],how="outer",suffixes=('_1','_2'))
print df


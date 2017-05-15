import pdb
# https://pythonconquerstheuniverse.wordpress.com/2009/09/10/debugging-in-python/
# n for next line of code
# q for quitting pdb
# l list 11 lines of code
# c for continue, it will end the program if no pdb_trace is found or it will execute all the other code in the loop and will again halt at pdb_trace()
# s is for stepping into subroutine or functions
# r is for returning from the subroutine or better "continue until return"
# In the following when we encounter that the next line is the function then to step into that
# function and debug it we can use 's'
# ex: /home/naveen/pg/mysample-programs/epdb1.py(32)<module>()
#    -> final = combine(a, b)
#    (Pdb) s
# *****Importanti below statement*****
# One of the nice things about the (Pdb) prompt is that you can do anything at it — you can enter
# any command that you like at the (Pdb) prompt. So you can, for instance, enter this command at the
# (Pdb) prompt.
# (Pdb) var1 = "bbb"

pdb.set_trace()
a = "aaa"
b = "bbb"
c = "ccc"
pdb.set_trace()
final = a + b + c
print final
for i in range(5):
    pdb.set_trace()
    print i
    print "again"


def combine(s1, s2):      # define subroutine combine, which...
    s3 = s1 + s2 + s1    # sandwiches s2 between copies of s1, ...
    s3 = '"' + s3 + '"'   # encloses it in double quotes,...
    return s3            # and returns it.


a = "aaa"
pdb.set_trace()
b = "bbb"
c = "ccc"
final = combine(a, b)
print final

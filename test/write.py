import time
print 'start'
f= open('test1','w')
for i in range(100000):
    f.write(str(i)+'\n')
f.close()
print 'finish'

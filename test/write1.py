import time
print 'start'
f= open('test2','w')
for i in range(100000):
    f.write(str(i)+'\n')
f.close()
print 'finish'

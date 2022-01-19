import datetime
from pydoc import splitdoc

from time import time

# ____________________________________Part 1 (1st task)__________________________________________

print('\n')
print('_____________')
print('Part 1 : 1st task')
print('_____________')
lines = []
with open('wk2_test2_in.log') as f:
    lines = f.readlines()

count = 0


# use datetime package & funtion to perform a simple abstraction for desirable date/time result
firstLog=lines[0]
firstLog=firstLog[0:27]
fdate = datetime.datetime(int(firstLog[0:4]),int(firstLog[5:7]),int(firstLog[8:10]),int(firstLog[11:13]),int(firstLog[14:16]),int(firstLog[17:19]))

lastLog=lines[len(lines) -1]
lastLog=lastLog[0:27]
ldate = datetime.datetime(int(lastLog[0:4]),int(lastLog[5:7]),int(lastLog[8:10]),int(lastLog[11:13]),int(lastLog[14:16]),int(lastLog[17:19]))

print('\n')
print('The period (time range) that is covered by this log:')


#Check miliseconds
if (float(firstLog[20:23])-float(lastLog[20:23]))>0:
    print(ldate-fdate,'hours and',(float(firstLog[20:23])-float(lastLog[20:23])),'miliseconds')
else:
    print(ldate-fdate,'hours and',(float(lastLog[20:23])-float(firstLog[20:23])),'miliseconds')
print('\n')




# ____________________________________Part 1 (2nd & 3rd task)__________________________________________

print('_____________')
print('Part 1 : 2nd & 3rd task')
print('_____________')
print('\n')
flagMinor=0;
flagMajor=0;
listOfMinor=[]
listOfMajor=[]
for row in lines:   
    splitC=row.split('[')[1]  # split and check the kind of Collection
    kindOfCollection=splitC[0:2]
    if kindOfCollection == 'GC':  # Minor
        flagMinor+=1
        listOfMinor.append(row)  # keep it for the next task
    
    
    else:                        # Major
        flagMajor+=1
        listOfMajor.append(row) # keep it for the next task

print('Number of Minor (GC) Collections:')
print(flagMinor)
print('\n')
print('Number of Major (Full GC) Collections:')
print(flagMajor)
print('\n')


# ____________________________________Part 2 (1st & 2nd task)__________________________________________
 

print('___________________________________________________________________________________________')
print('\n')
print('Part 2 : 1st & 2nd task')
print('_____________')
print('\n')
TimesForMinor=[]
TimesForMajor=[]
for row in listOfMinor:  
    splitMinor=row.split(',')[1]  #find the overall excecuted time (as per the form of .log file)
    splitMinor=splitMinor[1:8]
    splitMinor=float(splitMinor)
    TimesForMinor.append(splitMinor) # keep it for the next task
    splitMinor+=splitMinor
    

avgMinor=splitMinor/flagMinor
print('Average Time of Minor GC:')  
print(avgMinor)

for row in listOfMajor:  
    splitMaj=row.split(',')[1]  #find the overall excecuted time (as per the form of .log file)
    splitMaj=splitMaj[1:8]
    splitMaj=float(splitMaj)
    TimesForMajor.append(splitMaj)  # keep it for the next task
    splitMaj+=splitMaj



avgMajor=splitMaj/flagMajor
print('Average Time of Major GC:')
print(avgMajor)
print('\n')





# ____________________________________Part 2 (3rd task)__________________________________________

print('_____________')
print('Part 2 : 3rd task')
print('_____________')
print('\n')

TimesForMajor = sorted(TimesForMajor, key = float)
#print(TimesForMajor)

TimesForMinor = sorted(TimesForMinor, key = float)
#print(TimesForMinor)


top3Minor=TimesForMinor[-3:]
top3Minor=top3Minor[::-1]
print('\n')
print('_____________')
print('top 3 Minor Times')
print(top3Minor)


top3Major=TimesForMajor[-3:]
top3Major=top3Major[::-1]


print('\n')
print('_____________')
print('top 3 Major Times')
print(top3Major)

for row in listOfMinor:  
   if str(top3Minor[0]) in row:
       top1=row
   if str(top3Minor[1]) in row:
       top2=row
   if str(top3Minor[2]) in row:
       top3=row




print('\n')
print('Top 1 Minor Collection:')
print(top1)
print('\n')
print('Time Occured:')
print(top1[0:23])
print('\n')
print('Amount of Time Took:')
top1=top1.split(',')[1]  #find the overall excecuted time (as per the form of .log file)
top1=top1[1:8]
top1=float(top1)
print(top1)
print('_____________')



print('\n')
print('Top 2 Minor Collection:')
print(top2)
print('\n')
print('Time Occured:')
print(top2[0:23])
print('\n')
print('Amount of Time Took:')
top2=top2.split(',')[1]  #find the overall excecuted time (as per the form of .log file)
top2=top2[1:8]
top2=float(top2)
print(top2)
print('_____________')


print('\n')
print('Top 3 Minor Collection:')
print(top3)
print('\n')
print('Time Occured:')
print(top3[0:23])
print('\n')
print('Amount of Time Took:')
top3=top3.split(',')[1]  #find the overall excecuted time (as per the form of .log file)
top3=top3[1:8]
top3=float(top3)
print(top3)
print('_____________')


print('_____________')
print('_____________')


for row in listOfMajor:  
   if str(top3Major[0]) in row:
       top1=row
   if str(top3Major[1]) in row:
       top2=row
   if str(top3Major[2]) in row:
       top3=row



print('\n')
print('Top 1 Major Collection:')
print(top1)
print('\n')
print('Time Occured:')
print(top1[0:23])
print('\n')
print('Amount of Time Took:')
top1=top1.split(',')[1]  #find the overall excecuted time (as per the form of .log file)
top1=top1[1:8]
top1=float(top1)
print(top1)
print('_____________')

print('\n')
print('Top 2 Major Collection:')
print(top2)
print('\n')
print('Time Occured:')
print(top2[0:23])
print('\n')
print('Amount of Time Took:')
top2=top2.split(',')[1]  #find the overall excecuted time (as per the form of .log file)
top2=top2[1:8]
top2=float(top2)
print(top2)
print('_____________')

print('\n')
print('Top 3 Major Collection:')
print(top3)
print('\n')
print('Time Occured:')
print(top3[0:23])
print('\n')
print('Amount of Time Took:')
top3=top3.split(',')[1]  #find the overall excecuted time (as per the form of .log file)
top3=top3[1:8]
top3=float(top3)
print(top3)
print('_____________')
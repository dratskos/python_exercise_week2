import csv
import os
import re


input_file='wk2_test1_in.csv'
oldFile = open(input_file, 'r')
reader = csv.reader(oldFile, delimiter=',')



output_file='wk2_test1_out'
filename = output_file+'.csv'

if os.path.exists(filename):
    print('\n \n')
    print('\n \n')
    os.remove(filename)
    


with open(filename,'w') as newFile:
       writer = csv.writer(newFile, delimiter=',')
       for row in reader:

          #Clear empty spaces between elements
          filter_object = filter(lambda x: x != "", row)
          without_empty_strings = list(filter_object)
          row=without_empty_strings
          

          #Clear thrash variables (e.x end of original file)
          for i in range(0,len(row),1):
            row[i]=re.sub(r'[\W_]+', '', row[i])  
            
            

          #Control the range/length of each element(cut for <15 or fullfill for spaces >10)
            if len(row[i])<10:  
               row[i]="{:<10}".format(row[i])   
            elif len(row[i])>15:
                cutChars=row[i]
                row[i]=cutChars[:15]
            else:
                row[i]=row[i]
        
          #Delete empty rows
          if any(row):
            writer.writerow(row)
          
    

print('\n \n')
print('The Program Excecuted Succesfully! Please check your files....')
print('\n \n')
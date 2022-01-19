class MyCList_Mean:

    def __init__(self):
       self.variables=[]
       
    def setting_default(self):
        self.variables=[1,2,17,52.5, 43, 4.4,10]


    def set_list(self,vars):
        self.variables=vars

    def get_list(self):
        return self.variables

    def calc_avg(self):
        sum=0
        for i in range(0,len(self.variables),1):
            if isinstance(self.variables[i], str):  #Check if there is a string element
                i+=1                                # if true --ignore
                
            else:
                sum=sum+self.variables[i]

        avg=sum/len(self.variables)
        return avg

    
TestList1=MyCList_Mean()
TestList1.set_list([1,2,17,52.5, 43,4.4,10])

TestList2=MyCList_Mean()
TestList2.set_list([1,2,3,4,5,6,7,"dog"])


print('\n \n')
print('This is the Test1 you want: ' ,TestList1.get_list())
print('Total Average of Test1 List: %.4f'  % TestList1.calc_avg())


print('\n \n')
print('This is the Test2 you want: ' ,TestList2.get_list())
print('Total Average of Test2 List: %.4f'  % TestList2.calc_avg())
print('\n \n')








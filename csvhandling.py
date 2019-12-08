# import csv

# with open('registration.csv') as csvfile:#default is read only
#     rows=csv.DictReader(csvfile)
#     for row in rows:
#         name=row['name']
#         email=row['email']
#         print[name]

        # server.send_email(name.email)




        #classes and object



        # def car()
            #def __int__(self)
            #self.year=1990
            #def __int__(self,year)
            #self.year=year


            

            #constructors are the onces that can initialize the values in the class
            #__int___()>>>to define the constructor
            #__int__(self)>>> equal to "this " in c#


            #def display(self):
                #print("i am blah")

            #class tata(car)
            #def__int__(self,year):
            #....................


            #obj=tata(1990)
            #obj.display()# this tata will inherit display method from the class car


            #overriding
            #in tata class
            #def disp;ay(self):
            #print('i am child')

            # this will print i am child insteda when called now instead of i am parent



            class Car():
                def __int__(self,year):
                    self.year=year

                def display(self):
                    print('i am inside parent class')

                class Tata(Car):
                    def __int__(self,year):
                        self.year=year

                    def display(self):
                        print('i am inside the child class')



            t=Tata(2016)
            t.display()
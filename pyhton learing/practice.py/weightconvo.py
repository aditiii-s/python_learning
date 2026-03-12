#here is the problem of making a converter pound to kilo and vice versa 
weight= int(input("weight:"))
unit=input("K or P")

if unit.upper()== "P":
    converted= weight* 0.45
    print(f"weight is {converted} kilos ")
else:
    converted=weight/0.45
    print(f"weight is {converted} pounds ")    

    # i just have to take care we take weigth in integer 
    #and then we convert all the unit input taken into upper case so it dont get confused 
    #now in the if else part mei convert it into kilo and other units lets make a a converter from meter to kilo meter

length= int(input("length is : "))
unit=input("km or m ")
if unit.lower() == "km":
        convert=length*1000
        print(f"so so the length is {convert} m")
else:
        convert=length/1000
        print(f"so the length is {convert} km ")    

      #NOTE: HERE IS I GOT PROBLEM IN PRINTING THE SECOND CODE KYUKI MAINE FIRST CODE K ELSE PART MEI HI START KR DIYA SECOND CODE 
      
 
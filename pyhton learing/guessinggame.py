#here we gonna make a guess game for numbers 
secret_number=7
i =0
while ( i <3):
    guess=int(input("guess "))
    i +=1
    if guess==secret_number:
        print(f"guess:{guess}")
        print("won:")
        break  
else: 
 print("fail")    
        
    # 3 BAAR LOOP KO CONTIINUE KRNE K LIYE ELSE WHILE K USE HOGA 
    #so here is the mistake that i forget to include i++ increment operator to keep running the condition 
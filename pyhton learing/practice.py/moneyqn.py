#PRICE OF HOUSE IS 1 MILLION IF BUYERS HAS GOOD CREDIT THEY NEED TO PUT DOWN 10 % OTHERWISE THEY NEED TO PUT DOWN 20% PRINT DOWN THE PAYMENT 
price=1000000
down_pay=int(input("0/1"))
if down_pay == 1:
    pay =0.1*price
else:
    pay =0.2*price    

print(f"the price is {pay}")    
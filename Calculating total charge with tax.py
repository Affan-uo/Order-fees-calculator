                               #Calculating total charge with tax
#Setting  the variables
total_charge = 0
canadaiscountry = False
canprovince=False
alberta = False
all_other_province = False
cost = 0
province=' '
provincecalc = float(cost*0.5) 
albertacalc = float(cost * 0.3) 
othercalc=float(cost * 0.1) 
#Requesting for the user's details
cost=float(input('How much is the item ? '))
country=input('what is the name of your country ? ').lower()
#Setting the conditions
GST = .05  
HST = .13
PST = .06
albertacalc=(GST*cost) + cost
provincecalc=HST*cost + cost
total=GST*cost+ PST*cost
othercalc=total + cost
if country == 'canada' :
    canadaiscountry = True
    province = input('which province are you from ? ').lower()
    print("There will be tax charge")
    if canadaiscountry and province =="alberta" :
       print (f"The price of the item is ${albertacalc} ")
    elif canadaiscountry and (province =="ontario" or province == "new burnswick" \
        or province == "nova scotia") :
        print(f'The price of the item is ${provincecalc}')
    else :
        print(f"The cost of the item is ${othercalc}")
elif country != 'canada' :
    print ('There wil be no tax charge!')
    print (f'The price of the item is ${cost}')

print('Thank you for your patronage!  ')

q=[["The International Literacy Day is observed on:","sep 8","nov 28","may 2","sep 22",1],
   ["The language of Lakshadweep. a Union Territory of India, is:","Tamil","Hindi","Malayalam","Telugu",3],
   ["In which group of places the Kumbha Mela is held every twelve years?","Ujjain. Purl; Prayag. Haridwar","Prayag. Haridwar, Ujjain,. Nasik","Rameshwaram. Purl, Badrinath. Dwarika","Chittakoot, Ujjain, Prayag,'Haridwar",2],
   ["Bahubali festival is related to:","Islam","Hinduism","Buddhism","Jainism",4],
   ["Which day is observed as the World Standards  Day?","June 26","Oct 14","Nov 15","Dec 2",2],
   ["The International Literacy Day is observed on:","sep 8","nov 28","may 2","sep 22",1],
   ["The language of Lakshadweep. a Union Territory of India, is:","Tamil","Hindi","Malayalam","Telugu",3],
   ["In which group of places the Kumbha Mela is held every twelve years?","Ujjain. Purl; Prayag. Haridwar","Prayag. Haridwar, Ujjain,. Nasik","Rameshwaram. Purl, Badrinath. Dwarika","Chittakoot, Ujjain, Prayag,'Haridwar",2],
   ["Bahubali festival is related to:","Islam","Hinduism","Buddhism","Jainism",4],
   ["Which day is observed as the World Standards  Day?","June 26","Oct 14","Nov 15","Dec 2",2],
    ["The International Literacy Day is observed on:","sep 8","nov 28","may 2","sep 22",1],
   ["The language of Lakshadweep. a Union Territory of India, is:","Tamil","Hindi","Malayalam","Telugu",3],
   ["In which group of places the Kumbha Mela is held every twelve years?","Ujjain. Purl; Prayag. Haridwar","Prayag. Haridwar, Ujjain,. Nasik","Rameshwaram. Purl, Badrinath. Dwarika","Chittakoot, Ujjain, Prayag,'Haridwar",2],
   ["Bahubali festival is related to:","Islam","Hinduism","Buddhism","Jainism",4],
   ["Which day is observed as the World Standards  Day?","June 26","Oct 14","Nov 15","Dec 2",2]
]
amt=0
p=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000]
for i in range(len(q)):
    print(f"Question for Rs.{p[i]} is :")
    print(f"{q[i][0]}")
    print(f"a. {q[i][1]}            b. {q[i][2]} ")
    print(f"c. {q[i][3]}            d. {q[i][4]} ")
    ans=int(input("Enter your answer from 1 to 4:-"))
    if(ans==q[i][-1]):
        print(f"Congratulations, you have won Rs.{p[i]}")
        if(i==4):
            amt=10000
        elif(i==9):
            amt=320000
        elif(i==14):
            amt=10000000
    else:
        print("Ohh Noo!Wrong Answer")
        break 
print(f"Your winning amount is {amt}")
if(amt>0):
    print(f"The amount {amt} will be transffered in your bank account within 24 hours")  

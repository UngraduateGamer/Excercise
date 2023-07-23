qus_ans=[
[' Who is the father of Computers?','James Gosling','Charles Babbage','Dennis Ritchie','Bjarne Stroustrup',2],

['Which of the following is the correct abbreviation of COMPUTER?','Commonly Occupied Machines Used in Technical and Educational Research','Commonly Occupied Machines Used in Technical and Educational Researchee','Commonly Oriented Machines Used in Technical and Educational Research',
'Commonly Operated Machines Used in Technical and Educational Research',4],

['Which of the following is the correct definition of Computer?','Computer is a machine or device that can be programmed to perform arithmetical or logic operation sequences automatically','Computer understands only binary language which is written in the form of 0s & 1s',' Computer is a programmable electronic device that stores, retrieves, and processes the data','All of the mentioned',4],

['What is the full form of CPU?','Computer Processing Unit','Computer Principle Unit','Central Processing Unit','Control Processing Unit',3],

['Which of the following language does the computer understand?','Computer understands only C Language','Computer understands only Assembly Language','Computer understands only Binary Language','Computer understands only BASIC',3],

['Which of the following computer language is written in binary codes only?','pascal','machine language','C','c#',2],

['Which of the following is the brain of the computer?','Central Processing Unit','Memory','Arithmetic and Logic unit','Control unit',1],

['Which of the following is not a characteristic of a computer?','Versatility','Accuracy','Diligence','I.Q.',4],

['Which of the following is the smallest unit of data in a computer?','Bit','KB','Nibble','Byte',1],

[' Which of the following unit is responsible for converting the data received from the user into a computer understandable format?','Output Unit','Input Unit','Memory Unit','Arithmetic and Logic Unit',2],

['Which of the following monitor looks like a television and are normally used with non-portable computer systems?','LED','LCD','CRT','Flat Panel Monitors',3],

['Which of the following is not a type of computer code?','EDIC','ASCII','BCD','EBCDIC',1],

[' Which of the following part of a processor contains the hardware necessary to perform all the operations required by a computer?','Controller','Register','Cache','Data Path',4],

['Which of the following is designed to control the operations of a computer?','User','Application Software','System Software','Utility Software',3],

[' Which of the following is used in EBCDIC?','Super Computers','Mainframes','Machine Codes','Programming',2]

]
levels=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000]
money=0
for i in range(len(qus_ans)):
    questions=qus_ans[i]
    print(f"Question for  Rs.{levels[i]} in your computer Screen")
    print(f" \nQus: {i+1} : {questions[0]}")
    print(f"a: {questions[1]}")
    print(f"b: {questions[2]}")
    print(f"c: {questions[3]}")
    print(f"d: {questions[4]}")
    results=int(input("Enter Your Answer(1-4): "))  
    if i==5:
        money=levels[4]
    elif i==10:
        money=levels[9]
    elif i==15:
        money=levels[-1]
    if results==questions[5]:
        print("\ncongratulations! you choose the Correct Option")
    else:
        print("\nWrong Answer")
        break
        
print(f"Your Take Home Money is : Rs. {money}")
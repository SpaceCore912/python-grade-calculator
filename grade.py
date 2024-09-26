def calculator()->int:

    
    enumber="Enter the number of "
    egrade="Enter grade for "
    labs=int(input(enumber + "labs completed: "))
    quizzes=int(input(enumber + "quizzes completed: "))
    lista=[int(input(egrade +"Assignment 1: ")),int(input(egrade+"Assignment 2: ")),int(input(egrade +"Assignment 3: ")),int(input(egrade+"Assignment 4: "))]
    print(lista)
    

    midterm1=int(input(egrade+"Midterm 1: "))
    midterm2=int(input(egrade+"Midterm 2: "))
    final=int(input(egrade+"Final Exam: "))
    midfinalprep=int(input(egrade+"Midterms and Final Preparation: "))
    return round((labs*(20/6*100)+quizzes*(15/6*100)+(lista[0]+lista[1]+lista[2]+lista[3])*4+midterm1*12.5+midterm2*12.5+final*18+midfinalprep*6)/100)
print("Your grade is: "+ str(calculator()))
    

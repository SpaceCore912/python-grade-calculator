def calculator()->int:

    
    enumber="Enter the number "
    egrade="Enter grade for "
    labs=int(input(enumber + "labs completed: "))
    quizzes=int(input(egrade + "quizzes completed: "))
    listassign=[int(input(egrade +"1: ")),int(input(egrade+"2: ")),int(input(egrade +"3: ")),int(input(egrade+"4: "))]
    print(listassign)
    

    midterm1=int(input(egrade+"Midterm 1: "))
    midterm2=int(input(egrade+"Midterm 2: "))
    final=int(input(egrade+"Final Exam: "))
    midfinalprep=int(input(egrade+"MIdterms and Final Preparation"))
    return (labs*(20/6)+quizzes*(15/6)+(list[1]+list[2]+list[3]+list[4])*4+midterm1*12.5+midterm2*12.5+final*18+midfinalprep*6)
print(calculator())
    

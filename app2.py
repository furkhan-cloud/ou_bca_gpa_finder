class grade:
    def __init__(self,sub1,sub2,sub3,sub4,sub5,lab1,lab2,lab3):
        if sub1 == "S":
            sub1=10 
        elif sub1 == "A":
            sub1=9
        elif sub1 == "B":
            sub1=8
        elif sub1 == "C":
            sub1=7
        elif sub1 == "D":
            sub1=6
        elif sub1 == "E":
            sub1=5
        
        if sub2 == "S":
            sub2=10 
        elif sub2 == "A":
            sub2=9
        elif sub2 == "B":
            sub2=8
        elif sub2 == "C":
            sub2=7
        elif sub2 == "D":
            sub2=6
        elif sub2 == "E":
            sub2=5

        if sub3 == "S":
            sub3=10 
        elif sub3 == "A":
            sub3=9
        elif sub3 == "B":
            sub3=8
        elif sub3 == "C":
            sub3=7
        elif sub3 == "D":
            sub3=6
        elif sub3 == "E":
            sub3=5
        
        if sub4 == "S":
            sub4=10 
        elif sub4 == "A":
            sub4=9
        elif sub4 == "B":
            sub4=8
        elif sub4 == "C":
            sub4=7
        elif sub4 == "D":
            sub4=6
        elif sub4 == "E":
            sub4=5
        
        if sub5 == "S":
            sub5=10 
        elif sub5 == "A":
            sub5=9
        elif sub5 == "B":
            sub5=8
        elif sub5 == "C":
            sub5=7
        elif sub5 == "D":
            sub5=6
        elif sub5 == "E":
            sub5=5

        if lab1 == "S":
            lab1=10 
        elif lab1 == "A":
            lab1=9
        elif lab1 == "B":
            lab1=8
        elif lab1 == "C":
            lab1=7
        elif lab1 == "D":
            lab1=6
        elif lab1 == "E":
            lab1=5
        
        if lab2 == "S":
            lab2=10 
        elif lab2 == "A":
            lab2=9
        elif lab2 == "B":
            lab2=8
        elif lab2 == "C":
            lab2=7
        elif lab2 == "D":
            lab2=6
        elif lab2 == "E":
            lab2=5
        
        if lab3 == "S":
            lab3=10 
        elif lab3 == "A":
            lab3=9
        elif lab3 == "B":
            lab3=8
        elif lab3 == "C":
            lab3=7
        elif lab3 == "D":
            lab3=6
        elif lab3 == "E":
            lab3=5
        
        print(f"Your Gpa = {((sub1*4.0)+(sub2*4.0)+(sub3*4.0)+(sub4*4.0)+(sub5*4.0)+(lab1*2.0)+(lab2*2.0)+(lab3*2.0))/24}")


year_1=grade('S','S','S','E','B','S','S','S')
year_2=grade('S','S','S','S','E','S','S','S')

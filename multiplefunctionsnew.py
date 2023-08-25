
class multiplefunctions():
    def subfields():
        sub=("Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing")
        print("Sub-fields in AI are:")
        ret = "Sub-fields in AI are:"
        for i in sub:
            print(i)
            ret = i
        return ret

    def oddeven():
        num=int(input("Enter a number:"))
        if(num%2==0):
                print(num," is an EVEN number")
                oe=num,"is an EVEN number"
        else:
                print(num, "is an ODD number")
                oe=num, "is an ODD number"
        return oe
    
    def Elegible():
        Gender=str(input("Your Gender:")).lower()
        Age=int(input("Your Age:"))
        if(Gender=='male')and(Age>=21):
            print("ELIGIBLE")
            marriage="ELIGIBLE"
        elif(Gender=='female')and(Age>=18):
            print("ELIGIBLE")
            marriage="ELIGIBLE"
        else:
            print("NOT ELIGIBLE")
            marriage="NOT ELIGIBLE"
        return marriage

    def percentage():
        sub1=int(input("Subject1="))
        sub2=int(input("Subject2="))
        sub3=int(input("Subject3="))
        sub4=int(input("Subject4="))
        sub5=int(input("Subject5="))
        total=sub1+sub2+sub3+sub4+sub5
        percent=float((total/500)*100)
        print("Total=",total)
        print("Percentage=",percent)
        return(total,percent)

    def triangle():
        h=int(input("Height:"))
        b=int(input("Breadth:"))
        area=(h*b)/2
        print("Area formula:(Height*Breadth)/2")
        print("Area of Triangle:",area)
        h1=int(input("Height1:"))
        h2=int(input("Height2:"))
        b1=int(input("Breadth:"))
        peri=h1+h2+b1
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of Triangle:" ,peri)
        return(area,peri)

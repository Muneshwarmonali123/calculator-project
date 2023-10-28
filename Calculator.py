def add(a,b):
    ans=a+b
    print("Add=",ans)
def sub(a,b):
    ans=a-b
    print("Sub=",ans)
def mul(a,b):
    ans=a*b
    print("Mul=",ans)
def div(a,b):
    ans=a/b
    print("Div=",ans)
def power(a,b):
    ans=a**b
    print("Power=",ans)
def floordiv(a,b):
    ans=a//b
    print("Floordiv=",ans)

def mod(a,b):
    ans=a%b
    print("Mod=",ans)
while True:
    ch=int(input("\nEnter Choice:\n1.Add\t2.Sub\n3.Mul\t4.Div\n5.Power\t6.Floordiv\n7.Mod\t8.Exit"))
    if ch==1:
        print("Code for Add")
        fn=int(input("Enter First No.:"))
        sn=int(input("Enter Second No.:"))
        add(fn,sn)
    elif ch==2:
        print("Code for Sub")
        fn=int(input("Enter First No.:"))
        sn=int(input("Enter Second No.:"))
        sub(fn,sn)
    elif ch==3:
        print("Code for Mul")
        fn=int(input("Enter First No.:"))
        sn=int(input("Enter Second No.:"))
        mul(fn,sn)
    elif ch==4:
        print("Code for Div")
        fn=int(input("Enter First No.:"))
        sn=int(input("Enter Second No.:"))
        div(fn,sn)
    elif ch==5:
        print("Code for Power")
        fn=int(input("Enter First No.:"))
        sn=int(input("Enter Second No.:"))
        power(fn,sn)
        

    elif ch==6:
        print("Code for Floordiv")
        fn=int(input("Enter First No.:"))
        sn=int(input("Enter Second No.:"))
        floordiv(fn,sn)
        

    elif ch==7:
        print("Code for Mod")
        fn=int(input("Enter First No.:"))
        sn=int(input("Enter Second No.:"))
        mod(fn,sn)

    elif ch==8:
        print("Code for Exit")
        break
    else:
        print("Invalid Choice")
        

        

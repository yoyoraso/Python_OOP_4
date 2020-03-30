import read
import write
m=input("""
Enter 'Read' To Read a File'
Enter 'Write' To Read a File'
""").lower()
if m == "read":
    z=read.re(input("Enter File Name.Extintion:"),"r")
elif m == "write":
    z=write.wr(input("Enter File Name.Extintion:"),"a")
else :
    print("Error")
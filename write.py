def wr(a,b):
    f= open(a,b)
    f.write("\n")
    f.write(input("Enter What You Want To Write : "))
    f.close()
import io

try :
    with open("niema.txt","r") as f_open:
        content = f_open.readlines()
except FileNotFoundError:
    print("No such file")


try :
    with open("niema.txt","w") as f_open:
        content = f_open.readlines()
except io.UnsupportedOperation:
    print("Can't read this file")


try :
    with open("niema.txt","x") as f_open:
        print("done")
except FileExistsError:
    print("File exists")
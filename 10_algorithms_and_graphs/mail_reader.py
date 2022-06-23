def file_open():
    with open("mail.txt") as fopen:
        content = fopen.readlines()
        return content

def mail_in_list(mail,l_mails):
    return mail in l_mails

def main():
    mail = input("write down your e-mail")
    list_of_mails = file_open()
    print(mail_in_list(mail,list_of_mails))

if __name__ == "__main__":
    main()
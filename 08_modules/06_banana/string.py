def get_longest_string(string):
    longest_str = ""
    temp_str = "b"
    for i in string:
        print(temp_str)
        print(longest_str)
        if i == temp_str[0]:
            temp_str.join(i)
        else:
            if len(temp_str) >= len(longest_str):
                longest_str = temp_str
            temp_str = ""
            temp_str.join(i)
    return longest_str
def main ():
    string = "bannnnnnnnnnana"
    longest_list = get_longest_string(string)
    print(longest_list)


main()


"""
good.email@example.com True


"""
def check_email(string):
    if ' ' not in string and ('@' in string):
        print("In the first block")
        a = string.find('@')
        c = string.find('.', a, len(string))
        if c != 0:
            print('In the 2nd block')
            return '.' in string 
        else:
            return False
    else:
        return False

print(check_email('good.email@example.com'))
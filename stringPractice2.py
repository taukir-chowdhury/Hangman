def what_to_do(instructions):
    if instructions.startswith('Simon says') or instructions.endswith('Simon says'):
        temp = instructions.find('Simon says')
        if temp == 0 :
            return 'I' + instructions[len("Simon says"):]
        else:
            return 'I ' + instructions[0:temp]
    
    else :
         return "I won't do it!"

print(what_to_do('Simon says'))
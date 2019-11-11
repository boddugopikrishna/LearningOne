def sum_func(n):
    if len(str(n)) == 1:
        return n
    else:
        return n % 10 + sum_func(n//10)

def word_split(phrase,list_of_words,output= None):
    if len(phrase) == '':
        if list_of_words[0] in phrase:
            phrase.remove(list_of_words[0])
            list_of_words.pop(list_of_words[0])
            output.append(list_of_words[0])
            return word_split(phrase,list_of_words)
    else:
        return []

passwords = ['because','can','do','must','we','what']
loginAttempt = 'wedowhatwemustbecausewecan'
passwords2 = ['ozkxyhkcst','xvglh','hpdnb','zfzahm']
loginAttempt2 = 'zfzahm'
def passwordCracker(passwords, loginAttempt):
    if loginAttempt in passwords:
        return(loginAttempt)
    else:
        return "WRONG PASSWORD"



def concatPasswords(passwords,loginAttempt,output = None):
    if output == None:
        output = ""
    for password in passwords:
        if loginAttempt.startswith(password):
            output = output + password
            return concatPasswords(passwords,loginAttempt[len(password):],output)
    if output == loginAttempt:
        return output
    else:
        return "WRONG PASSWORD"

print(concatPasswords(passwords2,loginAttempt2))







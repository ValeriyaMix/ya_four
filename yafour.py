import re

line = input()
if line.isalpha():
    print(len(line))
else:
    number_list = re.split('[a-z]', line, flags=re.IGNORECASE)
    digit_list = []
    for i in number_list:
        if i.isdigit():
            digit_list.append(int(i))
    digit_sum = sum(digit_list)
    alphabet_list = re.split('[a-z][0-9]{1,1000}', line, flags=re.IGNORECASE)
    alp_list = []
    for i in alphabet_list:
        if i.isalpha():
            alp_list.append(i)
alph_string = ''.join(alp_list)
alph_sum = len(alph_string)

print(digit_sum + alph_sum)



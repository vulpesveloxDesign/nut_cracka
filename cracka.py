import time

a_list = []

with open('pw_1.txt', 'r') as f:
    for password in f.read().splitlines():
        a_list.append(password)

with open('names_g.txt', 'r') as f:
    for girlname in f.read().splitlines():
        a_list.append(girlname)

with open('names_b.txt', 'r') as f:
    for boyname in f.read().splitlines():
        a_list.append(boyname)

print(len(a_list))
for i in a_list:
    print(i)

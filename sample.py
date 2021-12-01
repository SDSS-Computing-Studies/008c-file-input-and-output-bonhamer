#!python3



filevar = open('data01.txt','r')
x = filevar.read()
print(x)

print("This is line 1\nThis is line 2\nThis is line 3\nThis is line 4\nThis is line 5")

y = x.split('\n')

for eachLine in y:
    print(f"The line was :{eachLine}")
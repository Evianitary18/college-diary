kalimat = input(). lower()
x = ""
for i in kalimat:
    if i.isalpha():
        x += i
y = ""
length = len(x)
for i in range(0, length // 1):
    if (kalimat[i]!=(kalimat[length-i])):
        y += x[i]
print(y)

if(x == y):
    print("Ini Palindrom")
else:
    print("Ini Bukan Palindrom")




# def misteri(a, b):
#     if a > b:
#         temp = a
#         a = b
#         b = temp

#     if a == b :
#         return a
#     else :
#         return misteri(a + 1, b) + a
    
# def misteri(a, b):
#     if a > b:
#         temp = a
#         a = b
#         b = temp

#     if a == b:
#         return b
#     else:
#         mid = (a + b) // 2
#         left_sum = misteri(a, mid)
#         right_sum = misteri(mid + 1, b)
#         return left_sum + right_sum

# a = int(input("Masukkan nilai a: "))
# b = int(input("Masukkan nilai b: "))

# result = misteri(a, b)
# print(f"Jumlah bilangan bulat antara {a} dan {b} adalah: {result}")


# def misteri(a, b):
#     if a > b:
#         temp = a
#         b = temp
#     else:
#         temp = a
#     a = 0
#     while temp <= b:
#         a += temp
#         temp += 1
#     return a

# print(misteri(5,2))

# def misteri(a, b):
#     if a > b:
#         temp = a
#         a = b
#         b = temp

#     if a == b:
#         return b
#     else:
#         mid = (a + b) // 2
#         left_sum = misteri(a, mid)
#         right_sum = misteri(mid + 1, b)
#         return left_sum + right_sum

# a = int(input("Masukkan nilai a: "))
# b = int(input("Masukkan nilai b: "))

# result = misteri(a, b)
# print(f"Jumlah bilangan bulat antara {a} dan {b} adalah: {result}")

# def misteri(a, b):
#     if a > b:
#         temp = a
#         a = b
#         b = temp

#     total = 0
#     while a <= b:
#         total += a
#         a += 1
    
#     return total

# a = int(input("Masukkan nilai a: "))
# b = int(input("Masukkan nilai b: "))

# result = misteri(a, b)
# print(f"Jumlah bilangan bulat antara {a} dan {b} adalah: {result}")

# def misteri(a, b):
#     if a > b:
#         temp = b
#         b = a
#     else:
#         temp = a
#     a = 0
#     while temp <= b:
#         a += temp
#         temp += 1
#     return a

# print(misteri(5,2))

def misteri(a, b):
    if a > b:
        temp = a
        a = b
        b = temp

    if a == b:
        return b
    else:
        temp = (a + b) // 2
        return misteri(a, temp) + misteri(temp + 1, b)
print(misteri(5,2))
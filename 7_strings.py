text = "Hello, world!"

print(text[0]) # H
print(text[7]) # w

#print(text[22]) # Помилка!

print(text[:10])    # Hello, wor
print(text[3:6])    # lo,
print(text[3:])     # lo, world!
print(text[3:10:4]) # lw
print(text[::2])    # Hlo ol!

print(text[-1]) # !
print(text[-4]) # r

print(text[::-1])
print(text[:-7:-1])
print(text[-3:-10:-1]) 
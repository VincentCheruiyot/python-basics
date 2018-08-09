file = open("data.txt","r")

lines= file.readlines()
for line in lines:
    print(line.upper())

# print(lines)

file.close()
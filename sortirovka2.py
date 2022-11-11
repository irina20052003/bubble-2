q = input("Введите свое имя: ")
print("Привет, " + q)
file = open("data.txt", "r")
temp = file.read()
lst1 = temp.split(" ")
file.close()
for i in range(len(lst1)):
    lst1[i] = int(lst1[i])
print("Изначальный список: ", lst1)
for i in range(len(lst1) - 1):
    for  j in range(len(lst1) - i - 1):
        if lst1[j] > lst1[j+1]:
            x = lst1[j]
            lst1[j] = lst1[j+1]
            lst1[j+1] = x
print("Упорядоченный список: ", lst1)

if __name__ == "__main__":
    pass

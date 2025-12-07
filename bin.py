num = input("Enter a number: ")

clean_num = num.replace("-", "").replace(".", "")

i = 0
count = 0

while i < len(clean_num):
    j = 0
    while j < 1:   
        count += 1
        j += 1
    i += 1

print("Total digits:", count)
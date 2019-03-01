import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()


duplicates = []

# sort each name lists alphabetically
names_1.sort()
names_2.sort()

# assign initial values
len_name1 = len(names_1)
len_name2 = len(names_2)

index_name1 = 0
index_name2 = 0

# below compare each item from both list.
# since list are alphabetized, if one is less than other
# that doesn't need to be compared again.
# while loop ends when one of the list reached the end.

# I think this should satisfy stretch goal

while index_name1 < len_name1 and index_name2 < len_name2:
    if names_1[index_name1] == names_2[index_name2]:
        duplicates.append(names_1[index_name1])
        index_name2 += 1
        index_name1 += 1
    elif names_1[index_name1] > names_2[index_name2]:
        index_name2 += 1
    else:
        index_name1 += 1

'''
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)
'''
end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

cases = int(input())
lists = [[] for _ in range(cases)]

for i in range(cases):
    lists[i] = str(input()).split()

for i in range(cases):
    Great = int(max(lists[i]))

    A = Great - int(lists[i][0])
    B = Great - int(lists[i][1])
    C = Great - int(lists[i][2])

    print(f"{A} {B} {C}")


#print(lists[0][2])
#for i in range(cases):
    


#print(f"There are {cases} cases")
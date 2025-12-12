print("Problema 1".center(50,"="))

dict1 = {'bananas': 7, 'apples': 3, 'pears': 14}
dict2 = {'bananas': 3, 'apples': 6, 'grapes': 9}
merged = dict1

def mergedic(d1,d2):
    for i in dict2:
        print(i)
        if i not in merged or dict2[i] > merged[i]:
            merged[i] = dict2[i]
    return merged

finaldic = mergedic(dict1, dict2)
print(finaldic)

print("Problema 2".center(50,"="))

desired = [10.0, 5.0, 8.0, 3.0, 2.0]
actual = [10.3, 5.2, 8.4, 3.0, 1.2]
margin = 0.5

def margen_de_perdida(desired, actual, margin): 
    count = 0
    badcount = 0
    for i in range(len(actual)):
        res = desired[i] - actual[i]

        if abs(res) >= margin:
            badcount += 1
            print(f"{badcount}/{len(actual)} no satisfactorio")
        else:
            count += 1
    return print(f"{count}/{len(actual)} satisfactorio")

margen_de_perdida(desired, actual, margin)

print("Problema 3".center(50,"="))

mylist = [3, 2, 4, 6, 1]
fanout_value = 3

def difference_fanout(list, value ):
    out = []
    print(mylist[:1])
    for i in range(len(mylist)):
        print(mylist[i])

        

difference_fanout(mylist, fanout_value)
    

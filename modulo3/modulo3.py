print("Problema 1 - Merge de diccionarios".center(50,"="))

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

print("Problema 2 - Prueba de satisfacción".center(50,"="))

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

print("Problema 3 - Fanout Number".center(50,"="))

mylist = [3, 2, 4, 6, 1]
fanout_value = 3

def difference_fanout(list, value ):
    out = []  # Lista principal para guardar todas las sublistas
    for i in range(len(mylist)):
        sublist = []  # Sublista para las diferencias del elemento actual
        for j in range(i + 1, min(i + 1 + value, len(mylist))):
            sublist.append(mylist[i] - mylist[j])
        out.append(sublist)
    return out

# Probar la función
result = difference_fanout(mylist, fanout_value)
print(result)

print("Problema 4 - Diccionario".center(50,"="))

s = [12,-14.23,"hello", True, "Aha", 10.1, None, 5]

def int_to_str(n):
    number_dic = {"0": "zero", "1": "one", "2": "two", "3": "three",
               "4": "four", "5": "five", "6": "six", "7": "seven",
               "8": "eight", "9": "nine", "-": "neg"}
    return "-".join(number_dic[digit] for digit in str(n))

def item_to_transcript(item):
    if isinstance(item, bool): 
        return '<OTHER>'
    if isinstance(item, int): 
        return int_to_str(item)
    if isinstance(item, float): 
        return int_to_str(int(item)) + " and float"
    if isinstance(item, str): 
        return item
    return '<OTHER>'

def concat_to_str(s):
    return print(" | ".join(item_to_transcript(item) for item in s))

concat_to_str(s)
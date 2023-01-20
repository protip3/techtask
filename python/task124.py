'#Task1'

result = {}
word = "Dotools Sberdata"
def task1(word):
    for i in range(len(word)):
        result[i] = word[i]


task1(word)
print(f"Task1 result: {result}")


'#Task2'

keyslist = list(result.keys())
vallist = list(result.values())
print(f"Task2 keys: {keyslist}")
print(f"Task2 values: {vallist}")

'#Task4'

def task4(dict):
    for i in keyslist:
        dict[dict[i]] = i
        del dict[i]


task4(result)
print(f"Task4 result: {result}")

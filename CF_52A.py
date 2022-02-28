def pangram_test(input_str):
    pangram = 'abcdefghijklmnopqrstuvwxyz'
    for i in pangram:
        if i not in word.lower():
            return False
        
    return True
    

n = int(input())
word = input()

if (pangram_test(word) == True):
    print("YES")
else:
    print("NO")
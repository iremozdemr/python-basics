print("hello")
print('hello')
#string oluştururken
#tek tırnak
#çift tırnak kullanılabilir

a = "hello"
a = 'hello'
a = """hello"""
a = """
hello
world
"""
#çok satırlı stringler için
#3 tane çift tırnak kullanılır

name = "john doe"
print(name[0])
#index 0 yazılır
print(name[0:3])
#index 0 1 2 yazılır
print("doe" in name)
#true
print("Doe" in name)
#false

string = "hello world"
print(len(string))
print(string.lower())
print(string.upper())
print(string.replace("o","a"))
print(string.replace("k","a"))
print(string.split())

string = "  hello world   "
print(string.strip())
#parametre almazsa boşluğa göre kırpma işlemi yapar

string = "*hello world*"
print(string.strip())

print("a" + "b")  #output:ab
print("a" "b")  #output:ab
print('a' + 'b')  #output:ab
print('a' 'b')  #output:ab
def example_function(*args):
    for arg in args:
        print(arg)

example_function(1, 2, 3, 'a', 'b', 'c')

#*args:
#fonksiyon değişken sayıda argüman alabilir
#gelen argümanları tuple olarak alır

def example_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

example_function(name='alice', age=25, city='new york')

#**kwargs:
#fonksiyon değişken sayıda keyword alabilir
#gelen argümanları dictionary olarak alır
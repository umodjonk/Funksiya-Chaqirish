def decor(function):
    def init(*args):
        mylis=[*args]
        summ, ints,strs,floats=0,0,0,0
        for x in mylis:
            summ+=1
            if type(x) is int:
                ints+=1
            elif type(x) is str:
                strs+=1
            elif type(x) is float:
                floats+=1
        svg=function(*args)
        print(f'Umumiy:{summ}')
        print(f'Int:{ints}')
        print(f'Str:{strs}')
        print(f'Float:{floats}')
        return svg
    return init

@decor
def Umumiy_info(*args):
    mylis=[*args]
    ints, strs, floats = [], [], []
    for i in mylis:
        if type(i) is int:
            ints.append(i)
        elif type(i)is str:
            strs.append(i)
        elif type(i)is float:
            floats.append(i)

    print(f"""
Int:{ints}
Str:{strs}
Float:{floats}""")


Umumiy_info(1,2,37.6,45,0.2,'shahzod',12,2.3,45,7.6,'Sardor')


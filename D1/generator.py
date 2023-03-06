#przykład 1
def liczby():
    for i in range(16):
        yield i*2

print(liczby())
print(list(liczby()))

for p in liczby():
    print(p)


#przykład 2
def wznowienie(n,k):
    print("wstrzymanie działania")
    yield 1001
    print("wznowienie działania")

    print("wstrzymanie działania")
    yield n+k
    print("wznowienie działania")

    print("wstrzymanie działania")
    yield n-k
    print("wznowienie działania")

    print("wstrzymanie działania")
    yield n*k
    print("wznowienie działania")

for i in wznowienie(8,5):
    if i==1001:
        continue
    print(f"wartość z yield: {i}")


#przykład 3

def kompleksowy():
    x = 0
    while True:
        print("pierwszy print x1")
        y = yield x
        print("drugi print x2")
        if y is None:
            x= x+1
        else:
            x=y


gn = kompleksowy()
print(next(gn))
print(next(gn))
print(next(gn))
print(gn.send(167))
print(next(gn))
print(next(gn))
print(next(gn))
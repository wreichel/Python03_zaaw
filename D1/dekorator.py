import time


#przykład 1
def startstop(funkcja):
    def wrapper(*args):
        print("startowanie procesu.....")
        funkcja(*args)
        print("kończenie proces.....")
    return wrapper

def zawijanie(czego):
    print(f"zawijanie {czego} w sreberka")

zw = startstop(zawijanie)

zw("czekoladek")

print("____________________________________")
zawijanie("ciastek")
print("____________________________________")

@startstop
def dmuchanie(czego):
    print(f"dmuchanie {czego} w urodziny")


dmuchanie("świeczek na torcie")

#przykład 2

def pomiarczasu(funkcja):
    def wrapper():
        starttime = time.perf_counter()
        funkcja()
        endtime = time.perf_counter()
        print(f"czas wykonania funkcji {funkcja.__name__}: {endtime-starttime} s")
    return wrapper


def sleep(funkcja):
    def wrapper():
        time.sleep(3)
        return funkcja()
    return wrapper

@pomiarczasu
def info():
    inf = []
    for u in range(1000):
        inf.append(u)

info()

@sleep
@pomiarczasu
def big_lista():
    sum([i**3 for i in range(10000000)])

big_lista()

#przykład 3
def debug(funkcja):
    def wrapper(*args,**kwargs):
        print(f"wołana funkcja: {funkcja.__name__}")
        funkcja(*args)
    return wrapper

@debug
def takafunkcja(n):
    print(f"informacja: {n}")


takafunkcja("2345356434")

#przykład 4

def repeater(n):
    def wrapper(funkcja):
        def inner(*args):
            for i in range(n):
                funkcja(*args)
        return inner
    return wrapper

@repeater(n=5)
def komunikat(k,m):
    print(f"komunikat: {k}, nr: {m}")

komunikat("fsdadgfafds",56)
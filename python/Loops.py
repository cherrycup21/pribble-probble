#TASK
#the provided code stub reads an integer,n from STDIN/ For all non-negative

#CODE
def new_func(i):
    return i ** 2

if __name__ == '__main__':
    n = int(raw_input())
    i = 0
    while i < n:
        print(new_func(i))
        i += 1

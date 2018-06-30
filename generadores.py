def generaPares(Limite):

    num=1

    while num<Limite:

        yield num*2

        num=num+1

devuelvePares=generaPares(10)


print(next(devuelvePares))
print("Aquí podría ir más codigo...")

print(next(devuelvePares))
print("Aquí podría ir más codigo...")

print(next(devuelvePares))


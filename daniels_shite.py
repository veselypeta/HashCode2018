# test

yeet = []

for index in range(1,10):
    print(index)
    yeet.append(index)

print(yeet)

class motherfucker():
    "a class to represent motherfuckers."

    def __init__(self, name):
        self.name = name

    def beAMotherfucker(self):
        print("I, " + self.name + ", am a motherfucker")

Petcho = motherfucker('Petr')
Petcho.beAMotherfucker()

class bitchAssMotherfucker(motherfucker):

    def __init__(self,name):
        self.name = name

    def transcend(self):
        print("\_(-_-)_/ ahhhhhhhh")

KanyeWest = bitchAssMotherfucker('ye')
KanyeWest.beAMotherfucker()
KanyeWest.transcend()
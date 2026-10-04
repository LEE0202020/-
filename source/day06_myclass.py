# class
class House:
    """
        아무 의미없음
    """
    houseCut = 0 # class변수
    def __init__(self):
        print("새로운 집을 만드셨네요?")
        House.houseCut += 1
        self.name = "이름"  # self.로 시작하는 변수가 인스턴스 변수

    def __init__(self, name="아직 못정함"):
        print("새로운 집을 만드셨네요?")
        House.houseCut += 1
        self.name = name  # self.로 시작하는 변수가 인스턴스 변수
print(House.__doc__)
my_house = House()
print(my_house.name, my_house.houseCut)
your_house = House("노이만성")
print(my_house.name, my_house.houseCut)
print(your_house.name, your_house.houseCut)
print(House.houseCut) # houseCut으 전 객체가 공용으로 사용하는 것
your_house.houseCut += 100 # 클래스 변수를 할 당하는  순간 인스턴스 변수가 된다
print(my_house.name, my_house.houseCut)
print(your_house.name, your_house.houseCut)
class Castle(House):
    def __init__(self,name="TBD"):
        self.anem = name
        self.room = 99
        self.furniture = []

    def addFurniture(self, str):
        self.furniture.append(str)

hisHouse = Castle("웨스트민스터 사원")
hisHouse.room = 1
hisHouse.addFurniture("의자")
hisHouse.addFurniture("파이프오르간")
print(hisHouse.furniture)

class A:
    def test(self):
        print("testA")

thing = A()
thing.test()  # 기능

class B:
    def test(self):
        print("testB")

class C(A, B):   # 앞에 있는걸 먼저 출력시킴
    # def test(self):
    #     print("testC")
    pass


thing = C()
thing.test()

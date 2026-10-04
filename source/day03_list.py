# set(집합)
set1 = {1, 2, 3, 4, 5, 3}
set2 = {3, 4, 5, 6, 7}
print(set1)
print(set2)

set3 = set1.intersection(set2)  # 교집합
set4 = set1.union(set2)  # 합집랍
set5 = set.difference(set2)   # 차집합
print(set3)
print(set4)
print(set5)

str1 = "The fox ran into a pool"
str2 = "Heaven helps those who help themelves"
seta = set(str1)
setb = set(str2)
setc = seta.intersection(setb)
print(seta)
print(setb)
print(setc)


setc.remove(' ')
print(setc)


# 공통적으로 존재하는 글자만 빨간색으로
for chr in str1:
    if chr in setc:
        print("\033[91m" + chr + "\033[0m", end="")
    else:
        print(chr, end="")
print()


for chr in str2:
    if chr in setc:
        print("\033[92m" + chr + "\033[0m", end="")
    else:
        print(chr, end="")
print()

# 빈칸있으면 자름
setd = set(str1.split(" "))
print(setd)

# dictionary
dic = {
    'name': 'one',
    'age':20,
    'subject': ['science', 'korean']
}
print(dic)
print(list(dic.keys()))
print(list(dic.values()))
print(list(dic.items()))

# addr 속성을 추가하고 "경기도"를 넣기
dic['addr'] = "경기도"
print(dic)


 # dic 에서 삭제하는 방법
dish = dic.pop('addr')
print(dish) # 데이터 꺼내오기
print(dic)
del dic['subject']
print(dic)


keywords = str.split(" ")
keywords.sort()
print(keywords.sort())
print(keywords)
print(keywords[0::2])


def printmessage1():
    print("************")
result = printmessage1()
print(result)
if result == None:
    print("없음")


def printmessage2(message):
    print(message)
printmessage2("Call ni back, please")


def printmessage3(message='초기메시지', i=10):
    for i in range(i):     # i는 갯수 (번수)
        print(message)

printmessage3()
printmessage3(message= "뭐라고", i=3)
printmessage3(i=5)
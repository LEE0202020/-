print("Welcome to Python!", end= "") # 마지막 문자룰 ""안에 있는 문자 넣기
print("*"* 40)

my_name = "I am Tom"
yourname = 'jack'
myscore = 30
print("너의 이름은 " + yourname + "이고, 점수는 " + str(myscore) + "점이네")
# f-string 을 이용한 print
print(f"너의 이름은 {yourname}이고, 점수는 {myscore}점이네")

# 입출력 함수
print("A", end="")  #디톨트는 한칸 내리기
print("B")
print(myname , yourname, myname, myscore, sep="|") # 문자 사이 사이에 적용 # 디폴트는 스페이스(바)

# 연산자
a = 30
b = 20
c = a > b
print(c)
print(f"10 > 2 and 10 < 20 : {10 > 2 and 10 < 20}")
print(3 < 4 < 5 < 6)

print("*" * 40)
print("Control Statement")
print("*" * 40)

R = "\033[31m"
G = "\033[32m"
B = "\033[34m"
END = "\033[0m"

temp = rd.randint(-18, 37)
if temp > 17:
    print(f"{R}아 너무 더운 날씨 : {temp}도 {END} ")
elif temp > 4:
    print(f"{G}딱 적당한 날씨 : {temp}도 {END}")
else:
    print(f"{B}얼어죽겠네 : {temp}도 {END}")    print(f"{B}얼어죽겠네 : {temp}도 {END}")

# loop
i = 0
while i < 10:
    print(i)
    i += 1   # i = i+ 1

while True:
    num = input("숫자만 입력부탁드립니다 : " )
    if num.isdecimal():
        break
print("귀하가 입력하신 숫자는 ", num)
# exception
try:
    a = int(input("나누어지는 수를 입력하시오 : "))
    c = 300 / a
    if a > 10000:
        raise Exception(f"{a} 크기가 큼 ")
except ValueError as e:
    print(e)
    print("ValueError 예외처리")

except ZeroDivisionError as e:
    print(e)
    print("0을 넣으면 오류나서 ZeroDivisionError 예외처리")
except Exception as e:  # Exception: 대부분의 오류를 받아주는 가장 넓은 범위의 예외 클래스
    print("B001: 실행 결과")
    # 데이터 베이스 또는 파일에 기록
else:
    peinr("예외 없이 수행 됨")
finally:
    print("무조건 끝냄")

print("프로그램이 정상 종료되었습니다")
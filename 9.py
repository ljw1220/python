number = 23
guess = int(input("숫자를 입력하세요: "))
if guess > number :
    print("틀렸습니다. 조금 더 작은 수입니다.")
    
if guess < number :
    print("틀렸습니다. 조금 더 큰 수입니다.")
    
if guess == number :
    print("맞았습니다.")
    
print("프로그램 종료")    
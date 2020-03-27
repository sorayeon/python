# Hangman(행맨) 미니 게임 재작(1)
# 기본 프로그램 제작 및 테스트
import time
# csv 처리
import csv
# 랜덤
import random
# 사운드 처리
import winsound

# 처음 인사
name = input("What is your name?")

print("Hi, " + name, "Time to play hangman game!")

print()

time.sleep(0.5)

print("Start Loading...")

print()
time.sleep(0.3)

# CSV 단어 리스트
words = []

# 문제 CSV파일 로드
with open('./resource/word_list.csv', 'r') as f:
    reader = csv.reader(f)
    # Header Skip (정답,힌트)
    next(reader)
    for c in reader:
        words.append(c)

# 리스트 섞기
random.shuffle(words)

q = random.choice(words)

# 정답 단어
word = q[0].strip() # strip공백제거

# 추측 단어
guesses = ''

# 기회
turns = 10

# 핵심 While Loop
# 찬스 카운터가 남아 있을 경우
while turns > 0:
    # 실패 횟수 (단어 매치 수)
    failed = 0
    
    # print(guesses)
    
    # 정답 단어 반복
    for char in word:
        # 정답 단어 내에 추축 문자가 포함되어 있는 경우
        if char in guesses:
            # 추축 단어 출력
            print(char, end=' ')
        else:
            # 틀린 경우 대시로 처리
            print('_', end=' ')
            failed += 1
            
    # 단어 추측이 성공 한 경우
    if failed == 0:
        print()
        print()
        # 성공 사운드
        winsound.PlaySound('./sound/good.wav', winsound.SND_FILENAME)

        print('Congratulation! The Guesses is correct.')
        # while 문 종료
        break
    print()

    print()
    
    # 힌트
    print('Hint : {}'.format(q[1].strip()))
    
    # 추측 단어 문자 단위 입력
    guess = input("guess a charter.")
    
    # 단어 더하기
    guesses += guess

    # 정답 단어에 추측한 문자가 포함되어 있지 않으면
    if guess not in word:
        # 기회 횟수 감소
        turns -= 1
        # 오류 메세지
        print("Oops! Wrong")
        # 남은 기회 출력
        print("You have", turns, "more guesses!")

        if turns == 0:
            # 실패 사운드
            winsound.PlaySound('./sound/bad.wav', winsound.SND_FILENAME)
            # 실패 메시지
            print("You hangman game failed. Bye!")
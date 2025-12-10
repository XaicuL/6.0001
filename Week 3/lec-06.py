# # # # # #####################################
# # # # # # EXAMPLE:  Towers of Hanoi
# # # # # #####################################
# # # # #
# # # # # def printMove(fr, to):
# # # # #     # '출발 기둥'과 '도착 기둥' 이름을 문자열로 변환하여 출력 (원반 이동을 기록)
# # # # #     print('move from ' + str(fr) + ' to ' + str(to))
# # # # #
# # # # #
# # # # # def Towers(n, fr, to, spare):
# # # # #     # n: 옮겨야 할 원반의 개수
# # # # #     # fr: 출발 기둥 (From)
# # # # #     # to: 도착 기둥 (To)
# # # # #     # spare: 보조 기둥
# # # # #     if n == 1: # 원반이 1개일 때: 그냥 출발지에서 도착지로 옮기면 끝!
# # # # #         printMove(fr, to)
# # # # #     else:
# # # # #         Towers(n - 1, fr, spare, to)
# # # # #
# # # # #         # Step A: n-1개의 원반을 출발(fr)에서 보조(spare) 기둥으로 옮김
# # # # #         # 이 호출은 'spare'를 임시 도착지로, 'to'를 임시 보조 기둥으로 사용함
# # # # #         # 컴퓨터는 이 시점에서 현재 함수 호출을 멈추고 메모리 스택에 저장한 후,
# # # # #         # Towers(n-1, ...)을 실행하기 위해 다시 처음부터 함수를 호출
# # # # #
# # # # #         Towers(1, fr, to, spare)
# # # # #
# # # # #         # Step B: 가장 큰 n번째 원반(1개)을 출발(fr)에서 도착(to) 기둥으로 옮김
# # # # #         # (이 단계는 n=1의 기본 조건을 실행하여 실제 이동을 출력)
# # # # #
# # # # #         Towers(n - 1, spare, to, fr)
# # # # #
# # # # #          # Step C: n-1개의 원반을 보조(spare)에서 도착(to) 기둥으로 옮김
# # # # #          # 이 호출은 'to'를 최종 도착지로, 'fr'을 임시 보조 기둥으로 사용함
# # # # #          # Step A와 마찬가지로, 다시 Towers(n-1, ...)을 실행하기 위해 재귀 호출
# # # # #
# # # # #
# # # # # print(Towers(4, 'P1', 'P2', 'P3') #최종 실행 명령: 원반 4개를 P1에서 P2로, P3를 보조 기둥으로 사용하여 옮겨라
# # # # #
# # # # # #####################################
# # # # # # EXAMPLE:  fibonacci
# # # # # #####################################
# # # # #
# # # #
# # # # # x = int(input('x = '))
# # # # #
# # # # # def fib(x):
# # # # #     """assumes x an int >= 0
# # # # #        returns Fibonacci of x"""
# # # # #     if x == 0 or x == 1:
# # # # #         return 1
# # # # #     else:
# # # # #         return fib(x - 1) + fib(x - 2)
# # # # #
# # # # # print(fib(x))
# # # #
# # # # ## x = 10000000000
# # # # #   =>  RecursionError: maximum recursion depth exceeded in comparison
# # # #
# # # #
# # # # #
# # # # #
# # # # # #####################################
# # # # # # EXAMPLE:  testing for palindromes
# # # # # #####################################
# # #
# #
# # s = input("s = ")
# #
# # def isPalindrome(s):  # isPalindrome 함수 정의: 입력 문자열 s를 받아 회문인지 검사하는 메인 함수
# #
# #     def toChars(s):  # 내부 함수 toChars 정의: 회문 검사를 위한 문자열 전처리를 담당
# #         s = s.lower()  # 1. 매개변수 s에 들어온 모든 대문자를 소문자로 변환하여 s에 재할당(Re-assignment)
# #         ans = ''  # 2. 전처리된 알파벳을 담을 빈 문자열(Empty String) 변수 ans를 초기화
# #
# #         # 3. 입력 문자열 s를 한 글자(c)씩 순서대로 순회(Iteration)함
# #         for c in s:
# #             # 4. 현재 문자 c가 'abcdefghijklmnopqrstuvwxyz' 안에 포함되어 있는지 확인 (즉, 알파벳인지 확인)
# #             if c in 'abcdefghijklmnopqrstuvwxyz':
# #                 # 5. 만약 알파벳이라면, 현재 ans 문자열에 c를 이어 붙여(Concatenation) ans에 재할당
# #                 #    (네가 언급한 'changing binding'이 이 부분임)
# #                 ans = ans + c
# #         return ans  # 6. 알파벳만 남고 소문자로 변환된 새로운 문자열 ans를 반환(return)
# #
# #         #########Notes#############
# #         # toChars 라는 함수를 정의하고,
# #         # s 라는 함수의 정의역은 s에 대해 대문자를 모두 소문자로 변형 시키고 ans은 우선 초기화 해둬
# #         # 허나 str이 들어갈거래 그리고나서 만약 c 라는 임시 변수 안에 s 가 있다면 그리고 만약 c 안에 abc 어쩌구 저게 있다면
# #         # ans 라는 str만이 가능한 변수엔 ans로 입력 받은 것과 c에 해당되는 알파벳을 더하고 그걸 ans라고 한다.
# #         ##########################
# #
# #     def isPal(s):
# #         if len(s) <= 1: #만약 s의 length가 1 이하라면
# #             return True #True를 반환한다.
# #         else: #만약 if의 여사건이라면
# #             return s[0] == s[-1] and isPal(s[1:-1]) #반환한다 s 집합의 index position 0, position -1
# #             # 그리고 isPal 이라는 함수의 정의역 s를 1:-1 (= start:stop) 로 slicing 한다
# #
# #     return isPal(toChars(s))
# #
# #
# # print(isPalindrome('eve'))
# #
# # print(isPalindrome('Able was I, ere I saw Elba'))
# #
# # print(isPalindrome('Is this a palindrome'))
# #
# #
# # #
# # # #####################################
# # # # EXAMPLE: using dictionaries
# # # #          counting frequencies of words in song lyrics
# # # #####################################
#
# def lyrics_to_frequencies(lyrics):
#     myDict = {} #myDict 라는 dic 변수에 대해 초기화를 진행
#     for word in lyrics: #range : lyrics 라고 해두고 임시 집합 word를 생성한다
#         if word in myDict: #만약 myDict라는 dic이 word라는 집합에 포함된다면
#             myDict[word] += 1
#         else:
#             myDict[word] = 1
#     return myDict
#
#
# she_loves_you = ['she', 'loves', 'you', 'yeah', 'yeah',
#                  'yeah', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
#                  'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
#
#                  'you', 'think', "you've", 'lost', 'your', 'love',
#                  'well', 'i', 'saw', 'her', 'yesterday-yi-yay',
#                  "it's", 'you', "she's", 'thinking', 'of',
#                  'and', 'she', 'told', 'me', 'what', 'to', 'say-yi-yay',
#
#                  'she', 'says', 'she', 'loves', 'you',
#                  'and', 'you', 'know', 'that', "can't", 'be', 'bad',
#                  'yes', 'she', 'loves', 'you',
#                  'and', 'you', 'know', 'you', 'should', 'be', 'glad',
#
#                  'she', 'said', 'you', 'hurt', 'her', 'so',
#                  'she', 'almost', 'lost', 'her', 'mind',
#                  'and', 'now', 'she', 'says', 'she', 'knows',
#                  "you're", 'not', 'the', 'hurting', 'kind',
#
#                  'she', 'says', 'she', 'loves', 'you',
#                  'and', 'you', 'know', 'that', "can't", 'be', 'bad',
#                  'yes', 'she', 'loves', 'you',
#                  'and', 'you', 'know', 'you', 'should', 'be', 'glad',
#
#                  'oo', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
#                  'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
#                  'with', 'a', 'love', 'like', 'that',
#                  'you', 'know', 'you', 'should', 'be', 'glad',
#
#                  'you', 'know', "it's", 'up', 'to', 'you',
#                  'i', 'think', "it's", 'only', 'fair',
#                  'pride', 'can', 'hurt', 'you', 'too',
#                  'pologize', 'to', 'her',
#
#                  'Because', 'she', 'loves', 'you',
#                  'and', 'you', 'know', 'that', "can't", 'be', 'bad',
#                  'Yes', 'she', 'loves', 'you',
#                  'and', 'you', 'know', 'you', 'should', 'be', 'glad',
#
#                  'oo', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
#                  'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
#                  'with', 'a', 'love', 'like', 'that',
#                  'you', 'know', 'you', 'should', 'be', 'glad',
#                  'with', 'a', 'love', 'like', 'that',
#                  'you', 'know', 'you', 'should', 'be', 'glad',
#                  'with', 'a', 'love', 'like', 'that',
#                  'you', 'know', 'you', 'should', 'be', 'glad',
#                  'yeah', 'yeah', 'yeah',
#                  'yeah', 'yeah', 'yeah', 'yeah'
#                  ]
#
# beatles = lyrics_to_frequencies(she_loves_you) #function call, Domain = she_loves_you
#
#
# def most_common_words(freqs):
#     values = freqs.values() #.values : Value만 얻고 싶다면 values 함수를 사용하면 된다, values 함수를 호출하면 dict_values 객체를 반환한다.
#     best = max(freqs.values())  #max min function
#     words = [] #words type is list
#     for k in freqs: #freqs 라는 range를 구성해두고, k 라는 임시 집합을 생성시킨다.
#         if freqs[k] == best:
#             words.append(k) #word 라는 list 내부에 k 라는 element를 추가한다.
#     return (words, best) #list type인 words와 max function best를 반환한다.
#
#
# def words_often(freqs, minTimes): #define function
#     result = []
#     done = False #bool
#     while not done: #done 변수가 False인 동안 반복 실행 (최소 기준을 만족하는 최빈 단어가 남아있는 동안).
#         temp = most_common_words(freqs) #현재 남아있는 freqs 딕셔너리에서 가장 많이 나온 단어 묶음(temp[0])과 그 빈도 수(temp[1])를 찾아서 temp에 저장.
#         if temp[1] >= minTimes: #가장 높은 빈도 수(temp[1])가 설정된 최소 기준(minTimes) 이상이면 다음 단계 진행 (가장 중요한 탈출 조건 제어).
#             result.append(temp) #최소 기준을 통과한 최빈 단어 묶음을 result 리스트에 추가.
#             for w in temp[0]: #현재 찾은 최빈 단어 묶음(temp[0])에 있는 모든 단어(w)를 반복적으로 순회.
#                 del (freqs[w])  # remove word from dict
#         else: #if temp[1] >= minTimes:가 거짓인 경우 (즉, 가장 높은 빈도가 최소 기준보다 작은 경우).
#             done = True #더 이상 유의미한 빈도 수의 단어가 남아있지 않다고 판단하여, 다음 반복부터는 멈추도록 done을 True로 설정.
#     return result #모든 반복이 끝난 후, 빈도 순으로 정렬된 단어 묶음(result)을 반환.
#
#
# print(words_often(beatles, 5))
# # #
# # # # # #####################################
# # # # # # EXAMPLE: comparing fibonacci using memoization
# # # # # #####################################

def fib(n): #Pure Recursion // O(2^n)
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n - 1) + fib(n - 2)


def fib_efficient(n, d): #Dynamic Programming // O(n)
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n - 1, d) + fib_efficient(n - 2, d)
        d[n] = ans
        return ans


d = {1: 1, 2: 2}

argToUse = 34
print("")
print('using fib')
print(fib(argToUse))
print("")
print('using fib_efficient')
print(fib_efficient(argToUse, d))
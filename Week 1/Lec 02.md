
**1. 문자열 (Strings & Input)**

• **문자열 (str):** 문자들의 나열(Sequence of characters).

• **특징:** 따옴표(`'` 또는 `"`)로 감싸서 표현 
~~아무거나 써도 그 어떤 일도 안 일어난다. 진짜다 나중에 말 안바꾼다.

• **연산:**
- Concatenation (+): 문자열을 이어 붙임 (`"hi" + "ana"` → `"hiana"`)
-  Repetition (*): 문자열을 반복함 (`"da" * 3` → `"dadada"`)

```
>x1 = 'Luciano'
>x2 = "Luciano"

>print('x1 type : ', type(x1))
>print('x2 type : ',type(x2))

>print('Concatenation Ex: ',"Hi" ,' ' + x1)
>print('Repetition Ex:',x1 * 3)

x1 type :  <class 'str'>
x2 type :  <class 'str'>
Concatenation Ex:  Hi  Luciano
Repetition Ex: LucianoLucianoLuciano

```



• **입력과 출력 (I/O):**
- `input("문구")`: 사용자가 입력한 모든 값을 **문자열(str)로 반환함. 

input에 대한 더 자세한 설명이 필요하다면 다음의 링크를 누르면 좋다. 
누군진 몰라도 input에 대한 글을 정말 열심히 적은 흔적이 있다. 
절대 나는 아니다. 진짜 아니다. 아닌게 아니다. 뭔 말이지 어쨋든 누군진 몰라도
정말 꼼꼼하고 잘생긴 사람 같다. 진짜 나는 아니다가 아니다.  일단 링크는 이거다.
https://dev.to/luc1a_no/1-1-python-inputeun-hangsang-munjayeolida-pmj
~~luciano..? 내 닉네임인데 누군가 뺏어간 것 같다. 나는 아니니까. 아닌게 아니니까.

```
>x = input('x = ')

>print(x)
>print(type(x))

x = 2
2
<class 'str'>
```

숫자를 원하면 `int()`나 `float()`으로 **변환(Casting)** 필수.
```
>x1 = int(input('x1 = '))

>x2 = float(input('x2 = '))

>x3 = str(input('x3 = '))

  

>def typetran():

    data = [x1, x2, x3]

	for i in range(len(data)):

        print(f'x{i+1} type : {type(data[i])}')

>typetran()

x1 = 2
x2 = 2
x3 = 2

x1 type : <class 'int'>

x2 type : <class 'float'>

x3 type : <class 'str'>
```
~~절대 귀찮아서 def를 쓴게 아니다. 곧 뒤에서 다룬다. 진짜다. 편하게 살자~~
• `print()`: 값을 콘솔에 출력. 콤마(`,`)로 여러 값을 나열하면 공백이 자동으로 추가됨.

**2. 분기 (Branching)** 
~~분기라는 단어가 어렵다면, Apple의 2026년 2분기 제품 출시를 검색해보다보면 분기라는 단어의 의미가 어렴풋 이해 된다. 공부하자. 그리고 책 읽자. 물론 이건 지나가는 철수가 쓰고 간 말이다. 
나는 독자들이 구글 딥마인드급 사람들이라는 것으로 믿고 있다. 내 믿음을 깨뜨리지 말아주길 바라며.

프로그램의 흐름을 조건에 따라 제어하는 구조 (Control Flow).

• **비교 연산자 (Comparison Operators):** 결과는 항상 **bool** (`True` / `False`)

• `==` (같다), `!=` (다르다), `>`, `<`, `>=`, `<=`

• **주의:** `=`는 대입(Assignment), `==`는 비교(Comparison)
cf, 처음에 가장 많이 하는 실수다. 괜찮다. 
그러면서 서비스도 터져보고 코드도 터져보고 
5시간동안 머리 끙끙 싸매다가 찾으면 도파민이 터진다. 즐기자. ~~경험담이다.~~
~~아 근데 독자들은 구글 딥마인드급이니 이런 실수는 없을거라고 믿는다. 난 아직도 믿고 있다.

• **논리 연산자 (Logic Operators):**

• `not a`: a가 참이면 거짓
-> Ex) 전현준은 여자다. (여자인게 참이라면 이 명제는 거짓이 된다. 전현준은 남자화장실 vip다.)

• `a and b`: 둘 다 참이어야 참
-> 수학적으로 가보자. **and** 는 교집합이다.

• `a or b`: 둘 중 하나만 참이어도 참
-> 수학적으로 가보자. **or** 는 합집합이다.

??: 수학이 너무 어려워요 !
~~국어국문학과를 추천한다.~~

• **조건문 구조 (if-elif-else):**
![[Pasted image 20260222214453.png]]


```
if condition:
    # 조건이 True일 때 실행
elif condition:
    # 위 조건이 False이고, 이 조건이 True일 때 실행
else:
    # 모든 조건이 False일 때 실행
```
```
x = int(input('x = '))
n = int(input('n = '))

  

if x > n:
	print('x = n')

elif x == n:
	print('x != n')
else:
	print('x LOSE')
print('------------= x,n = ------------') 
print('x = ', x)
print('n = ', n)
```


**중요 (Indentation):** 파이썬에서 **들여쓰기**는 문법의 **일부**이다.
블록(Block)의 시작과 끝을 들여쓰기로 구분해야한다. 

How To USE: 띄어쓰기 * 4 OR **tab**

??: 저는 띄어쓰기로 할래여 ㅎㅎㅎ
=> 조심해야 할 사람이다. 언제 터질지 모른다. 이상 성욕이라고 하면 내가 논란이 터지니 말은 아끼지만
언젠가 띄어쓰기 3번 하고 에러 터져서 맥북 바꿀 일 생긴다고 확신하지 아니한다.

**3. 반복 (Iteration)** 

변수의 값이 변함(Changing Bindings)에 따라 코드를 반복 실행하는 구조.

**While 루프 (Unbounded Loop)**

• **특징:** 조건이 `True`인 동안 계속 실행. 반복 횟수를 미리 알 수 없을 때 주로 사용.

• **위험성:** 종료 조건이 충족되지 않으면 **무한 루프(Infinite Loop)** 에 빠짐 (젤다의 전설 '미로 숲' 예시).

```
n = 0
while n < 5:
    print(n)
    n = n + 1  # 이 부분이 없으면 무한 루프 발생!
```

종종 언제 끝나는지 묻는 사람이 있는데, 3000년이 와도 컴퓨터만 살아있다면 그때도 출력중일거다.
??: 아니면요? 내기할래요? 만빵?
-> ㅇㅋ ㄱㄱ 3000년 즈음 DM 하길 바란다. 오래 살자.

**for 루프 (Bounded Loop)**

• **특징:** 정해진 시퀀스(Sequence)의 길이만큼 반복 실행.

• **range 함수:** `range(start, stop, step)`

 -  `start`부터 `stop - 1`까지 `step` 간격으로 숫자 생성.
 - 예: `range(0, 5)` → `0, 1, 2, 3, 4`

```
mysum = 0
for i in range(5, 11, 2): # 5, 7, 9
    mysum += i
```

**break 문**

• **기능:** 루프를 즉시 종료하고 빠져나감.

• **범위:** 자신을 감싸고 있는 **가장 안쪽 루프(innermost loop)** 하나만 탈출

깨알tip.

python이 너무 어렵고 초보라 막막하고 그래서 앞이 어둡고 일어나기 귀찮고
프로그래밍 할 빠엔 릴스 숏츠 틱톡을 보고 싶다면 그대들에게 선물을 주고 싶다.

https://pythontutor.com/visualize.html#mode=edit

시각화 사이트다.
개인적으로 python docs보다 더 이용하는 편이다.
애용하길 바란다.
정말 사소한 문법일지라도 시각화를 해준다. 진짜 짱이다.
유료 아니다. 광고 아니다. 

~~잠만 근데 내 독자들은 딥마인드 연구원인데 프로그래밍이 즐거울텐데..?

-> 지나가는 까마귀에게 python을 알려줄때 이용하길 바란다.
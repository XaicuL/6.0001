
**1. 문자열 (Strings & Input)**

• **문자열 (str):** 문자들의 나열(Sequence of characters).

• **특징:** 따옴표(`'` 또는 `"`)로 감싸서 표현

• **연산:**

    ◦ Concatenation (+): 문자열을 이어 붙임 (`"hi" + "ana"` → `"hiana"`)

    ◦ Repetition (*): 문자열을 반복함 (`"da" * 3` → `"dadada"`)

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

• `input("문구")`: 사용자가 입력한 모든 값을 **문자열(str)로 반환함. 
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

프로그램의 흐름을 조건에 따라 제어하는 구조 (Control Flow).

• **비교 연산자 (Comparison Operators):** 결과는 항상 **bool** (`True` / `False`)

• `==` (같다), `!=` (다르다), `>`, `<`, `>=`, `<=`

• **주의:** `=`는 대입(Assignment), `==`는 비교(Comparison)

• **논리 연산자 (Logic Operators):**

• `not a`: a가 참이면 거짓

• `a and b`: 둘 다 참이어야 참

• `a or b`: 둘 중 하나만 참이어도 참

• **조건문 구조 (if-elif-else):**

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


**중요 (Indentation):** 파이썬에서 **들여쓰기**는 문법의 일부이다.
블록(Block)의 시작과 끝을 들여쓰기로 구분해야한다.

**3. 반복 (Iteration)**

변수의 값이 변함(Changing Bindings)에 따라 코드를 반복 실행하는 구조.

**While 루프 (Unbounded Loop)**

• **특징:** 조건이 `True`인 동안 계속 실행. 반복 횟수를 미리 알 수 없을 때 주로 사용.

• **위험성:** 종료 조건이 충족되지 않으면 **무한 루프(Infinite Loop)**에 빠짐 (젤다의 전설 '미로 숲' 예시).

```
n = 0
while n < 5:
    print(n)
    n = n + 1  # 이 부분이 없으면 무한 루프 발생!
```

**for 루프 (Bounded Loop)**

• **특징:** 정해진 시퀀스(Sequence)의 길이만큼 반복 실행.

• **range 함수:** `range(start, stop, step)`

    ◦ `start`부터 `stop - 1`까지 `step` 간격으로 숫자 생성.

    ◦ 예: `range(0, 5)` → `0, 1, 2, 3, 4`

```
mysum = 0
for i in range(5, 11, 2): # 5, 7, 9
    mysum += i
```

**break 문**

• **기능:** 루프를 즉시 종료하고 빠져나감.

• **범위:** 자신을 감싸고 있는 **가장 안쪽 루프(innermost loop)** 하나만 탈출

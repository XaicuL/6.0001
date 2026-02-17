# **1. 컴퓨팅 사고 (Computational Thinking)** 란 무엇인가 ? 

## 지식의 두 유형
- 선언적 지식(**Declarative**): "무엇인가(Fact)" (Ex: y = x) 

- 명령적 지식(**Imperative**): "어떻게 하는가" (Ex: y좌표를 구하는 단계별 방법 ~= 알고리즘)

• 컴퓨터의 본질 : 계산을 수행하는 기계

## 2. 프로그래밍 언어의 3요소

• **Syntax (문법)** : 문장의 형식이 맞는가 ?
	(만약 틀리다면 : Syntax Error)
	Ex) 
	5 + : (X)
	5 + 5 : (O)

• **Static Semantics (정적 의미):** 문법은 맞지만 말이 되는가?
	Ex) 
	"HelloWorld" / 5 : 의미 없음 -> Type Error

```
>print('Helloworld'/5)
TypeError: unsupported operand type(s) for /: 'str' and 'int'
```


• **Semantics (의미):** 의도한 대로 작동하는가?
> 주의해야 할 점은 정상적으로 실행이 되더라도, 답이 틀릴 수 있다.

# 3. 파이썬의 기본 재료(Objects & Types)

• **Scalar Objects (더 쪼갤 수 없는 것):**
	- int : 정수 (3)
	- float : 실수 (3.0)
	-  bool : 참/거짓 = 1/0
	- NoneType : 값 없음

• **Type Conversion (형 변환):** 
- float(3) -> 3.0
- int(3.9) -> 3
```
>x1 = 3
>x2 = 3.0
>x3 = **False**

>x1a = float(x1) 
>x2a = int(x2)

>print('x1 type : ',type(x1))
>print('x2 type : ',type(x2))
>print('x3 type : ',type(x3))

>print('---------------Type Conversion-----------------')

>print('x1a : int to float')
>print('x1a type : ',type(x1a))

>print('x2a : float to int')
>print('x2a type : ',type(x2a))

---------------------------------------------------------------------------------------------------------------
x1 type :  <class 'int'>
x2 type :  <class 'float'>
x3 type :  <class 'bool'>

---------------Type Conversion-----------------

x1a : int to float
x1a type :  <class 'float'>
x2a : float to int
x2a type :  <class 'int'>
```

# 4. **변수 값 변경 (Changing Bindings)**

• **개념:** 이미 값이 있는 변수에 등호(`=`)를 다시 사용하면, 변수라는 이름표를 **새로운 객체로 옮겨 붙이는 것**
• **특징:** 이전 값은 메모리에 남아있을 수 있지만, 이름표가 떨어졌으므로 더 이상 접근할 수 없다.

**수학 vs 프로그래밍 (중요!)** 프로그래밍에서 `x = x + 1`은 성립하지만, 
수학에서는 불가능한 식이라는 점을 명심해야한다.

- **수학:** 방정식의 해를 구하는 것 (Solve for x).
 - **코딩:** 오른쪽의 값을 계산해서 왼쪽 변수에 **대입(Assign)**하는 것.

**⚠️ 자동 업데이트 안 됨 (No Automatic Update)**

변수의 값이 바뀌어도, 이전에 그 변수를 사용해 계산해둔 결과값은 **변하지 않는다**

```
radius = 2.2
area = 3.14 * (radius ** 2) 
# 현재 area는 약 15.2

radius = radius + 1  # radius가 3.2로 바뀜 (Changing Binding)
```
질문: **area 값은 바뀌었을까?**
정답: 아니오! area는 여전히 15.2 라고 답해야한다. 
업데이트하려면 area 계산 코드를 다시 실행해야만 한다.

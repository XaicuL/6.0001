# **functions & Scope**

**1. 구조화의 기술 (Structuring)**

코드가 길어질수록 복잡해지는 것을 막기 위한 두 가지 전략

??: 코드가 길어져야 간지나지!!
~~하......~~
-> 사무라이가 칼을 두 번 휘두르는걸 본 적 있나? ~~일단 나는 없다.~~

• **분해 (Decomposition):** 큰 문제를 작고 독립적인 부분(Modules)으로 쪼개는 것. 
(코드 정리라고 불러도 좋다. ~~클린코드 짱!!~~)

• **추상화 (Abstraction):** 내부의 복잡한 디테일은 숨기고, **"무엇을 하는지(What it does)"** 만 
알면 쓸 수 있게 만드는 것. (블랙박스화)
![[Pasted image 20260222220938.png]]

**2. 함수 (Functions)**

분해와 추상화를 구현하는 파이썬의 도구라고 보면 된다.

• **정의 (Definition):** `def` 키워드 사용. 코드를 실행하지 않고 저장만 해둠.

• **호출 (Call/Invocation):** 함수 이름 뒤에 `()`를 붙여서 실제로 실행함. (function call 이라 부른다)

• **Docstring:** 함수 바로 아래 `""" """`로 적는 **설명서**. `help(함수명)`으로 확인 가능 

```
  
def f(x):
'''y = f(x) 이고, f(x) = x+1 이라고 가정하자''' #해당 부분을 docs 라고 부른다. 설명서라고 보아도 좋다
	return x + 1
y = f(5) #정의역 x = 5 라고 하자(수학적으로는 대입) #이 부분이 function call 이다.

print(y)  

```

**3. 핵심: Return vs print 

가장 많이 헷갈리는 부분

• **return**:
- - 함수의 **결과값**을 호출한 곳(Caller)으로 돌려준다.
- - `return`을 만나면 함수는 **즉시 종료**.
- - 이 값을 변수에 저장하거나 다른 계산에 쓸 수 있다.

• **print**:

   - 값을 단순히 콘솔(화면)에 **보여주기만** 하고 끝

   - 함수 밖으로 값을 전달하지 않는다 (변수에 저장하면 `None`이 저장됨).

**4. 변수의 범위 (Variable Scope)**

• **Global Scope (전역):** 메인 프로그램에서 정의된 변수. 어디서든 읽을 수 있음.

• **Local Scope (지역):** 함수 **안에서** 정의된 변수. 함수가 끝나면 **사라짐**.

```
set = [2,4,6,8]

def Name(x):

	x = set.append(10) #Local

	return x

x = set.copy() #Global

```

• **주의:** 함수 안에서 Global 변수와 같은 이름의 변수를 만들면, 
	함수 안에서는 Local 변수가 우선임(영어로는 이렇게 말한다 Name Shadowing) 

cf.
python을 RUN 시키면 python은 보통 top - down 방식으로 위에서 아래로 순서대로 내려온다.
근데 이때 def된 function이 있다면 function 안에 에러가 있을지라도 넘어간다.
다만 아래에 print or function call을 했다면 다시 위로 올라가 해당 function을 검사하고
Error OR ~Error을 시사한다.
아래의 코드는 필자의 다른 저장소에서 가져온 코드인데, 왜 def를 써야**만** 하는지를 적나라하게 보여준다.
그냥 가볍게 보자.

```
import sympy as sp
sp.init_printing()

x = sp.symbols('x')

ex1 = x**2 - 1
ex2 = x**2 + x
ex3 = x+3

cal_expanded = sp.expand(ex1 * ex2 * ex3)
display(cal_expanded)
######################################################
print('-----------------------성질----------------------------')

print('###교환법칙###')

cal_A = ex1 * ex2
cal_A_ep = sp.expand(cal_A)

display(cal_A)
display(cal_A_ep)

cal_B = ex2 * ex1
cal_B_ep = sp.expand(cal_B)

display(cal_B)
display(cal_B_ep)

print('-----------------검증-----------------')

if cal_A_ep == cal_B_ep:
    print('교환법칙 성립')
else:
    print('교환법칙 성립X')

######################################################

print('###결합법칙###')

cal_C = (ex1 * ex2) * ex3
cal_C_ep = sp.expand(cal_C)

display(cal_C)
display(cal_C_ep)

cal_D = ex1* (ex2 * ex3)
cal_D_ep = sp.expand(cal_D)

display(cal_D)
display(cal_D_ep)

print('-----------------검증2-----------------')

if cal_C_ep == cal_D_ep:
    print('결합법칙 성립')
else:
    print('결합법칙 성립X')

######################################################

print('###분배법칙(1)###')

cal_E = ex1 * (ex2 + ex3)
cal_E_ep = sp.expand(cal_E)

display(cal_E)
display(cal_E_ep)

cal_F = (ex1 * ex2) + (ex1 * ex3)
cal_F_ep = sp.expand(cal_F)

display(cal_F)
display(cal_F_ep)

print('-----------------검증3-----------------')

if cal_E_ep == cal_F_ep:
    print('분배법칙 성립(1)')
else:
    print('분배법칙 성립X (1)')

######################################################

print('###분배법칙(2)###')

cal_G = (ex1 + ex2) * ex3
cal_G_ep = sp.expand(cal_G)

display(cal_G)
display(cal_G_ep)

cal_H = (ex1 * ex3) + (ex2 * ex3)
cal_H_ep = sp.expand(cal_H)

display(cal_H)
display(cal_H_ep)

print('-----------------검증3-----------------')

if cal_G_ep == cal_H_ep:
    print('분배법칙 성립(2)')
else:
    print('분배법칙 성립X (2)')

# cf
# 하나하나 다 치다가 진짜 미칠 뻔 했다. 수학자 분들에게 존경을 표한다
#그런데, 여기서 하나 보여주고픈게 있다. 우리는 def와 친해져야 할 이유가 있다. 다음의 코드를 보자

def verify_all_polynomial_laws(A, B, C):

    sp.init_printing()

    # 1. 교환법칙
    is_commutable = sp.expand(A * B) == sp.expand(B * A)

    # 2. 결합법칙
    is_associative = sp.expand((A * B) * C) == sp.expand(A * (B * C))

    # 3. 분배법칙
    dist_left = sp.expand(A * (B + C)) == sp.expand(A * B + A * C)
    dist_right = sp.expand((A + B) * C) == sp.expand(A * C + B * C)

    # --- 결과 출력 섹션 ---
    print("\n" + "="*30)
    print('-----------------검증-----------------')
    print(f"1. 교환법칙: {'✅ 통과' if is_commutable else '❌ 실패'}")
    print(f"2. 결합법칙: {'✅ 통과' if is_associative else '❌ 실패'}")
    print(f"3. 분배법칙(좌): {'✅ 통과' if dist_left else '❌ 실패'}")
    print(f"4. 분배법칙(우): {'✅ 통과' if dist_right else '❌ 실패'}")
    print("="*30)

    if all([is_commutable, is_associative, dist_left, dist_right]):
        print('최종 결과 A*B*C')
        display(sp.expand(A * B * C))
    else:
        print("\n오류 발생")

verify_all_polynomial_laws(ex1, ex2, ex3)
#hahahahahahahahahahahahahahahahahahaaaaaaaaaaaaa 내 10분은 무너졌어.

```



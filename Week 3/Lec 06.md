
# **Recursion & Dictionaries**

**1. 재귀 (Recursion)**

• **정의:**

   **알고리즘적:** 문제를 더 작고 단순한 **동일한 문제(Self-similar)**로 쪼개서 해결하는 방법 
   (분할 정복, Divide and Conquer) 

    ◦ **의미적:** 함수가 자기 자신을 호출하는 것 [Source 139].

• **필수 구성 요소 (매우 중요!):**

   1. **Base Case (기본 단계):** 재귀 호출을 멈추는 종료 조건. 문제의 가장 단순한 형태 (예: 1!=1) 

   2. **Recursive Step (재귀 단계):** 문제를 더 작게 만들어서 자기 자신을 호출하는 부분 (예: n!=n×(n−1)!) 

   ◦ _주의: Base case가 없으면_ **무한 재귀(Infinite Recursion)** _에러 발생._

**2. 재귀의 예시 (Examples)**

• **팩토리얼 (Factorial):** n!=n×(n−1)!

• **피보나치 (Fibonacci):** fib(n)=fib(n−1)+fib(n−2)

    ◦ 특징: Base case가 두 개임 (fib(0)=1,fib(1)=1).

```
def fibonacci_iter(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    fib_list = [0, 1]
    
    while len(fib_list) < n:
        next_fib = fib_list[-1] + fib_list[-2]
        fib_list.append(next_fib)
    return fib_list
    
print(fibonacci_iter(10))
```

• **하노이의 탑 (Towers of Hanoi):** 복잡해 보이지만 재귀적으로 생각하면 "n-1개를 옮기고, 제일 큰 거 옮기고, 다시 n-1개 옮긴다"는 단순한 논리로 풀림 

**3. 딕셔너리 (Dictionaries)**

• **특징:** 순서가 없는 **Key-Value** 쌍의 집합 (`dict`). 리스트보다 검색 속도가 매우 빠름 

• **구조:** `{ Key : Value }`

    ◦ **Keys:** 반드시 **유일(Unique)**해야 하며, **불변(Immutable)** 타입만 가능 (int, string, tuple 등) [Source 157].

    ◦ **Values:** 어떤 타입이든 가능 (Mutable, 중복 가능) [Source 156].

• **주요 연산:**

    ◦ `d[k]`: Key `k`에 해당하는 Value 반환.

    ◦ `d[k] = v`: Key `k`에 Value `v` 할당 (추가하거나 수정).

    ◦ `del(d[k])`: 해당 Key-Value 쌍 삭제 [Source 155].

**4. ★ 핵심: 메모이제이션 (Memoization)**

• **문제:** 피보나치 수열을 단순 재귀로 짜면, 똑같은 계산을 수백만 번 반복해서 매우 느림 (비효율적) 

• **해결:** **딕셔너리**를 사용해 **"이미 계산한 값은 저장해두고(Memo), 나중에 다시 계산하지 않고 꺼내 쓰는"** 기술 

• **효과:** 실행 시간을 획기적으로 줄여줌 (Efficiency Gains)
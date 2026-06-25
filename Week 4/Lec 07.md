
# **Testing, Debugging, Exceptions, Assertions**

**1. 방어적 프로그래밍 (Defensive Programming)**

• **개념:** 버그가 발생하는 것을 미연에 방지하는 코딩 습관 

지나가는 누군가 내게 말했다.
넌 오류가 병이라 생각하느냐 오류는 병이 아니다. 오류는 병이 아닌 것이 아니다.
오류는 병이 아닌 것이 아닌 것이 아니다 

즉 Error은 우리의 정신 건강에도 좋지 않다. 
건강을 지키기 위해선 Error을 미연에 방지하는 것이 필요하다

• **핵심 방법:**

   ◦ 함수에 명세서(Specifications/Docstring) 정확히 작성하기

   ◦ 프로그램을 작게 쪼개서 모듈화(Modularize)하기 

   ◦ 입출력 조건 검사하기 (Assertions 활용) 

**2. 테스팅과 디버깅 (Testing vs Debugging)**

강의에서는 이 둘의 차이를 '수프에 빠진 벌레'에 비유한다

• **테스팅 (Testing):** 만들어진 수프에 벌레(Bug)가 있는지 확인하는 과정 (문제를 발견하는 것)

• **디버깅 (Debugging):** 벌레가 어디서 떨어졌는지 원인을 찾고 주방을 청소해 해결하는 과정 
(문제를 고치는 것) 

**3. 예외 처리 (Exceptions)**

• **개념:** 코드를 실행하다가 에러(IndexError, TypeError 등)가 발생했을 때, 프로그램이 강제로 종료되지 않고 **안전하게(우아하게) 대처하도록 만드는 문법**이다.

!!! 주의 !!!
예외 처리를 가득가득하게 만들면 좋지 않나? 라는 함정에 빠질 수 있다.
그 발상이 나쁜 것은 아니지만, 언제나 쉬운 선택엔 부작용이 따른다.
만약 예외처리를 가득가득하게 넣는다면, 장점은 Run 이후 우리의 정신 건강은 지킬 수 있다.
다만 단점으로는 정말 치명적인 Error 또한 예외 처리 덕분에 예외로 처리가 된다면 
언젠가 터질지 모르는 시한 폭탄이 된다.

• _예: 사용자가 숫자를 입력해야 하는데 문자를 입력했을 때 에러를 띄우지 않고 다시 입력하라고 요청하는 기능._

```
def calculate_ratio(numerator, denominator):

    try:
        # 1. 타입 검사 (문자열 등이 들어오는 것 방지)
        if not isinstance(numerator, (int, float)) or not isinstance(denominator, (int, float)):
            raise TypeError("수식에는 숫자만 입력 가능합니다.")
        # 2. 계산 수행
        result = numerator / denominator
    except ZeroDivisionError:
        # 분모가 0인 것은 수학적으로 정의되지 않음 -> 명확한 에러 전파 혹은 특정 값(None/inf) 약속
        print("Log: 분모가 0입니다. 계산을 중단합니다.")
        return None 
    except TypeError as e:
        print(f"Log: 입력 데이터 오류 - {e}")
        raise  # 이 에러는 호출한 쪽에서 알아야 하므로 다시 던짐
    else:
        return result

print(calculate_ratio(30, 25))
```

**4. 단언문 (Assertions)**

• **개념:** 코드의 특정 지점에서 조건이 반드시 참(`True`)이어야 한다고 강제하는 기능 

• **특징:** 만약 조건이 `False`라면 그 즉시 `AssertionError`를 발생시키며 프로그램을 멈춥니다. 버그가 더 크게 번지기 전에 초기에 잡아내는 아주 훌륭한 방어막 역할을 합니다
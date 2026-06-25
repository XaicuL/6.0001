
# **Testing, Debugging, Exceptions, Assertions**

## **# 1. 테스트와 디버깅: 신뢰의 필연성**

프로그램의 품질을 높이는 과정은 마치 국을 끓일 때 천장에서 벌레(Bug)가 떨어지는 상황에 대처하는 것과 같다.

### **(1) 방어적 프로그래밍 (Defensive Programming)**

- **[Necessity]**: 애초에 벌레가 국에 들어가지 않도록 **뚜껑을 닫는(Keep lid closed)** 행위다.
    
- **방법**:
    
    - 함수의 **사양(Specifications)**을 명확히 작성한다.
        
    - 프로그램을 **모듈화**하여 각 단위를 독립적으로 검증한다.
        
    - **어설션(Assertions)**을 통해 입력/출력 조건을 엄격히 체크한다.
        

### **(2) 테스트의 종류 (Classes of Tests)**

- **Unit Testing**: 각 함수나 모듈을 개별적으로 검증하는 단계다.
    
- **Regression Testing**: 버그를 수정할 때마다 새로운 테스트 케이스를 추가하여, 과거에 고친 에러가 재발하지 않는지 확인한다.
    
- **Integration Testing**: 개별 모듈이 합쳐졌을 때 전체 프로그램이 의도대로 작동하는지 최종 확인한다.
    

---

## **# 2. BLACK BOX vs GLASS BOX TESTING**

### **(1) Black Box Testing (명세 기반)**

- **[Analysis]**: 내부 코드를 보지 않고 오직 **함수의 사양(Specification)**만을 보고 테스트를 설계한다.

    
- **[Necessity]**: 구현 방식이 바뀌어도 테스트 케이스를 재사용할 수 있으며, 개발자의 편향을 배제할 수 있다.
    
- **핵심**: 경계 조건(0, 빈 리스트, 극한의 큰 수/작은 수)을 반드시 포함해야 한다.

    

### **(2) Glass Box Testing (구현 기반)**

- **[Analysis]**: 코드의 모든 경로(Path)를 직접 확인하며 테스트 케이스를 만든다.

    
- **목표**: 모든 조건문(if), 반복문(for/while)이 적어도 한 번은 실행되도록 설계하는 **'Path-complete'**를 지향한다.
    

---

## **# 3. EXCEPTIONS: 예외 처리의 메커니즘**

예기치 못한 입력이나 조건이 발생했을 때 프로그램이 폭발하지 않도록 제어권을 핸들링하는 기법이다.

### **(1) `try-except` 구조**

- **[Analysis]**: `try` 블록에서 에러가 발생하면 즉시 중단하고 `except` 블록으로 넘어가 에러를 처리한다.
    
- **Specific Handling**: `ValueError`, `ZeroDivisionError` 등 특정 에러 타입별로 다른 처리 로직을 제공하는 것이 엄밀한 방식이다.
    

### **(2) [Necessity] `else`와 `finally`**

- **`else`**: `try` 블록이 에러 없이 완벽하게 실행되었을 때만 추가로 수행된다.
    
- **`finally`**: 에러 발생 여부와 상관없이 **무조건** 실행된다. 파일 닫기(`close`) 등 반드시 수행되어야 할 정리 작업에 필연적으로 사용된다.
    

---

## **# 4. ASSERTIONS: 단호한 선언**

프로그래머의 가정을 강제하는 도구로, 조건이 충족되지 않으면 즉시 실행을 중단시킨다.

Python

```
def avg(grades):
    # [Necessity]: 빈 리스트가 들어오면 무의미한 연산을 방지하고 즉시 에러 발생
    assert len(grades) != 0, 'no grades data' # [cite: 2432]
    return sum(grades)/len(grades)
```

### **[Analysis]: 왜 어설션을 쓰는가?**

- 버그가 발생한 지점을 즉시 포착하여 에러가 프로그램 전체로 전파되는 것을 차단하기 위함이다.
    
- 주로 함수의 입력값(Arguments)의 타입이나 제약 조건을 체크하는 **방어적 프로그래밍**의 핵심 무기다.
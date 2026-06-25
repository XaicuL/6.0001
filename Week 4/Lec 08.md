
# **Object Oriented Programming (OOP)**

## **# 1. 객체(Objects): 데이터 추상화의 실체**

파이썬의 모든 데이터(int, list, dict 등)는 객체이며, 각 객체는 다음 세 가지 요소를 가진다:

1. **Type**: 객체의 종류 (예: `int`, `string`).
    
2. **Internal Representation**: 데이터가 내부적으로 어떻게 저장되는지 (Primitive or Composite).
    
3. **Procedures (Methods)**: 해당 객체와 상호작용하기 위한 도구 세트.
    

### **[Necessity] 왜 OOP인가?**

- **기존 방식의 모순**: 데이터와 그 데이터를 처리하는 함수가 분리되어 있으면, 코드가 복잡해질수록 어떤 함수가 어떤 데이터를 다루는지 추적하기 어려워진다.
    
- **해결책**: 관련 있는 데이터와 절차를 하나의 **'패키지'**로 묶어 관리한다. 이를 통해 복잡성을 줄이고 코드 재사용성을 극대화한다.

## **# 2. 클래스(Classes): 새로운 타입의 설계도**

클래스는 객체를 만들기 위한 **청사진(Blueprint)** 이며, 
객체는 그 클래스의 실제 **인스턴스(Instance)** 다.

### **(1) 클래스 정의와 상속**


예1)
```
class Coordinate(object): # [1]
    # 여기에 속성과 메서드를 정의
```

- **[1] [Analysis]**: `object`를 상속받는다는 것은 `Coordinate`가 파이썬의 기본 객체 속성을 모두 물려받는다는 뜻이다.
    

### **(2) 특수 메서드: `__init__` (생성자)**

- **[Necessity]**: 객체가 생성되는 순간, 데이터를 초기화하기 위한 장치가 필연적으로 필요하다.
    
예2)
```
def __init__(self, x, y): # [2]
    self.x = x # [3]
    self.y = y
```

- **[2] `self`**: 생성된 인스턴스 자기 자신을 가리키는 파라미터다. 파이썬은 호출 시 자동으로 이를 넘겨주므로 우리가 직접 인자를 줄 필요는 없다.
    
- **[3] Data Attributes**: 인스턴스마다 고유하게 가지는 변수(Instance variables)다.
    

---

## **# 3. 메서드(Methods): 객체의 행동**

메서드는 특정 클래스의 객체에서만 작동하도록 설계된 함수다.

Python

```
def distance(self, other): # [4]
    x_diff_sq = (self.x - other.x)**2
    y_diff_sq = (self.y - other.y)**2
    return (x_diff_sq + y_diff_sq)**0.5
```

- **[4] [Analysis]**: 메서드는 항상 `self`를 첫 번째 인자로 받으며, 도트(`.`) 연산자를 통해 호출한다. `c.distance(origin)`은 내부적으로 `Coordinate.distance(c, origin)`과 동일하게 작동한다.
    

---

## **# 4. 특수 연산자 오버라이딩 (Overriding)**

파이썬의 기본 동작(`print`, `+`, `==` 등)을 우리 클래스에 맞게 재정의할 수 있다.

### **[Necessity] `__str__`의 필연성**

- **모순**: 클래스를 그냥 출력하면 `<main.Coordinate object at 0x...>` 같은 불친절한 정보만 나온다.
    
- **해결책**: `__str__` 메서드를 정의하여 사용자가 원하는 형태의 문자열을 반환하게 만든다.
    

| **특수 메서드** | **대응 연산자** | **[Necessity]** |
| ---------- | ---------- | --------------- |
| `__add__`  | `+`        | 객체 간의 덧셈 정의     |
| `__eq__`   | `==`       | 객체 간의 동등성 비교    |
| `__len__`  | `len()`    | 객체의 길이 반환       |

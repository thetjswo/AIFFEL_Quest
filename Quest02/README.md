# AIFFEL Campus Online 7th Code Peer Review Templete

- 코더 : 이선재
- 리뷰어 : 조수민



🔑 **PRT(Peer Review Template)**

- [O]  **1. 주어진 문제를 해결하는 완성된 코드가 제출되었나요?**
    - 문제에서 요구하는 최종 결과물이 첨부되었는지 확인
    - 문제를 해결하는 완성된 코드란 프로젝트 루브릭 3개 중 2개, 
    퀘스트 문제 요구조건 등을 지칭
        - 해당 조건을 만족하는 부분의 코드 및 결과물을 근거로 첨부
    
    *조수민: 조건을 충족시키는 코드를 아래에 첨부*
  #헤엄치는 시간 지정을 위한 라이브러리 import
from time import sleep


# 물고기 객체 움직임 시작 함수
def start_movement(fish_list):
  print("Using Comprehension: ")
  #컴프리헨션 함수 호출
  show_fish_movement_comprehension(fish_list)
  print("Using Generator: ")
  #제너레이터 함수 호출
  gen = show_fish_movement_generator(fish_list)
  for i in range(len(fish_list)):
    # 순차적으로 반환된 값으로 요구하는 결과물 출력
    print(next(gen), "is swimming at", next(gen), "m/s")

# 컴프리헨션 함수 정의
def show_fish_movement_comprehension(fish_list):
  #리스트에 있는 딕셔너리 추출
  for i in range(len(fish_list)):
    # 딕셔너리에 있는 요소들 추출 후, 요구하는 결과물 출력
    list = [x for x in fish_list[i].values()]
    print(list[0], "is swimming at", list[1], "m/s")

# 제너레이터 함수 정의
def show_fish_movement_generator(fish_list):
  #리스트에 있는 딕셔너리 추출
  for i in range(len(fish_list)):
    # 딕셔너리에 있는 요소 추출
    list = [x for x in fish_list[i].values()]
    # key와 value 값 yield로 반환
    yield list[0]
    yield list[1]


fish_list = [{"이름":"Nemo", "speed":3}, {"이름":"Dory", "speed":5}]

# 물고기 객체 움직임 출력
for i in range(3):
  start_movement(fish_list)
  # 2초 간격으로 물고기 움직임
  sleep(2)
    
    
- [O]  **2. 전체 코드에서 가장 핵심적이거나 가장 복잡하고 이해하기 어려운 부분에 작성된 
주석 또는 doc string을 보고 해당 코드가 잘 이해되었나요?**
    - 해당 코드 블럭에 doc string/annotation이 달려 있는지 확인
    - 해당 코드가 무슨 기능을 하는지, 왜 그렇게 짜여진건지, 작동 메커니즘이 뭔지 기술.
    - 주석을 보고 코드 이해가 잘 되었는지 확인
        - 잘 작성되었다고 생각되는 부분을 근거로 첨부합니다.

*조수민: 위에 첨부한 코드대로, 이해되기 쉽도록 주석을 구석구석 작성하였다.*
        
- [O]  **3. 에러가 난 부분을 디버깅하여 문제를 “해결한 기록을 남겼거나” 
”새로운 시도 또는 추가 실험을 수행”해봤나요?**
    - 문제 원인 및 해결 과정을 잘 기록하였는지 확인 또는
    - 문제에서 요구하는 조건에 더해 추가적으로 수행한 나만의 시도, 
    실험이 기록되어 있는지 확인
        - 잘 작성되었다고 생각되는 부분을 근거로 첨부합니다.

    *조수민: 문제 해결을 위해 시도한 부분이 코랩에 모두 기록되어있었다. 회고 섹션에서 서술해놓았다.* 
        
- [O]  **4. 회고를 잘 작성했나요?**
    - 주어진 문제를 해결하는 완성된 코드 내지 프로젝트 결과물에 대해
    배운점과 아쉬운점, 느낀점 등이 상세히 기록되어 있는지 확인
        - 딥러닝 모델의 경우,
        인풋이 들어가 최종적으로 아웃풋이 나오기까지의 전체 흐름을 도식화하여 
        모델 아키텍쳐에 대한 이해를 돕고 있는지 확인

   *조수민: 회고 내용에 시도했던 함수 또는 명령어가 적혀있었고, 그 동안 배운 개념들을 최대한 사용하려한 흔적이 보였다.*

- [X]  **5. 코드가 간결하고 효율적인가요?**
    - 파이썬 스타일 가이드 (PEP8) 를 준수하였는지 확인
    - 코드 중복을 최소화하고 범용적으로 사용할 수 있도록 모듈화(함수화) 했는지
        - 잘 작성되었다고 생각되는 부분을 근거로 첨부합니다.

    *조수민: 중복을 최소화하려고 한 부분이 개인적으로 인상깊었다.*

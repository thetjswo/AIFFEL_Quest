퀘스트 README.md

- 코더 : 이선재
- 리뷰어 : 김양희


🔑 **PRT(Peer Review Template)**

- [o]  **1. 주어진 문제를 해결하는 완성된 코드가 제출되었나요?**
    - 문제에서 요구하는 최종 결과물이 첨부되었는지 확인
    - 문제를 해결하는 완성된 코드란 프로젝트 루브릭 3개 중 2개, 
    퀘스트 문제 요구조건 등을 지칭
        - 해당 조건을 만족하는 부분의 코드 및 결과물을 근거로 첨부

     [리뷰]
  - 루브릭 2개를 달성하였습니다. (VGG16를 활용한 Transfer learning, 학습 과정 및 결과에 대한 설명 시각화를 포함하여 체계적으로 진행)
    
- [o]  **2. 전체 코드에서 가장 핵심적이거나 가장 복잡하고 이해하기 어려운 부분에 작성된 
주석 또는 doc string을 보고 해당 코드가 잘 이해되었나요?**
    - 해당 코드 블럭에 doc string/annotation이 달려 있는지 확인
    - 해당 코드가 무슨 기능을 하는지, 왜 그렇게 짜여진건지, 작동 메커니즘이 뭔지 기술.
    - 주석을 보고 코드 이해가 잘 되었는지 확인
        - 잘 작성되었다고 생각되는 부분을 근거로 첨부합니다.
     
    [리뷰]
  ```
  # 연산량 조절을 위해 사용 노드 수는 128으로 설정
dense_layer = tf.keras.layers.Dense(units=128,activation='relu')
# 예측을 해야하는 총 클래스의 개수가 5개이므로, 최종 출력 노드 개수는 5개로 설정
prediction_layer = tf.keras.layers.Dense(units=5, activation='softmax')

prediction_batch = prediction_layer(dense_layer(feature_batch_average))
print(prediction_batch.shape)
  ```

```
# 이미지 파일 경로 지정
img_dir_path = os.getenv('HOME') + '/git/Aiffel_Node/Data/flower/images'

# 이미지 로드, 확인, 변환, 예측, 결과 출력을 한 번에 진행하는 함수 정의
def show_and_predict_image(dirpath, filename, img_size=IMG_SIZE):
    # 이미지 파일 접근
    filepath = os.path.join(dirpath, filename)
    # 이미지 파일 로드
    image = load_img(filepath, target_size=(img_size, img_size))
    # 이미지 파일 확인
    plt.imshow(image)
    plt.axis('off')
    # 이미지 파일 형태 변환
    image = img_to_array(image).reshape(1, img_size, img_size, 3)
    # 모델을 통한 분류 진행
    prediction = model.predict(image)[0]

    # 각 클래스 별 퍼센티지 연산
    dandelion_percentage = round(prediction[0] * 100)
    daisy_percentage = round(prediction[1] * 100)
    tulip_percentage = round(prediction[2] * 100)
    sunflower_percentage = round(prediction[3] * 100)
    rose_percentage = round(prediction[4] * 100)

    # 결과 출력
    print(f"This image seems {dandelion_percentage}% dandelion, {daisy_percentage}% daisy, {tulip_percentage}% tulip, {sunflower_percentage}% sunflower, and {rose_percentage}% rose.")
```
        
- [o]  **3. 에러가 난 부분을 디버깅하여 문제를 “해결한 기록을 남겼거나” 
”새로운 시도 또는 추가 실험을 수행”해봤나요?**
    - 문제 원인 및 해결 과정을 잘 기록하였는지 확인 또는
    - 문제에서 요구하는 조건에 더해 추가적으로 수행한 나만의 시도, 
    실험이 기록되어 있는지 확인
        - 잘 작성되었다고 생각되는 부분을 근거로 첨부합니다.

    [리뷰]
    - 분류하는 클래스 외의 종류의 꽃으로 테스트
    - 생화 이미지 뿐만 아니라 초등학생이 그린 그림과 명화를 활용
    위의 2가지가 인상적이었습니다!
    <img width="1006" alt="image" src="https://github.com/thetjswo/Aiffel_Quest/assets/145723730/1c7df8e2-a04b-413c-86cb-fe98f3e13c49">

        
- [o]  **4. 회고를 잘 작성했나요?**
    - 주어진 문제를 해결하는 완성된 코드 내지 프로젝트 결과물에 대해
    배운점과 아쉬운점, 느낀점 등이 상세히 기록되어 있는지 확인
        - 딥러닝 모델의 경우,
        인풋이 들어가 최종적으로 아웃풋이 나오기까지의 전체 흐름을 도식화하여 
        모델 아키텍쳐에 대한 이해를 돕고 있는지 확인

    [리뷰]
    회고 및 summary에 핵심적인 내용과 개선 방향이 포함되었으며, 모델 아키텍처 시각화를 잘 활용해주셨습니다.

- [ㅇ]  **5. 코드가 간결하고 효율적인가요?**
    - 파이썬 스타일 가이드 (PEP8) 를 준수하였는지 확인
    - 코드 중복을 최소화하고 범용적으로 사용할 수 있도록 모듈화(함수화) 했는지
        - 잘 작성되었다고 생각되는 부분을 근거로 첨부합니다.

    [리뷰]
    전반적으로 필요하고 핵심적인 내용만 간략하게 잘 활용되었습니다.

---
layout : post
title : "데이터의 성능을 높이는 방법"
categories : [Data science, ML, AIFFEL]
date : 2020-07-31 11:00
---

## 데이터의 성능을 높이는 방법

### Augmentation

- [Data Preprocessing & Augmentation](https://nittaku.tistory.com/272)
- 원래의 데이터를 부풀려서 성능을 더 좋게 한다.
- 원본에 추가되는 개념이니 성능이 떨어지지 않는다. 쉽고 패턴이 정해져 있다.
- **좌우반전, 이미지 잘라주기, 밝기조절 등**이 있다.
- 사용 예시
    - **AlexNet**
        - 여기서 처음으로 Augmentation을 Heavy하게 썼다고 한다.
            1. 좌우 반전
            2. **224*224px의 이미지**를 → **256*256px로 resize** 한 다음 → **224*224px로 랜덤하게 2048번 잘라서 데이터를 2048배 늘림**
            3. 테스트시에는 2048배 늘이면 너무 느리니까
            256*256px로 resize한 다음 → 좌상단/우상단/좌하단/우하단/가운데 5번만 잘라서 5배 늘림 → 좌우반전까지 **총 10배 늘림** → 10개 따로 predict 한 다음, 평균을 낸다.
            4. PCA를 통해 RGB채널을 조절해주었다. (요즘엔 잘 안쓰는 방식)
    - **VGGNet**
        - 사진 데이터에서 가장 많이 사용하는 방식.
            1. **RGB값을 각각 빼서 RGB 값의 평균을 0**으로 만든다. → Loss 수렴이 빨라진다.
                - weight를 초기화할 때도 E(X)와 E(Y)=0에서 시작한 이유가 loss 수렴이 좋아져서였다.
                - X와 Y는 모두 activation output이었다. Hidden layer 사이의 input과 ouput의 평균이 0인 것만 유지하도록 해주면 Layer를 더 쌓을 수 있는 개념이었다.
                - 처음 이미지를 넣는 Input은 세로, 가로, RGB 값은 activation output이 아니므로 강제로 RGB값을 평균에서 빼주면, 사실상 input값의 평균이 0이 되어서 수렴이 빨라진다.
            2. 같은 이미지를 **256*256px, 384*384px, 512*512px 3가지 버전**으로 만든 뒤, → **224*224px로 랜덤 crop** 한다.
                - 256*256px에서 224*224px로 Crop하면 대부분의 이미지가 들어간다. 하지만 512*512px에서 224*224px은 이미지의 1/4 정도밖에 안들어간다. 고양이로 치면 고양이 한마리 전체가 들어갈 일은 거의 없다. 즉, 고양이의 귀, 꼬리, 털 등등이 짤려서 들어간다.
                - 사람처럼 일부만 보고도 고양이로 인식하도록 train 되는 효과가 난다.
            3. 테스트시에는 마찬가지로 하는 것이 가장 error가 낮았다.
        - 결과적으로 이러한 방식으로 전처리를 하면 error가 10.4% → 7.1%로 줄어들었다고 한다.

        ![https://t1.daumcdn.net/cfile/tistory/996B2D385B62CED70D](https://t1.daumcdn.net/cfile/tistory/996B2D385B62CED70D)

        - Multi-crop : Alexnet에서 했던, 좌상단~가운데 5개 크롭 + 좌우반전 2개 → 10배 늘리는 방법
        - Dense : (1, 1) Conv layer처럼, Fully-connected layer를 바꿔주면 test할 때 이미지를 더 크게 넣어줄 수 있다. 크게 넣어주면 (1, 1)으로 나오던 결과가 (2, 2)로 나오는데, 그 결과값은 5군데 crop하는 것과 동일하고, 그것을 평균 내준다.
        - VGGNet에서는 Multi-Crop과 Dense를 따로 써주면 선응이 좋아지지만 결과는 거의 비슷하고, 같이 써주면 성능이 더 좋아졌다. 굳이 따지면 실행속도가 빠른 Dense를 쓰는 것을 권장했지만, 결국에는 같이 쓰는 것을 택했다.

        ![https://t1.daumcdn.net/cfile/tistory/99AA06375B62CED81E](https://t1.daumcdn.net/cfile/tistory/99AA06375B62CED81E)

### Validation Data

- Training Data에 일부분을 Validation data로 두는 것.
- Overfitting을 방지에 유용하다
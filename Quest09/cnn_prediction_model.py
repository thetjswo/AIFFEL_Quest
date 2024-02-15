# cnn_prediction_model.py

# 예측에 필요한 라이브러리
import tensorflow as tf
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing import image

def map_prediction(label, prediction):
    # 가장 높은 확률을 갖는 인덱스를 조회
    max_index = np.argmax(prediction)
    # 해당 인덱스에 해당하는 레이블을 반환
    predicted_label = label[max_index]
    max_probability = np.max(prediction)
    
    return predicted_label, max_probability

async def prediction_model():
    model = tf.keras.models.load_model('./CNN_V2_adddata_best_model_epoch_130.h5')
    
    img = Image.open('./sample_data/01.jpeg')

    # resize
    target_size = 224
    img = img.resize((target_size, target_size)) 

    #numpy array로 변경
    np_img = image.img_to_array(img)

    #4차원으로 변경 
    img_batch = np.expand_dims(np_img, axis=0)
    #feature normalization
    pre_processed = img_batch / 255.0
    
    # 예측
    y_preds = model.predict(pre_processed).tolist()
    np.set_printoptions(suppress=True, precision=5) #소수 5자리까지 
    
    # 레이블 정의
    label = ["barrel_jellyfish", "blue_jellyfish", "compass_jellyfish", "lions_mane_jellyfish", "mauve_stinger_jellyfish", "Moon_jellyfish"]

    # 예측 결과를 레이블과 매핑
    predicted_label, max_probability = map_prediction(label, y_preds[0])
    result = {"predicted_label" : predicted_label, "max_probability" :  max_probability}
    return result
from keras.applications.vgg16 import VGG16, preprocess_input, decode_predictions
from keras.preprocessing import image
import numpy as np

# 学習済みモデルVGG16の読み込み
model = VGG16(weights='imagenet')

# 画像判定のための関数
def predict(filename, featuresize=5):
    # 画像の読み込みと前処理
    img = image.load_img(filename, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    
    # モデルで予測
    preds = model.predict(x)
    results = decode_predictions(preds, top=featuresize)[0]
    return results

# 画像ファイル名（この部分を適切なファイルパスに置き換えてください）
filename = 'dog.jpg'

# 画像を判定し、結果を表示
results = predict(filename)
for result in results:
    # 各予測結果の詳細（クラスID、ラベル、確率）を表示
    print('予測結果: {}, 確率: {:.2f}%'.format(result[1], result[2] * 100))

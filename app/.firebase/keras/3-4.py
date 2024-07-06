import numpy as np
import matplotlib.pyplot as plt

# x軸の値を生成: 0から2πまで0.01刻み
x = np.arange(0, 2 * np.pi, 0.01)
# y軸の値を計算: sin関数を使用
y = np.sin(x)

# グラフをプロット
plt.plot(x, y)

# タイトルと軸ラベルを設定
plt.title('Sine Curve')
plt.xlabel('x')
plt.ylabel('sin(x)')

# グラフを表示
plt.show()

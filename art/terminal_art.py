import math

# 1. 図形のサイズと使用する文字を決める
WIDTH = 30
HEIGHT = 15
SYMBOL = "*"
BACKGROUND = " "

# 2. 描画用の関数を定義する
def draw_circle(radius):
    for y in range(HEIGHT):
        line = ""
        for x in range(WIDTH):
            # 3. 各ピクセル（文字）をベクトル（座標）として考える
            # 中心からの距離を計算する
            center_x, center_y = WIDTH / 2, HEIGHT / 2
            distance = math.sqrt((x - center_x) ** 2 + (y - center_y) ** 2)

            # 4. 円の周上にいるか判定する
            # distanceが半径（radius）に近い場所にSYMBOLを配置
            if radius - 0.5 < distance < radius + 0.5:
                line += SYMBOL
            else:
                line += BACKGROUND
        print(line)

# 5. 描画関数を呼び出して図形を描く
print("--- ターミナル・アート (円) ---")
draw_circle(5)

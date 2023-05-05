import os
from PIL import Image


def trim_image(image_path):
    image = Image.open(image_path)
    image = image.convert("RGBA")
    pixel_data = image.load()

    # 画像のサイズを取得
    width, height = image.size

    # 画像の境界を取得
    left = width
    right = 0
    top = height
    bottom = 0

    for y in range(height):
        for x in range(width):
            r, g, b, a = pixel_data[x, y]
            if a != 0:
                if x < left:
                    left = x
                if x > right:
                    right = x
                if y < top:
                    top = y
                if y > bottom:
                    bottom = y

    # 全て透明のPNGファイルの場合はNoneを返す
    if left == width and right == 0 and top == height and bottom == 0:
        return None

    # 画像をトリミング
    image = image.crop((left, top, right+1, bottom+1))
    # ログ出力
    print(image_path + " ...OK!!")
    return image


# スクリプトが実行されているディレクトリにある全てのPNGファイル名を取得
image_paths = [f for f in os.listdir() if f.endswith(".png")]

# 各画像ファイルをトリミングして保存
for i, image_path in enumerate(image_paths):
    trimmed_image = trim_image(image_path)

    # 全て透明のPNGファイルの場合はスキップする
    if trimmed_image is None:
        continue

    trimmed_image.save(f"trimmed_image{i}.png")

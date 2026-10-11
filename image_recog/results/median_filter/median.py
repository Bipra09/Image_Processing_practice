from PIL import Image
import numpy as np

img = Image.open(r"C:\Users\b.biswasu\Documents\Study\image_recog\image\images.jpg").convert("L")
px = np.array(img)
print(px.shape)
print(px)

step = 3
half = step // 2

h, w = px.shape
canvas = np.zeros((h, w), dtype=np.uint8)

for x in range(h):
    for y in range(w):

        values = []

        for dx in range(-half, half + 1):
            for dy in range(-half, half + 1):

                a = x + dx
                b = y + dy

                if 0 <= a < h and 0 <= b < w:
                    values.append(px[a][b])

        values.sort()

        median = values[len(values) // 2]

        canvas[x][y] = median

Image.fromarray(canvas).save("median_result.png")

print("done")
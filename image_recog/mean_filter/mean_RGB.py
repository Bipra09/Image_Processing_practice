from PIL import Image
import numpy as np

img = Image.open(r"C:\Users\b.biswasu\Documents\Study\image_recog\image\images.jpg")   

px = np.array(img)
h, w, channels = px.shape
canvas = np.zeros((h, w, channels), dtype=np.uint8)

for c in range(channels):          
    for x in range(h):
        for y in range(w):
            total = 0
            count = 0
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    a = x + dx
                    b = y + dy
                    if 0 <= a < h and 0 <= b < w:
                        total += int(px[a][b][c])  
                        count += 1
            canvas[x][y][c] = total // count

Image.fromarray(canvas).save("mean_rgb_result.png")
print("done")
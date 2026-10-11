from PIL import Image
import numpy as np
import math

img = Image.open(r"C:\Users\Bipro\OneDrive\Documents\Study\image_recog\image\images.jpg").convert("L")
px = np.array(img)
h,w = px.shape

canvas = np.zeros((h,w),dtype=np.uint8)

Gx = [[-1,0,1],[-2,0,2],[-1,0,1]]
Gy = [[-1,-2,-1],[0,0,0],[1,2,1]]

k = 3
hf = k//2

for x in range(h):
    for y in range(w):
        gx_value = 0
        gy_value = 0
        for dx in range(-hf, hf+1):
            for dy in range(-hf, hf+1):
                a, b = x+dx, y+dy
                if 0 <= a < h and 0 <= b < w:
                    gx_value += int(px[a][b]) * Gx[dx+hf][dy+hf]
                    gy_value += int(px[a][b]) * Gy[dx+hf][dy+hf]

        magnitude = math.sqrt(gx_value**2 + gy_value**2)
        canvas[x][y] = min(255, int(magnitude))
Image.fromarray(canvas).save("sobel.png")
                 

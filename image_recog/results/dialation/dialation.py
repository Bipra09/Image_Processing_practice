from PIL import Image
import numpy as np

img = Image.open(r"C:\Users\Bipro\OneDrive\Documents\Study\image_recog\image\images.jpg").convert("L")
px = np.array(img)

step = 3
half = step//2

h,w = px.shape
canvas = np.zeros((h,w),dtype=np.uint8)

for x in range(h):
    for y in range(w):
        max_val = 0
        for dx in range(-half,half+1):
            for dy in range(-half,half+1):
                a = x + dx
                b = y + dy
                if 0<=a<h and 0<=b<w:
                    if px[a][b] > max_val:
                        max_val = px[a][b]
        canvas[x][y] = max_val
Image.fromarray(canvas).save("dilated.png")
print("done")
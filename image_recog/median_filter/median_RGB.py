from PIL import Image
import numpy as np

img = Image.open(r"C:\Users\b.biswasu\Documents\Study\image_recog\image\images.jpg")
px = np.array(img)
print(px.shape)
h,w,chanel= px.shape
canvas = np.zeros((h,w,chanel),dtype=np.uint8)
k = 3
hf = k//2
for c in range(chanel):
    for x in range(h):
        for y in range(w):
            pix_val = []
            for dx in range(-hf,hf+1):
                for dy in range(-hf,hf+1):
                    a,b = dx+x,dy+y
                    if 0<=a<h and 0<=b<w:
                        pix_val.append(px[a][b][c])
            pix_val.sort()
            median = pix_val[len(pix_val)//2]
            canvas[x][y][c] = median
Image.fromarray(canvas).save("medain_RGB.png")
print("done")
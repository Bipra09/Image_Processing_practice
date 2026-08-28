from PIL import Image
import numpy as np
def weight(dx,dy,sigma):
    return np.exp(-(dx**2 + dy**2)/(2* sigma**2))

img = Image.open(r"C:\Users\b.biswasu\Documents\Study\image_recog\image\images.jpg")
px = np.array(img)

print(px.shape)

h,w,chanel = px.shape
canvas = np.zeros((h,w,chanel),dtype=np.uint8)

k = 3
hf = k//2
sigma = 2
for C in range (chanel):
    for X in range(h):
        for Y in range(w):
            weight_sum = 0
            total_WW = 0
            for dx in range  (-hf,hf+1):
                for dy in range (-hf,hf+1):
                    a,b = X+dx,Y+dy
                    if 0<=a<h and 0<=b<w:
                        WW = weight(dx,dy,sigma)
                        total_WW += WW
                        weight_sum += WW * int(px[a][b][C])
            canvas[X][Y][C] = weight_sum/total_WW
Image.fromarray(canvas).save("RGB_Gaussian.png")
print("done") 
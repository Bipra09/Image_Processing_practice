from PIL import Image
import numpy as np
import math

img = Image.open(r"C:\Users\Bipro\OneDrive\Documents\Study\image_recog\image\images.jpg").convert("L")
px = np.array(img)

h,w = px.shape

#  Gaussian blur
def weight(dx,dy,sigma):
    return np.exp(-(dx**2 + dy**2)/(2*sigma**2))

sigma = 2
step = 5
half = step//2
blurred = np.zeros((h,w))

for x in range(h):
    for y in range(w):
        total_weight = 0
        weight_sum = 0
        for dx in range(-half,half+1):
            for dy in range(-half,half+1):
                a = x + dx
                b = y + dy
                if 0<=a<h and 0<=b<w:
                    weigh = weight(dx,dy,sigma)
                    total_weight += weigh
                    weight_sum += weigh * px[a][b]
        blurred[x][y] = weight_sum/total_weight

# Sobel (gradient magnitude + direction) 
Gx = [[-1,0,1],[-2,0,2],[-1,0,1]]
Gy = [[-1,-2,-1],[0,0,0],[1,2,1]]
mag = np.zeros((h,w))
ang = np.zeros((h,w))

for x in range(1,h-1):
    for y in range(1,w-1):
        gx = 0
        gy = 0
        for dx in range(-1,2):
            for dy in range(-1,2):
                gx += blurred[x+dx][y+dy] * Gx[dx+1][dy+1]
                gy += blurred[x+dx][y+dy] * Gy[dx+1][dy+1]
        mag[x][y] = math.sqrt(gx**2 + gy**2)
        ang[x][y] = math.degrees(math.atan2(gy,gx)) % 180

# Non-max suppression 
thin = np.zeros((h,w))
for x in range(1,h-1):
    for y in range(1,w-1):
        a = ang[x][y]
        q, r = 255, 255
        if (0<=a<22.5) or (157.5<=a<=180):
            q, r = mag[x][y+1], mag[x][y-1]
        elif 22.5<=a<67.5:
            q, r = mag[x+1][y-1], mag[x-1][y+1]
        elif 67.5<=a<112.5:
            q, r = mag[x+1][y], mag[x-1][y]
        elif 112.5<=a<157.5:
            q, r = mag[x-1][y-1], mag[x+1][y+1]
        if mag[x][y] >= q and mag[x][y] >= r:
            thin[x][y] = mag[x][y]

# - Double threshold 
strong_val = 255
weak_val = 75
max_val = thin.max()
high = max_val * 0.15
low = high * 0.05
result = np.zeros((h,w),dtype=np.uint8)

for x in range(h):
    for y in range(w):
        if thin[x][y] >= high:
            result[x][y] = strong_val
        elif thin[x][y] >= low:
            result[x][y] = weak_val

#  Hysteresis (connect weak edges to strong ones)
for x in range(1,h-1):
    for y in range(1,w-1):
        if result[x][y] == weak_val:
            connected = False
            for dx in range(-1,2):
                for dy in range(-1,2):
                    if result[x+dx][y+dy] == strong_val:
                        connected = True
            result[x][y] = strong_val if connected else 0

Image.fromarray(result).save("canny.png")
print("done")
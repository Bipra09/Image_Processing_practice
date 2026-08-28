from PIL import Image
import numpy as np

img = Image.open(r"C:\Users\b.biswasu\Documents\Study\image_recog\image\images.jpg").convert("L")
px = np.array(img)

print(px.shape)
print(px)

step = 3
half = step//2
h,w = px.shape
canvas = np.zeros((h,w),dtype=np.uint8)
for x in range (h):
    for y in range (w):
        total = 0
        count = 0
        for dx in range(-half,half+1):
            for dy in range(-half,half+1):
                a = x + dx
                b = y + dy
                if 0 <= a < h and 0 <=b < w :
                    total += int(px[a][b])
                    count +=1
        canvas[x][y] = total//count
Image.fromarray(canvas).save("mean_result.png")
print("done")

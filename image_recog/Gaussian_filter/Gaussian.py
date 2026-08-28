from PIL import Image
import numpy as np
def weight(dx,dy,sigma):# sigma is decay rate
    return np.exp(-(dx**2 + dy**2)/(2* sigma**2))


img = Image.open(r"C:\Users\b.biswasu\Documents\Study\image_recog\image\images.jpg").convert("L")
px = np.array(img)


sigma = 10
step = 15
half = step//2

h,w = px.shape
canvas = np.zeros((h,w),dtype=np.uint8)

for x in range (h):
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
                              weight_sum += weigh *px[a][b]
            canvas[x][y] =  weight_sum/total_weight
Image.fromarray(canvas).save("G.png")    
print("done")         
                              
                   
          



            


  
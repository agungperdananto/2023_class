from matplotlib import pyplot as plt
import cv2

# 
img_cv = cv2.imread('images/image-1.jpg')
# img_plt = plt.imread('images/image-3.jpg')

p, l, d = img_cv.shape

for i in range(800, 1200):
    for j in range(500, 600):
        # B G R
        img_cv[i, j] = 0

for i in range(int(p/2-100), int(p/2+100)):
    for j in range(int(l/2-200), int(p/2+200)):
        # B G R
        img_cv[i, j] = [0, 0, 0]

print('dimension_cv2', img_cv.shape)
# print('dimension_plt', img_plt.shape)
cv2.imshow('Original image', img_cv)

cv2.waitKey(0)
cv2.destroyAllWindows()

# plt.subplot(121),
# plt.imshow(img_plt)
# plt.show()

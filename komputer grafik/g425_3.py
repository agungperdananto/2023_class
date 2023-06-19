import cv2 

img = cv2.imread('images/image-1.jpg')

print(img.shape)

# x(500, 600) y(300, 400) color=black

# looping
# for y in range(600, 700):
#     for x in range(500, 1200):
#         img[y, x] = [255, 0, 0]

# y, x, color
new_img = img[200:1000, 500:1000]
# print(new_img.shape)

def slicing(img, x, y, size):
    img[y:y+size, x:x+size] = 0
    return img

def end_slicing(img, size):
    y, x, color = img.shape
    img[y-size:y, x-size:x] = 0
    return img

# new_img = slicing(img, 600, 600, 450)
# new_img = end_slicing(img, 800)

cv2.imwrite('images/image-out1.jpg', new_img)

# cv2.imshow('Image', new_img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()


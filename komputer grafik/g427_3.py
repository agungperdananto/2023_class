import cv2 

img = cv2.imread('images/image-out.jpg')


y, x, color = img.shape

print('x', x)
print('y', y)
print('color', color)


# block color x = (0, 100), y = (0, 150)

# looping
# for y in range(0, 150):
#     for x in range(0, 100):
#         img[y,x]=0

# y, x color[B, G, R]
# array slicing
def slicing(img, x=0, y=0, size=0):
    return img[y:y+size, x:x+size]

def center_slicing(img, size, color=[]):
    pass

# new_img = slicing(img, 800, 300, 650)
# cv2.imwrite('images/image-out.jpg', new_img)
# cv2.imshow('new Image', new_img)

# img[0:750, 0:750] = [132, 203, 244]
# cv2.imshow('Original Image', img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

import cv2 

img = cv2.imread('images/image-1.jpg')
# looping
# for y in range(200, 800):
#     for x in range(800, 1200):
#         img[y, x] = 0

# y, x, color = img.shape
# print(f'panjang {x} lebar {y} warna {color} channel' )

# slicing
# img[200:, 800:1200] = [124, 88, 255]

def slicing(img, x, y, size):
    img[y:y+size, x:x+size] = 0
    return img

def slicing_end(img, size):
    y, x, color = img.shape
    img[y-size:y, x-size:x] = 0
    return img
# gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# print('shape original', img.shape)
# print('shape gray', gray_img.shape)
# cv2.imshow('Images', img)
# cv2.imshow('gray', gray_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# crop = img[200:600, 500:1200]
# cv2.imwrite('images/image-gray.jpg', gray_img)
# cv2.imwrite('images/image-original.jpg', img)


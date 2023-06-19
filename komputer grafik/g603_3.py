import cv2 

img = cv2.imread('images/image-1.jpg')
print('BGR', img.shape)
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# print('Gray', gray.shape)
# Y, X, [B,G, R]
# img[300:800, 1000:1200] = [223, 173, 90]

# cv2.imshow('Image', img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

def end_slice(img, size, color = 0):
    max_y,  max_x, channel = img.shape
    print(max_y)
    print(max_x)
    img[max_y-size:max_y, max_x-size:max_x] = color
    return img

def center_slice(img, size, color = 0):
    max_y,  max_x, channel = img.shape

    # img[max_y-size:max_y, max_x-size:max_x] = color
    return img
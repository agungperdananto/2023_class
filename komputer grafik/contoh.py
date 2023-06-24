import cv2 


folder_name = input('folder_name: ')
size_in = input('ukuran_kotak: ')
size = int(size_in)
img = cv2.imread('../images/image-1.jpg')


# top_left
# top_center
# top_right
# center_left
# center
# center_right
# bottom_left
# bottom_center
# bottom_left

def crop_by_position(img, position, size):
    pass


top_left = crop_by_position(img, 'top_left', size)
cv2.imwrite(f'{folder_name}/top_left.jpg', top_left)
top_center = crop_by_position(img, 'top_center', size)
cv2.imwrite(f'{folder_name}/top_center.jpg', top_center)
top_right = crop_by_position(img, 'top_right', size)
cv2.imwrite(f'{folder_name}/top_right.jpg', top_right)
center_left = crop_by_position(img, 'center_left', size)
cv2.imwrite(f'{folder_name}/center_left.jpg', center_left)
center = crop_by_position(img, 'center', size)
cv2.imwrite(f'{folder_name}/center.jpg', center)
center_right = crop_by_position(img, 'center_right', size)
cv2.imwrite(f'{folder_name}/center_right.jpg', center_right)
bottom_left = crop_by_position(img, 'bottom_left', size)
cv2.imwrite(f'{folder_name}/bottom_left.jpg', bottom_left)
bottom_center = crop_by_position(img, 'bottom_center', size)
cv2.imwrite(f'{folder_name}/bottom_center.jpg', bottom_center)
bottom_right = crop_by_position(img, 'bottom_right', size)
cv2.imwrite(f'{folder_name}/bottom_right.jpg', bottom_right)


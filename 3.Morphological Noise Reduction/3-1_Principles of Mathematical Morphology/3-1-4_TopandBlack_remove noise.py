import cv2

original_img = cv2.imread(r"D:\pyrhon_test\2.Image Dehazing Technology\Lenna.bmp", 0)

#定義矩形結構元素
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3, 3))
#頂帽運算
TOPHAT_img = cv2.morphologyEx(original_img, cv2.MORPH_TOPHAT, kernel)
#黑帽運算
BLACKHAT_img = cv2.morphologyEx(original_img, cv2.MORPH_BLACKHAT, kernel)
#二值化
bitwiseXor_gray = cv2.bitwise_xor(original_img, TOPHAT_img)
#顯示以下侵蝕後的影像
cv2.imshow('original_img', original_img)
cv2.imshow('TOPHAT_img', TOPHAT_img)
cv2.imshow('BLACKHAT_img', BLACKHAT_img)
cv2.imshow('bitwiseXor_gray', bitwiseXor_gray)

cv2.waitKey(0)
cv2.destroyAllWindows()

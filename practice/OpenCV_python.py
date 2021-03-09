import numpy
from cv2 import cv2

"""
cv.imread()，cv.imshow()，cv.imwrite()
cv.waitKey()是一个键盘绑定函数。

cv.IMREAD_COLOR： 加载彩色图像。任何图像的透明度都会被忽视。它是默认标志。
cv.IMREAD_GRAYSCALE：以灰度模式加载图像
cv.IMREAD_UNCHANGED：加载图像，包括alpha通道

"""
# 读取图像
# img = cv2.imread('File/captcha.jpg',cv2.IMREAD_GRAYSCALE)
# print(img)

# 显示图像
# cv2.imshow('captcha.jpg',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.destroyWindow('captcha.jpg')

# 调整窗口
# cv2.namedWindow('captcha.jpg',cv2.WINDOW_NORMAL)
# cv2.imshow('captcha.jpg',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 写入图像
# cv2.imshow('image',img)
# k = cv2.waitKey(0)
# if k == 27:     # 等待按DEC退出窗口
#     cv2.destroyAllWindows()
# elif k == ord('s'):     # 等待关键字保存并退出窗口
#     cv2.imwrite('File/验证码.png',img)
#     cv2.destroyAllWindows()





# 访问和修改像素值
img = cv2.imread('File/captcha.jpg',cv2.IMREAD_COLOR)
# print(img)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 访问像素值
px = img[0,22]
print(px)

color = img[22,22,0]
print(color)

# 修改像素值
img[22,22] = [255,255,255]
print(img[22,22])


import cv2
import numpy as np
import os
img1 = cv2.imread("D:\iphone pics\CUSJ3426.JPG",cv2.IMREAD_GRAYSCALE)
img2 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
#re_size= cv2.resize(img1,(300,300))

#h =np.hstack((re_size,re_size,re_size))
#v= np.vstack((h,h))


cv2.imshow("DTU",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

# list_name = os.listdir(r"D:\testimages")
# print(list_name)

# for name in list_name:
#     path="D:\\testimages"
#     imagename= path + "\\"+ name

#     img = cv2.imread(imagename)
#     img3 = cv2.resize(img,(500,600))

#     cv2.imshow("DTU1",img3)
#     cv2.waitKey(0)

# cv2.destroyAllWindows()

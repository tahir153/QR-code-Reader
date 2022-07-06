import cv2

d = cv2.QRCodeDetector()
return_value,points, straight_qrcode = d.detectAndDecode(cv2.imread('QR path here'))
print(return_value)

import cv2
import numpy as np

# 画像を読み込む
id = 1
path = fr"data\images\tyusyajo{id}.jpg"

img = cv2.imread(path)
# cv2.imshow("img", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# # マウスクリックで4点を取得
# lline = []
# rline = []

# def mouse_event(event, x, y, flags, param):
#     if event == cv2.EVENT_LBUTTONDOWN:
#         # 左クリックで赤い点を描画
#         cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
#         cv2.imshow("img", img)
#         lline.append([x, y])
#         print(f"lline: {lline}, rline: {rline}")
#     if event == cv2.EVENT_RBUTTONDOWN:
#         # 右クリックで青い点を描画
#         cv2.circle(img, (x, y), 3, (255, 0, 0), -1)
#         cv2.imshow("img", img)
#         rline.append([x, y])
#         print(f"line1: {lline}, rline: {rline}")

# cv2.namedWindow("img")
# cv2.setMouseCallback("img", mouse_event)

# while True:
#     cv2.imshow("img", img)
#     if cv2.waitKey(0):
#         break

# cv2.destroyAllWindows()

lline = [[24, 102], [123, 114]]
rline = [[82, 76], [175, 90]]

# 透視変換のための4点を設定
pts1 = np.float32([lline[0], lline[1], rline[0], rline[1]])
pts2 = np.float32([[0, 0], [100, 0], [0, 100], [100, 100]])

# 透視変換行列を求める
M = cv2.getPerspectiveTransform(pts1, pts2)

# 透視変換
dst = cv2.warpPerspective(img, M, (100, 100))

# 画像を表示
cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

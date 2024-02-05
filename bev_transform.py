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

pt1, pt2, pt3, pt4 = lline[0], lline[1], rline[0], rline[1]

pts1 = np.float32([pt1, pt2, pt3, pt4])  # 左上、右上、左下、右下
pts2 = np.float32([[0, 0], [100, 0], [0, 100], [100, 100]])  # 左上、右上、左下、右下

# 透視変換行列を求める
M = cv2.getPerspectiveTransform(pts1, pts2)
print(M)

src_h, src_w = img.shape[:2]
src_pt1 = np.array([0, 0])
src_pt2 = np.array([src_w, 0])
src_pt3 = np.array([0, src_h])
src_pt4 = np.array([src_w, src_h])

dst_pt1 = np.dot(M, np.array([src_pt1[0], src_pt1[1], 1]))
dst_pt2 = np.dot(M, np.array([src_pt2[0], src_pt2[1], 1]))
dst_pt3 = np.dot(M, np.array([src_pt3[0], src_pt3[1], 1]))
dst_pt4 = np.dot(M, np.array([src_pt4[0], src_pt4[1], 1]))

dst_h = max(dst_pt1[1], dst_pt2[1], dst_pt3[1], dst_pt4[1])
dst_w = max(dst_pt1[0], dst_pt2[0], dst_pt3[0], dst_pt4[0])

# 透視変換
dst = cv2.warpPerspective(img, M, (int(dst_w), int(dst_h)))

# 画像を表示
cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

import sys
from pathlib import Path

import cv2

# git clone した pytorch_yolov3 ディレクトリのパスを指定してください
yolov3_path = Path("pytorch_yolov3")

sys.path.append(str(yolov3_path))
from pytorch_yolov3.yolov3.detector import Detector

config_path = yolov3_path / "config/yolov3_coco.yaml"
weights_path = yolov3_path / "weights/yolov3.weights"

# 検出器を作成する
detector = Detector(config_path, weights_path)

# 画像を読み込む
path = r"data\images\cars.jpg"
img = cv2.imread(path)
# print(img.shape)
# cv2.imshow("img", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# exit()

# 検出する
detections = detector.detect_from_imgs(img)
# from pprint import pprint
# pprint(detections)
# pprint(detections[0])
# pprint(detections[0][0])

# 車両の検出結果のみ抽出する
target = ["bicycle", "car", "motorcycle", "bus", "truck"]
cars = list(filter(lambda x: x["class_name"] in target, detections[0]))

# 検出結果を画像に描画する
for bbox in cars:
    cv2.rectangle(
        img,
        (int(bbox["x1"]), int(bbox["y1"])),
        (int(bbox["x2"]), int(bbox["y2"])),
        color=(0, 255, 0),
        thickness=2,
    )

# 画像を表示する
cv2.imshow("car detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

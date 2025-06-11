import torch
import cv2
import numpy as np
from ultralytics import YOLO
import os

# 設定裝置
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# 建立儲存圖片的資料夾（如果尚未存在）
save_folder = "C:/GitHub/2025_Spring_EmbededSystem/final_project"
os.makedirs(save_folder, exist_ok=True)

# 設定圖片檔名
image_filename = "test_picture.jpg"
image_path = os.path.join(save_folder, image_filename)
abs_image_path = os.path.abspath(image_path)

# 拍攝一張照片（樹莓派相機）
camera = cv2.VideoCapture(0)  # 0 表示默認攝影機
ret, frame = camera.read()
if ret:
    cv2.imwrite(abs_image_path, frame)
    print(f"Image saved to {abs_image_path}")
else:
    print("Failed to capture image.")
camera.release()

# 讀取圖片
image = cv2.imread(abs_image_path)
if image is None:
    raise ValueError(f"Failed to load image at {abs_image_path}")
img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# 載入模型
model_path = "C:/GitHub/2025_Spring_EmbededSystem/final_project/yolo_result/weights/best.pt"
model = YOLO(model_path).to(device)

# 推論
results = model.predict(img_rgb, device=device, verbose=False)

# 解析推論結果
if results and len(results[0].boxes) > 0:
    for box in results[0].boxes:
        cls_idx = int(box.cls.cpu().numpy())
        cls_name = ['trash', 'recycle'][cls_idx]  # 依據訓練時的標籤
        confidence = float(box.conf.cpu().numpy())
        print(f"Classification result: {cls_name} (Confidence: {confidence:.2f})")
else:
    print("No objects detected.")

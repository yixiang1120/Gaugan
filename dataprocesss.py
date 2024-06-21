from PIL import Image
import os

# 定義輸入和輸出資料夾路徑
input_folder = 'results\road_v3\test_latest\images\synthesized_imag'
output_folder = 'results\road_v3\test_latest\images\ro'

# 確保輸出資料夾存在，如果不存在就建立資料夾
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 將資料夾中的每個PNG圖片轉換為JPG格式
for filename in os.listdir(input_folder):
    if filename.endswith(".png"):
        # 讀取PNG圖片
        img = Image.open(os.path.join(input_folder, filename))
        # 將PNG圖片轉換為JPG格式（品質為95）
        img.convert("RGB").save(os.path.join(output_folder, filename.replace(".png", ".jpg")), quality=95)

print("轉換完成！")

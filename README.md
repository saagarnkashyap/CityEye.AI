# CityEye.AI - Traffic-Detection
Traffic Detection using YOLOv11
=======
# 🚦 CityEye.AI — Smart Traffic Object Detection with YOLOv11

[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)](https://www.python.org/)
[![YOLOv11](https://img.shields.io/badge/YOLO-v11-orange?logo=ultralytics)](https://github.com/ultralytics/ultralytics)
[![Status](https://img.shields.io/badge/Status-In%20Progress-yellow)]()
[![Made with ❤️ by Saagar](https://img.shields.io/badge/Made%20by-Saagar-red)](https://github.com/saagarnkashyap)

---

### 👀 What It Does

**CityEye.AI** is an object detection system that analyzes traffic footage and identifies:
- 🚗 Cars & Bikes  
- 🧍‍♂️ Men & Women  
- 🚸 Children  
- 🏍️ Vehicles & More...

Trained with YOLOv11, this project turns *raw street video* into *intelligent detections* that could power:
> Smart cities, traffic analytics, surveillance, or even social trends!

---

### 🎞️ Demo Preview

<p align="center">
  <img src="InShot_20250520_232839379.gif" width="30%" alt="CityEye.AI demo preview"/>
</p>

>Video posted on Linkedin https://www.linkedin.com/in/saagar-n-kashyap-7231ab206/
---

### ⚙️ Tech Stack

| Tool         | Purpose                      |
|--------------|------------------------------|
| **YOLOv11**  | Object Detection (Ultralytics) |
| **Python 3.11** | Programming Language       |
| **OpenCV**   | Video I/O and Frame Processing |
| **FFmpeg**   | Video Conversion   |

---

### 🧪 How to Run Locally

1. **Clone the repo**
```bash
git clone https://github.com/saagarnkashyap/CityEye.AI.git
cd CityEye.AI
```

2. **Create a Virtual Environment**
```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3.  **Install Required Packages**
```bash
pip install -r requirements.txt
```

4. **Download the YOLOv11 Model**
Make sure the yolo11n.pt file exists in the project directory.
If not present, use this command below in the terminal
```bash
yolo download model=yolo11n
```

5. **Run Object Detection on Your Video**
```bash
from ultralytics import YOLO
model = YOLO("yolo11n.pt")
results = model.predict(source="input_video.mp4", save=True, conf=0.25)
```
>considering **input_video.mp4** your input video.


Thank you,
Mail me at saagarcourses@gmail.com for suggestions.


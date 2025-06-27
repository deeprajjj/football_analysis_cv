# ⚽ Football Match Analysis using Computer Vision (WIP)

This is a real-time football match analysis system using machine learning, and computer vision techniques. The project uses YOLOv8 for object detection, tracks players and the ball across frames, and will incorporate clustering, optical flow, and perspective transformation to analyze player movement, speed, and distance covered.

---

##  Features(Planned)

-  Detect players, referees, and ball using YOLOv8
-  Train a custom object detector using Roboflow
-  Process video into frames and reconstruct annotated video
-  Track objects across frames using Supervision or DeepSORT
-  Use KMeans clustering to identify team colors from t-shirt pixels
-  Apply optical flow to detect camera movement
-  Use perspective transformation for real-world distance measurement
-  Calculate speed and distance traveled by players

---

## 🏗️ Project Status

| Feature                     | Status         |
|----------------------------|---------------- |
| YOLOv8 Detection           | ✅ Done         |
| Custom Dataset & Training  | ✅ Done         |
| Tracking                   | 🛠️ In Progress  |
| KMeans Clustering          | 🔜 Planned      |
| Optical Flow               | 🔜 Planned      |
| Perspective Transform      | 🔜 Planned      |
| Speed/Distance Estimation  | 🔜 Planned      |

---

## 🧠 Technologies Used

- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
- Python & OpenCV (cv2)
- Scikit-learn (KMeans clustering)
- Supervision / DeepSORT (tracking)
- Roboflow (dataset download and annotation)

---

## 📁 Project Structure
football-cv/
├── main.py # Main pipeline script
├── yolo_infer.py # YOLOv8 inference logic
├── trackers/ # Tracking utilities
├── util/ # Frame-video processing helpers
├── traning/ # Custom training code and configs
├── input_videos/ # Raw video input (not pushed to GitHub)
├── output_videos/ # Processed results (not pushed to GitHub)
├── .gitignore # Ignore unnecessary files
├── requirements.txt # Python dependencies
├── README.md # Project overview


from ultralytics import YOLO
import cv2
import math

class RealTime:
    def __init__(self):
        self.class_names = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
                            "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
                            "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack",
                            "umbrella", "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball",
                            "kite", "baseball bat", "baseball glove", "skateboard", "surfboard", "tennis racket",
                            "bottle", "wine glass", "cup", "fork", "knife", "spoon", "bowl", "banana", "apple",
                            "sandwich", "orange", "broccoli", "carrot", "hot dog", "pizza", "donut", "cake", "chair",
                            "sofa", "pottedplant", "bed", "diningtable", "toilet", "tvmonitor", "laptop", "mouse",
                            "remote", "keyboard", "cell phone", "microwave", "oven", "toaster", "sink",
                            "refrigerator", "book", "clock", "vase", "scissors", "teddy bear", "hair drier",
                            "toothbrush"]
        self.model = YOLO('yolo-Weights/yolov8n.pt')

    def real_time_show(self):
        cap = cv2.VideoCapture(0)
        cap.set(3, 960)
        cap.set(4, 640)

        while True:
            ret, img = cap.read()
            # results = self.model(img, stream=True)

            if not ret:
                print("Error: Failed to capture frame")
                break

            try:
                results = self.model(img, stream=True)
            except Exception as e:
                print("Error processing frame with YOLO:", e)
                continue

            for r in results:
                boxes = r.boxes

                for box in boxes:
                    # bounding box
                    x1, y1, x2, y2 = box.xyxy[0]
                    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)  # convert to int values

                    # put box in cam
                    cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

                    # confidence
                    confidence = math.ceil((box.conf[0] * 100)) / 100
                    print("Confidence --->", confidence)

                    # class name
                    cls = int(box.cls[0])
                    print("Class name -->", self.class_names[cls])

                    # object details
                    org = [x1, y1]
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    fontScale = 1
                    color = (255, 0, 0)
                    thickness = 2

                    cv2.putText(img, self.class_names[cls], org, font, fontScale, color, thickness)

            cv2.imshow('Webcam', img)

            if cv2.waitKey(1) == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

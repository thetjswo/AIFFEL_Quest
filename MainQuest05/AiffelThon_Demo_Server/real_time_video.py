import numpy as np
import cv2

def showVideo():
    cap = cv2.VideoCapture(0)

    cap.set(3, 960)
    cap.set(4, 640)

    ret = cap.read()
    if not ret:
        print("Error: Failed to capture frame")
        # 프로그램 종료, 다른 프레임 소스 사용 등 옵션 고려
    else:
        while True:
            ret, frame = cap.read()

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow('video', gray)

            k = cv2.waitKey(1) & 0xff1
            if k == 27:
                break
        cap.release()
        cv2.destroyAllWindows()

# showVideo()

def writeVideo():
    cap = cv2.VideoCapture(0)

    cap.set(3, 960)
    cap.set(4, 480)

    fps = 20
    width = int(cap.get(3))
    height = int(cap.get(4))
    fcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')

    out = cv2.VideoWriter('./resource/video/DIVX.mp4', fcc, fps, (width, height))

    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame")
        # 프로그램 종료, 다른 프레임 소스 사용 등 옵션 고려
    else:
        while True:

            cv2.imshow('divx', frame)

            k = cv2.waitKey(1) & 0xff
            if k == 27:
                break

            cap.release()
            out.release()
            cv2.destroyAllWindows()

writeVideo()
import numpy as np
import cv2 as cv


def resizeVideo(src, dest, size):
    fourcc = cv.VideoWriter_fourcc(*'XVID')
    video = cv.VideoCapture(src, )
    writer = cv.VideoWriter(dest, fourcc, video.get(cv.CAP_PROP_FPS), size)
    while True:
        ret, frame = video.read()
        if (ret == True):
            n = cv.resize(frame, size, fx=0, fy=0, interpolation=cv.INTER_CUBIC)
            writer.write(n)
        else:
            break
    video.release()
    writer.release()
    cv.destroyAllWindows()


def bgSub(src):
    video = cv.VideoCapture(src)
    backSub = cv.createBackgroundSubtractorMOG2(23)
    kernel = np.ones((5, 5), np.uint8)
    while True:
        ret, frame = video.read()
        if frame is None:
            break
        frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        fgMask = backSub.apply(frame, learningRate= 0.05)
        cv.imshow('FG Mask', fgMask)
        key = cv.waitKey(16)
        if key == ord('q'):
            break
    cv.destroyAllWindows()
    exit()


def mybgSub(src = 0):
    print("start")
    video = cv.VideoCapture(src)

    (ret, first) = video.read()

    first_gray = cv.cvtColor(first, cv.COLOR_BGR2GRAY)
    while True:
        (ret, frame) = video.read()
        if not ret:
            break
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        different = cv.absdiff(gray, first_gray)
        first_gray = gray
        thresh = cv.threshold(different, 35, 255, cv.THRESH_BINARY)[1]
        # thresh = cv.dilate(thresh, None, iterations=2)
        cv.imshow("thesh", thresh)
        cv.imshow("Src", frame)
        key = cv.waitKey(16)
        if key == ord('q'):
            break
    video.release()
    cv.destroyAllWindows()

def MOG(src =0):
    pass



if __name__ == '__main__':
    src = r'./video/160410_46_LA_Motorway_5_1080p.mp4'
    motoway720 = r'./video/160410_46_LA_Motorway_5_720p.mp4'
    detroit720 = r'./video/160522_140_Detroit_TigersStadium7_720p.mp4'
    # mybgSub(motoway720)
    bgSub(motoway720)
    exit(0)

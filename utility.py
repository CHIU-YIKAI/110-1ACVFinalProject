import cv2


def SaveToVideo(bboxList, frames, fileName):
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(fileName, fourcc, 30.0, (1920,  1080))
    for i in bboxList:
        cv2.rectangle(frames[i[0]], i[1], i[2], i[3], 3)
    for frame in frames:
        out.write(frame)

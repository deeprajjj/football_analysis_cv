import cv2 

# function to read video and return all the frames(img ) of the video 
def read_video(videopath):
    cap = cv2.VideoCapture(videopath)
    frame = []


    """
    cap.read() ==> returns (boolean , <frame(img) in format of np_array>)
    """
    while True:
        ret , video_instance = cap.read() # reading next frame
        if not ret: # if no frame ==> video ended 
            break
        frame.append(video_instance)
    return frame 

def save_video(output_video_frames , output_video_path):
    if not output_video_frames:
        print("No frames to save ==> skipping video write.")
        return
    format = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_video_path,format,24,(output_video_frames[0].shape[1], output_video_frames[0].shape[0]))

    for frame in output_video_frames:
        out.write(frame)
    print("succesfully saved video to output folder ")
    out.release()
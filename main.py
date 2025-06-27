from util.video_util import read_video, save_video
from trackers import Tracker
def main():
    # reading video and collecting frames 
    path = 'input_videos/08fd33_4.mp4'
    video_frame = read_video(path)

    # instance of Tracker class 
    tracker = Tracker('models/best.pt')
    tracks = tracker.get_object_tracks(video_frame)
    # making a video from frames collected 
    path_to_save = "output_videos/"
    save_video(video_frame,path_to_save+'output_video.avi')
    print("ello")

if __name__ == '__main__':
    main()
from ultralytics import YOLO
import supervision as sv
class Tracker : 
    def __init__(self,model_path):
        self.model = YOLO(model_path)

    def detect_frame(self, frames):
        batch_size = 20 
        detection = []
        for i in range(0,len(frames),batch_size):
            detection_batch = self.model.predict(frames[i:i+batch_size],conf=0.1)
            detection +=detection_batch
            # detection = self.model.predict(frames)
            break
        return detection

    def get_object_tracks(self , frames):
        detections = self.detect_frame(frames)

        # tracks = {'string' : []}
        tracks = {
            "players":[],
            "referees":[],
            "ball":[]
        }


        # to overwrite goalkeeper as player since no goli stats needed and do the tracking 
        for frame_num , detections in enumerate(detections):
            # to find out {index:classification}
            class_name = detections.names
            # just for ease or kinda formating {classification : index}
            inv_class_name = {v:k for k,v in class_name.items()}
            detection_sv = sv.Detections.from_ultralytics(detections)

            for object_ind , class_id in enumerate(detection_sv.class_id):
                if class_name[class_id] == "goalkeeper":
                    detection_sv.class_id[object_ind] = inv_class_name["player"]

            # now this one will actually assign a id to each bounding frame and track it in various iterations 
            # so basically it will add one one list where [a,b,c....] where a = id of the boudunding box which is at dect[0] index
            detection_with_tracks = self.tracker.update_with_detections(detection_sv)

            tracks["players"].append({}) # track.player = [{},{}] ==> so now its a dict of list with dict 
            tracks["referees"].append({})
            tracks["ball"].append({})


            for frame_detection in detection_with_tracks: 
                #det_with_track = [[xyxy], "mask",[confidence], [class id ],[bbox id ]
                bbox = frame_detection[0].tolist()
                cls_id = frame_detection[3]
                track_id = frame_detection[4]

                if cls_id == inv_class_name['player']:
                    tracks["players"][frame_num][track_id] = {"bbox":bbox}
                
                if cls_id == inv_class_name['referee']:
                    tracks["referees"][frame_num][track_id] = {"bbox":bbox}
            
            for frame_detection in detection_sv:
                bbox = frame_detection[0].tolist()
                cls_id = frame_detection[3]

                if cls_id == inv_class_name['ball']:
                    tracks["ball"][frame_num][1] = {"bbox":bbox}


            print('this is ultralytivs output in sv.detection format for the fist 20 frames ')
            print(detection_sv)
            break
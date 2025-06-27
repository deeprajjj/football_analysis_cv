from ultralytics import YOLO # to import 

# to load  kinda creating instace of model with all its functionality
model = YOLO('models/best.pt')

res = model.predict('input_videos/08fd33_4.mp4',save=True)

print(res[0])
print('===================')
i = 0 
for box in res[0].boxes:
    print (i)
    i+=1
    print(box)


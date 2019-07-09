import cv2
import os
from mtcnn.mtcnn import MTCNN
# go to directory
# obama, donal trump, billgates, stevejobs, mark zukebeg, caption american
# read each video and save about 200 frame which is 40 for test, 160 for train
# save each image in path: /dataset/train/obama/
                          # /dataset/test/obama


def make_dataset(video_path,train_path,test_path):
	cap = cv2.VideoCapture(video_path)
	count_frame = 0
	cap.set(cv2.CAP_PROP_FPS, 60)
	# detector = MTCNN()
	while(True):
	    # Capture frame-by-frame
	    ret, frame = cap.read()
	    # result = detector.detect_faces(frame)
	    # Our operations on the frame come here
	    # for person in result:
	    #   bounding_box = person['box']
	    #   cv2.rectangle(frame,
	    #                 (bounding_box[0], bounding_box[1]),
	    #                 (bounding_box[0]+bounding_box[2], bounding_box[1] + bounding_box[3]),
	    #                 (0,155,255),
	    #                 2)
	    # print ("w:%s h:%s"%(bounding_box[2],bounding_box[3]))
	    # Display the resulting frame
	    if ret == True:
	    	cv2.imshow('frame',frame)
	    	if cv2.waitKey(1) & 0xFF == ord('q'):
	        	break
	# When everything done, release the capture
	cap.release()
	cv2.destroyAllWindows()





train_path = "./dataset/train"
test_path = "./dataset/test"


if not os.path.isdir("dataset"):
	os.mkdir("dataset")

if not os.path.isdir(train_path):
	os.mkdir(train_path)

if not os.path.isdir(test_path):
	os.mkdir(test_path)

for video_name in os.listdir("./video"):
	video_path = "./video/" + video_name
	if "barrack_obama" in video_name :
		make_dataset(video_path,train_path,test_path)
	elif "steve_jobs"  in video_name :
		make_dataset(video_path,train_path,test_path)
	elif "bill_gates" in video_name :
		make_dataset(video_path,train_path,test_path)
	elif "mark_zukerbeg" in video_name : 
		make_dataset(video_path,train_path,test_path)


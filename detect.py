# USAGE
# python detect.py --conf config/config.json

# import the necessary packages
from __future__ import print_function
from pyimagesearch.notifications import TwilioNotifier
from pyimagesearch.utils import Conf
from imutils.video import VideoStream
from imutils.io import TempFile
from datetime import datetime, date
import numpy as np
import argparse
import imutils
import signal
import time
import cv2
import sys

# function to handle keyboard interrupt
def signal_handler(sig, frame):
	print("[INFO] You pressed `ctrl + c`! Closing mail detector" \
		" application...")
	sys.exit(0)

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-c", "--conf", required=True,
	help="Path to the input configuration file")
args = vars(ap.parse_args())

# load the configuration file and initialize the Twilio notifier
conf = Conf(args["conf"])
tn = TwilioNotifier(conf)

# initialize the flags for luna found and notification sent
lunaFound = False
notifSent = False

# initialize the video stream and allow the camera sensor to warmup
print("[INFO] warming up camera...")
vs = VideoStream(usePiCamera=True).start()
time.sleep(2.0)

# signal trap to handle keyboard interrupt
signal.signal(signal.SIGINT, signal_handler)
print("[INFO] Press `ctrl + c` to exit, or 'q' to quit if you have" \
	" the display option on...")

# initialize the video writer and the frame dimensions
writer = None
W = None
H = None

# loop over the frames of the stream
while True:
	# grab the next frame from the stream
	frame = vs.read()
	lunaPrevFound = lunaFound

	# quit if there was a problem grabbing a frame
	if frame is None:
		break

	# resize the frame and convert the frame to grayscale
	frame = imutils.resize(frame, width=200)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# if the frame dimensions are empty, set them
	if W is None or H is None:
		(H, W) = frame.shape[:2]

	# calculate the average of all pixels where a higher mean
	# indicates that there is more light coming into the refrigerator
	mean = np.mean(gray)

	# determine if luna is currently in frame
	lunaFound = mean > 50

	# if the luna is in frame and previously she was not, it means
	# the luna has just been spotted
	if lunaFound and not lunaPrevFound:
		# record the start time
		startTime = datetime.now()

		# create a temporary video file and initialize the video
		# writer object
		tempVideo = TempFile(ext=".mp4", basePath="./temp_videos")
		
		fourcc = cv2.VideoWriter_fourcc(*"mp4v")
		writer = cv2.VideoWriter(tempVideo.path, fourcc, 10, (W, H),
			True)

	# if Luna was in frame but has suddenly left the frame
	elif lunaPrevFound and not lunaFound:
		# calculate the time different between the current time and
		# start time
		timeDiff = (datetime.now() - startTime).seconds

		# if a notification has already been sent, then just set
		# the notifSent to false for the next iteration
		if notifSent:
			notifSent = False

		# if a notification has not been sent, then send a
		# notification
		else:
			# record the end time and calculate the total time in
			# seconds
			endTime = datetime.now()
			totalSeconds = (endTime - startTime).seconds

			# build the message and send a notification
			msg = "Luna was spotted at {} for {} " \
				"seconds.".format(
				startTime.strftime("%I:%M%p"), totalSeconds)

			# release the video writer pointer and reset the
			# writer object
			writer.release()
			writer = None

			# send the message and the video to the owner
			tn.send(msg, tempVideo)

	# check to see if we should write the frame to disk
	if writer is not None:
		writer.write(frame)

# check to see if we need to release the video writer pointer
if writer is not None:
	writer.release()

# cleanup the camera and close any open windows
cv2.destroyAllWindows()
vs.stop()
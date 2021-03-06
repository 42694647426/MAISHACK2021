# Original source: Adrian Rosebrock, Pyimagesearch blog owner 

# USAGE
# python classify.py --images ../small_dataset/train 

# import the necessary packages
from __future__ import print_function
from pyimagesearch.descriptors import RGBHistogram
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import sklearn
from imutils import paths
import numpy as np
import argparse
import cv2

# handle previous versions of sklearn which use the cross_validation module
if int((sklearn.__version__).split(".")[1]) < 18:
	from sklearn.cross_validation import train_test_split

# otherwise, if sklearn version is > 0.18, use the model_selection module
else:
	from sklearn.model_selection import train_test_split

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", required=True, help="path to the image dataset")
#ap.add_argument("-m", "--masks", required=False, help="path to the image masks")
args = vars(ap.parse_args())

# grab the image and mask paths
imagePaths = sorted(list(paths.list_images(args["images"])))
print(imagePaths)
#maskPaths = sorted(list(paths.list_images(args["masks"])))

# initialize the list of data and class label targets
data = []
target = []

# initialize the image descriptor
desc = RGBHistogram([8, 8, 8])

# loop over the image and mask paths
for imagePath in imagePaths:
	# load the image and mask
	image = cv2.imread(imagePath)
	#mask = cv2.imread(maskPath)
	#mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)

	# describe the image
	features = desc.describe(image)

	# update the list of data and targets
	data.append(features)
	target.append(imagePath.split("\\")[-2])

# grab the unique target names and encode the labels
targetNames = np.unique(target)
le = LabelEncoder()
target = le.fit_transform(target)

# construct the training and testing splits
(trainData, testData, trainTarget, testTarget) = train_test_split(data, target,
	test_size=0.3, random_state=42)

# train the classifier
model = RandomForestClassifier(n_estimators=25, random_state=84)
model.fit(trainData, trainTarget)

# save the model
from joblib import dump, load
dump(model, 'RF_model.joblib')

# evaluate the classifier
print(classification_report(testTarget, model.predict(testData),
	target_names = targetNames))

# loop over a sample of the images
for i in np.random.choice(np.arange(0, len(imagePaths)), 10):
	# grab the image
	imagePath = imagePaths[i]
	#maskPath = maskPaths[i]

	# load the image and mask
	image = cv2.imread(imagePath)
	#mask = cv2.imread(maskPath)
	#mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)

	# describe the image
	features = desc.describe(image)

	# predict what type of flower the image is
	flower = le.inverse_transform(model.predict(features.reshape(1, -1)))[0]
	print("[INFO] prediction: {}, path: {}".format(flower.upper(), imagePath))
	cv2.imshow("image", image)
	cv2.waitKey(100)

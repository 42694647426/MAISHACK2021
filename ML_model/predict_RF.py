from joblib import dump, load
from keras.preprocessing import image
from pyimagesearch.descriptors import RGBHistogram
from sklearn.preprocessing import LabelEncoder
import numpy as np
import matplotlib.pyplot as plt
import os

# filepath = './ML_model/saved_model/VGG16_2.h5'
filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'saved_model/RF_model.joblib')

# Load the RF model
model = load(filepath)

def load_image(img_path, show=False):

    img = image.load_img(img_path, target_size=(128, 128))
    img_tensor = image.img_to_array(img)                    # (height, width, channels)
    #img_tensor = np.expand_dims(img_tensor, axis=0)         # (1, height, width, channels), add a dimension because the model expects this shape: (batch_size, height, width, channels)
    #img_tensor /= 255.                                      # imshow expects values in the range [0, 1]


    if show:
        plt.imshow(img_tensor[0])
        plt.axis('off')
        plt.show()

    return img_tensor



if __name__ == '__main__':
    img_path = 'test.jpg'
    new_image = load_image(img_path)

    # check prediction
    # describe the image
	features = desc.describe(new_image)
    # predict what type of flower the image is
	prediction = le.inverse_transform(model.predict(features.reshape(1, -1)))[0]
    print("[INFO] prediction: {}, path: {}".format(prediction.upper(), img_path))
    #pred = model.predict(new_image)
    print(prediction)

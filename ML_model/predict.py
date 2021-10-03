from keras.models import load_model
from keras.preprocessing import image
import numpy as np
import matplotlib.pyplot as plt
import os

# filepath = './ML_model/saved_model/VGG16_2.h5'
filepath = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), 'saved_model/VGG16_2.h5')
# Load the model
model = load_model(filepath, compile=True)


def load_image(img_path, show=False):

    img = image.load_img(img_path, target_size=(128, 128))
    # (height, width, channels)
    img_tensor = image.img_to_array(img)
    # (1, height, width, channels), add a dimension because the model expects this shape: (batch_size, height, width, channels)
    img_tensor = np.expand_dims(img_tensor, axis=0)
    # imshow expects values in the range [0, 1]
    img_tensor /= 255.

    if show:
        plt.imshow(img_tensor[0])
        plt.axis('off')
        plt.show()

    return img_tensor


if __name__ == '__main__':
    img_path = 'test.jpg'
    new_image = load_image(img_path)
    # check prediction
    pred = model.predict(new_image)
    print(pred)

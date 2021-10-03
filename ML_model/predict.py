from keras.models import load_model
from keras.preprocessing import image
import numpy as np
import matplotlib.pyplot as plt
import os

CLASSES = ['alfalfa', 'allium', 'borage', 'calendula', 'chicory', 'chive_blossom', 
                    'common_mallow', 'coneflower', 'cowslip', 'daffodil', 
                    'garlic_mustard', 'geranium', 'henbit', 'mullein', 'red_clover']



def load_image(img_path, show=False):

    img = image.load_img(img_path, target_size=(128, 128))
    img_tensor = image.img_to_array(img)                    # (height, width, channels)
    img_tensor = np.expand_dims(img_tensor, axis=0)         # (1, height, width, channels), add a dimension because the model expects this shape: (batch_size, height, width, channels)
    img_tensor /= 255.                                      # imshow expects values in the range [0, 1]

    if show:
        plt.imshow(img_tensor[0])                           
        plt.axis('off')
        plt.show()

    return img_tensor

def predict(img_path: str):
    # filepath = './ML_model/saved_model/VGG16_2.h5'
    filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'saved_model/VGG16_2.h5')
    # Load the model
    model = load_model(filepath, compile = True)
    img_path = 'ML_model/photo-1604085572504-a392ddf0d86a.jpg'
    new_image = load_image(img_path)
    # check prediction
    pred = model.predict(new_image)
    return CLASSES[np.argmax(pred)]
    


if __name__ == '__main__':
    print(predict('ML_model/photo-1604085572504-a392ddf0d86a.jpg'))
    
    
    

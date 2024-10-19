import numpy as np
from keras.preprocessing import image

test_image = image.load_img('fruits_360/realtime_images/image1.jpeg', target_size = (256,256))

test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
result = cnn.predict(test_image)

for i in range(0,132):
    if (result[0][0] == i):       # == 1
        prediction = class_labels[i]



print(prediction)
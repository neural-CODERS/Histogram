from skimage import io
import matplotlib.pyplot as plt
image = io.imread('color.png')

img = plt.hist(image.ravel(), bins = 256, color = 'orange', )
img = plt.hist(image[:, :, 0].ravel(), bins = 256, color = 'red', alpha = 0.5)
img = plt.hist(image[:, :, 1].ravel(), bins = 256, color = 'Green', alpha = 0.5)
img = plt.hist(image[:, :, 2].ravel(), bins = 256, color = 'Blue', alpha = 0.5)
img = plt.xlabel('Intensity Value')
img = plt.ylabel('Count')
img = plt.legend(['Total', 'Red_Channel', 'Green_Channel', 'Blue_Channel'])
plt.show()

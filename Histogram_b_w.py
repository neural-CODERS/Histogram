from skimage import io
import matplotlib.pyplot as plt
image = io.imread('black_and_white.png')
ax = plt.hist(image.ravel(), bins = 256)
plt.show()

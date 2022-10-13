# from PIL import Image, ImageOps
# import matplotlib.image as mpimg
# from matplotlib import pyplot as plt
# import numpy as np


# img = mpimg.imread('cat.jpeg')
# print("RGB Of original image \n", img)
# # img1 = plt.imread('cat.jpeg')[:,:,:3]
# # print("RGB of given image is: \n", img1)

# # cat_with_border = ImageOps.expand(img, border=20, fill='black')
# cat_with_border = np.pad(img, pad_width=20, mode='constant', constant_values=12)
# mpimg.imsave('cat_with_border.jpeg', cat_with_border)
# img1 = mpimg.imread('cat-with-border.jpeg', 3)
# print("RGB of given image is: \n", img1)


# cat_with_border = np.pad(img, pad_width=20, mode='constant', constant_values=12)
# # mpimg.imsave('cat_with_border.jpeg', cat_with_border)
# # mpimg.imsave("cat_with_border.jpeg", cat_with_border)
# fig = plt.savefig("cat_with_border.jpeg", bbox_inches='tight')
# print(cat_with_border)


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

img = plt.imread("cat.jpeg")

def add_borders(image_sample, border_len=20):
  img_cpy = image_sample.copy()
  img_cpy = np.hstack((np.zeros((img_cpy.shape[0], border_len, 3), dtype="int8"), img_cpy))
  img_cpy = np.vstack((img_cpy, np.zeros((border_len, img_cpy.shape[1], 3), dtype="int8")))
  img_cpy = np.vstack((np.zeros((border_len, img_cpy.shape[1], 3), dtype="int8"), img_cpy))
  img_cpy = np.hstack((img_cpy, np.zeros((img_cpy.shape[0], border_len, 3), dtype="int8")))
  return img_cpy

border_img = add_borders(img)
res_img = border_img.reshape(-1, 3)
res_df = pd.DataFrame(columns=["c1", "c2", "c3"])
res_df["c1"] = res_img[:, 0]
res_df["c2"] = res_img[:, 1]
res_df["c3"] = res_img[:, 2]
res_df.to_csv('try1.csv',index=False)
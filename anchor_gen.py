import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from generate_anchors import generate_anchors

featureMap_size = (5, 5)
ratios = [0.5, 1, 2]
scales = [0.5, 1, 2]
base_size = 2  # 感知野的大小 base_size * base_size
base_anchors = generate_anchors(base_size, ratios, scales)
print(base_anchors)
shift_x = np.arange(featureMap_size[0]) * base_size
shift_y = np.arange(featureMap_size[1]) * base_size
shift_x, shift_y = np.meshgrid(shift_x, shift_y)
shifts = np.vstack((shift_x.ravel(), shift_y.ravel(),
                    shift_x.ravel(), shift_y.ravel())).transpose()

anchors_num = base_anchors.shape[0]
A = anchors_num
K = shifts.shape[0]
all_anchors = (base_anchors.reshape((1, A, 4)) +
               shifts.reshape((1, K, 4)).transpose((1, 0, 2)))
all_anchors = all_anchors.reshape((K * A, 4))

# plt.figure(figsize=(10, 10))
img = np.ones((10, 10, 3))
plt.imshow(img, extent=(0, 10, 10, 0))
axs = plt.gca()  # get current axies
for i in range(0, all_anchors.shape[0]):
    box = all_anchors[i]
    rec = patches.Rectangle((box[0], box[1]), box[2] - box[0] + 1, box[3] - box[1] + 1, edgecolor='r', facecolor='none')
    axs.add_patch(rec)

plt.show()

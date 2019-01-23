import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

featureMap_size = (5, 5)  # 如今feature_map的大小为5*5
ratios = [1]  # anchor的宽高比为1:1
scales = [1, 1.96]  # anchor的面积比1:1.96
rpn_stride = 2  # 感知野的大小 4 = 2*2

base_anchors = np.array([[0, 0, 2, 2], [-0.4, -0.4, 2.4, 2.4]])
shift_x = np.arange(featureMap_size[0]) * rpn_stride
shift_y = np.arange(featureMap_size[1]) * rpn_stride
shift_x, shift_y = np.meshgrid(shift_x, shift_y)
shifts = np.vstack((shift_x.ravel(), shift_y.ravel(),
                    shift_x.ravel(), shift_y.ravel())).transpose()

anchors_num = base_anchors.shape[0]
A = anchors_num
K = shifts.shape[0]
tmp = shifts.reshape((1, K, 4))
all_anchors = (base_anchors.reshape((1, A, 4)) +
               shifts.reshape((1, K, 4)).transpose((1, 0, 2)))
all_anchors = all_anchors.reshape((K * A, 4))
print(all_anchors)

# plt.figure(figsize=(10,10))
img = np.ones((10,10,3))
plt.imshow(img)
axs = plt.gca() # get current axies
for i in range(0,4):
    box = all_anchors[i]
    rec = patches.Rectangle((box[0],box[1]),box[2]-box[0],box[3]-box[1],edgecolor='r',facecolor='none')
    axs.add_patch(rec)

plt.show()

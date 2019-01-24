# --------------------------------------------------------
# 根据ratios，scales和感知野的大小，生成base anchors
# 参考Ross Girshick
# --------------------------------------------------------

import numpy as np

def generate_anchors(base_size=16, ratios=[0.5, 1, 2],
                     scales=[8, 16, 32]):

    base_anchor = np.array([1, 1, base_size, base_size]) - 1
    ratio_anchors = _ratio_enum(base_anchor, ratios)
    print(ratio_anchors)
    anchors = None
    for i in range(len(scales)):
        if anchors is None:
            anchors = ratio_anchors * scales[i]
        else:
            anchors = np.vstack((anchors, ratio_anchors * scales[i]))
    w, h, x_ctr, y_ctr = _whctrs(base_anchor)
    anchors = _mkanchors(anchors[:, 0], anchors[:, 1], x_ctr, y_ctr)
    return anchors


def _whctrs(anchor):
    # 给出anchor 左上及右下坐标点，返回中心点及宽和高
    w = anchor[2] - anchor[0] + 1
    h = anchor[3] - anchor[1] + 1
    x_ctr = anchor[0] + 0.5 * (w - 1)
    y_ctr = anchor[1] + 0.5 * (h - 1)
    return w, h, x_ctr, y_ctr

def _mkanchors(ws, hs, x_ctr, y_ctr):
    ws = ws[:, np.newaxis]
    hs = hs[:, np.newaxis]
    anchors = np.hstack((x_ctr - 0.5 * (ws - 1),
                         y_ctr - 0.5 * (hs - 1),
                         x_ctr + 0.5 * (ws - 1),
                         y_ctr + 0.5 * (hs - 1)))
    return anchors

def _ratio_enum(anchor, ratios):
    # 计算面积为感知野的大小时，宽高应是多少
    w, h, x_ctr, y_ctr = _whctrs(anchor)
    size = w * h
    size_ratios = size / ratios
    ws = np.round(np.sqrt(size_ratios))
    hs = np.round(ws * ratios)
    ws = ws[:, np.newaxis]
    hs = hs[:, np.newaxis]
    ratios_anchors = np.hstack((ws, hs))
    return ratios_anchors

if __name__ == '__main__':
    a = generate_anchors()

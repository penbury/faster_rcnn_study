# --------------------------------------------------------
# 根据ratios，scales和感知野的大小，生成base anchors
# 参考Ross Girshick
# --------------------------------------------------------

import numpy as np


def generate_anchors(base_size=2, ratios=[1, 2],
                     scales=[1, 2, 4]):
    # base_size 感知野的大小
    # ratios 宽高比为1,2
    # scales 面积分别为1*4,2*4,4*4
    base_anchor = np.array([1, 1, base_size, base_size]) - 1 #[0,0,1,1]
    w,h,x_ctr,y_ctr = _whctrs(base_anchor) # 2,2,0.5,0.5
    ratio_anchors = _ratio_enum(base_anchor, ratios)
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
    # 获取中心点坐标及宽高 此处为(0.5,0.5) 宽=高=2
    w, h, x_ctr, y_ctr = _whctrs(anchor)
    size = w * h
    size_ratios = size / ratios
    ws = np.round(np.sqrt(size_ratios))
    hs = np.round(ws * ratios)
    anchors = _mkanchors(ws, hs, x_ctr, y_ctr)
    return anchors


def _scale_enum(anchor, scales):
    """
    Enumerate a set of anchors for each scale wrt an anchor.
    """

    w, h, x_ctr, y_ctr = _whctrs(anchor)
    ws = w * scales
    hs = h * scales
    anchors = _mkanchors(ws, hs, x_ctr, y_ctr)
    return anchors


if __name__ == '__main__':
    import time

    t = time.time()
    a = generate_anchors()
    print(time.time() - t)
    print(a)
    from IPython import embed;

    embed()

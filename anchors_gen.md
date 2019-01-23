学习faster rcnn项目，generate_anchors之后，希望自己可以动手简单的实现下，于是便有了如下的假设：在一张10 * 10的图片上，经过filter = 2 * 2，stride = 2的池化，生成一张5 * 5的feature map。在feature map上生成ratios=[1,2],scales=[1,4]的anchors，应如何实现？并展示出来？

首先，因为经过了2 * 2 的池化，feature map上的1个像素点相当于是原图上的4个像素点，也就是感知野的大小为2 * 2 = 4。如下图：

![1548235644872](C:\Users\Admin\AppData\Roaming\Typora\typora-user-images\1548235644872.png)

可以认为feature map上第(0,0)个像素点对应原图中(0,0),(0,1),(1,0),(1,1)四个像素点。即feature map上第(0,0)个像素点对应原图中(0,0,1,1)------左上及右下坐标点，面积为4，宽高比为1:1，宽=2，高=2。

而ratios=[1,2],是希望生成的anchors的宽高比为1:1,1:2两种；

scales=[1,2,4],是希望生成的anchors的面积为感知野面积的1倍、2倍和4倍三种，即面积分别为4,8,16。

我们已知ratio=1(宽高比为1:1)，scale=1(面积为4)，对应的anchor为(0,0,1,1),那么，如何求出不同ratios和scales的其他anchor呢？

![1548236765262](C:\Users\Admin\AppData\Roaming\Typora\typora-user-images\1548236765262.png)





我们首先算出feature map上(0,0)点对应的anchors，再通过一系列矩阵变换算出整张feature map对应的anchors。






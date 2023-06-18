---
relevant:
  - ./digital-signal-processing.md
  - ./signals-and-systems.md
---

# 数字图像处理

## §1–§2 基础

### 成像方式

> :material-clock-edit-outline: 2023年6月13日。

- 电磁波

  |   波段    | 波长下限 |        特点        |                   应用                    |
  | :-------: | :------: | :----------------: | :---------------------------------------: |
  | 宇宙线、γ |    –     |   穿透，破坏生命   | 天文、PET（positron emission tomography） |
  |     X     | 0.01 nm  |      （同上）      |    CT（computed tomography）、血管造影    |
  |   紫外    |  10 nm   |     化学、荧光     |                细胞、印刷                 |
  |  可见光   |  380 nm  |    反射成像居多    |                  最广泛                   |
  |   红外    |  760 nm  |       热效应       |                   夜视                    |
  |   微波    |   1 mm   | 绕射强，穿冠、冰层 |                   遥感                    |
  |  无线电   |   1 m    |                    |     MRI（magnetic resonance imaging）     |

- 声波、超声波

- 物质波：电子

- 合成

### 视觉

> :material-clock-edit-outline: 2023年6月13日。

|  细胞   | 数量  | 功能  |
| :-----: | :---: | :---: |
| 锥 cone | 700万 |  色   |
| 杆 rod  |  亿   |  亮   |

“感觉亮度”并非与光强一一对应，还与背景照明（两种细胞）、周围光强（马赫带）、形状（心理）等有关。

## §3 空间域

### 点处理

> :material-clock-edit-outline: 2023年6月13日。

又名灰度变换。这些变换根据原灰度 ↦ 新灰度命名。

- **反转**

- **对数**

  扩展暗部，压缩亮部。

- **幂次**

  改变亮度或颜色比例。

  $γ > 1$ 压缩暗部，扩展亮部；$γ < 1$ 反之。

  CRT 天然 $γ > 1$，需补偿。

- **分段线性**

  拉伸对比度或灰度切分。

由此引出灰度直方图，可用于评估成像条件（动态范围）、增强图像（<u>直方图均衡化</u>）、分割图像、压缩图像（统计编码）。

### 空间滤波

> :material-clock-edit-outline: 2023年6月18日。

用空间子图像掩模增强图像，邻域处理。

- 平滑：加权均值（模糊扩散），统计排序（不会模糊图像）。
- 锐化：一阶微分（梯度模，斜坡），二阶微分（Laplacian，点、线），

## §4 频率域

### 多维 DFT

> :material-clock-edit-outline: 2023年6月18日。
>
> :material-eye-arrow-right: [Discrete Fourier transform - Wikipedia](https://en.wikipedia.org/w/index.php?title=Discrete_Fourier_transform&oldid=1153873152#Multidimensional_DFT)。

$$
\begin{aligned}
  X_\vb*{k} &= \sum_{\vb*n} e^{-2 \pi j \times \vb*{k} \vdot \frac{\vb*n}{\vb*N}} x_\vb*{n}. \\
  x_\vb*{n} &= \frac{1}{\prod \vb*{N}} \sum_{\vb*n} e^{2 \pi j \times \vb*{k} \vdot \frac{\vb*n}{\vb*N}} x_\vb*{k}. \\
\end{aligned}
$$

(The division is element-wise.)

The multidimensional DFT expresses the input as a superposition of plane waves, or multidimensional sinusoids. It can be computed by the composition of a sequence of one-dimensional DFTs along each dimension. 

时域因变量共轭对应频域两次因变量共轭、自变量反转，两次共轭抵消了。

频谱因变量中，相位反映图像空间特征内容，幅度反映灰度；自变量中，直流对应平均，低频对应缓变，高频对应边缘和突变。关于方向性，请参考单缝衍射。

### 滤波

> :material-clock-edit-outline: 2023年6月18日。

基本步骤如下。

1. 时域补零，然后实现频域中心化。
2. 正变换。
3. 乘滤波器。
4. 反变换。
5. 时域取结果实部，恢复频域中心化，丢弃之前补零多的部分。

## §5 复原与重建

## §6 彩色

## §8 压缩

## §9 形态学处理

## §10 分割

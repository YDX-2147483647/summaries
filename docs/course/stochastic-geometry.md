---
relevant:
  - ./stochastic-signal-processing.md
---

# Stochastic Geometry


!!! info "课程名称"

    本课完整名称如下。

    - 概率、随机过程和随机几何及其应用
    - Probability, Random Process and Stochastic Geometry in Engineering

## Filters

### Matched filter

> :material-clock-edit-outline: 2024年10月16日。
>
> :material-eye-arrow-right: [“数字通信原理”同名小节](./digital-communication.md#匹配滤波形式)。这里更一般。

- 模型：可能存在的已知信号为 $v$。接收到 $v + x$ 或 $x$，其中 $x$ 是平稳噪声。将它输入滤波器。
- 目标：最大化信噪比。（根据滤波器输出检测信号有无或判断信号种类）

设滤波器的传输函数为 $h$，则输出中

- 信号频谱密度：$HV$。（量纲：`[幅度]/[频率]`）
- 噪声功率谱密度：$S_X \abs{H}^2$。（量纲：`[幅度平方]/[频率]`）

瞬时信噪比

$$
\begin{split}
r
&= \frac {\eval{\abs{v_\text{output}}^2}_{t_0}} {\int S_X \abs{H}^2 \dd{f}} \\
&= \frac {\qty(H^*,\ V e^{j\omega t_0})^2}
  {\qty(H \sqrt{S_X}, H \sqrt{S_X})}
    \qq{(inverse Fourier transform)} \\
&= \frac {\qty(H^* \sqrt{S_X},\ V e^{j\omega t_0} / \sqrt{S_X})^2}
  {\qty(H^* \sqrt{S_X}, H^* \sqrt{S_X})} \\
&\leq \qty(\frac{V e^{j\omega t_0}}{\sqrt{S_X}},\ \frac{V e^{j\omega t_0}}{\sqrt{S_X}})^2
  \qq{(Cauchy–Schwarz inequality)} \\
&= \qty(\frac{V}{\sqrt{S_X}},\ \frac{V}{\sqrt{S_X}})^2. \\
\end{split}
$$

!!! note "记号"

    $(x,y) = \int x^* y \dd{f}$ 是内积。

取等条件是 $H^* \sqrt{S_X} \parallel V e^{j\omega t_0} / \sqrt{S_X}$，即

$$
H \parallel \frac{V^* e^{-j\omega t_0}} {\sqrt{S_X}}.
$$

### Wiener Filter

> :material-clock-edit-outline: 2024年10月17日。

- 模型：存在未知平稳信号 $V$，接收到 $U = V + X$，其中 $X$ 是平稳噪声。将它输入滤波器。
- 目标：最小化均方误差。（从滤波器输出估计原信号）

设最优滤波器输出 $\hat{V}$，把它与任意滤波器的输出 $\tilde{V}$ 比较。以互相关为内积 $(\cdot, \cdot)$，则目标等价于 $\forall \tilde{V}, (\hat{V} - V, \hat{V} - V) \leq (\tilde{V} - V, \tilde{V} - V)$。（这里 $V, \hat{V}, \tilde{V}$ 是同一时刻的。）

!!! info "任意时刻还是时间平均？"

    按原始定义，均方误差是时间的函数，并不能比大小，更不用说最小化了。

    一般有两种解决方案，一是要求任意时刻都最小，不过这样未必存在最小的；二是用时间平均度量大小，最小化这一个数。

    这里都处理平稳信号，均方误差是常函数，两种方案殊途同归。

从线性空间几何上考虑，若 $\hat{V}$ 是 $V$ 到子空间 $\{\tilde{V}\}$ 的垂足，即 $\forall \tilde{V}, (\hat{V} - V) \perp \tilde{V}$，则满足要求。这称作 orthogonality principle。

注意 $\tilde{V}$ 从 $U$ 滤波而来，总是各时刻 $U$ 的线性组合，所以其实可排除仅用于比较的任意滤波器，直接要求 $\forall t', (\hat{V} - V) \perp U_{t'}$ 就够了。（这里 $V, \hat{V}$ 的时刻仍相同，但未必与 $U$ 一致。）回归互相关的形式，$(\hat{V} - V) \perp U_{t'} \iff (\hat{V}, U_{t'}) \equiv (V, U_{t'}) \iff R_{\hat{V} U} \equiv R_{V U} \iff S_{\hat{V} U} \equiv S_{V U}$。

现在从中解出滤波器的传递函数 $H$。由 $U \overset{h}{\rightarrow} \hat{V}$ 可知 $S_{\hat{V} U} = H S_u$，再结合 $U = V + X$ 可得

$$
H = \frac{S_{V U}}{S_U}
= \frac{S_V + S_{V X}}{S_V + S_X + 2 S_{V X}}.
$$

!!! tip "相关中时间差的定义"

    本课中 $R_{X Y}$ 的自变量是 $X$ 对应时刻减 $Y$ 对应时刻，与[随机信号分析](./stochastic-signal-processing.md)相反。

不过此滤波器不能保证因果。（以下才是 Wiener 的主要工作。）若希望局限于因果滤波器，则前述要求 $(\hat{V} - V) \perp U_{t'}$ 可放宽，只谈 $U$ 的时刻不超过 $\hat{V}$ 的时刻这种情形，不谈其它破坏因果性的情形。这样列出的互相关在半无界区域上的积分方程（$R_{V U}\ u \equiv R_{\hat{V} U} = R_U * h$，$h = h u$，其中 $u$ 是 Heaviside 阶跃）称作 Wiener–Hopf 方程。求解方法如下。

1. 用因果滤波器 $K$ 将 $U$ 白化为 $W$，简化问题。

    具体来说，$S_W = \abs{K}^2 S_U \equiv 1$，也可写作 $K = 1 / S^+_U$。（Wiener–Hopf factorization）

2. 针对 $W$ 设计因果滤波器 $H_0$。

    具体来说，$R_{V W} u \equiv R_{\hat{V} W} = R_W * h_0 = \delta * h_0 = h_0$，其中 $R_W = \delta$ 归功于上一步白化。此外，实际求解时还要代入 $S_{V W} = S_{V U} K^*$，即 $S_{V U} / S^-_U$。

3. 串联以上两步，得 $H = K H_0$。

    具体结果为 $H = 1 / S^+_U \times \operatorname{Causal~part~of} S_{V U} / S^-_U$。

---
relevant:
  - ./signals-and-systems.md
  - ./artificial-intelligence.md
---

# 智能多源感知

$$
\def\R{\mathbb{R}}
$$

## 1 雷达系统与信号模型

### Doppler 效应

> :material-clock-edit-outline: 2023年9月14日。

始终采用雷达参考系。

设 $t_\text{transmit}$ 到 $t'_\text{transmit}$ 发射，$t_\text{receive}$ 到 $t'_\text{receive}$ 接收到回波。

!!! note "四个时刻，两种增量"

    四个时刻的先后顺序如下，注意 $t_r, t'_t$ 顺序不确定。

    ```mermaid
    flowchart LR
        t_t[t<sub>transmit</sub>]
        t_r[t<sub>receive</sub>]
        t_t_[t'<sub>transmit</sub>]
        t_r_[t'<sub>receive</sub>]

        t_t --> t_r -.-> t_r_
        t_t -.-> t_t_ --> t_r_
    ```

    可见这里有两种增量：起止（虚线）、收发（实线）。

    $$
    \begin{aligned}
      \Delta (\cdot) &\coloneqq (\cdot)' - (\cdot). \\
      \eval{(\cdot)}_t^r &\coloneqq (\cdot)_\text{receive} - (\cdot)_\text{transmit}. \\
    \end{aligned}
    $$

由物理过程，$2 r = c\eval{t}_t^r$，其中 $r$ 是目标反射这束光时的位置，即 $\frac{t_r + t_t}{2}$ 时刻的位置。考查起止增量：

$$
\frac{2 \Delta r}{c} = \Delta \qty(\eval{t}_t^r) = \eval{\qty(\Delta t)}_t^r.
$$

注意 $\eval{\qty(\Delta t)}_t^r \neq 0$ 正是 Doppler 效应——接收的光与发射的不同，它刚好反映 Doppler 效应对周期 $T$ 的影响。考查相对变化：

$$
\frac{\eval{T}_t^r}{T_t}
= \frac{\eval{\qty(\Delta t)}_t^r}{\Delta t_t}
= \frac{2}{c} \frac{\Delta r}{\Delta t_t}
\approx \frac{2}{c} v,
$$

其中 $v$ 是目标的速度。“$\approx$”是因为 $v$ 应当对应 $t_t$ 的起止增量，而 $\Delta r$ 对应 $\frac{t_r + t_t}{2}$ 的起止增量，多了 $\frac12 \Delta \eval{t}_t^r$。**走停假设**认为这可以忽略。

另外 $T$ 的偏移与频率 $f$ 的偏移紧密相关。$T f \equiv 1$，则 $\dd{f} / f = \dd \ln f = - \dd \ln T = - \dd{T} / T$。故 Doppler 效应不太显著（$v \ll c$）时，Doppler 频偏约等于

$$
- f \times \frac{2}{c}v = - \frac{2 v}{\lambda}.
$$

!!! note "只差相对论效应的严格版本"

    $\Delta r$ 对应时间与 $v$ 对应时间之比

    $$
    \frac{\Delta \eval{\frac{t_r + t_t}{2}}_t^r}{\Delta t_t}
    = \frac{\frac{\Delta r}{v}}{\frac{\Delta r}{v} - \frac{\Delta r}{c}}
    = \frac{1}{1 - \frac{v}{c}}.
    $$

    因此 Doppler 效应的周期相对变化

    $$
    \frac{\eval{T}_t^r}{T_t}
    = \frac{2v}{c} \times \frac{1}{1 - \frac{v}{c}}.
    $$

    再看第二处近似。由 $T f \equiv 1$，不用 $\dd \ln$ 近似，严格来说是

    $$
    \frac{\eval{f}_t^r}{f_t}
    = - \frac{\eval{T}_t^r / T_t}{1 + \eval{T}_t^r / T_t}
    = - \frac{2v}{c} \times \frac{1}{1 + \frac{v}{c}}.
    $$

    代入得

    $$
    \eval{f}_t^r
    = - \frac{2 v}{\lambda_t} \times \frac{1}{1 + \frac{v}{c}}.
    $$

    ——“走停”恐怕并不准确，这种近似只要求 $v \ll c$（从而 $\Delta r \approx v \Delta t$）和 $v$ 恒定，而与 $\Delta r \lesseqgtr \lambda$ 之类的无关。

## 3 距离分辨率和角分辨率

> :material-clock-edit-outline: 2022年3月17日。

我们讲了两种处理啁啾信号的方法——脉冲压缩、去斜。其中脉冲压缩是通用方法，去斜则只适用于啁啾信号。（两种方法的分辨率同量级，我感觉去斜更容易理解。）

### 脉冲压缩

“脉冲压缩”字面指这种处理方法的效果，让宽脉冲也能有窄脉冲的效果。（窄脉冲距离分辨率高；宽脉冲能量大，从而测距范围大）

具体实现就像某种书上的解密卡片，只有“滑动窗”平移到刚好和信号中的回波完全重合时才有显著输出。“比较是否重合”就是给两个信号内积，比较一系列不同位置的滑动窗就是卷积/相关。

### 去斜

去斜是在“瞬时频率 $f$—时间 $t$”意义上讨论的。

啁啾信号可表示成 $x = A \exp(i 𝜑)$，$𝜑 = \pi K t^2+ \cdots$，这样 $\dv{\varphi}{t} = 2\pi Kt + \cdots$ 就是瞬时（角）频率，它随时间线性变化，$K$ 称为“调频”率。

若有两个信号 $x = (\cdots) \exp(i 𝜑)$、$y = (\cdots) \exp(i ψ)$，很容易构造它们的相位差：$x y^* = (\cdots) \exp(i (𝜑-ψ))$。注意 $x,\ y,\ xy^*$ 的频率，其实频率差也构造出来了。（此即“差拍”）

雷达测距把位置差转化为时间差。由于线性调频，时间差可继续转化成频率差。

- 准备一个本振信号作为基准，它满足 $f = K t$。（时间原点是接收机开始工作的时刻，不一定是发射时刻。）
- 回波（的非零部分）满足 $f = K (t-t_0)$，其中 $t_0$ 是回波前沿到达的时刻，反映目标距离。
- 作差拍，它（在回波非零时段）满足 $f = K t_0$，频率稳定。
- 再变换到频域，$K t_0$ 频率稳定存在了一段时间，会出现主峰；其它频率不曾稳定存在，基本没有。
  因此，只要把主峰的频率记下，就可反推出 $t_0$，从而进一步测距。

现在讨论分辨率。

设有两个目标，它们在频域各自形成一峰，（认为）两峰间距大于峰宽时才可分辨出。两峰间距取决于距离差，峰宽取决于时域宽度，即回波（非零部分）的时长。（→幻灯片 19 页）

### 带宽

零带宽的信号只有持续时间无限长的正弦波，实际信号是持续时间有限的多种正弦波的叠加，有两种因素导致带宽。

- 对于简单脉冲，主要因素是持续时间。
- 对于啁啾信号，主要因素是人为混入的各种频率。（算一下会发现 $KT \gg 1/T$。）粗略估计可考虑“频率$f$—时间$t$”图，把那条图线在频率轴的投影当作频带，从而带宽是 $KT$。

### 距离分辨率

从我们课上的论证看，脉冲压缩和去斜的距离分辨略都是 $c/(2B)$ 只是巧合。

时间分辨率为 $1/B$ （相当于距离分辨率为 $c/2 × B$）是算出来的，在幻灯片11页至14页。

## 4 信号检测、匹配滤波、雷达方程

### 模糊

> :material-clock-edit-outline: 2022年4月17日。

距离“不模糊”指回波周期性不会有影响。

### 雷达方程

> :material-clock-edit-outline: 2023年9月12日。

信号：

- Power $P_\text{transmit}$。
- Gain $G_\text{transmit}$，由方向特性决定。
- $\sigma / \qty(4 \pi R^2)$，其中 $\sigma$ 是 radar cross section。
- $A / \qty(4\pi R^2)$，其中 $A$ 是雷达天线面积。另外 $A = G_\text{receive} \times \lambda^2 / \qty(4\pi)$。

噪声：

- $k_B T$。
- Band width $B$。

另外还有损耗 $L$。

### Stationary Phase Approximation

> :material-clock-edit-outline: 2023年9月13日。
>
> :material-eye-arrow-right: [Stationary phase approximation - Wikipedia](https://en.wikipedia.org/w/index.php?title=Stationary_phase_approximation&oldid=1153005878).
>
> :material-eye-arrow-right: [Via stationary phase method - Chirp spectrum - Wikipedia](https://en.wikipedia.org/w/index.php?title=Chirp_spectrum&oldid=1150891958#Via_stationary_phase_method).

若 $x \mapsto \theta = K \frac{x^2}{2} + o(x^2)$ 且 $x \mapsto A$ 缓变，则定积分

$$
\int\limits_\R A e^{j \theta} \dd{x}
$$

可近似计算。

- $x \to 0$ 时，$\dv{\theta}{x} \approx 0$，被积函数近似同相，能积累起来。
- 其余 $x$ 时，$\dv{\theta}{x}$ 较大，被积函数相位变化剧烈，难以积累，近似为零。

因此原积分近似化为

$$
\begin{split}
& \int\limits_\R \eval{A}_{x=0} e^{j \theta} \dd{x} \\
&\approx \eval{A}_{x=0} \int\limits_\R e^{j \theta} \dd{x} \\
&\approx \eval{A}_{x=0} \int\limits_\R e^{j K \frac{x^2}{2}} \dd{x}. \\
\end{split}
$$

现在计算剩下的定积分。考虑解析函数 $e^{- z^2 / 2}$ 在辐角属于 $\qty[0, \frac\pi4]$ 扇形的边界上的围道积分，结合 $\int_{\R^+} e^{-x^2/2} \dd{x} = \sqrt{\pi / 2}$，可得

$$
\int\limits_\R e^{j K \frac{x^2}{2}} \dd{x}
= \sqrt{\frac{2\pi j}{K}}.
$$

!!! note "算术平方根"

    规定 $\sqrt{j}$ 表示 $e^{j \pi / 4}$。

计算啁啾信号的频谱时，积分变量是 $t$，定积分带参数 $\omega$。

- $t \mapsto A$ 是门函数，确实缓变（除了个别点）。

- $t \mapsto \theta$ 不符合原来的要求，但它是二次函数，总存在唯一驻点 $t_0$（它含 $\omega$）。在 $t_0$ 处按幂级数展开：

  $$
  \theta = \eval{\theta}_{t_0} + \eval{\dv[2]{\theta}{t}}_{t_0} \times \frac{(t-t_0)^2}{2} + o\qty((t-t_0)^2).
  $$

  这就可以处理了。

最终可知啁啾信号的频谱与 $\operatorname{sinc}$ 的类似，但相位没对齐，而是按 $\omega \mapsto t_0 \mapsto \eval{\theta}_{t_0}$ 变化。具体来说，若 $t \mapsto \theta = \qty(\alpha + \beta t + \gamma \frac{t^2}{2}) - \omega t$，则

$$
\omega \mapsto t_0 \mapsto \eval{\theta}_{t_0}
= a - \frac{(\beta-\omega)^2}{2 \gamma},
$$

还是二次函数。

## 10 代价函数匹配激活函数

> :material-clock-edit-outline: 2022年5月3日。

避免导数太小。

代价函数 $J = \eval{J}_{\vb* a}$，激活 $a_\mu = g(z_\mu)$。希望反向传播的起始 $\delta_\mu = \pdv{z_\mu} J$ 不致太小。

$$
\delta_\mu = \eval{g'}_{a_\mu} \pdv{J}{a_\mu}.
$$

$g$ 是 Logistic 函数时，$g'$ 很有可能非常小。若 $J$ 是离差平方和，则无法抑制。

$$
\begin{cases}
    \ln a, & y=1. \\
    \ln(1-a), & y=0. \\
\end{cases}
$$

若 $J$ 是交叉熵（如上），则 $\pdv{a_\mu} J$ 可响应除以掉，最终 $\delta_\mu = a_\mu - y_\mu$，不会太小。

---

跳出来看，原来希望$\pdv{a_\mu} J = \qty(a_\mu-y_\mu) / \eval{g'}_{a_\mu}$。

比如 soft-max 激活函数

$$
a_i = \frac{\exp z_i}{\sum_j \exp z_j}.
$$

试试解那个方程？

$$
\begin{split}
    \pdv{a_\mu} J
    &= \frac{a_\mu - y_\mu}{\pdv{a_\mu}{z_\mu}} \\
    &= \frac{a_\mu - y_\mu}{a_\mu - \frac{a_\mu}{\sum \exp z} \times \exp z_\mu} \\
    &= \frac{a_\mu - y_\mu}{a_\mu (1 - a_\mu)} \\
    &= \begin{cases}
        - \frac{1}{1-a_\mu}, & y_\mu = 0. \\
        - \frac{1}{a_\mu}, & y_\mu = 1.
    \end{cases}
\end{split}
$$

若忽略 $y=0$，则对应对数似然代价函数 $y \log a$。（其它输出不会放任自流，有其它样本限制着。）

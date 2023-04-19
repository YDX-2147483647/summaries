# 相关时间一定非负吗？

> :material-clock-edit-outline: 2023年3月29日，2023年4月14日，2023年4月18–19日。

$$
\DeclareMathOperator\expect{\mathbb{E}}
\def\R{\mathbb{R}}
\def\C{\mathbb{C}}
\newcommand\mark[1]{{\color{teal}#1}}
$$

## 问题

今有随机信号 $X: \Omega \times \R \to \C$，其自相关函数 $R: \R \times \R \to \C$ 定义如下。

$$
\eval{R}_{\mu, \nu} \coloneqq \expect \eval{X^*}_\mu \eval{X}_\nu.
$$

!!! note inline end "记号"

    $\expect$ 是数学期望，上标 $*$ 表共轭，所有小写希腊字母都默认在 $\R$ 中任取。

若$X$在自相关意义下平稳（$\eval{R}_{\mu,\mu+\tau} \equiv \eval{R}_{0,\tau}$），则$R$可简写为一元函数（$\eval{R}_\tau$）。

若$X$是实随机信号（其值域包含于$\R$），则$R$的值域也包含于$\R$。此时定义<u>相关时间</u>为

$$
\int\limits_{\R^+} \eval{r}_\tau \dd{\tau},
$$

其中相关系数 $\eval{r}_\tau \coloneqq \eval{R}^\tau_\infty / \eval{R}^0_\infty$。

这个相关时间一定非负吗？

## 相关时间的另一种写法

注意任给随机过程 $X$ 及其自相关函数$R$、相关系数$r$，都能构造另一个随机过程 $X' = (X - \eval{R}_\infty) / \eval{R}^0_\infty$，使$X'$的自相关函数、协方差、相关系数都等于$r$，所以后面就只管协方差$K$了。

由于$K$共轭对称（$\eval{K}_\tau \equiv \eval{K^*}_\tau$），

$$
\begin{split}
\qty(\int\limits_{\R^+} \eval{K}_\tau \dd{\tau})^*
&= \int\limits_{\R^+} \eval{K^\mark{*}}_\tau \dd{\tau} \\
&= \int\limits_\mark{\R^-} \eval{K^*}_\mark{-\tau} \dd{\tau} \\
&= \int\limits_{\R^-} \mark{\eval{K}_{\tau}} \dd{\tau}. \\
\end{split}
$$

所以其实

$$
\begin{split}
\int\limits_\R \eval{K}_\tau \dd{\tau}
&= \int\limits_\mark{\R^+} \eval{K}_\tau \dd{\tau}
    + \int\limits_\mark{\R^-} \eval{K}_\tau \dd{\tau} \\
&= 2 \times \Re \int\limits_\mark{\R^+} \eval{K}_\tau \dd{\tau} \\
&\in \R.
\end{split}
$$

——在相关时间的定义中，若把积分范围从$\R^+$改到$\R$，则没有本质区别，还能保证复随机信号算出来也是实数。

!!! note "$\tau = 0$ 怎么办？"

    上述论证不适用于 $\R = \delta$，但结论好像适用（同理换元）。

## 频域理解

由 Wiener–Хи́нчин–Einstein 定理，$K$ 与功率谱密度 $S$ 互为 Fourier 变换对，因此

$$
\int\limits_\R \eval{K}_\tau \dd{t} = \eval{S}_{\omega = 0}.
$$

注意功率谱密度按定义是恒非负函数的极限，于是也恒非负。故 $\eval{S}_0 \geq 0$。

这就说明了相关时间非负。

## 时域理解

### 协方差的性质

$K$ 总是[半正定](https://math.stackexchange.com/a/2997540/1031068)：任给确定信号 $x: \R \to \C$，

$$
\iint \eval{K}_{\mu,\nu} \eval{x^*}_\mu \eval{x}_\nu \dd{\mu} \dd{\nu} \geq 0.
$$

因为上式等于随机变量 $\int \eval{X}_\mu \eval{x}_\mu \dd{\mu}$ 的方差。

!!! note "总可以比较大小"

    根据不等式左边的形式和$K$共轭对称，不等式左边总是实数，可以比大小。

!!! tip "Cauchy–Schwartz 不等式"

    $x = \eval{\delta}_{\mu - m},\ \eval{\delta}_{\mu - n}$ 对应的顺序主子式是

    $$
    \begin{vmatrix}
        \eval{K}_{m,m} & \eval{K}_{m,n} \\
        \eval{K}_{n,m} & \eval{K}_{n,n} \\
    \end{vmatrix},
    $$

    它非负。

    利用 $\eval{K}_{n,m} = \eval{K^*}_{m,n}$ 可得出

    $$
    \eval{K}_{m,m} \eval{K}_{n,n}
    \geq \eval{\abs{K}^2}_{m,n}.
    $$

!!! tip "Fourier 变换？"

    $x = e^{j\omega\mu}$ 时积分式是

    $$
    K_{\mu,\nu} \times e^{j \omega (\nu-\mu)},
    $$

    类似 Fourier 变换。

    如果后文的 $x$ 再乘上 $e^{j\omega\mu}$，会得到功率谱密度。

### 构造相关时间

取 $x = G_{2T} / \sqrt{2T}$，其中$G$是门函数，$T > 0$。

此时半正定性质是

$$
\begin{split}
0
&\leq \frac{1}{2T} \iint
\eval{K}_{\mu,\nu} \eval{G_{2T}}_\mu \eval{G_{2T}}_\nu
\dd{\nu} \dd{\mu} \\
&= \frac{1}{2T} \iint
K \times I_{[-T,T] \times [-T,T]}
\dd{\nu} \dd{\mu}. \\
\end{split}
$$

!!! note inline end "记号"

    集合$A$的示性函数 $\eval{I_A}_x$ 定义为

    $$
    \begin{cases}
      1 & x\in A. \\
      0 & x\not\in A. \\
    \end{cases}
    $$

换元 $(t,\tau) = (\frac{\mu+\nu}{2},\ \nu-\mu)$，化为

$$
\frac{1}{2T} \iint
K \times I_\mathcal{D}
\dd{t} \dd{\tau},
$$

其中

$$
\begin{split}
\mathcal{D}
&= \qty{(t,\tau) : \abs{t- \frac\tau2} < T \land \abs{t+ \frac\tau2} < T} \\
&= \qty{(t,\tau) : \abs{\tau} < 2T \land \abs{t} < T - \frac{\abs{\tau}}2}. \\
\end{split}
$$

### 极限

将二重积分继续化为累次积分 $\int \kappa_T \dd{\tau}$，其中

$$
\eval{\kappa_T}_\tau
\coloneqq \frac{1}{2T} \int K \times I_\mathcal{D} \dd{t}.
$$

!!! note "详细写法"

    如果你真的想把上述定义详细写出来……

    $$
    \begin{cases}
        \frac{1}{2T} \int\limits_{\frac{\abs{\tau}}2 - T}^{T - \frac{\abs{\tau}}2}
            \eval{K}_{t-\frac\tau2, t+\frac\tau2}
            \dd{t}
            & \abs{\tau} < 2T. \\
        0 & \abs{\tau} \geq 2T. \\
    \end{cases}
    $$

好，我们取极限 $T \to +\infty$，应用 [Lebesgue 控制收敛原理](https://en.wikipedia.org/wiki/Dominated_convergence_theorem)，由极限的保号性，

$$
\int \kappa_\infty \dd{\tau}
= \lim \int \kappa_T \dd{\tau}
\geq 0.
$$

现在有如下问题。

- Lebesgue 控制收敛原理的前提是否成立？

  - $\kappa_T$ 逐点收敛吗？（$\kappa_\infty$ 存在吗？）

  - $\abs{\kappa_T}$ 能被某个可积函数控制吗？

- $\kappa_\infty$ 是某种 $K$ 吗？（$\int \kappa_\infty \dd{\tau}$ 是相关时间吗？）

这些问题都归结于理解 $\kappa_\infty$。

### $K$ 的时间平均

可以证明：如果

$$
\frac{1}{2T} \int K \times I_{D} \dd{t},
$$

的极限存在，则 $\kappa_\infty$ 也存在，并且相等，其中 $D = \qty{(t,\tau) : \abs{t} < T} \supset \mathcal{D}$。

下面作差证明。上式的极限与 $\kappa_\infty$ 之差等于

$$
\lim \frac{1}{2T} \int K \times \qty(I_{D} - I_\mathcal{D}) \dd{t}.
$$

$T$ 充分大（$T > \frac{\abs{\tau}}{2}$）后，极限式的绝对值

$$
\begin{split}
&= \frac{1}{2T} \abs{\int\limits_{0 < T - \abs{t} < \frac{\abs{\tau}}2} K \dd{t}} \\
&\leq \frac{1}{2T} \int\limits_{0 < T - \abs{t} < \frac{\abs{\tau}}2} \abs{K} \dd{t} \\
&\leq \frac{1}{2T} \int\limits_{0 < T - \abs{t} < \frac{\abs{\tau}}2} \max \abs{K} \dd{t} \\
&= \frac{\abs{\tau}}{2T} \max \abs{K} \\
&\to 0.
\end{split}
$$

!!! note "$\max \abs{K}$ 存在"

    一般信号功率有上界，故 $\eval{K}_{t,t} \in \R$ 有上界，$\max_t \eval{K}_{t,t}$ 存在。

    按 Cauchy–Schwartz 不等式，

    $$
    \begin{split}
    \abs{\eval{K}_{t-\frac\tau2, t+\frac\tau2}}
    &\leq \sqrt{
        \eval{K}_{t-\frac\tau2, t-\frac\tau2} \times
        \eval{K}_{t+\frac\tau2, t+\frac\tau2}
    } \\
    &\leq \max \eval{K}_{t \pm \frac\tau2, t \pm \frac\tau2} \\
    &\leq \max_t \eval{K}_{t,t},
    \end{split}
    $$

    从而 $\max \abs{K}$ 也存在。

    另外对于平稳信号，“功率有上界”等价于“功率有限”。

因此 $\kappa_\infty = \lim \frac{1}{2T} \int K \times I_{D} \dd{t}$。

### 补丁

回顾前面的问题——

- Lebesgue 控制收敛原理的前提是否成立？

  - $\kappa_T$ 逐点收敛吗？（$\kappa_\infty$ 存在吗？）

    如果$K$的时间平均存在，一定如此。

  - $\abs{\kappa_T}$ 能被某个可积函数控制吗？

    $\abs{\kappa_\infty}$ 可积是 $\abs{\kappa_T}$ 可积的必要条件。如果信号含周期分量（直流也有周期），$\abs{\kappa_\infty}$ 并不可积，尽管仍能用 Dirac δ 表示。

    另外，

    $$
    \begin{split}
    \abs{\kappa_T}
    &\leq \frac{1}{2T} \int \abs{K} \times I_\mathcal{D} \dd{t} \\
    &\leq \frac{1}{2T} \int \abs{K} \times I_D \dd{t},
    \end{split}
    $$

    因此若$K$的时间平均能被控制，则 $\kappa_T$ 也能。

- $\kappa_\infty$ 是某种 $K$ 吗？（$\int \kappa_\infty \dd{\tau}$ 是相关时间吗？）

  没错，它是$K$的时间平均。

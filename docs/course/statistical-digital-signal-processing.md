---
relevant:
  - ./probability-and-statistics.md
---

# Statistical Digital Signal Processing

!!! info "课程名称"

    本课有多个名字。

    - 随机数字信号处理
    - Statistical Digital Signal Processing
    - Random Digital Signal Processing

$$
\DeclareMathOperator\expect{\mathbb{E}}
\DeclareMathOperator\variant{\mathbb{V}}
\def\R{\mathbb{R}}
$$

## §1 Performance

### Criteria of performance

> :material-clock-edit-outline: 2023年10月12日。
>
> :material-eye-arrow-right: [“概率论与数理统计”讨论的无偏与相合](./probability-and-statistics.md#无偏与相合)。

Fisher 拨开迷雾，驱散阴影，指明了评价估计的标准：

- Unbiased 无偏——期望
- Consistent 相合——依概率收敛
- Effective 有效——方差

本课讨论了方差的下界，让“有效”有了绝对意义。此外还增加了以下标准：

- Valid 合法——可操作

  严格来说这不算评价标准，只是明确讨论范围，不许用未知信息耍赖。

- Sufficient 充分——信息

## §2 Minimum variance unbiased estimation

### Error, variance, and bias

> :material-clock-edit-outline: 2023年10月12日。

$\theta$ is a parameter. $\hat \theta$ is a random variable aiming at estimating $\theta$.

$$
\expect(\hat\theta - \theta)^2
= \variant \hat\theta + (\expect\hat\theta - \theta)^2.
$$

:material-eye-arrow-right: [“人工智能导论”类似讨论](./artificial-intelligence.md#bias-vs-variance)。

## §3 Cramér–Rao lower bound

> :material-clock-edit-outline: 2023年9月18日，2023年10月13日，2023年10月14日。

随机变量 $\xi$ 服从参数为 $\theta$ 的分布，概率密度 $p$ 是 $\xi, \theta$ 的函数。Likelihood is $\theta \mapsto p$ when $\xi$ is given as a sample.

### Lemma: Derivative of expectation

对 $\xi$ 的任意函数 $f$，

$$
\begin{split}
\pdv{\theta} \expect f
&\coloneqq \pdv{\theta} \int f p \dd{\xi} \\
&= \int \pdv{\theta} (f p) \dd{\xi} \\
&= \int \pdv{f}{\theta} p \dd{\xi} + \int f \pdv{p}{\theta} \dd{\xi} \\
&= \expect \pdv{f}{\theta} + \int f \pdv{\ln p}{\theta} p \dd{\xi} \\
&= \expect \pdv{f}{\theta} + \expect f \pdv{\ln p}{\theta}. \\
\end{split}
$$

!!! note "Operator precedence"

    Product ($\times$) takes precedence over expectation ($\expect$), and the latter is over sum ($+$). 而且 $\expect(X \expect Y) \equiv (\expect X) \expect Y$。

!!! note "期望"

    这里求的是给定 $\theta$ 下的条件期望。

$\pdv{\theta}$ 与 $\int \dd{\xi}$ 总能交换吗？这是累次极限换序问题。“This is generally true except when the domain of the PDF for which it is nonzero depends on the unknown parameter.”

### Regular

Regularity: $\expect \pdv{\theta} \ln p = 0$.

In fact,

$$
\begin{split}
\expect \pdv{\ln p}{\theta}
&= \expect\qty(1 \times \pdv{\ln p}{\theta}) \\
&= \pdv{\theta} \expect 1 - \expect \pdv{\theta} 1 \\
&= 0 - 0 \\
&= 0.
\end{split}
$$

To be rigorous, this is a corollary of the regular conditions, rather than the reverse.

:material-eye-arrow-right: [Fisher information - Wikipedia](https://en.wikipedia.org/wiki/Fisher_information)

*Real* regular conditions:

- $\pdv{\theta} p$ exists almost everywhere.
- The support of $p$ does not depend on $\theta$.
- $\pdv{\theta} \int p \dd{\xi}$ exists.

### Yet another form of Cauchy–Schwarz inequality

对于 $\xi$ 的两个函数 $X,Y$，

$$
\abs{\expect \bar{X}Y}^2 \leq \expect \abs{X}^2 \times \expect \abs{Y}^2.
$$

Because $(X, Y) \mapsto \expect \bar{X} Y$ is an inner product.

另外这也相当于对函数 $\xi \mapsto \sqrt{p} X$ 和 $\xi \mapsto \sqrt{p} Y$ 应用定积分形式的 Cauchy–Schwarz 不等式。

### Unbiased

An estimator (a function of $\xi$ aiming at estimating $\theta$) $\hat\theta$ is unbiased: $\expect \hat\theta = \theta$.

Differentiate it:

$$
\begin{split}
0
&= \pdv{\theta} \expect \qty(\hat\theta - \theta) \\
&= \expect \qty(\pdv{\hat\theta}{\theta} - \pdv{\theta}{\theta})
    + \expect \qty(\hat\theta - \theta) \pdv{\ln p}{\theta}. \\
\end{split}
$$

$\pdv{\hat\theta}{\theta} = 0$ as $\hat\theta$ does not depend on $\theta$, $\pdv{\theta}{\theta} = 1$, therefore

$$
1 = \expect \qty(\hat\theta - \theta) \pdv{\ln p}{\theta}.
$$

!!! tip "间接估计"

    有时并不想估计 $\theta$，而想用 $\hat\alpha$ 估计 $\alpha = g(\theta)$。这时 $\expect\pdv{\theta}{\theta}$ 变为 $\expect\pdv{\alpha}{\theta} = \pdv{\alpha}{\theta}$。

    另一角度是假装参数是 $\alpha$，当成直接估计，把上式所有 $\theta$ 相关量替换为 $\alpha$ 的，再利用 $\pdv{\alpha} = \pdv{\theta}{\alpha} \pdv{\theta}$ 转为原来那样 $\theta$ 的表达式。

    若 $g$ 是一次函数，MVU 变换后还是 MVU；即使不是一次函数，当 $N \to +\infty$ 时，PDF 会按大数定律集中，若 $g$ 可微，则它在局部仍是一次函数——statistical linear (affine)。

### The theorem

$$
\begin{split}
1
&= \abs{\expect \qty(\hat\theta - \theta) \pdv{\ln p}{\theta}}^2 \\
&\leq \expect \abs{\hat\theta - \theta}^2
    \times \expect \abs{\pdv{\ln p}{\theta}}^2. \\
\end{split}
$$

The first part is mean squared error (MSE), and the second part is

$$
\begin{split}
\expect \qty(\pdv{\ln p}{\theta})^2
&= \expect \pdv{\ln p}{\theta} \pdv{\ln p}{\theta} \\
&= \pdv{\theta} \expect \pdv{\ln p}{\theta}
    - \expect \pdv{\theta} \pdv{\ln p}{\theta} \\
&= \pdv{\theta} 0
    - \expect \pdv[2]{\ln p}{\theta} \\
&= - \expect \pdv[2]{\ln p}{\theta}. \\
\end{split}
$$

!!! note "这一步的意义"

    这一步没有意义，变换前后都是含 $\theta$ 而不含 $\xi$ 的数。之所以变一下，是因为一些情况下二阶导数天然不含 $\xi$，从而 $\expect$ 更容易计算。

    由变换前的形式，其相反数恒非负；由变换后的形式，增多相互独立的 $\xi$ 时可加（将 $p$ 换为 $p_1 \times p_2$，值是 $p_1,p_2$ 对应值之和）。如此种种，人们把它的相反数称作 Fisher information。

To wrap up,

$$
\expect \abs{\hat\theta - \theta}^2
\geq \frac{1}{- \expect \pdv[2]{\ln p}{\theta}}.
$$

Moreover, the two sides are equal if and only if $\qty(\hat\theta - \theta) \parallel \pdv{\theta}\ln p$ with respect to $\xi$. In other words, there exists a function $\theta \mapsto \lambda$, such that $\pdv{\theta} \ln p = \lambda \qty(\hat\theta - \theta)$ (assuming $\hat\theta \not\equiv \theta$). Note that in this case, $1 = \expect\abs{\hat\theta - \theta}^2 \times \expect\abs{\lambda \qty(\hat\theta - \theta)}^2$, therefore $\expect\abs{\hat\theta - \theta}^2 = 1 / \abs{\lambda}$.

!!! info "最大似然"

    如果 $\pdv{\theta} \ln p = \lambda \qty(\hat\theta - \theta)$，那么 $\hat\theta$ 最大似然。

### Matrix form

Use Einstein summation.

设有参数 $\theta^b$，希望估计 $\alpha_a$。样本分布取决于 $\theta^b$，$\hat{\alpha}_a$ 是样本的函数，$\alpha_a$ 是 $\theta^b$ 的函数。

同标量形式，

$$
\expect (\hat{\alpha}_a - \alpha_a) \pdv{\ln p}{\theta^b} = \pdv{\alpha_a}{\theta^b}.
$$

Fisher information matrix $I_{ab} \coloneqq \expect \pdv{\ln p}{\theta^a} \pdv{\ln p}{\theta^b}$ is always positive semidefinite ($I_{ab} \succeq 0$), and it's positive definite ($I_{ab} \succ 0$) for regular statistical models. We'll only discuss the latter case.

同标量形式，另一形式是

$$
I_{a b}
= - \expect \pdv{\theta^a} \pdv{\theta^b} \ln p.
$$

协方差 $\Sigma_{ab} := \expect (\hat{\alpha}_a - \alpha_a) (\hat{\alpha}_b - \alpha_b)$ 总是半正定（$\Sigma_{ab} \succeq 0$），我们要讨论它的范围。

设 $z_a$ 是 $(\hat{\alpha}_a - \alpha_a)$ 和 $\pdv{\ln p}{\theta^a}$ 拼成的列向量，则

$$
\expect z_a z_b
:= \begin{bmatrix}
    \Sigma_{ab}
    & \expect (\hat{\alpha}_a - \alpha_a) \pdv{\ln p}{\theta^b}
    \\
    \expect \pdv{\ln p}{\theta^a} (\hat{\alpha}_b - \alpha_b)
    &
    I_{a b}
\end{bmatrix}
= \begin{bmatrix}
    \Sigma_{ab} & \pdv{\alpha_a}{\theta^b} \\
    \pdv{\alpha_b}{\theta^a} & I_{a b} \\
\end{bmatrix}.
$$

按形式 $\expect z_a z_b \succeq 0$，因此其 Schur complement

$$
\expect z_a z_b / I_{a b}
\coloneqq \Sigma_{ab} - \pdv{\alpha_a}{\theta^c} \pdv{\alpha_b}{\theta^d} I^{cd}
\succeq 0.
$$

!!! note "记号"

    $I_{a b} I^{b c} = {\delta_a}^c$——上下标转换表示逆。

!!! note "Schur complement 半正定的依据"

    $$
    \begin{bmatrix}
        \expect z_a z_b / I_{a b}
        & 0_{ab}
        \\
        0_{a b}
        & I_{a b}
    \end{bmatrix}
    $$

    与 $\expect z_a z_b$ 合同。

整理得估计量协方差在正定意义下的下界：

$$
\Sigma_{ab} \succeq \pdv{\alpha_a}{\theta^c} \pdv{\alpha_b}{\theta^d} I^{cd}.
$$

The conditions for equality are $(\hat{\alpha}_a - \alpha_a) \parallel \pdv{\ln p}{\theta^c}$ with respect to samples (i.e. the factor does not depend on samples). In factor the factor is $\pdv{\alpha_a}{\theta^b} I^{bc}$ or $\pdv{\theta^b}{\alpha_a} I_{bc}$.

:material-eye-arrow-right: [“随机信号分析”提到的最小二乘法](./stochastic-signal-processing.md#边缘分布和条件分布)

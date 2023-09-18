---
relevant:
  - ./probability-and-statistics.md
---

# Statistical Digital Signal Processing

$$
\DeclareMathOperator\expect{\mathbb{E}}
\def\R{\mathbb{R}}
$$

## §3 Cramér–Rao lower bound

> :material-clock-edit-outline: 2023年9月18日。

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

$\pdv{\theta}$ 与 $\int \dd{\xi}$ 总能交换吗？这是累次极限换序问题。

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

### Yet another form of Cauchy–Schwartz inequality

对于 $\xi$ 的两个函数 $X,Y$，

$$
\abs{\expect \bar{X}Y}^2 \leq \expect \abs{X}^2 \times \expect \abs{Y}^2.
$$

Because $(X, Y) \mapsto \expect \bar{X} Y$ is an inner product.

另外这也相当于对函数 $\xi \mapsto \sqrt{p} X$ 和 $\xi \mapsto \sqrt{p} Y$ 应用定积分形式的 Cauchy–Schwartz 不等式。

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

To wrap up,

$$
\expect \abs{\hat\theta - \theta}^2
\geq \frac{1}{- \expect \pdv[2]{\ln p}{\theta}}.
$$

Moreover, the two sides are equal if and only if $\qty(\hat\theta - \theta) \parallel \pdv{\theta}\ln p$ with respect to $\xi$. In other words, exists a function $\theta \mapsto \lambda$, such that $\pdv{\theta} \ln p = \lambda \qty(\hat\theta - \theta)$ (assuming $\hat\theta \not\equiv \theta$). Note that in this case, $1 = \expect\abs{\hat\theta - \theta}^2 \times \expect\abs{\lambda \qty(\hat\theta - \theta)}^2$, therefore $\expect\abs{\hat\theta - \theta}^2 = 1 / \abs{\lambda}$.

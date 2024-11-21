---
relevant:
  - ./set-theory.md
  - ./calculus-1.md
  - ./calculus-2.md
---

# 概率论与数理统计

$$
\def\N{\mathbb{N}}
\def\Z{\mathbb{Z}}
\def\R{\mathbb{R}}
$$

## §1 随机事件与概率

### 独立

> :material-clock-edit-outline: 2021年9月22日。

伯恩斯坦（哪位？）反例。给 $n$ 面体类似地涂上 $n-1$ 种颜色，相应的事件并不两两独立。

---

:material-eye-arrow-right: [随机事件a、b、c两两独立和相互独立有什么区别？ - 黑夜里的白猫的回答 - 知乎](https://www.zhihu.com/question/21872177/answer/1247392105)，图自 [Borromean rings - Wikipedia](https://en.wikipedia.org/wiki/Borromean_rings)。

:material-eye-arrow-right: [On the Construction of Independence Counterexamples on JSTOR](https://www.jstor.org/stable/2685037)（[Sci-Hub](https://sci-hub.se/https://doi.org/10.2307/2685037)）

## §2 随机变量

### 分布

> :material-clock-edit-outline: 2021年10月15日。

#### 二项分布 $B(n,p)$

> （Binomial）

$n$ 次<u>独立</u>重复试验的成功次数。

> - $n$：试验次数。
> - $p$：单次试验成功概率。
> - $q = 1-p$。

$$
\begin{array}{l}
    \xi \sim {B}(n,p). \\
    \displaystyle
    \Pr(\xi=k) = \binom{n}{k} p^k q^{n-k}, \quad
    k = 0,\cdots, n.
\end{array}
$$

---

单次试验的成功次数服从 $B(1,p)$，称作二点／伯努利（Bernoulli）分布。

#### 超几何分布 $H(n,M,N)$

> （Hypergeometric）

$n$ 次不放回抽样中“好”的数量。

$$
\begin{array}{l}
    \xi \sim {H}(n,M,N). \\
    \displaystyle
    \Pr(\xi=m) = \frac{\binom{M}{m} \binom{N-M}{n-m}}{\binom{N}{n}} = \frac{\binom{n}{m} \binom{N-n}{M-m}}{\binom{N}{M}}, \\
    \quad m = \max[0, n-(N-M)], \cdots, \min[n, M].
\end{array}
$$

> - $n$：样本量。
> - $N$：总体。
> - $M$：总体中“好”的数量。

#### 几何分布 $G(p)$

> （Geometric）

独立重复试验中第一次成功时的试验次数。（重复直至成功）

$$
\begin{array}{l}
    \xi \sim {G}(p). \\
    \Pr(\xi = n) = p q^{1-n}, \quad
    n \in \N_+.
\end{array}
$$

> - $p$：单次试验成功概率。
> - $q = 1-p$。

---

独立重复试验中第 $r$ 次成功时的试验次数服从负二项（negative binomial）分布 ${NB}(r,p)$，又名 Pascal 分布。

$$
\Pr(\xi = n) = \binom{n-1}{r-1} p^r q^{n-r} , \quad n \in [r, +\infty) \cap \Z.
$$

${NB}(1,p)$ 即 ${G}(p)$。

> 这两个分布的定义都比较混乱，有的指成功次数，有的指失败次数。

#### 泊松分布 $\pi(\lambda)$

> （Poisson，`/ˈpwɑːsɒn/`）

一段时间内发生的事件次数。（这种事件以恒定可能性独立发生）

$$
\begin{array}{l}
    \xi \sim \pi(\lambda). \\
    \displaystyle
    \Pr(\xi=k) = \frac{\lambda^k e^{-\lambda}}{k!}, \quad
    k \in \N.
\end{array}
$$

> - $\lambda$：期望，或者说发生率×时长。

#### 均匀分布 $U(l,r)$

> （Uniform）

$$
\begin{array}{l}
    X \sim U(l,r),\quad X \in [l,r]. \\
    \displaystyle
    \dv{P}{x} \equiv \frac{1}{r-l}. \\
    \displaystyle
    \Pr(X<x) = \frac{x-l}{r-l}.
\end{array}
$$

#### 指数分布 $E(\lambda)$

> （Exponential）

无后效连续型随机变量。

$$
\begin{array}{l}
    X \sim E(\lambda),\quad X \in [0,\infty). \\
    \displaystyle
    \dv{P}{x} = \lambda e^{-\lambda x}. \\
    \displaystyle
    \Pr(X<x) = 1 - e^{-\lambda x}.
\end{array}
$$

> - $\lambda$：$\eval{\dv{P}{x}}_{x=0^+}$。
>
> 以上 PDF、CDF 仅限 $x \geq 0$。

#### 正态分布 $N(\mu, \sigma^2)$

→中心极限定理。

$$
\begin{array}{l}
    X \sim N(\mu, \sigma^2),\quad X \in \R. \\
    \displaystyle
    \dv{P}{x} = \frac{\exp( -\frac{(x-\mu)^2}{2\sigma^2})}{\sqrt{2\pi} \sigma}. \\
    \displaystyle
    \Pr(X<x) = \Phi\qty(\frac{x-\mu}{\sigma}).
\end{array}
$$

> - $\mu$：期望。
> - $\sigma^2$：方差。

## §5 极限定理

> :material-clock-edit-outline: 2021年11月15日。

- 大数定律：算术平均值稳定。
  - Chebyshev：独立序列 $\xi_i$，$E\xi_i = \mu_i$，$D\xi_i$ 存在且有公共<u>上界</u>，则 $\bar \xi \overset{P}{\to} \bar \mu$。
  - 伯努利：独立<u>重复</u>试验，$f \overset{P}{\to} P$。
  - Khintchine（Алекса́ндр Я́ковлевич Хи́нчин）：独立<u>同分布</u>序列 $\xi_i$，$E\xi_i = \mu$，则 $\bar\xi \overset{P}{\to} \mu$。
- 中心极限定理：算术和标准化后的渐近分布是标准正态分布。
  - Linderberg – Levy：独立<u>同分布</u>序列 $\xi_i$，<u>方差</u>存在，则 $\sum\xi$ 标准化后服从标准正态分布。
  - De Moivre – Laplace：独立重复试验，结论类似。
  - Lyapunov（Алекса́ндр Миха́йлович Ляпуно́в）：独立序列，标准差存在且其方均根为 $B_n$，同时 $2+\delta$ 阶中心矩是 $o(B_n^{2+\delta})$，则算术和服从标准正态分布。

## §6 抽样分布

### 抽样分布

> :material-clock-edit-outline: 2021年11月15日。

抽样分布指样本的统计量的分布。

都需要各个随机变量相互独立。

- $\chi^2(n)$：$\sum_i \xi_i^2$，$\xi_i$ 来自标准正态总体。（Pearson）

  $E\chi^2 = n$，$D\chi^2 = 2n$。（标准正态变量的四阶矩是 $3$）

  $n=2$ 时恰为指数分布。

  $\text{PDF} \propto x^{n/2-1} e^{-x/2}$。

- $t(n)$：$\frac{\xi}{\sqrt{\chi^2/n}}$，$\xi\sim N(0,1)$，$\chi^2 \sim \chi^2(n)$。（W. S. Gosset，*student*）

  > $E\xi=0$，$E\frac{\chi}{\sqrt{n}} = 1$。

  $ET=0$（$n \geq 2$），$DT = \frac{n}{n-2}$（$n\geq 3$）。

  $\text{PDF} \propto \qty(1+\frac{t^2}{n})^{-(n+1)/2}$。

- $F(m,n)$：$\frac{M/m}{N/n}$，$M\sim \chi^2(m)$，$N\sim\chi^2(n)$。（Fisher）

  $\text{PDF} \propto x^{\frac{m}{2}-1} \qty(1+\frac{m}{n}x)^{-(m+n)/2}$。

### 抽样分布定理

> :material-clock-edit-outline: 2021年11月15日。

$E\bar\xi = \mu$，$D\bar\xi = \frac{1}{n} \sigma^2$，$Es^2 = \sigma^2$。

对于正态总体 $N(\mu,\sigma^2)$，$\bar\xi$ 与 $s^2$ 独立，且

$$
\begin{aligned}
\bar\xi &\sim N\qty(\mu, \frac{\sigma^2}{n}). \\
\sum_i \qty(\xi_i-\bar\xi)^2 &\sim \sigma^2 \chi^2_{n-1}. \\
\frac{\bar\xi - \mu}{s/\sqrt{n}} &\sim t(n-1). \\
\end{aligned}
$$

对于两个相互<u>独立</u>的不同均值、<u>相同方差</u>的正态总体，

$$
\begin{aligned}
\sqrt{m^{-1} + n^{-1}} U &= (\bar\xi-\mu_\xi) - (\bar\eta - \mu_\eta), \\
(m+n-2) V &= \sqrt{\sum_i \qty(\xi-\bar\xi)^2 + \sum_i \qty(\eta-\bar\eta)^2}. \\
%
\implies \frac{U}{V} \sim t(m+n-2).
\end{aligned}
$$

> $U \sim N(0,\sigma^2)$，$V \sim \sigma^2 \chi^2_{m+n-2}$。

对于两个相互<u>独立</u>的正态总体，

$$
\frac{s_\xi^2}{s_\eta^2} \sim \frac{\sigma_\xi^2}{\sigma_\eta^2} F(m-1,n-1).
$$

## §7 参数估计

### 无偏与相合

> :material-clock-edit-outline: 2022年11月17日。
>
> :material-eye-arrow-right: [probability - Consistency and asymptotically unbiasedness? - Mathematics Stack Exchange](https://math.stackexchange.com/a/239199/1031068).

相合和大数定律有几分相像，而无偏只描述准确性（渐近无偏是更弱的条件）。

即使是渐近无偏和相合，两个概念也没有蕴含关系。

下面用估计值的 μ、σ 举几个比喻式的例子。

- 相合但有偏：μ+σ = 真值，σ = 1/n。（类似例子：样本均值，不过最大的样本多算一遍。）
- 相合但渐近也有偏：估计值取零的概率为 1-1/n，取 n 的概率为 1/n，真值为零。
- 无偏但不相合：μ = 真值，σ = 1。（类似例子：只用第一个样本。）

用切比雪夫不等式能证明：渐近无偏 ∧ 方差收敛到零 ⇒ 相合。

// 是“渐近”，而非“渐进”。

# 后备箱

- 计数时注意是否放回。
- 区分条件和无条件概率。
- 求级数时注意求和范围。
- 注意随机变量的<u>范围</u>，尤其是写概率密度时。
- 求随机变量的函数的概率密度时，注意是否是<u>一一映射</u>。
- 区分概率密度和累积分布。
- 区分泊松分布和指数分布。
- 按定义验证抽样分布时，强调<u>独立</u>性。
- 矩估计时，强调用样本矩代替总体矩。
- 若 $\xi \sim N(0,1)$，则 $-\xi$ 也服从。
- 累积分布是分段函数时，概率密度往往也是。

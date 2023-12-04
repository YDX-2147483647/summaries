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
\DeclareMathOperator\expect{\operatorname{\mathbb{E}}}
\DeclareMathOperator\variant{\operatorname{\mathbb{V}}}
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
- Efficient 有效——方差

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

> :material-clock-edit-outline: 2023年9月18日，2023年10月13日，2023年10月14日，2023年10月25日。

随机变量 $\xi$ 服从参数为 $\theta$ 的分布，概率密度 $p$ 是 $\xi, \theta$ 的函数。Likelihood is $\theta \mapsto p$ when $\xi$ is given as a sample.

!!! info "Cramér"

    Harald Cramér (Swedish: `[kraˈmeːr]`, `eː` ≈ m**ay**or in English) was a Swedish mathematician, actuary, and statistician.

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

!!! info "Loewner order"

    Let $A,B$ be two Hermitian matrices with same shape. We say that $A \succeq B$ if $A − B$ is positive semidefinite. Similarly, we say that $A \succ B$ if $A − B$ is positive definite.

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

## §5 General Minimum Variance Unbiased Estimation

### Properties of a statistic

> :material-clock-edit-outline: 2023年10月25日，2023年10月29日。
>
> :material-eye-arrow-right: [Completeness (statistics) - Wikipedia](https://en.wikipedia.org/wiki/Completeness_(statistics)).
>
> :material-eye-arrow-right: [Lecture 1 - SF3961 Graduate Course in Statistical Inference](https://www.math.kth.se/matstat/gru/Statistical%20inference/Lecture1_2015.pdf).
>
> :material-eye-arrow-right: [Lecture 4 - SF3961 Graduate Course in Statistical Inference](https://www.math.kth.se/matstat/gru/Statistical%20inference/Lecture2_2015.pdf).
>
> :material-eye-arrow-right: [exponential family - Are complete statistics always sufficient? - Cross Validated](https://stats.stackexchange.com/questions/187869/).
>
> :material-eye-arrow-right: [Is a minimal sufficient statistic also a complete statistic - Cross Validated](https://stats.stackexchange.com/questions/272531/is-a-minimal-sufficient-statistic-also-a-complete-statistic).
>
> :material-eye-arrow-right: [Basic intuition about minimal sufficient statistic - Cross Validated](https://stats.stackexchange.com/questions/166661/basic-intuition-about-minimal-sufficient-statistic).
>
> :material-eye-arrow-right: [st.statistics - Is a function of complete statistics again complete? - MathOverflow](https://mathoverflow.net/a/182661).

- **Sufficient**——Information of $\vb*{X}$ from $T$

  $\Pr(\vb*{x}|T)$ does not depend on $\theta$.

- **Complete**——Family of distributions of $T$

  For any measurable function $g$, $\expect g(T) \equiv 0$ implies $\Pr(g(T) = 0) \equiv 1$. (“$\equiv$” means $\forall \theta$)

  Equivalently, $\qty{P_{T|\theta}: \theta \in \text{parameter space}}$ spans the whole $\mathcal{T} \to \mathbb{R}$ functions. (Hint: $\expect g(T)$ is an inner product of $P_{T|\theta}$ and $g$)

> Consider the map $f:p_{\theta }\mapsto p_{T|\theta}$ which takes each distribution on model parameter $\theta$ to its induced distribution on statistic $T$. The statistic $T$ is said to be complete when $f$ is surjective, and sufficient when $f$ is injective.

:material-eye-arrow-right: [function - Sufficient/complete statistic $\leftrightarrow$ injective/surjective map? - Cross Validated](https://stats.stackexchange.com/a/629917/399511).

1. Probability triple $(\Omega, \mathcal{F}, \mu)$:
   - $\Omega$ is the sample space,
   - $\mathcal{F} \subset 2^\Omega$ is the event space, and
   - $\mu: \mathcal{F} \to [0,1]$ is the probability function.
2. Random variable $X: \Omega \to \mathcal{X}$, where $\mathcal{X}$ is a measurable space with $\sigma$-field $\mathcal{B}$.
3. Statistic $T: \mathcal{X} \to \mathcal{T}$, where $\mathcal{T}$ is another measurable space with $\sigma$-field $\mathcal{C}$ contains all singletons. Besides, we can also think the random variable $T \circ X: \Omega \to \mathcal{T}$ as the statistic.
4. Sufficiency: $\mu_{T|\Theta}(C|\theta) = \mu_{X|\Theta}(T^{-1} C|\theta)$ is probability measure on $\mathcal{C}$.
5. Sufficiency (in the Bayesian sense): For every prior $\mu_\Theta$, there exists versions of the posterior distributions $\mu_{\Theta|X}, \mu_{\Theta|T}$ such that, $\forall A \in \text{parameter space}$, $\mu_{\Theta|X}(A|x) = \mu_{\Theta|T}(A|T(x))$, $\mu_X$-almost surely, where $\mu_X$ is the marginal distribution of $X$.
6. One should note that completeness is a statement about the entire family $\qty{\mu_{T|\Theta}(\cdot|\theta) : \theta \in \text{parameter space}}$ and not only about the individual conditional distributions $\mu_{T|\Theta}(\cdot|\theta)$.

Counterexamples:

- Sufficient but not complete

  - $X \sim \mathcal{U}(\theta, \theta+2\pi)$ itself is a sufficient (and even minimal sufficient) statistic. However $\expect \sin X \equiv 0$ and it tells nothing about the distribution of $\sin X$.

- Complete but not sufficient

  - Constant statistics.
  - First we work out a complete and sufficient statistic for $n$ samples. Now we're given more samples but we stick to the old statistic. Then this statistic is still complete but not sufficient any more.

### Rao–Blackwell–Lehmann–Scheffé theorem

> :material-clock-edit-outline: 2023年10月25日，2023年10月29日。

In fact there are two independent theorems.

- C.R. **Rao** (Indian-American) and David **Blackwell** (American):

  For any estimator $\delta$ used for estimating $\theta$ and a <u>sufficient</u> statistic $T$, we have

  - $\delta' \coloneqq \expect(\delta | T)$ is a <u>valid</u> estimator.
  - And it has <u>smaller mean-squared error</u>: $\expect (\delta' - \theta)^2 \leq \expect (\delta - \theta)^2$.
  - Additionally, the improved estimator is unbiased iff. the original estimator is unbiased: $\expect \delta' \equiv \theta \iff \expect \delta \equiv \theta$.

- Erich Leo **Lehmann** (German-born American) and Henry **Scheffé** (American):

  If an <u>unbiased</u> estimator $\delta$ <u>only</u> depends on samples through a <u>complete</u> <u>sufficient</u> statistic $T$, then it's the <u>minimum variance</u> unbiased estimator.

!!! tip "Conditional expectation"

    While $\expect X$ is a simple _number_, the conditional expectation $\expect(X|Y)$ is a _random_ variable depends on the value of $Y$. In other words, $\expect(X|Y)$ is a function of the random variable $Y$.

    We can take $Y = y$ as an event depends on $y$, then $\expect(X|Y = y)$ (conditioning on the _event_) is a number depends on $y$.

    Since $\expect(X|Y)$ is random, we can take another $\expect$. This is the law of total expectation: $\expect \expect(X|Y) = \expect X$.

#### Rao–Blackwell theorem

**First**, $\delta'$ does not depend on $\theta$ (therefore it's valid) because $T$ is sufficient (thus $\Pr(\delta|T)$ does not depend on $\theta$).

The **second** part can be proved by the following decomposition.

$$
\expect (\delta - \theta)^2
= \expect (\delta' - \theta)^2 + \expect \variant(\delta | T)
\geq \expect (\delta' - \theta)^2.
$$

Consider the well-known formula

$$
\expect (X-m)^2
= \qty(\expect X - m)^2 + \expect \qty(X-\expect X)^2
= \qty(\expect X - m)^2 + \variant X.
$$

Let $\expect \mapsto \expect(\cdot|T)$, $X \mapsto \delta$, $m \mapsto \theta$, and $\expect X \mapsto \expect(\delta|T) = \delta'$. After substitution, take a real $\expect$ to both sides of the equation, and you'll get the decomposition.

!!! note "Old version of this proof"

    The decomposition holds because

    - $\expect \variant(\delta|T) = \expect \expect \left(\qty(\delta - \expect(\delta|T))^2 \middle| T\right) = \expect\qty(\delta-\delta')^2$ by definition and law of total expectation.
    - $2 \expect (\delta-\delta')(\delta'-\theta) = \expect \expect(\cdots|T)$. Given $T$, we know $\delta', \theta$, thus $(\delta-\delta')(\delta'-\theta)$ is an affine function of $\delta$. And by definition, $\expect(\delta|T) - \delta' = 0$, therefore the whole cross term is zero.

Besides, the inequality is also implied by Jensen's inequality, yielding out a more general Rao–Blackwell theorem where the square function can be changed to any convex “loss” function.

The **third** part is because $\expect \delta' = \expect \expect(\delta|T) = \expect \delta$.

#### Lehmann–Scheffé theorem

Suppose $\psi$ is another candidate unbiased estimator. By Rao–Blackwell theorem, $\psi' := \expect(\psi|T)$ is a valid unbiased estimator with smaller $\variant$.

Note that both $\delta$ and $\psi'$ are functions of $T$, so is $\delta - \psi'$, and $\expect(\delta - \psi') \equiv 0$ because they are both unbiased.

As $T$ is complete for $\theta$, $\expect(\delta - \psi') \equiv 0$ implies $\delta \equiv \psi'$ almost surely. Therefore, $\variant \delta = \variant \psi' \leq \variant \psi$.

## §3 Linear Models, §6 Best Linear Unbiased Estimation, and §8 Least Squares

### Setup

> :material-clock-edit-outline: 2023年10月30日，2023年10月31日。

There are two maps that can be assumed to be linear.

- **Data model** (parameters → distributions)

  $\theta \mapsto \expect X$ is linear, and $X - \expect X$ is exponentially distributed independently to $\theta$.

  $$
  \vb*{X} \sim \mathcal{N}(H \vb*{\theta}, C),
  $$

  where $H,C$ are known matrices.

- **Estimators** (samples → estimators)

  $X \mapsto \delta$ is linear.

  $$
  \vb*{\delta} = A \vb*{X},
  $$

  where $A$ is to be chosen. To work out a solution, we need to assume moments:

  $$
  \begin{aligned}
    \expect \vb*{X} &= H \vb*{\theta}, \\
    \variant \vb*{X} &= C, \\
  \end{aligned}
  $$

  where $H,C$ are known matrices.

In both cases, the _best_ unbiased estimator turns out to be

$$
\vb*{\delta} = (H^\dagger \Phi H)^{-1} H^\dagger \Phi \vb*{X},
$$

where $\Phi = C^{-1}$ is the precision matrix. In addition, $\variant \vb*{\delta} = (H^\dagger \Phi H)^{-1}$.

Note that _best_ in linear model means minimum variance among _all_ estimators, but _best_ in linear estimator means minimum variance among _linear_ estimators.

:material-eye-arrow-right: [Best Linear Unbiased Estimation (stat.duke.edu)](https://www2.stat.duke.edu/~pdh10/Teaching/721/Materials/ch2blue.pdf).

This is highly related to ordinary/generalized least squares, projection matrices and Moore–Penrose inverse.

1. If $\vb*{\delta}, \vb*{\delta'}$ are both linear unbiased estimator, then the difference $\vb*{\delta'} - \vb*{\delta} = B^\dagger \vb*{X}$, where $B \perp H$ (their columns spaces are perpendicular, or $B^\dagger H = O$) ——linearity throws the “$\expect$”.

2. If $\vb*{\delta} = A \vb*{X}$, then

  $$
  \begin{split}
     \variant \vb*{\delta'}
     &= (A + B^\dagger) (\variant \vb*{X}) (A^\dagger + B) \\
     &= A C A^\dagger + B^\dagger C B + A C B + (A C B)^\dagger.
  \end{split}
  $$

  The first term is $\variant \vb*{\delta}$, the second $\succeq 0$, and the last two terms are zero if $A = (H^\dagger \Phi H)^{-1} H^\dagger \Phi$ (a generalized inverse of $H$), because

  $$
  A C B
  = (\cdots) H^\dagger \Phi C B
  = (\cdots) H^\dagger B
  = (\cdots) O.
  $$

3. Therefore, for any $\vb*{\delta'}$, $\variant \vb*{\delta'} \succeq \variant \vb*{\delta}$ if $\delta$ is with that $A$.

### Constrained least squares

> :material-clock-edit-outline: 2023年12月4日。

Lagrangian multipliers:

$$
J = \frac12 (\vb*{x} -  H \vb*{\theta})^\dagger \Phi (\vb*{x} -  H \vb*{\theta}) + \vb*{\lambda}^\dagger (A \vb*{\theta} - \vb*{b}).
$$

Setting its $\pdv{\vb*{\theta}}$ and constraints to zero produces

$$
\begin{bmatrix}
  H^\dagger \Phi H & A^\dagger \\
  A & O \\
\end{bmatrix}
\begin{bmatrix}
  \vb*{\theta} \\ \vb*{\lambda}
\end{bmatrix}
=
\begin{bmatrix}
  H^\dagger \Phi \vb*{x} \\ \vb*{b}
\end{bmatrix}.
$$

# 注意

- Always check the prerequisite of the theorem.

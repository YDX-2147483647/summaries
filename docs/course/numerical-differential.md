---
relevant:
  - ./calculus-1.md
  - ./complex-functions-and-equations-of-mathematical-physics.md
  - ./linear-algebra.md
---

# 科学与工程计算

$$
\def\dif{\mathop{}\!\mathrm{d}}
$$

## 话题

> :material-clock-edit-outline: 2024年9月26日。

本课入口是（一维）两点边值问题，主要是二阶非齐次线性可变系数常微分方程：

$$
\begin{aligned}
y'' + p y' + q y = f, x \in (0,l). \\
\eval{y}_{x=0} = \alpha, \quad \eval{y}_{x=l} = \beta.
\end{aligned}
$$

一般要求 $\forall x, q \leq 0$，这是为了解存在且唯一。其道理大致如下：

1. 为简单，我们考虑齐次版本，或者说考虑解结构中的齐次部分。

2. 通过凑 $y'' + p y'$ 的微分，相应齐次方程可重述为 Sturm–Liouville 问题：$\mathcal{L} y = \lambda y$，其中特征值 $\lambda = 1$，算子

  \[
  \mathcal{L} y = \frac{1}{-q} \left(e^{\int p \dif x}\, y'\right)'.
  \]

  （这里之所以用 $-q$ 而非 $+q$，是为了能作后面内积的权重。）

  这种问题可看作 $\mathcal{L}$ 的特征分析问题——研究 $1$ 是不是 $\mathcal{L}$ 的特征值。

3. 两次分部积分，用齐次边界条件扔掉余项，可证明 $\mathcal{L}$ 在内积 $(\square, \triangle) \mapsto \int \square \triangle (-q) \dif x$ 的意义下 self-adjoint，因此特征值非负，$1$ 基本上是特征值，解正常存在。

4. 假设 $q > 0$，那内积和 $\mathcal{L}$ 定义中的 $-q$ 要改为 $+q$，齐次方程化出来是 $\mathcal{L} y = -y$，说明 $\mathcal{L}$ 有特征值 $-1$，与它 self-adjoint 矛盾，故解不存在。

这种做法还有助于理解变分法。

### 差商的误差

> :material-clock-edit-outline: 2024年9月26日。

用差商代微商难免有误差，估计误差的量级很有用。

例如二阶差商 $(y_{i+1} - 2 y_i + y_{i-1}) / h^2$：

- $y$ 是常数、一次函数时它都相互抵消为零；
- $y$ 是二次函数时它等于二次项系数的两倍，故可用于近似二阶导数。
- $y$ 是三次幂函数时它等于 $(h^3 - 0 + (-h)^3) / h^2 = 0$，故误差没有三阶项。
- $y$ 是四次幂函数时它等于 $(h^4 - 0 + h^4) / h^2 = 2 h^2$，故误差是 $2 h^2 / 4! = h^2/12$ 倍四阶导数量级。

（这种方法算出的误差满足“差商 = 微商 + 误差”，是其它定义的相反数。）

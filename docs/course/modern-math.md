---
math: typst
relevant:
  - ./probability-and-statistics.md
  - ./linear-algebra.md
  - ./set-theory.md
---

# 近代数学基础

!!! info "课程名称"

    本课讲的其实是“现代”数学的基础。

    - 近代数学一般是指高等数学，可分为代数、几何、分析。
    - 现代数学则指十九世纪末以来的数学，它用公理体系和结构观点统观数学，标志是集合论、非欧几何、非交换代数、分析的算术化。

## 集合与映射

> :material-clock-edit-outline: 2025年5月14日。

- 集合
- 映射
- 对等、势、可列、不可列
- 直线上的点集：确界、极限，确界原理
- 稠密
- 实数列的极限理论
  - 闭区间套定理
  - Bolzano–Weierstrass定理（有界数列必有收敛子列）
  - Cauchy收敛定理
  - 有限覆盖定理
- 实数上的连续函数：函数和函数列的一致连续

## 代数系统

> :material-clock-edit-outline: 2025年5月14日。

- 群
  - 内外运算
  - 半群、群
  - 对称群
  - 子群、同构
- 环、域

## 测度与积分

> :material-clock-edit-outline: 2025年5月14日。

!!! info "测度 ≠ 度量"

    测度是 measure，度量是 metric。

## 度量空间

### 概念

> :material-clock-edit-outline: 2025年5月14日。

- 度量、收敛
- 度量空间中的点集：内点、开集，聚点、闭集
- 连续映射、开映射
- 可分
- 完备
- 压缩映射原理（Banach不等点唯一存在定理）

### 评论

> :material-clock-edit-outline: 2025年5月16、17日。

导集与闭包的多种刻画：一点邻域与集合的相交情况，集合中点列能收敛的范围。

连续的多种刻画：ε–δ 作为距离、收敛、一点之像的邻域的原像总能覆盖该点的邻域、开集的原像总开（换成闭集同样成立）。

### 第二类Volterra积分方程解的存在性

> :material-clock-edit-outline: 2025年5月17日。

> :material-eye-arrow-right: [Volterra Integral Equation of the Second Kind -- from Wolfram MathWorld](https://mathworld.wolfram.com/VolterraIntegralEquationoftheSecondKind.html)

用压缩映射原理分析关于 $phi$ 的积分方程

$$
phi (x) equiv f(x) + integral K(x,y) phi(y) dif y
$$

的解的存在性，其中 $abs(K)$ 有上界 $M$。

从等式右侧到左侧是个映射，其不动点就是原方程的解。若它是压缩映射（采用 $L^oo$ 度量的连续函数空间），则存在不动点。因此积分方程解的存在性归结为映射的压缩性。

- 若积分区间为固定的 $[a,b]$，则 $M$ 必须充分小（小于 $1 / (b-a)$），才能保证有解。

- 若积分区间为变化的 $[a,x]$，则 $M$ 只要存在就能保证有解。

  因为无论 $M$ 多大，都能保证方程在开始的 $1/M$ 长度内有解，然后一段一段延长即可。

## 代数与拓扑相容的空间

### 概念

> :material-clock-edit-outline: 2025年5月14日。

- 赋范线性空间，依范数收敛，Banach空间
- $l^p$ 与 $L^p$ 空间
- 内积空间，平行四边形法则、Cauchy–Schwarz不等式，Hilbert 空间
- 正交集、正交规范基，Bessel 不等式、Parseval 等式
- 最佳逼近、投影定理

### 范数与内积

> :material-clock-edit-outline: 2025年5月16日。

范数升级为内积，关键在于内积是二元函数，这让线性的意义扩大了。范数的三角不等式到了内积，就是 Cauchy–Schwarz 不等式。

### Bessel 不等式与 Parseval 等式

> :material-clock-edit-outline: 2025年5月16日。

对于内积空间中的向量 $x in X$ 和正交规范向量之集合 ${e_alpha}_alpha$（其中指标 $alpha$ 可有无穷多），有如下结论。

1. 若限制 $alpha$ 只取前<u>有限</u>多个指标，则向量 $0$、$sum_alpha (x, e_alpha) e_alpha$、$x$ 构成直角三角形，三条边的范数满足勾股定理。

2. 若逐渐放松对 $alpha$ 的限制，由于 $norm(sum_alpha (x, e_alpha) e_alpha)^2 = sum_alpha abs((x, e_alpha))^2$ 一直被固定的 $norm(x)^2$ <u>限制</u>，它无法无限制地增长。

   事实上，由可数集的可数并仍可数，能论证 $(x, e_alpha)$ 最多只有可数项非零。

3. 现在完全不再限制 $alpha$，考虑<u>数</u>的和式 $sum_alpha abs((x, e_alpha))^2$。因为其中只有可数项非零，它是个合法的级数。由极限的保号性，它收敛且不超过 $norm(x)^2$，这称作 **Bessel 不等式**。

4. 继续考虑<u>向量</u>的和式 $sum_alpha (x, e_alpha) e_alpha$。如果其中有无穷项非零，它未必仍在空间中。不过根据系数的级数 $sum_alpha abs((x, e_alpha))^2$ 收敛，能证明向量的和式必然 <u>Cauchy 收敛</u>。

5. 如果这空间是 Hilbert 空间，<u>完备</u>，那么向量的和式收敛。于是向量 $0$、$sum_alpha (x, e_alpha) e_alpha$、$x$ 仍在空间内构成直角三角形，相应勾股定理仍成立。

6. ${e_alpha}_alpha$ 选得好时，一条直角边退化为点，这时 $norm(x)^2 = sum_alpha abs((x, e_alpha))^2$，这称作 **Parseval 等式**。

   事实上，以下三条等价。

   - ${e_alpha}_alpha$ 构成基（$x$ 可用它线性表示）
   - ${e_alpha}_alpha$ 完全（其正交补为零）
   - Parseval 等式成立

### 最佳逼近

> :material-clock-edit-outline: 2025年5月16日。

空间中一点到一子空间的最近点称作最佳逼近点。这是个拓扑概念，只需度量就能定义；而**内积**赋予了几何结构，最佳逼近点会有垂直性质。

若父空间是内积空间，子空间是线性空间（部分结论可能不需要），则

- 投影若存在，则唯一，而且是最佳逼近点。
- 最佳逼近点若存在，则唯一。（⇐ 平行四边形法则）
- 如果子空间**闭**，那么……
  - 最佳逼近点若存在，则就是投影。（⇐ 二次函数顶点）
  - 若父空间**完备**，则最佳逼近点存在。（⇐ 子空间内的 Cauchy 列能收敛到子空间内）

由此可得**投影定理**：若父空间完备，子空间闭，则投影唯一存在，并且是最佳逼近点。

## 算子与泛函

### 概念

> :material-clock-edit-outline: 2025年5月14、16日。

- 算子线性、有界、连续

  线性赋予了代数结构，于是一处的性质可以外推到别处。从而一点连续、处处连续、全局有界（由于线性，值域不可能有界，此处“有界”指放大倍数有界，即算子的范数有界）等价。

- 线性有界算子构成赋范线性空间，算子陪域的完备性蕴含了算子空间的完备性

# 注意

- 区分**正交规范**集与普通的向量集合。
- **空集**又开又闭。
- 群、度量空间等要求**非空**，环要求至少有两个元素。
- $L^p$ 或 $l^p$ 中的元素要求**范数有限**。
- 区分**充分**条件与**必要**条件。
- 同构要求**双射**。
- Lebesgue 测度的 $p$ 可以无穷。
- $L[a,b]$ 和 $L^1 [a,b]$ 意义相同，但 $C[a,b]$ 和 $C^0 [a,b]$ 意义相同。

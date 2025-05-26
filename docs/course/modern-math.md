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

### 共轭空间（对偶空间）

> :material-clock-edit-outline: 2025年3月27、30日，2025年5月26–27日。

0. 设 $p,q in [1, +oo]$ 是一对共轭指数，即满足 $1/p + 1/q = 1$。

  !!! info "共轭指数的等价公式"

      参考理想凸透镜成像公式，$1/p + 1/q = 1$ 等价于 $(p-1) (q-1) = 1$，$p q = p + q$，$p\/q = p-1$ 等。

1. 任何序列 $f in l^p$（可以无限长）都可诱导出映射 $F: l^q -> CC$——

  $$
  u |-> F(u) = sum_n f_n u_n.
  $$

  - 可以证明这种诱导保范，即 $norm(f)_p = norm(F)$，从而总收敛。
  - 这种诱导是单射：取序列空间标准的基 ${e^((n))}_n$，则 $F(e^((n)))$ 就是 $f_n$。

2. 其实 $F$ 是 $l^q$ 上的有界线性泛函，它所在的空间称作 $l^q$ 的共轭空间 $(l^q)^*$。以上命题其实是说，$(l^q)^*$ 存在子空间（在保范线性的意义下）与 $l^p$ 同构。

3. 若 $q < +oo$，可以证明这个子空间就是 $(l^q)^*$ 本身；若 $q = +oo$，则在通常的公理下，$(l^oo)^* supset.neq l^1$，称作 ba space（ba 表示 bounded additive）。

!!! note "保范"

    $F: l^q -> CC$ 的范数

    $$
    norm(F)
    &:= sup_(norm(u)_q = 1) abs(F(u))
    &= sup_(norm(u)_q = 1) abs(sum_n f_n u_n)
    &= sup_(norm(u)_q = 1) sum_n abs(f_n u_n).
    $$

    下面证明它等于 $norm(f)_p$。

    - **上界**：$forall u, norm(u)_q = 1 => abs(F(u)) <= norm(f)_p$

      分类讨论。若 $p = +oo$，则 $abs(u)$ 在目标 $abs(f u)$ 与限制 $abs(u)^q$ 中的倍率相同，一分钱一分货，把 $abs(u)$ 完全布置到 $abs(f)$ 最大处即最大化目标，于是 $abs(F(u)) = sup abs(f)$，刚好是 $norm(f)_oo$。下面只讨论 $p < +oo$ 的情形。

      由 $1 <= p < +oo$，根据 $y |-> y^p$ 在 $RR_(>=0)$ 的凸性，任取随机变量 $xi$ 和非负函数 $h$，$EE^p thin h(xi) <= EE thin h^p (xi)$。

      取分布列为 $abs(u)^q$，取 $h := abs(f) thin abs(u)^(1-q)$，$h^p = abs(f)^p abs(u)^(-q)$，则上述不等式化为

      $$
      (sum abs(f) thin abs(u)^(1-q) dot abs(u)^q)^p <= sum abs(f)^p abs(u)^(-q) dot abs(u)^q,
      $$

      也就是

      $$
      (sum abs(f) thin abs(u))^p <= sum abs(f)^p,
      $$

      即 $abs(F(u))^p <= norm(f)_p^p$。

    - **取等**：$exists u, norm(u)_q = 1 and abs(F(u)) = norm(f)_p$

      凸性不等式的取等条件是 $h$ 为常值，即 $abs(f)^p$ 与 $abs(u)^q$ 成比例。这样的 $u$ 显然存在。

!!! tip "Hölder 不等式"

    以上保范命题其实几乎是 Hölder 不等式。

    $sum_n abs(f_n u_n)$ 就是 $norm(f u)_1$，然后由范数的齐次性，$norm(u)_q = 1 ==> norm(f u)_1 <= norm(f)_p$ 相当于 $norm(f u)_1 <= norm(f)_p norm(u)_q$。

    另外，Hölder 不等式还可推广到一般的 $1/p' + 1/q' = 1/r'$，得到 $norm(f' u')_r' <= norm(f')_p' norm(u')_q'$。证明只需取 $(p,q) := (p',q') \/ r'$，$abs(f)^p := abs(f')^p', abs(u)^q := abs(u')^q'$ 即可。

!!! note "$supset.neq$ 还是 $=$"

    $(l^q)^* supset.neq l^p$ 还是 $(l^q)^* = l^p$，问题在于从 $l^p$ 序列到 $(l^q)^*$ 泛函的诱导关系 $f |-> F$ 是不是满射。

    等一下，我们刚才证明单射时，已经事实上给出了诱导关系的逆：输入泛函 $F in (l^q)^*$，输出序列 $n |-> F(e^((n)))$。难道这个映射不适用于整个 $(l^q)^*$ 吗？

    适用，但输出结果的范数 $norm(dot)_p$ 未必有限，从而未必属于 $l^p$。让我们分析几个例子，分析后会发现 $norm(dot)_p < +oo$ 并不平凡。

    - $p = +oo, q = 1$ 时，$(l^1)^* = l^oo$

      $norm(F(e^((dot))))_p = sup abs(F(e^((dot)))) = sup norm(F) dot norm(e^((dot))) = norm(F) < +oo$。

    - $p = 2 = q$ 时，$(l^2)^* = l^2$

      $l^2$ 可以定义内积，有正交补的概念。$F: l^2 -> CC$，$dim im F <= dim CC = 1$，故 $dim (ker F)^perp = dim l^2 \/ ker F = dim im F <= 1$。于是，$F(e^((dot)))$ 要么为零，要么就在一维的 $(ker F)^perp$ 中，所以 $norm(F(e^((dot))))_2 < +oo$。

    - $p = 1, q = +oo$ 时，$(l^oo)^* supset.neq l^1$

      $norm(F(e^((dot))))_p = sum abs(F(e^((dot))))$，这有无穷项，似乎没有什么特别的理由收敛。

# 注意

- 区分**正交规范**集与普通的向量集合。
- **空集**又开又闭。
- 群、度量空间等要求**非空**，环要求至少有两个元素。
- $L^p$ 或 $l^p$ 中的元素要求**范数有限**。
- 区分**充分**条件与**必要**条件。
- 同构要求**双射**。
- Lebesgue 测度的 $p$ 可以无穷。
- $L[a,b]$ 和 $L^1 [a,b]$ 意义相同，但 $C[a,b]$ 和 $C^0 [a,b]$ 意义相同。

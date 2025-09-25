---
math: typst
math-preamble: |
  #let image = math.op("image")
  #let kernel = math.op("kernel")

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

> :material-clock-edit-outline: 2025年5月16、17日，2025年9月22日。

导集与闭包的多种刻画：一点邻域与集合的相交情况，集合中点列能收敛的范围。

连续的多种刻画：ε–δ 作为距离、收敛、一点之像的邻域的原像总能覆盖该点的邻域（或者说，该点存在能被覆盖的邻域）、开集的原像总开（换成闭集同样成立）。

### 映射保持拓扑结构的程度

> :material-clock-edit-outline: 2025年5月27日，2025年9月17、22日。

> :material-eye-arrow-right: [两个拓扑空间间的闭映射一定是开映射吗？ - 知乎](https://www.zhihu.com/question/303043369)

对于拓扑空间 $X,Y$，映射 $f: X->Y$ 定义了以下几种性质。

- **连续**映射：$Y$ 中的开集 $U$ ⇒ $X$ 中的 $f^(-1)(U)$ 开；或者等价地说，$Y$ 中的闭集 ⇒ $X$ 中的 $f^(-1)(U)$ 闭。
- **商**映射（强连续映射）：$Y$ 中的开集 $U$ ⇔ $X$ 中的 $f^(-1)(U)$ 开；或者等价地说，$Y$ 中的闭集 $U$ ⇔ $X$ 中的 $f^(-1)(U)$ 闭。
- **开**映射：$X$ 中的开集 $U$ ⇒ $Y$ 中的 $f(U)$ 开。
- **闭**映射：$X$ 中的闭集 $U$ ⇒ $Y$ 中的 $f(U)$ 闭。

注意，连续映射、商映射的定义谈论原像 $f^(-1)$，这时用开集、闭集讨论一样；然而开映射、闭映射的定义谈论像 $f$，这时用开集、闭集讨论不同。原因在于，补的原像总是原像的补，但补的像未必是像的补——$X$ 中的集合 $A$ 在映射 $f$ 下不一定“饱和”，可能有 $A$ 之外的元素同样能映射到 $f(A)$ 里，即可能 $A subset.neq f^(-1) (f (A))$。若 $f$ 是单射，则用开集、闭集讨论等价。

另外注意，缩小集合时，即使保持邻域结构，也可能改变子集的开闭。考虑某点的邻域，缩小集合时这邻域也会缩减，导致更容易出现开集和闭集，更不容易出现既不开也不闭的子集。例如 $RR^3$ 缩减为 $RR^2 times {0}$，考虑子集 $[0,1]^2 times {0}$，它从既不开也不闭变成了闭。

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

### 常见空间模型

> :material-clock-edit-outline: 2025年5月17–18日，2025年9月28日。

- $l^p$ Lebesgue 可和序列

  完备，包括 $p = +oo$ 时。

  - $p < +oo$ 时可分，“仅前有限项非零的序列”是其可数稠密子集
  - $p = +oo$ 时不可分，${0,1}^oo$ 两两间距为 $1$，却有不可数个。

  $p < +oo$ 时 $l^p$ 的共轭空间与 $l^q$ 同构，其中 $1/p + 1/q = 1$。$l^oo$ 的共轭空间会比 $l^1$ 大，并不同构，可能还和公理有关。

- $L^p [a,b]$ Lebesgue 可积函数

  完备，包括 $p = +oo$ 时。

  - $p < +oo$ 时可分，有界连续函数在其中稠密。
  - $p = +oo$ 时不可分，区间的示性函数两两间距为 $1$，却有不可数个。

- $C[a,b]$ 连续函数（默认 $L^oo$ 度量，对应一致收敛）

  可分，有理系数多项式是其可数稠密子集。

  在配套度量下，完备；若换用 $L^1$ 度量，会减弱为逐点收敛，就不完备了。

## 算子与泛函

### 各种结构

> :material-clock-edit-outline: 2025年9月22日。

> :material-eye-arrow-right: [245B, notes 3: $L^p$ spaces | What's new](https://terrytao.wordpress.com/2009/01/09/245b-notes-3-lp-spaces/)

为了允许各种有意义的操作，函数（算子）空间经常具备以下若干结构，以及某些结构之间的兼容条件。（不过通常并非以下全部结构）

- 代数
  - **向量空间** vector space：加法、数乘。不过通常无穷维。
  - **代数** algebra：某种乘法，比如逐点相乘、卷积；或者共轭空间之类的。
  - **群操作** group actions：描述函数空间的对称性，比如旋转、反射、平移、调制、拉伸，甚至 Lie 群之类的。群操作还生出表示理论、Fourier分析等手法。
- 拓扑
  - **范数** norm：描述一个函数的大小。与数域不同，函数空间有高、宽、振荡、正则、衰减快慢等许多性质，所以也有许多种范数。为兼容向量空间，设置三角不等式；为兼容代数结构，设置齐次性。
  - **度量** metric：描述两个函数的距离，可由合适的范数结构诱导。收敛、完备等话题依赖度量结构。紧性也属于度量结构，可惜函数空间通常不具备。
  - **拓扑** topology：描述相邻、开闭、收敛等。保持拓扑结构引出了连续概念。合适的度量结构会诱导一种拓扑。
- 混合
  - **泛函** functional：把函数转换成更简单的数研究。范数、积分、求值都是泛函，另外内积结构会诱导一类泛函。泛函所在的空间还引出对偶概念。
  - **内积** inner product：描述两个函数之间的相互作用或关系。除了通常的共轭积之和，还有 $(f,mu) |-> integral f dif mu$ 这种两个函数分属不同空间的内积。合适的范数可与内积相互诱导。Cauchy–Schwarz 不等式和正交是内积结构引出的有力工具。为与向量空间兼容，设置与标量域匹配的双线性。
- **序** order：描述函数之间的大小关系，比如非负、“控制”、最大等。

函数空间似乎不太考虑**测度** measure，大概因为通常无穷维，定量的测度手段容易遇到困难。往往可用定性的拓扑手段解决。

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

    - $p = 2 = q$ 时，$(l^2)^* = l^2$（$l^2$ 自共轭）

      $l^2$ 可以定义内积，有正交补的概念。$F: l^2 -> CC$，$dim im F <= dim CC = 1$，故 $dim (ker F)^perp = dim l^2 \/ ker F = dim im F <= 1$。于是，$F(e^((dot)))$ 要么为零，要么就在一维的 $(ker F)^perp$ 中，所以 $norm(F(e^((dot))))_2 < +oo$。

    - $p = 1, q = +oo$ 时，$(l^oo)^* supset.neq l^1$

      $norm(F(e^((dot))))_p = sum abs(F(e^((dot))))$，这有无穷项，似乎没有什么特别的理由收敛。

    - 若取有限数 $N$，只考虑 $l^p$、$l^q$ 中最多前 $N$ 项非零的子集 $V_p, V_q$，则 $V_p = V_q$（此处不是保范同构，仅在集合的意义上），并且 $V^p = (V^q)^* = (V^p)^(**)$（此处是保范同构），即 $V_p$ 自反。

### 开映射定理

> :material-clock-edit-outline: 2025年9月19、22日。

之所以要关心映射 $T: X -> Y$ 的这些性质，是因为它与关于 $x$ 的方程 $T x = y$ 的解的性质紧密相关。考虑 $Y ->^U X ->^T Y ->^V X$：

- 若总**存在**解（$forall y, exists x, T x = Y$），则 $T$ 是满射，$T U: Y -> Y$ 可以是恒等映射，即存在 $U$ 是 $T$ 的右逆。
- 若总无解或最多**一解**（$forall y, T x_1 = y = T x_2 => x_1 = x_2$），则 $T$ 是单射， $V T: X -> X$ 可以是恒等映射，即存在 $V$ 是 $T$ 的左逆。
- 在总有唯一解的基础上（$T^(-1)$ 存在），若解**稳定**（$x_0 = T^(-1) y_0$ 随 $y_0$ 连续变化），则 $T^(-1): Y -> X$ 连续，也即 $T: X -> Y$ 是开映射。

对于线性算子，特别是线性有界算子，这些条件可以进一步简化。

> :material-eye-arrow-right: [245B, Notes 9: The Baire category theorem and its Banach space consequences | What's new](https://terrytao.wordpress.com/2009/02/01/245b-notes-9-the-baire-category-theorem-and-its-banach-space-consequences/)

先分析开映射。开映射是全局概念，但对于线性算子，可等价转换为一点邻域的性质，特别是原点邻域的性质——这与连续类似。具体如下。

- 开映射 ⇒ “定量”可解性

  1. 若 $T$ 是**开映射**，则 $T(B_X (0,1))$ 开，$exists r > 0, B_Y (0, r) subset T(B_X (0,1))$。换句话说，$forall norm(y) < r, exists x in X, y = T x and norm(x) < 1$，进而 $norm(x) < norm(y) \/ r$。
  2. 由于 $T$ 和 $norm(x) < norm(y) \/ r$ 都**齐次**，上述命题的前提 $norm(y) < r$ 可去掉，于是得到 $exists r > 0, forall y, exists x, y = T x and norm(x) < norm(y) \/ r$。
  3. 总结一下，$exists C > 0, forall y, exists x, y = T x and norm(x) < C norm(y)$——这一条件姑且称做“定量”可解性。

- “定量”可解性 ⇒ 开映射

  1. 由“定量”**可解性**，$forall norm(y) < 1, exists x, y = T x and norm(x) < C norm(y) < C$，于是 $forall norm(y) < 1, exists norm(x) < C, y = T x$，即 $B_Y (0, 1) subset T(B_X (0, C))$。
  2. 由于 $T$ 和 $B_Y (0, 1) subset T(B_X (0, C))$ 都**齐次**，任取 $X$ 中以原点为中心的开球 $B_X (0,r)$，它的像都包含开球 $B_Y (0, r\/C)$，所以是开集。
  3. 由于 $T$ **线性**，以上可外推至 $X$ 中一般的开集，从而 $T$ 是开映射。

!!! note "与有界性的区别"

    注意“定量”可解性不同于 $T$ 有界。$T$ 有界可以仿照描述为 $exists C > 0, forall x, exists y, y = T x and norm(y) < C norm(x)$。这种“对仗”正如开映射与连续映射。

注意“定量”可解性显然可推出“定性”可解性（指解的存在性，$forall y, exists x, y = T x$，也即 $T$ 是满射）。[**开映射定理**（open mapping theorem）](https://en.wikipedia.org/wiki/Open_mapping_theorem_(functional_analysis))指出，对于 $T in B(X,Y)$ 的**完备**情形，“定量”可解性不仅是“定性”可解性的充分条件，还是必要条件。“定量”可解性其实对应解方程时附加的正则项。开映射定理指出，添加这个定则项仅仅是表面上弱化问题，实际上仍然等价。

下面简要介绍开映射定理的证明。

1. 定义 $E_n := {y in Y : exists x, y = T x and norm(x) <= n norm(y)}$，则“定性”可解性等价于 $union.big_(n in NN) E_n = Y$。
2. 由于 **$Y$ 完备**，故也是 [Baire 空间](https://en.wikipedia.org/wiki/Baire_space)，所以确定存在某个 $n$ 保证 $E_n$ 不是无处稠密的。也就是说，$E_n$ 在某个开球 $B(y_0, r)$ 内稠密，即 $forall epsilon > 0, forall y in B(y_0, r), exists x, norm(y - T x) <= epsilon and norm(x) <= n norm(y)$。（$x$ 相当于 $y = T x$ 的近似解）
3. 利用 **$T$ 可加**，取两个这样的 $y$，可把结论转换到原点附近，具体来说是 $forall epsilon > 0, forall y in B(0, 2r), exists x, norm(y - T x) <= 2 epsilon and norm(x) <= 2n (r+epsilon)$。利用**齐次**性，再进一步去掉 $y$ 的限制，转换为 $forall y, forall epsilon > 0, exists x, norm(y - T x) <= 2 epsilon and norm(x) <= 2n (1+epsilon) norm(y)$。
4. 由于 **$X$ 完备**、$T$ 连续，可取极限 $epsilon -> 0$，得到 $forall y, exists x, y = T x and norm(x) <= 3n norm(y)$，即“定量”可解性。

开映射定理有一等价命题：**逆算子定理**（bounded inverse theorem）指出，若 $T in B(X,Y)$ 不仅是满射，还是双射，则 $T^(-1)$ 连续。

### 闭图像定理

> :material-clock-edit-outline: 2025年9月23–24日。

映射 $T: X -> Y$ 的[图像](https://en.wikipedia.org/wiki/Graph_of_a_function)是指 $X times Y$ 平面内的子集 ${ (x, T x) : x in X }$。这样定义既符合绘图习惯，又有数学上的优势。

- 图像是一种看待函数的视角，有些性质用图像描述更直观。例如，“向下凸”等价于[图像“上方”的区域](https://en.wikipedia.org/wiki/Epigraph_(mathematics))是凸的。

- 图像连接了函数的定义域和值域，$X in.rev x <-> (x, T x) |-> T x in image f$。第一步从定义域到图像，必为双射，且其逆连续；第二步从图像到值域，如果空间允许定义连续，那么也连续。此外两步都会继承 $T$ 的性质。

- 用图像可以捕捉更弱的函数，以及函数更弱的性质。

  - 即使函数只在 $D subset.neq X$ 上有定义，也可用 $X times Y$ 中的图像描述，不丢弃 $X$ 的好性质。

  - 记 $y_n = T x_n$。函数具有**闭图像**是指图像是闭集，即若 $x_n -> x$，且 $y_n -> y$，则 $y = T x$；而函数连续是指若 $x_n -> x$，则 $y_n -> y$，且 $y = T x$。由此可见，闭图像性质是连续的必要条件。

    闭图像性质确实比连续弱。求导算子就有闭图像，但无界，所以不连续。

!!! info "名称"

    闭图像性质的“闭”和开映射的“开”指不同东西，两个概念并无直接关系。

    具有闭图像性质的映射最好不要简称为“闭映射”，不然会与[描述拓扑结构的那种“闭映射”](#映射保持拓扑结构的程度)混淆。

继续[开映射定理](#开映射定理)的话题。连续反映方程解的稳定性，条件在线性时可能简化。[闭图像定理（closed graph theorem）](https://en.wikipedia.org/wiki/Closed_graph_theorem_(functional_analysis))指出，对于完备空间之间的线性映射，闭图像性质不仅是连续的必要条件，还是充分条件。

下面简要介绍闭图像定理的证明。若 $T$ 具有闭图像，则图像本身构成完备空间。考虑 $x <-> (x, T x) |-> T x$。第一步的逆是是连续双射，由开映射定理，它正过来也连续。于是 $x |-> y$ 是两个连续映射的串联，从而连续。

图像是看待函数的视角，应用到各领域都有类似的闭图像定理。以上介绍的是泛函分析版本，其它版本可参考[陶哲轩的总结](https://terrytao.wordpress.com/2012/11/20/the-closed-graph-theorem-in-various-categories/)。

### 谱论

> :material-clock-edit-outline: 2025年9月25、28日。

特征值理论推广到无穷维空间就是谱论。对于线性变换 $T: X -> X$，考虑方程 $T x = λ x$ 的解的情况，其中 $λ in CC$。这归结为分析 $T_λ := T - lambda I$ 的核与像（值域）。

#### 核与像的性质

对于有限维空间，$X$ 与 $kernel T_λ plus.circle image T_λ$ [等价](https://en.wikipedia.org/wiki/Rank–nullity_theorem)，单射（$kernel T_λ = {0}$）与满射（$image T_λ = X$）相互蕴含；但对于无限维空间，$X$ 可能更大，有更多内容。

- **核**的性质——空间中不同的两点是否必有不同的像

  分类：名副其实的单射、名不副实的单射、非单射

  若把“不同”理解为“不相等”，则描述映射是否是<u>集合</u>论意义上的单射；若给空间附加<u>度量</u>结构，把“不同”理解为“相距较远”，则描述放大倍数 $norm(T (x_1 - x_2)) \/ norm(x_1 - x_2)$ 是否存在正的下界。“放大倍数有下界”比“始终不相等”更强，据此可将单射进一步区分为“名副其实的单射”与“名不副实的单射”。

  对于有限维空间，将映射按基分解后，放大倍数的下界会归结为有限个数的下界，所以单射都名副其实。对于无限维空间，下界可能涉及无限多数，未必如此。

- **像**的性质——空间中任意点是否都存在某点的像与之相同

  分类：满射、半满不满、很空

  若把“相同”理解为“相等”，则描述映射是否是<u>集合</u>论意义上的满射；若给空间附加<u>度量</u>结构，把“相同”理解为“相距较近”，则描述像在陪域中是否稠密。“像稠密”比“像不满”更强，据此可将非满射进一步区分为“半满不满”与“很空”两种。

  对于有限维空间，将空间以及像按基分解后，可证明不存在稠密的真子空间，所以不存在半满不满的映射。对于无限维空间，基必须加上系数才能确定子空间（参考 [Hamel 基](https://en.wikipedia.org/wiki/Basis_(linear_algebra)#Hamel_basis)与 [Schauder 基](https://en.wikipedia.org/wiki/Schauder_basis)的区别），无法保证如此。

!!! note "例：名不副实的单射"

    考虑 $l^oo$ 上的变换 $(a, b, c, ...) |-> (a/1, b/2, c/3, ...)$。它是单射，但会把 $0, e_n$ 分别映射到 $0, 1/n e_n$，放大倍数可以任意接近零。

!!! note "例：半满不满的映射"

    考虑 $l^1$ 上的变换 $(a, b, c, ...) |-> (a/1, b/2, c/4, ...)$。它不是满射，因为可和序列的“原像”未必可和；不过像仍然稠密，因为总可用前有限项逼近过去。

    比如 $y = (1, 1/2, 1/4, ...) in l^1$。假如存在 $x$ 满足 $y = T x$，则 $x$ 必为 $(1,1,1,...) in.not l^1$，所以 $y$ 在像空间之外。不过 $y$ 与像空间很接近，只要依次映射 $(1, 0, ...), (1,1,0,...), (1,1,1,0,...), ...$，就能让像逐渐收敛到 $y$。

!!! note "例：不满的单射"

    考虑 $l^oo$ 上的变换 $(a,b,c,...) |-> (0,a,b,c,...)$（右移），它不满（而且很空），但是单射（名副其实）。映射前后表面上减少了维度，但实际上又等势——这正是无限维的定义。

#### 谱的划分

根据核、像的性质，可将 $CC$ [划分](https://en.wikipedia.org/wiki/Decomposition_of_spectrum_(functional_analysis))为 $rho union sigma = rho union sigma_p union sigma_c union sigma_r$：

- $sigma$ 谱点，谱集——不满或不单，$kernel T_λ != {0} or image T_λ subset.neq X$

  - $sigma_p$ **点谱** point，特征值——不单（有非零解），$kernel T_λ != {0}$

    $kernel T_λ$ 是 $T$ 的特征子空间，直接反映 $T$ 的性质。

    有时 $kernel T_λ$ 还不够充分，需进一步考虑 $kernel (T_λ)^2, kernel (T_λ)^3, ...$ 等一[串](https://en.wikibooks.org/wiki/Linear_Algebra/Strings)不变子空间，最终拆分成 Jordan 标准形。

  - 无限维特有情况——不满的单射，$kernel T_λ = {0} and image T_λ subset.neq X$

    - $sigma_c$ **连续谱** continuous——像稠密，$overline(image T_λ) = X$
    - $sigma_r$ **剩余谱** residual——像不稠密，$overline(image T_λ) subset.neq X$

    连续谱与剩余谱的区别取决于度量结构。

- $rho$ 正则点，[预解集](https://en.wikipedia.org/wiki/Resolvent_set)——双射，$kernel T_λ = {0} and image T_λ = X$

  这是最常见的情况。

正则点与谱点的区别取决于空间范围。

!!! note "例：双边序列的右移映射"

    - 若按 $l^oo (ZZ)$，则 $sigma_p = sigma = TT := { λ : abs(λ) = 1 }$，$λ in sigma_p$ 对应的特征向量是复指数序列 $(..., λ^(-1), 1, λ, λ^2, ...)$。
    - 若按 $l^2 (ZZ)$，由于复指数序列不再属于空间，则 $sigma_c = sigma = TT := { λ : abs(λ) = 1 }$，点谱换成了连续谱。

<figure id="spectrum-decomp" markdown="span">
  <style>
    #spectrum-decomp {
      table {
        border: none;
      }
      th, td {
        border: .05rem solid var(--md-typeset-table-color);
        vertical-align: middle;
        text-align: center;
      }
      th {
        min-width: 3rem;
        padding-inline: 0.5em;
      }
    }
  </style>
  <table markdown="span">
    <caption>一般空间中有界线性变换的谱</caption>
    <tr>
      <th rowspan="3" colspan="3"></th>
      <th scope="col" colspan="3">核的性质</th>
    </tr>
    <tr>
      <th scope="col" colspan="2">单射</th>
      <th scope="col" rowspan="2">非单射</th>
    </tr>
    <tr>
      <th scope="col">名副其实</th>
      <th scope="col">名不副实</th>
    </tr>
    <tr markdown="span">
      <th scope="row" rowspan="3">像的性质</th>
      <th scope="row" colspan="2">满射</th>
      <td markdown="span">正则 $rho$</td>
      <td markdown="span">$nothing$</td>
      <td rowspan="3" markdown="span">点谱 $sigma_p$</td>
    </tr>
    <tr markdown="span">
      <th scope="row" rowspan="2">非满射</th>
      <th scope="row">半满不满</th>
      <td markdown="span">$nothing$</td>
      <td markdown="span">连续谱 $sigma_c$</td>
    </tr>
    <tr markdown="span">
      <th scope="row">很空</th>
      <td colspan="2" markdown="span">剩余谱 $sigma_r$</td>
    </tr>
  </table>
  <table markdown="span">
    <caption>有限维空间中线性变换的谱</caption>
    <tr>
      <th rowspan="2" colspan="2"></th>
      <th scope="col" colspan="2">核的性质</th>
    </tr>
    <tr>
      <th scope="col">单射（名副其实）</th>
      <th scope="col">非单射</th>
    </tr>
    <tr markdown="span">
      <th scope="row" rowspan="2">像的性质</th>
      <th scope="row">满射</th>
      <td markdown="span">正则 $rho$</td>
      <td markdown="span">$nothing$</td>
    </tr>
    <tr markdown="span">
      <th scope="row">非满射（很空）</th>
      <td markdown="span">$nothing$</td>
      <td markdown="span">点谱 $sigma_p$</td>
    </tr>
  </table>
</figure>

!!! note "两个 $nothing$ 的来源"

    - “双射”都是“名副其实的单射”

      对于双射，“放大系数有下界”等价于“逆映射有界”。[逆算子定理](#开映射定理)保证了这一点。

    - “名副其实的单射”不可能“半满不满”

      设 $T$ 的放大系数有下界，首先证明 $image T$ 必为闭集。任取收敛列 ${y_n}_n subset image T$，并配套选取序列 ${x_n}_n$ 满足 $forall n, T x_n = y_n$。由 $T$ 的放大系数有下界，以及 ${y_n}_n$ Cauchy 收敛，可知 ${x_n}_n$ Cauchy 收敛。由 $X$ 完备，可设 $x := lim_n x_n$。构造 $y := T x$，则由 $T$ 连续，$y_n -> y in image T$。

      既然像必为闭集，那么稠密（不很空）就意味着是全集（满射），所以不可能出现稠密的真子集（半满不满）。

# 注意

- 区分**正交规范**集与普通的向量集合。
- **空集**又开又闭。
- 群、度量空间等要求**非空**，环要求至少有两个元素。
- $L^p$ 或 $l^p$ 中的元素要求**范数有限**。
- 区分**充分**条件与**必要**条件。
- 同构要求**双射**。
- Lebesgue 测度的 $p$ 可以无穷。
- $L[a,b]$ 和 $L^1 [a,b]$ 意义相同，但 $C[a,b]$ 和 $C^0 [a,b]$ 意义相同。
- 有些字母有多种意义。
  - $L(X,Y)$ 表示 $X -> Y$ 线性（linear）映射，但是 $L[a,b]$ 表示 $L^1 [a,b]$（Lebesgue）。
  - $B(X,Y)$ 表示完备（Banach）的 $L(X,Y)$，但是 $B(x,r)$ 表示以 $x$ 中心、$r$ 为半径的开球（ball）。

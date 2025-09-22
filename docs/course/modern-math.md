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

首先分析开映射。开映射是全局概念，但对于线性算子，可等价转换为一点邻域的性质，特别是原点邻域的性质——这与连续类似。具体如下。

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

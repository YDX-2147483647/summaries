---
relevant:
  - ./physics-2.md
  - ./complex-functions-and-equations-of-mathematical-physics.md
---

# 理论物理导论

$$
\def\R{\mathbb{R}}
$$

## 2 薛定谔方程

### 旧量子论

> :material-clock-edit-outline: 2021年10月16日。

- 黑体辐射 Planck 1900

  综合高频的 Wien 公式与低频的 Ray leigh–Jeans 公式时，提出了能量量子化 $\varepsilon_0 = h\nu$。

- 光电效应 Einstein 1905

  光电效应中电子会即时逸出，且存在截止频率。为此提出光是粒子流，每个光子携带 $h\nu$ 的能量，$E_{km} = h\nu - W_0$。后来又提出 $E^2 = m_0^2 c^4 + p^2 c^2$ 等。

- 原子光谱 Bohr 1913

  定态、跃迁。只适用于氢原子这样的简单体系。

光的粒子性在 Compton 散射（1923）中得到直接证明。

$$
\begin{aligned}
    E &= hv = \hbar \omega. \\
    \vb*{p} &= \frac{h}{\lambda} = \hbar \vb*{k}.
\end{aligned}
$$

⇒波粒二象性。

### 波函数

> :material-clock-edit-outline: 2021年10月16日。

> 经典平面波：$y = A\sin(\omega t- \vb*{k}\vdot\vb*{x} + \varphi_0)$。

$\abs{\Psi}^2$ 表示概率密度。（统计解释，1926，M. Born）

由物理意义，波函数必须有限、单值、连续（对位置连续可微、平方可积）。（标准条件）

由于 $\abs{a+b}^2 = \abs{a}^2 + \abs{b}^2 + {\color{red} a^*b+ ab^*}$，存在**线性叠加态**。

> $z^*$ 表示 $z$ 的共轭复数。

波函数的演化符合薛定谔（Schrödinger）方程：

$$
i\hbar \pdv{t} \Psi = \vu*{H} \Psi, \quad \vu*{H} =-\frac{\hbar^2 \laplacian}{2m} + U.
$$

> - $-i\hbar \grad$ 类似动量，$\vb*{p}^2/2m$ 是动能。
> - $U$ 是势能。

$U$ 不显含 $t$ 时称作“定态”。此时可分离变量：设 $\eval{\Psi}_{\vb*{r},t} = \eval{\psi}_{\vb*{r}} \eval{f}_t$。得到

$$
\begin{cases}
    i \hbar \pdv{t}f &= E f. \\
    \va*{H} \psi &= E \psi.
\end{cases}
$$

> 其中 $E$ 是常数，物理意义是能量。

解得 $f \propto \exp(-i \omega t)$，其中 $\omega = E/\hbar$。

### 高斯积分

> :material-clock-edit-outline: 2021年10月16日。

最基础的：

$$
\begin{aligned}
    \int\limits_{-\infty}^{+\infty} \exp(-\frac{x^2}{2}) \dd{x} &= \sqrt{2\pi}. \\
    \int\limits_{-\infty}^{+\infty} \exp(-x^2) \dd{x} &= \sqrt{\pi}. \\
    \int\limits_{-\infty}^{+\infty} \exp(-a^2x^2) \dd{x} &= \frac{\sqrt{\pi}}{a}. \\
\end{aligned}
$$

> 证明：
>
> $$
> \begin{split}
>     \qty( \int\limits_{\R} \exp(-\frac{x^2}{2})\dd{x} )^2
>     &= \iint\limits_{\R^2} \exp(-\frac{x^2 + y^2}{2}) \dd{x}\dd{y} \\
>     &= \int\limits_0^{2\pi} \dd{\theta} \int\limits_{0}^{+\infty} \exp(-\frac{r^2}{2}) r\dd{r} \\
>     &= 2\pi \int\limits_{0}^{+\infty} \exp(-\frac{r^2}{2}) \dd{\frac{r^2}{2}} \\
>     &= 2\pi. \\
> \end{split}
> $$
>
> 又 $\int_{\R} \exp(-x^2/2) \dd{x} > 0$，故为 $\sqrt{2\pi}$。

乘上 $x^n$：

$$
\int\limits_\R x^n \exp(-\frac{x^2}{2}) \dd{x} = \begin{cases}
    (n-1)!! \sqrt{2\pi} & n\text{是偶数}, \\
    0 & n\text{是奇数}, \\
\end{cases}
$$

以及

$$
\int\limits_0^{+\infty} x^n \exp(-\frac{x^2}{2}) \dd{x} = \begin{cases}
    (n-1)!! \sqrt{\frac\pi2} & n\text{是偶数}. \\
    (n-1)!!= 2^{\frac{n-1}{2}} \qty(\frac{n-1}{2})! & n\text{是奇数}. \\
\end{cases}
$$

> 证明：
>
> $$
> \begin{aligned}
>  \int\limits_\R x^n \exp(-\frac{x^2}{2}) \dd{x}
>  &= \int\limits_\R x^{n-1} \exp(-\frac{x^2}{2}) \dd{\frac{x^2}{2}} \\
>  &= -\int\limits_\R x^{n-1} \dd{\exp(-\frac{x^2}{2})} \\
>  &= -\eval{ x^{n-1} \exp(-\frac{x^2}{2})}_{-\infty}^{+\infty}
>         + \int\limits_\R \exp(-\frac{x^2}{2}) \dd{\qty(x^{n-1})} \\
>     &= (n-1) \int\limits_\R x^{n-2} \exp(-\frac{x^2}{2}) \dd{x}.
> \end{aligned}
> $$
>
> （积分区间改为 $[0,+\infty)$ 也可）
>
> 另外，《新概念》上有不同的证明，利用 $\pdv{a} x^n e^{-ax^2} = -x^{n+2}e^{-ax^2}$。

另外，$\Gamma(t) = \int_0^\infty x^{t-1} e^{-t} \dd{x} = (t-1)!$。令 $x = \frac{u^2}{2}$，$\dd{x} = u\dd{u}$，得

$$
\begin{aligned}
    & \Gamma(t) = \int\limits_0^{+\infty} \frac{u^{2t-1}}{2^{t-1}} \exp(-\frac{u^2}{2}) \dd{u}. \\
    &\implies \int\limits_0^{+\infty} x^{2t-1} \exp(-\frac{x^2}2) \dd{x} =  2^{t-1} \Gamma(t). \\
    &\implies \int\limits_0^{+\infty} x^{n} \exp(-\frac{x^2}2) \dd{x} =  2^{\frac{n-1}{2}} \Gamma\qty(\frac{n+1}{2}) \\
    &\qquad = 2^{\frac{n-1}{2}} \qty(\frac{n-1}{2})!. \\
\end{aligned}
$$

---

```mathematica
Table[{i, i!, (2 i)!!}, {i, -2, 5, 1/2}];
TableForm[%, TableHeadings -> {None, {i, i!, (2 i)!!}}]
% // TeXForm
```

$$
\begin{array}{ccc}
 i & i! & (2i)!! \\
 \hline
 -2 & \infty & \infty \\
 -\frac{3}{2} & -2 \sqrt{\pi } & -1 \\
 -1 & \infty & \infty \\
 -\frac{1}{2} & \sqrt{\pi } & 1 \\
 0 & 1 & 1 \\
 \frac{1}{2} & \frac{\sqrt{\pi }}{2} & 1 \\
 1 & 1 & 2 \\
 \frac{3}{2} & \frac{3 \sqrt{\pi }}{4} & 3 \\
 2 & 2 & 8 \\
 \frac{5}{2} & \frac{15 \sqrt{\pi }}{8} & 15 \\
 3 & 6 & 48 \\
 \frac{7}{2} & \frac{105 \sqrt{\pi }}{16} & 105 \\
 4 & 24 & 384 \\
 \frac{9}{2} & \frac{945 \sqrt{\pi }}{32} & 945 \\
 5 & 120 & 3840 \\
\end{array}
$$

```mathematica
{n, (n-1)!!, 2^((n - 1)/2) ((n - 1)/2)!};
Table[%, {n, 0, 5}];
TableForm[%, TableHeadings -> {None, %%}]
% // TeXForm
```

$$
\begin{array}{ccc}
 n & (n-1)!! & 2^{\frac{n-1}{2}} \qty(\frac{n-1}{2})!\\
 \hline
 0 & 1 & \sqrt{\frac{\pi }{2}} \\
 1 & 1 & 1 \\
 2 & 1 & \sqrt{\frac{\pi }{2}} \\
 3 & 2 & 2 \\
 4 & 3 & 3 \sqrt{\frac{\pi }{2}} \\
 5 & 8 & 8 \\
\end{array}
$$

## 5 定态微扰论

### 无简并情况

> :material-clock-edit-outline: 2021年11月15日，2021年11月25日，2021年11月26日。

#### 记号

- 共轭上标 $*$，共轭转置上标 $\dagger$。例如 $i^* = -i$，$H^\dagger = H$。

- 实际的东西加上划线，$n$ 级近似项加 $n$ 个撇号，或者上标 $(n)$。例如

  $$
  \begin{aligned}
  \bar H &= H + H'. \\
  \bar \varphi &= \varphi + \varphi' + \varphi'' + \cdots &= \sum_{n=1}^{+\infty} \varphi^{(n)}.
  \end{aligned}
  $$

- 类似矩阵的东西用大写字母，类似向量或数的东西用小写字母。例如

  $$
  \Phi = \begin{bmatrix}
  \varphi_1 & \varphi_2 & \varphi_3 & \cdots
  \end{bmatrix}.
  $$

- 波函数 $\phi, \psi$ 之间的内积采用 $\int \phi^* \psi \dd{x}$，记为 $\braket{\phi}{\psi}$ 或 $\phi^\dagger \psi$。

  比如 $H^\dagger = H$ 表示 $\braket{\phi}{H\psi} = \braket{H^\dagger \phi}{\psi} = \braket{H\phi}{\psi}$。（这种东西记作 $\mel{\phi}{H}{\psi}$）

#### 问题

求解定态薛定谔方程 $\bar H \bar\Phi = \bar\Phi \bar E$。

> 其中 $\bar H$ 是哈密顿算符，矩阵 $\bar\Phi$ 的各列是特征向量（本征态，一个“向量”），（由数组成的）对角阵 $\bar E = \operatorname{diag}(\bar e_1, \bar e_2, \ldots)$ 的对角线上是特征值（能量，一个数）。

设 $\bar H = H + H'$，先求解 $H$ 的特征系统，即 $H\Phi = \Phi E$。

> 需要具体问题具体分析，总之求完得到 $\Phi,E$。

#### 一阶

然后再考虑微扰 $H'$，求 $H+H'$ 的特征系统，即

$$
\qty(H+H') \qty(\Phi + \Phi' + \cdots)
= \qty(\Phi + \Phi' + \cdots) \qty(E+E'+\cdots) .
$$

乘开上式，将一阶以上的项都合并到“$\cdots$”中，得

> 某个单项式的“阶数”与其中撇号的总数相同，例如 $H'\Phi'$ 是二阶，$\Phi^{(2)} E^{(5)}$ 是 $7$ 阶。

$$
H\Phi + H'\Phi + H\Phi' + \cdots
= \Phi E + \Phi'E + \Phi E' + \cdots.
$$

对于两侧的零阶项 $H\Phi$ 与 $\Phi E$，我们之前已经保证它们相等，可以约去。对于两侧未写出的高阶项，我们假装它们是零，直接丢掉。于是只剩下这些东西：

$$
H'\Phi + H\Phi' \overset?= \Phi'E + \Phi E'.
$$

我们在这里的任务就是选取适当的 $E'$、$\Phi'$，让上式近似成立。

---

由本征态的正交归一完备性（$\Phi^\dagger\Phi = I$），总可以设（由数组成的）方阵 $C'$ 使 $\Phi' = \Phi C'$。从而将“求 $\Phi'$”转化为“求 $C'$”。

> 注意：$\varphi'_j = \sum_i \varphi_i c'_{ij}$，其中 $\varphi'_j$ 是 $\Phi'$ 的第 $j$ 列，$\varphi_i$ 是 $\Phi_i$ 的第 $i$ 列，$c'_{ij}$ 是 $C'$ 的第 $i$ 行第 $j$ 列。换句话说，$C'$ 的第 $j$ 列是 $\varphi'_j$ 在 $\{\varphi_i\}$ 下的坐标。

代入上式，得

$$
H'\Phi + H\Phi C' = \Phi C' E + \Phi E'.
$$

同时在等式两端左乘 $\Phi^\dagger$ 以消掉 $\Phi$，然后利用 $H\Phi = \Phi E$，得

$$
\Phi^\dagger H' \Phi + EC' = C'E + E'.
$$

> 另一种推出此式的方法：直接把 $H,\Phi$ 等东西都换成在 $\{\varphi_i\}$ 下的坐标。

$$
\implies E' = EC'-C'E + \Phi^\dagger H' \Phi.
$$

---

先考察 $EC'-C'E$。回想一下，$E,E'$ 都对应特征值，它们都是对角阵。$EC'$ 相当于给 $C'$ 做初等行变换，第 $i$ 行变为原来的 $e_i$ 倍；$C'E$ 相当于给 $C'$ 做初等列变换，第 $j$ 列变为原来的 $e_j$ 倍。因此

$$
EC' - C'E = \begin{bmatrix}
0 & (e_1-e_2)c'_{12} & (e_1-e_3)c'_{13} & \cdots \\
(e_2-e_1) c'_{21} & 0 & (e_2-e_3)c'_{23} & \cdots \\
(e_3-e_1) c'_{31} & (e_3-e_2)c'_{32} & 0 & \cdots \\
\vdots & \vdots & \vdots & \ddots \\
\end{bmatrix}.
$$

> 第 $i$ 行第 $j$ 列：$e_i c_{jk} - c_{ij} e_{j} = (e_i-e_j)c_{ij}$。

——对角线上都是零。

再看 $\Phi^\dagger H' \Phi$。$H’$ 由问题提供，$\Phi$ 之前已经算好，反正 $\Phi^\dagger H' \Phi$ 是个已知的（数组成的）方阵。另外，一见形式就知道它的共轭转置是其自身：$\qty(\Phi^\dagger H' \Phi)^\dagger = \Phi^\dagger H'^\dagger \Phi = \Phi^\dagger H' \Phi$。

现在，怎样保证 $E'$ 是对角阵？

- 对角线上是 $e’_i$。由于 $EC'-C'E$ 不提供对角线，所以 $e_i'$ 只来自 $\Phi^\dagger H\Phi$。因此 $e'_i = \varphi_i^\dagger H' \varphi_i$。

- 除此以外全是零。$EC'-C'E$ 要抵消 $\Phi^\dagger H' \Phi$ 的非对角元，所以 $(e_i-e_j) c'_{ij} = - \varphi_i^\dagger H' \varphi_j$。

  $$
  c'_{ij} = - \frac{\mel{\varphi_i}{H'}{\varphi_j}} {e_i - e_j}
  $$


  > 顺带得到 $c_{ij} = -c_{ji}^\dagger$，反 Hermitian。

至此确定了 $E'$ 和 $C'$（除了对角线）。

---

检验一下 $\bar \Phi$ 的正交归一完备性。

> 事实上由于 $\bar H, H, H'$ 的共轭转置都是自身，这是必然的。

$$
\begin{split}
I &\overset?=
\qty(\Phi + \Phi' + \cdots)^\dagger (\Phi + \Phi' + \cdots) \\
&= \Phi^\dagger\Phi + \Phi'^\dagger \Phi + \Phi^\dagger \Phi' + \cdots. \\
\end{split}
$$

> 仍旧将一阶以上的项合并到“$\cdots$”中。

$\Phi'^\dagger \Phi + \Phi^\dagger \Phi'$ 是零吗？其实它就是 $\Phi^\dagger \Phi C' + C'^\dagger \Phi^\dagger\Phi = IC'+C'^\dagger I = C'+ C'^\dagger$。在非对角线上，由 $c'_{ij}$ 的公式，确实如此。在对角线上，我们还未确定 $c'_{ii}$，现在知道要求 $c'_{ii} \in i\R$；由于此时虚部不影响物理现实，我们直接都取零，保持 $C'^\dagger = - C'$。

#### 二阶

同理得目标

$$
H'\Phi' + H\Phi'' \overset?= \Phi''E + \Phi' E' + \Phi E''.
$$

仍设 $\Phi' = \Phi C'$，$\Phi'' = \Phi C''$。同理

$$
\begin{split}
&\implies H'\Phi C' + H\Phi C'' = \Phi C'' E + \Phi C' E' + \Phi E''. \\
&\implies \Phi^\dagger H'\Phi\ C' + E C''
    = C'' E + C'E' + E''. \\
&\implies E'' = \qty(EC'' - C'' E) + \qty(\Phi^\dagger H'\Phi C' - C' E').
\end{split}
$$

$E''$ 仍是对角阵，$EC''-C''E$ 仍不提供对角线。$C'$ 的对角线是零，$C'E'$ 也不提供对角线。因此 $E''$ 的对角线只由 $\Phi^\dagger H' \Phi C'$ 提供。故

$$
\begin{split}
e''_i &= \sum_j\varphi_i^\dagger H' \varphi_j \ c'_{ji} \\
&= -\sum_{j} \mel{\varphi_i}{H'}{\varphi_j} \frac{\mel{\varphi_j}{H'}{\varphi_i}} {e_j - e_i} \\
&= \sum_{j} \frac{\mel{\varphi_i}{H'}{\varphi_j}^2} {e_i - e_j}.
\end{split}
$$

### 有简并情况

> :material-clock-edit-outline: 2021年11月26日。

采用类似记号。

> 由 Hermitian 的性质，即使 $H$ 的特征值简并了，相应的特征子空间也不会退化。因此沿用记号是合理的。

同理可得

$$
E' = EC'-C'E + \Phi^\dagger H' \Phi.
$$

还是先看 $EC'-C'E$。这仍然是给 $C'$ 做两种初等变换后的差，但因为特征值有简并（$e_i$ 有重复），会有成片的零（而非仅对角线是零），比如下面这样的对角线加正方形。

$$
\left[\begin{array}{c|c|cc|c}
0 & & & & \\
\hline
& 0 & & & \\
\hline
& & 0 & \color{red}{0} & \\
& & \color{red}{0} & 0 & \\
\hline
& & & & 0
\end{array}\right]
$$

> 空白处是任意数。

再看 $\Phi^\dagger H' \Phi$。呃，它好像没什么变化……

现在同样想保证 $E'$ 是对角阵，怎么做？

- 对角线上是 $e’_i$。$EC'-C'E$ 只是多了些零，仍旧不提供对角线，所以 $e_i'$ 还是只来自 $\Phi^\dagger H\Phi$。因此 $e'_i = \varphi_i^\dagger H' \varphi_i$。
- 除此以外全是零。$EC'-C'E$ 要抵消 $\Phi^\dagger H' \Phi$ 的非对角元。对于非零部分，仍令 $(e_i-e_j) c_{ij} = - \varphi_i^\dagger H' \varphi_j$ 即可；对于剩下的部分（上面矩阵中对角线以外的零，即红色部分），无论 $c_{ij}$ 怎么取，$EC'-C'E$ 中对应项都是零，<u>**无法抵消**</u>——这怎么办？

---

再看看 $E' = EC' - C'E + \Phi^\dagger H' \Phi$ —— $EC'-C'E$ 是没辙了，其它部分能否活动活动呢？

$E'$ 对应特征值，必须是对角阵，这改变不了。那对 $\Phi^\dagger H' \Phi$ 下手。$H'$ 由问题提供，无回旋余地；$\Phi$ 是 $H$ 的特征向量—— $H$ 只把空间划分为若干正交的特征子空间，它并不限制每个子空间里的基怎么选！

因此，我们准备换个 $\Phi$，让 $\Phi^\dagger H' \Phi$ 中 $EC'-C'E$ 抵消不了的部分天然是零。换句话说，把 $H'$ 的这部分也一起对角化，或者说继续把 $\Phi^\dagger H' \Phi$ 的这部分对角化；再换个抽象一点儿的说法，挑出 $H$ 的那些简并特征值对应的多维特征子空间，在这个子空间中求解 $H'$ 的特征系统。

> 直观上感觉这就有可能。非简并特征值对应的部分无从修改，只能换简并特征值对应的部分，而 $EC'-C'E$ 抵消不了的部分正是这些。

> 换了 $\Phi$ 之后 $\Phi^\dagger H'\Phi$ 的对角线也换了，所以 $E'$ 对角线上的元素不一定是刚才估计的那些。

书上其实只求了这些特征系统的特征值，那我们直接给出特征方程 $\det(\Phi_d^\dagger H'_d \Phi_d - E_d'I) = 0$ 就完了。

> 下标 $d$ 表示只有简并（degenerate）的那些部分。

# 后备箱

---
relevant:
  - ./calculus-2.md:
      dir: both
---

# 线性代数

$$
\def\C{\mathbb{C}}
%
\def\i{\mathrm{i}}
\def\e{\mathrm{e}}
\def\tran{\mathsf T}
%
\def\rank{\operatorname{rank}}
$$

## 术语或记号

<dl>
    <dt>阶梯阵</dt>
    <dt>RREF</dt>
    <dd>简化行阶梯形式（Reduced Row Echelon Form）。</dd>
    <dt>反对称阵</dt>
    <dd>转置为自身的负矩阵的矩阵。</dd>
    <dt>相抵标准形矩阵</dt>
    <dd>一种与给定矩阵相抵（一种等价关系）的矩阵，其左上角是单位矩阵，其余三块为零矩阵。</dd>
    <dt>相似</dt>
    <dd>同一线性变换在不同基下的矩阵表示。</dd>
    <dt>合同</dt>
    <dd>同一二次型在可逆变量替换前后对应的矩阵的关系。</dd>
    <dt>标准形（二次型）</dt>
    <dd>没有交叉项的二次型。</dd>
    <dt>规范形（二次型）</dt>
    <dd>没有交叉项，而且平方项系数只有0、1（不允许复线性替换时还允许-1）的二次型。</dd>
    <dt>正交阵</dt>
    <dd>列向量<strong>标准</strong>正交的方阵。</dd>
</dl>


## §1 矩阵

### 将矩阵化为阶梯阵或RREF

> :material-clock-edit-outline: 2021年3月6日。

化为阶梯阵时，利用前一行（其中$a_1$非零）化简后一行，这可看作计算若干行列式：

$$
\displaylines{
\begin{bmatrix}
    a_1 & \cdots & a_i & \cdots \\
    b_1 & \cdots & b_i & \cdots
\end{bmatrix}
\rightarrow
\begin{bmatrix}
    a_1 & \cdots & a_i & \cdots \\
    0 & \cdots & \begin{vmatrix}
            a_1 & a_i \\
            b_1 & b_i
        \end{vmatrix} & \cdots
\end{bmatrix}
\\
\left(
    \vec b
    \rightarrow \vec b - \frac{b_1}{a_1} \vec a
    \rightarrow a_1 \left(\vec b - \frac{b_1}{a_1} \vec a \right)
    = a_1\vec b - b_1\vec a
\right)
}
$$

> 写成行列式方便找数；数较大时也能利用多线性变小，提高效率，有时还能提高功率。

> 2021年4月24日：这对整数封闭。

当变为零的不是 $b_1$ 时，行列式应保证 $b_c$ 的位置一致，而不是两列的左右顺序一致。

另外，如果 $a_1=1$，则计算会简化，之后化为RREF时也少一个步骤。将 $\vec a$ 单位化可归一，但这往往导致出现大量分数，得不偿失；若 $a_1,b_1$ 互质，可利用关于$x,y$的方程 $a_1x + b_1y=1$ 存在整数解来化为一。

> 若$[a_i]$存在公因数，将整行约去它还是能减小计算量。
>
>  $a_1x+b_1y=1$ 可转化为 $ax \equiv1\pmod{b_1}$，扩展的辗转相除法可解，但一般能直接看出来。

将阶梯阵化为RREF时类似：

$$
\begin{bmatrix}
    \vec a & c_1 &\cdots& c_j &\cdots \\
      & b_1 &\cdots& b_j &\cdots
\end{bmatrix}
\rightarrow
\begin{bmatrix}
    \vec a & 0 &\cdots& -\dfrac1{b_1} \begin{vmatrix}
            c_1 & c_j \\
            b_1 & b_j
        \end{vmatrix} &\cdots \\
      & b_1 &\cdots& b_j &\cdots
\end{bmatrix}
$$

### 矩阵乘法不满足消去律

> :material-clock-edit-outline: 2021年3月8日、2021年3月17日。

$$
\displaylines{
\begin{split}
AB=O
&\Leftrightarrow \operatorname{Null Space}(A) \supset \operatorname{Column Space}(B) \\
&\Leftrightarrow \operatorname{Row Space}(A) \subset \operatorname{Null Space}(B^\tran) \\
&\Rightarrow \rank A_{m\times n} + \rank B \leq n
\end{split}
\\
\begin{split}
&\text{If}\, \rank{A_{m\times n}} = m=n,\\
&\text{then}\, AB=O \Leftrightarrow \rank B = \rank{AB} = \rank O =0 \Leftrightarrow B=O.
\end{split}
}
$$

### 用 Gauss–Jordan 方法求逆矩阵

> :material-clock-edit-outline: 2021年3月12日、2021年3月15日。

不必立即机械应用算法。可暂停程序，用行变换让行前面多些零，主元变成一，少些分数。（被乘的那一行随后可能变得混乱，故需暂停）

另外，求 $A^{-1}B$ 也可用类似方法，一般能减少计算量。（相当于把 $A,B$ 的每一列拿出来解方程）

$$
\begin{bmatrix}
    A & B
\end{bmatrix}
\xrightarrow{E(\cdots)}
\begin{bmatrix}
    EA & EB
\end{bmatrix}
=
\begin{bmatrix}
    I & A^{-1}B
\end{bmatrix}
$$

### 方阵的二次式

> :material-clock-edit-outline: 2021年3月13日、2021年3月15日。

对于$n$阶方阵$X$，$XI=X=IX$，满足交换律，故 $X^2-(p+q)X+pqI = (X-pI)(X-qI)$。

因此，对于矩阵方程 $X^2+bX+cI = O$，对任意不为复数方程 $x^2+bx+c=0$ 的根的数 $\lambda$，有

$$
\displaylines{
\begin{split}
    (X-\lambda I) \left(X+(b+\lambda)I \right) 
    &= X^2 +bX -\lambda(b+\lambda)I \\
    &= -(\lambda^2+b\lambda+c)I.
\end{split}\\
\therefore
(X+\lambda I)^{-1} = -\frac{X+(b+\lambda)I}{\lambda^2+b\lambda+c}. \\
}
$$

> 如果取$\lambda$为上述复数方程的根，则 $Y=X-\lambda I$ 满足方程
> 
> $$
> Y \left( Y+(b+2\lambda)I \right) = Y^2+(b+2\lambda)Y = O
> $$
> 
> 即消除了零次项。若$\lambda$是重根，则进一步变为 $Y^2=O$ 。
>
> 如果取 $\lambda = -\frac12 b$ 且不是重根，则 $Y=X-\lambda I$ 满足方程
> 
> $$
> Y^2 = (\cdots) I
> $$
> 
> 据说，这样的矩阵称为对合矩阵。

另外，对于两个同型方阵 $A,B$ 有下式，这可用于解某些矩阵方程。

$$
(A-aI)(B-bI) = AB -aB -bA +ab
$$

---

> :material-clock-edit-outline: 2021年5月30日。

$X$ 的所有特征值都是方程 $x^2+bx+c=0$ 的根（$p$或$q$）。并且若 $p\neq q$，则

$$
\displaylines{
\begin{split}
    n &= \rank \left( (q-p)I \right) \\
    &= \rank \left( (X-pI) - (X-qI) \right) \\
    &\leq \rank(X-pI) + \rank(X-qI) \\
    &\leq \rank\left((X-pI)(X-qI)\right) + n \\
    &= 0+n = n.
\end{split}
\\
\therefore\rank(X-pI) + \rank(X-qI) = n.
}
$$

这说明 $X-pI,X-qI$ 的解空间~~互为正交补~~的和空间是全空间（其中一个可能是零空间），所以$X$一定可以相似对角化。

> :material-clock-edit-outline: 2021年6月29日。
>
> 另外，能直接从 $X-pI,X-QI$ 的列向量们线性表示出自然基，从而得证。

> :material-clock-edit-outline: 2021年12月4日。
>
> 好像无法说明两个解空间是正交的。

若 $p=q$，则

$$
\displaylines{
\begin{split}
    0 &\leq 2\rank(X-pI) \\
    &\leq \rank(X-pI)^2 +n \\
    &= 0 + n =n.
\end{split}
\\
\therefore \rank(X-pI) \leq \frac n2.
}
$$

 由于$X$只有一个特征值$p$，能相似对角化则要求 $\rank(X-pI)=0$，即 $X=pI$，否则不能。

### 分块矩阵

> :material-clock-edit-outline: 2021年3月15日、2021年3月16日、2021年3月17日。

利用分块矩阵的“消元”可证明一些关于秩等的命题。具体来说，只要形状匹配，初等变换中的“数”都可变为矩阵，只需注意“行”变换为左乘，“列”变换为右乘。另外，将某一“行”（或“列”）翻倍时，倍“数”必须可逆。

### 矩阵积的秩的范围

> :material-clock-edit-outline: 2021年3月16日、2021年3月24日。
>
> :material-eye-arrow-right: [热雪](https://www.zhihu.com/people/re-xue-23-7)《[矩阵的秩的不等式汇总及其证明](https://zhuanlan.zhihu.com/p/341263037)》。

对于 $A_{l\times m}, B_{m \times n}$，

$$
\displaylines{
\begin{split}
    &\operatorname{Null Space}(AB) \supset \operatorname{Null Space}(B) \Rightarrow n-\rank(AB) \geq n-\rank B \\
    \Rightarrow\ & \rank(AB) \leq \rank B \\
    \Rightarrow\ & \rank(AB) = \rank(B^\tran A^\tran) \leq \rank A^\tran = \rank A \\
\end{split}
\\[2em]
\begin{split}
    &\rank(AB)+n \\
    =\ & \rank\begin{bmatrix} AB & \\ & I_n \end{bmatrix}
    = \rank\begin{bmatrix} AB & B \\ & I \end{bmatrix}
    = \rank\begin{bmatrix}  & B \\ -A & I \end{bmatrix} \\
    \geq\ & \rank A + \rank B
\end{split}
}
$$

另证：$AB$ 的每列向量都是 $A$ 各列向量的线性组合，故 $\rank(AB) \leq \rank A$。

### 秩

> :material-clock-edit-outline: 2021年6月22日、2021年6月22日。

用消元定义了矩阵的秩，用线性组合定义了向量组的秩。要统一“行”或“列”、“消元”或“线性组合”组合形成的四种秩。

显然的部分：矩阵的初等行变换不改变“行消元秩”，也不改变“列线性组合秩”。（用 $A=CR$ 可说明这两个秩一致；这里用别的方法证了。）

首先说明对于阶梯阵，四秩合一。以行阶梯阵为例。由于都等于非零行数，“行消元秩”与“行线性组合秩”一致；且主元所在列可作为列向量组的极大无关组，故“列线性组合秩”也等于主元数。又，初等列变换能将它化为相抵标准形，这说明它的“列消元秩”也等于主元数。

对于 $m\times n$ 矩阵 $A$，先做初等行变换（相应方阵记为 $P$）化为行阶梯阵，再做初等列变换（相应方阵记为 $Q$）化为相抵标准形 $S$，则 $PAQ=S$，$A \overset行\cong PA \overset列\cong S \overset行\cong AQ \overset列\cong A$。

> $\overset行\cong$ 表示只允许初等行变换的相抵，$\overset列\cong$ 类似。

$S$ 也是行阶梯阵，其秩记为 $r$。

- $PA \overset列\cong S$：两个矩阵都是行阶梯阵，本来它们的四个秩就分别一致。再由列相抵，它们的八个秩都是 $r$。
- $A \overset行\cong PA$：由行相抵，$A$ 与 $PA$ 的“行消元秩”与“列线性组合秩”分别一致。由于 $PA$ 是行阶梯阵，这两个秩又都等于 $PA$ 的秩，即 $r$。
- $S \overset行\cong AQ$：$S$ 的后 $n-r$ 列本来全为零，所以无论怎么行变换，后 $n-r$ 列都为零，因此 $AQ$ 只有前 $r$ 列非零。故 $AQ$ 的“列消元秩”与“行线性组合秩”小于等于 $r$。（也可说明另外两个秩小于等于 $r$，但后面用不到。）
- $AQ \overset列\cong A$：由列相抵，$AQ$ 与 $A$ 的“列消元秩”与“行线性组合秩”分别一致。由上，都小于等于 $r$。

因此，$A$ 的“行消元秩”等于“列线性组合秩”等于 $r$ 大于等于“列消元秩”，且 $r$ 大于等于“行线性组合秩”。故“行消元秩”大于等于“列消元秩”。

若对 $A$ 先做初等列变换，则得到“列消元秩”大于等于“行消元秩”。综合二者，行、列“消元秩”一致。同理可得行、列“线性组合秩”一致。

因此，四秩合一。

### 矩阵方程的解何时可逆

> :material-clock-edit-outline: 2021年6月29日。

以一例来说明，

$$
\begin{bmatrix}
    1 & 3 & 0 \\
    0 & -\frac12 & 1
\end{bmatrix}
X
=
\begin{bmatrix}
    0 & 1 & 1 \\
    \frac12 & \frac12 & \frac12
\end{bmatrix}
$$

的解是

$$
X = \begin{bmatrix}
    3 & 4 & 4 \\
    -1 & -1 & -1 \\
    0 & 0 & 0
\end{bmatrix} +
\begin{bmatrix} 6 \\ -2 \\ -1 \end{bmatrix}
\begin{bmatrix} \lambda & \mu & \nu \end{bmatrix}.
$$

若 $X$ 可逆，则后两列线性独立，故 $\mu\neq\nu$。此时后两列与 $(6,-2,-1)^\tran, (4,-1,0)^\tran$ 等价，故它们也与 $(3,-1,0)^\tran$ 线性独立，故 $X$ 已必然可逆。

## §3 线性空间与线性变换

### 正交化向量组

> :material-clock-edit-outline: 2021年4月24日、2021年6月27日。

Gram–Schmidt 正交化方法是给计算机设计的，从第一步开始就可能出现非整数，对人很不友好。

考虑将 $\{\vec v_i\}$ 正交化为 $\{\vec\eta_i\}$，……（待续）

计算好 $\lvert\vec\eta_i\rvert$ 后可以记下它，以后直接用。

### 基变换与线性变换

> :material-clock-edit-outline: 2021年4月28日、2021年6月27日。

过渡方阵为 $T$ 的基变换：$[\vec e'\cdots] = [\vec e \cdots]T$，而 $T \vec x' = \vec x$。$T$的各列是 $\{\vec e'\}$ 在基 $\{\vec e\}$ 下的坐标。

方阵 $T$ 相应的线性变换：$\sigma(\vec x)=T\vec x$，特例是 $\sigma(\vec e) = T\vec e$。$T$的各列是 $\{\sigma(\vec e)\}$ 在基 $\{\vec e\}$ 下的坐标。

## §4 行列式

### 行列式的化简

> :material-clock-edit-outline: 2021年5月23日。

降阶法和三角化法本质上一样，只是前者书写过程比较简洁，重复内容少。

### 分块行列式

> :material-clock-edit-outline: 2021年6月29日。

对于 $n$ 阶方阵 $A,B,C,D$，其中$A$ 可逆，且 $AB=BA$，则

$$
\begin{split}
    \begin{vmatrix}
        A & B \\
        C & D
    \end{vmatrix}
    &=
    \begin{vmatrix}
        A & B \\
        C-CA^{-1}A & D-CA^{-1}B
    \end{vmatrix}
    =
    \begin{vmatrix}
        A & B \\
        O & D-CA^{-1}B
    \end{vmatrix} \\
    &= \lvert A \rvert \cdot \lvert D-CA^{-1}B \rvert
    = \lvert AD-ACA^{-1}B \rvert \\
    &= \lvert AD - CAA^{-1}B \rvert \\
    &= \lvert AD - CB \rvert.
\end{split}
$$

### $n$ 阶行列式

> :material-clock-edit-outline: 2021年6月29日。

有一类都可以把所有行加起来，提取公因式。

例：

$$
\begin{split}
    \begin{vmatrix}
        1-\lambda & 1 & 1 & \cdots & 1 \\
        1 & 1-\lambda & 1 & \cdots & 1 \\
        \vdots & \vdots & \vdots & & \vdots \\
        1 & 1 & 1 & \cdots & 1-\lambda \\
    \end{vmatrix}_n
    &= \begin{vmatrix}
        n-\lambda & n-\lambda & n-\lambda & \cdots & n-\lambda \\
        1 & 1-\lambda & 1 & \cdots & 1 \\
        \vdots & \vdots & \vdots & & \vdots \\
        1 & 1 & 1 & \cdots & 1-\lambda \\
    \end{vmatrix}
    &\quad （把所有行加到第一行）
    \\
    &= (n-\lambda) \begin{vmatrix}
        1 & 1 & 1 & \cdots & 1 \\
        1 & 1-\lambda & 1 & \cdots & 1 \\
        \vdots & \vdots & \vdots & & \vdots \\
        1 & 1 & 1 & \cdots & 1-\lambda \\
    \end{vmatrix}
    \\
    &= (n-\lambda) \begin{vmatrix}
        1 & 1 & 1 & \cdots & 1 \\
        0 & -\lambda & 0 & \cdots & 0 \\
        \vdots & \vdots & \vdots & & \vdots \\
        0 & 0 & 0 & \cdots & -\lambda \\
    \end{vmatrix}
    &\quad （所有行都减去第一行）
    \\
    &= (n-\lambda) (-\lambda)^{n-1}
    &\quad （上三角阵的性质）
    \\
    &= (-1)^{n-1} (n-\lambda) \lambda^n.
\end{split}
$$

## $5 特征值与特征向量

### $A=\vec u\vec u^\dagger$

> :material-clock-edit-outline: 2021年5月30日。
>
> :material-file-move-outline: 教材 264 页 36. 在[线性代数-学习指导与习题解答-重制书签.pdf](https://onedrive.bit101.cn/zh-CN/course/%E7%BA%BF%E6%80%A7%E4%BB%A3%E6%95%B0A-100172110/book/%E7%BA%BF%E6%80%A7%E4%BB%A3%E6%95%B0-%E5%AD%A6%E4%B9%A0%E6%8C%87%E5%AF%BC%E4%B8%8E%E4%B9%A0%E9%A2%98%E8%A7%A3%E7%AD%94-%E9%87%8D%E5%88%B6%E4%B9%A6%E7%AD%BE.pdf) 248页的注，那里讨论了 $\vec\alpha \vec\beta^\tran$。

若 $\vec u^\dagger \neq \vec 0$，讨论 $A=\vec u\vec u^\dagger$ 的特征系统。

显然 $A$ 的行简化阶梯阵是 $\begin{bmatrix} \vec u &\vec 0 &\cdots& \vec0 \end{bmatrix}^\dagger$，所以 $\rank A = 1$。

另外 $A^2 = \vec u \vec  (u^\dagger\vec u) \vec u^\dagger = \lVert \vec u \rVert^2 A$，所以 $A$ 的特征值必满足 $\lambda^2 = \lVert\vec u\rVert \lambda$，不是 $0$ 就是 $\lVert \vec u \rVert^2$，并且 $A$ 可相似对角化。（→“[方阵的二次式](#方阵的二次式)”）

$A-0I = A$ 的解空间由 $\rank A = 1$ 可知是 $n-1$ 维，故 $\lambda = 0$ 对应 $n-1$ 个特征向量。具体来说，$A\vec x = 0\vec x$ 相当于 $\vec u\vec u^\dagger\vec x = \vec 0$，而 $\vec u^\dagger \vec x \in \C$ 且 $\vec u\neq \vec 0$，所以这由等价于 $\vec u^\dagger \vec x = 0$，即 $\vec u \perp \vec x$ —— $\lambda=0$ 的特征子空间就是 $\vec u$ （所张成空间）的正交补。

$A-\lVert\vec u\rVert^2I$ 的解空间呢？结合 $A$ 可相似对角化与 $\lambda=0$ 的情况可知它的维度是 $1$，其它的就不好说了，还是从原始形式 $A\vec x = \lVert\vec u \rVert^2\vec x$ 入手吧。这等价于 $\vec u\vec u^\dagger\vec x = \vec x\vec u^\dagger \vec u$，显然 $\vec x = \vec u$ 是它的一个解，故特征子空间就是 $\vec u$ （所张成的空间）。

这样就清楚了 $A$ 的特征系统。其实 $\frac1{\lVert\vec u\rVert^2}A$ 是投影阵，它将向量投影到 $\vec u$ 上。

### 正交阵的特征值的模总为一

> :material-clock-edit-outline: 2021年6月29日。

设 $Q\vec x = \lambda \vec x$，$\vec x \neq\vec 0$ 则 $\vec x^\dagger Q^\dagger = \bar\lambda \vec x^\dagger$，故

$$
\displaylines{
\lambda\bar\lambda \vec x^\dagger \vec x = \vec x^\dagger Q^\dagger Q \vec x = \vec x^\dagger I \vec x = \vec x^\dagger \vec x.
\\
\implies (1-\lambda\bar\lambda) \vec x^\dagger \vec x = \vec 0. \\
\implies \lambda \bar\lambda = 1 \implies \lvert\lambda\rvert = 1.
}
$$

## §6 二次型

### 可交换矩阵

> :material-clock-edit-outline: 2021年6月29日。

由矩阵乘法定义，与对角阵可交换的矩阵基本只能是对角阵。

> 如果两个对角元相等，则相应位置可任意选取。

$AB = BA$ 的充要条件是 $A,B$ 可同时相似对角化。

> 必要性：设 $P^{-1}AP = \Lambda$，则由于 $P^{-1}BP$ 与 $P^{-1}AP$ 天然可交换，所以 $P^{-1}BP$ 也基本是对角阵，从而 $P$ 也能把 $B$ 相似对角化。
>
> 充分性：写成 $P\Lambda P^{-1}$，显然。

若实对称阵 $A,B$ 正定，则 $AB$ 正定的充要条件是 $AB=BA$。

> 充分性：同时相似对角化后，很容易写出 $AB$ 的特征值。
>
> 必要性：正定要求实对称，$AB = (AB)^\tran = B^\tran A^\tran = BA$。

# 注意

- 矩阵乘法<u>不满足消去律</u>。
- 化简带参数的矩阵时，注意分类讨论。
- 转置分块矩阵时，每个小矩阵也要转置。
- 区分向量与其坐标。
- 坐标与基的<u>顺序</u>有关。
- 伴随矩阵的下标与一般情况相反。
- 求标准正交基或正交相似变换因子时记得<u>单位化</u>。
- 写通解时要指明参数范围。
- 多项式空间 $F[x]_n$ 表示一个 $n$ 维线性空间，即次数小于等于 $n-1$ 的多项式的集合。
- 线性空间要求<u>非空</u>，证明其子集是子空间时也要求非空。
- Gram–Schmidt 正交化方法中分母是模的平方。

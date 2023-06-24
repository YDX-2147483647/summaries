---
relevant: ./calculus-2.md
---

# 复变函数与数理方程

$$
\def\N{\mathbb{N}}
\def\Z{\mathbb{Z}}
\def\R{\mathbb{R}}
\def\Rho{Ρ}
\def\oiint{∯}
$$

## A§3 积分

### 化不解析函数为解析函数

> :material-clock-edit-outline: 2021年12月12日。

求 $\int_{\abs{z} = 2}\frac{\dd{z}}{\abs{z-1}^2}$，如果不想用参数方程，那需要构造一个在围道上与被积函数相等（其它地方不总相等）的解析函数。$\abs{z-1}^2$ 是二次的，不好处理，先转化成 $(z-1)\overline{z-1}$，解决共轭。

最原始的思路是单位复数的性质 $\bar z = \frac{1}{z}$，这里也仿照它。围道的圆心是 $0$，故先凑个 $\bar z$ 出来。

$$
\overline{z-1} = \overline{z}-1。
$$

围道的半径是 $2$，故

$$
\bar z = \frac{4}{z}.
$$

于是被积函数化为

$$
\frac{1}{(z-1) \qty(\frac{4}{z} - 1)}
= \frac{z}{(z-1)(4-z)}.
$$

后边随便做就行了。

> :material-clock-edit-outline: 2021年12月17日。

$$
\frac{\dd{z}}{z} = \dd{\operatorname{Ln}}z = \dd{\abs{z}} + i\dd{\arg z}.
$$

## §4 级数

### 最简单的例子

> :material-clock-edit-outline: 2021年10月15日。

$$
\begin{aligned}
    &\frac{1}{1-z} = z + z^2 + z^3 + \cdots &= \sum_{n=0}^{+\infty} z^n, &\quad \abs{z} < 1. \\
    &\frac{1}{1-z} = -\frac1z - \frac{1}{z^2} - \frac{1}{z^3} + \cdots &= -\sum_{n=-1}^{-\infty} z^n, &\quad \abs{z} > 1. \\
\end{aligned}
$$

## A§5 留数

### 其它方法

> :material-clock-edit-outline: 2021年10月23日。
>
> :material-eye-arrow-right: 113页习题五10(1)。

$C: \abs{z} = 3$。

$$
\begin{split}
    &\oint\limits_C \frac{z^{15} \dd{z}} {\qty(z^2-1)^2 \qty(z^4+2)} \\
    &= \oint\limits_{2C} \frac{u^{7} \dd{\frac u2}} {\qty(u-1)^2 \qty(u^2+2)}
        \qquad (u=z^2) \\
    &= \oint\limits_{C} \frac{u^{7} \dd{u}} {\qty(u-1)^2 \qty(u^2+2)} \\
    &= - 2\pi i\ \Res(\frac{u^7} {\qty(u-1)^2 \qty(u^2+2)}, \infty) \\
    &= 2\pi i \cross \text{“} \frac{u^7} {\qty(u-1)^2 \qty(u^2+2)} \text{在$\infty$的展开式中$\frac 1u$的系数”}. \\
\end{split}
$$

注意

$$
\begin{split}
    \frac{u^7} {\qty(u-1)^2 \qty(u^2+2)}
    &= \frac{u^3} {\qty(1 - \frac 1u)^2 \qty(1 + \frac{2}{u^2})} \\
    &= u^3 \qty(1 - \frac{1}{u})^{-2} \qty(1 + \frac{2}{u^2})^{-1} \\
    &= u^3 \qty(\sum_{n=0}^{+\infty} \binom{-2}{n} \frac{(-1)^n}{u^n}) \qty(\sum_{m=0}^{+\infty} \frac{ (-2)^m}{u^{2m}}). \\
\end{split}
$$

$\dfrac{1}{u}$ 对应的 $(n,m)$ 为 $\{(0,2), (2,1), (4,0)\}$，相应系数如下

$$
\begin{array}{c|c}
    n & m & \binom{-2}{n} (-1)^n
        & (-2)^m & \text{最终系数} \\
    \hline
    0 & 2 & 1
        & 4 & 4\\
    2 & 1 & \frac{(-2)\times (-3)}{1 \times 2} = 3
        & -2 & -6\\
    4 & 0 & \frac{(-2) \times \cdots \times(-5)}{4!} = 5
        & 1 & 5\\
\end{array}
$$

故上述系数是 $4-6+5 = 3$，进而得原式为 $6\pi i$。

## B§1 建立方程

> :material-clock-edit-outline: 2021年11月7日。

- 方程：
  - 波动方程： $\pdv[2]{u}{t} = v^2 \pdv[2]{x}{t}$。
  - 扩散方程：$\pdv{u}{t} = \alpha^2 \pdv[2]{x}{t}$。
- 边界条件：$u,\pdv{u}{x}$ 及其线性组合。
- 初始条件。

## B§2 分离变量法

### 齐次方程、齐次边界条件

> :material-clock-edit-outline: 2021年11月7日，2021年11月12日。

设 $\eval{u}_{x,t} = \eval{X}_x \eval{T}_t$，则齐次方程化为两个特征值问题。

- 波动方程

  $X'' = - k^2 X$，$T'' = - \omega^2 T$，其中 $\omega = kv$。（边界条件一般导致 $k \in i\R$ 时无解）

  根据边界条件类型，$kl$ 是 $\pi$ 的整数或半整数倍。

- 扩散方程

  $X$ 的情况同上。$T' = -(k\alpha)^2 T$。

- 旋转对称域上的调和方程

  可能有自然边界条件（$\eval{u}_{r=0}$ 有限）或周期性条件（$\eval{u}_{\theta}$ 有 $2\pi$ 的周期）。

  径向的微分方程形式将是欧拉方程。

### 非齐次问题

> :material-clock-edit-outline: 2021年11月12日。

- 很多例子，包括非齐次边界条件

  代换 $u = v+w$，转化为齐次问题：使边界条件齐次，有时也能把方程弄成齐次。

- 齐次边界条件

  由边界条件可得特征函数系，将所有东西按此展开，可得一系列常微分方程。

## B§3 行波法和积分变换法

此章研究无界域的问题。

### 行波法

> :material-clock-edit-outline: 2021年11月12日。

$$
\pdv{f}{\xi}{\eta} = 0
\implies f = f_1(\xi) + f_2(\eta).
$$

> $\xi,\eta = x \pm v t$。
>
> $\pdv{x} = \pdv{\xi} + \pdv{\eta}$，$\frac{1}{v} \pdv{t} = \pdv{\xi} - \pdv{\eta}$。

### 特征线法

> :material-clock-edit-outline: 2021年12月12日。

波动是沿特征线传播的。

$$
\begin{split}
A\pdv[2]{x} + 2B \pdv{}{x}{y} + C \pdv[2]{y} +\\
2D\pdv{x} + 2E\pdv{y} + F = 0.
\end{split}
$$

这个方程的特征线满足 $A(\dd{y})^2-2B\dd{y}\dd{x} + C(\dd{x})^2 = 0$。

将两条特征线的方程中的常数设为新的变量，可去除 $\partial^2_{xx}, \partial^2_{yy}$ 项。

---

达朗贝尔公式：

$$
u = \frac{1}{2} \sum \eval{u}_{t=0,\ x=x\pm vt}
+ \frac{1}{2} \int\limits_{x-vt}^{x+vt} \eval{\frac{1}{v} \pdv{u}{t}}_{t=0,\ x=\xi} \dd{\xi}.
$$

### 积分变换法

> :material-clock-edit-outline: 2021年12月12日。

$\mathcal{F}$ 需要函数在 $\R$ 上有定义，$\mathcal{L}$ 则是 $\R^+$。

## B 杂项

### $\nabla$

> :material-clock-edit-outline: 2021年11月7日。

$$
\laplacian = \frac{1}{J} \sum_i \pdv{u_i} \frac{J}{h_i^2} \pdv{u_i}.
$$

> $h_i$ 是 [scale factors](https://mathworld.wolfram.com/ScaleFactor.html)；$J$ 是 Jacobian 行列式，等于 $\prod_i h_i$。

对于极坐标，$\va*{u} = (r,\theta)$，$\va*{h} = (1, r)$，于是

$$
\begin{split}
    \laplacian
    &= \frac{1}{r} \pdv{r}(r \pdv{r}) + \frac{1}{r} \pdv[2]{\theta} \\
    &= \pdv[2]{r} + \frac{1}{r} \pdv{r} + \frac{1}{r} \pdv[2]{\theta}.
\end{split}
$$

### 常微分方程

#### 欧拉方程

> :material-clock-edit-outline: 2021年11月12日。

$$
\sum_i x^i \dv[i]{x} = 0.
$$

令 $x = e^t, x\dv{x} = \dv{t}$ 可转化为常系数方程。

> $$
>  \begin{split}
> x^2 \dv[2]{x}
> &= x^2 \dv{t} \dv{x} \\
> &= x^2 \dv{x}(\frac{1}{x}\dv{t}) \\
> &= -\frac{x^2}{x^2} \dv{t} + x \dv{t} \dv{t} \\
> &= \dv[2]{t} - \dv{t}.
> \end{split}
> $$

$\rho^2 \Rho'' + \rho \Rho' = n^2 \Rho$ 的解是 $1,\ln \rho$（$n = 0$）或 $\rho^{\pm n}$（$n \neq 0$）的线性组合。

#### 线性非齐次常系数微分方程

> :material-clock-edit-outline: 2021年11月12日。

线性非齐次常系数微分方程可用常数变易法得特解。

  $y'' + \omega^2 y = f(x)$，$\eval{y}_{x=0} = 0$，$\eval{\dv{y}{x}}_{x=0} = 0$ 的一个特解是

$$
y = \frac{1}{\omega} \int\limits_0^x f(t) \sin(\omega(x-t)) \dd{t}.
$$

---

> :material-clock-edit-outline: 2021年12月13日。

要解如下常微分方程，初始条件为 $\eval{y}_0=0, \eval{y'}_0 =0$。

$$
y'' + k^2 y = f.
$$

$ki$ 是特征根之一，构造 $u = y/e^{ikx}$，则

$$
\left\{\begin{array}{r}
y &=& e^{ikx} u \\
y' &=& ike^{ikx}u &+& e^{ikx}u' \\
y'' &=& -k^2 e^{ikx}u &+& 2ike^{ikx}u' &+& e^{ikx} u'' \\
\end{array}\right..
$$

代入初始条件，得到 $\eval{u}_0 = 0, \eval{u'}_0$。

代入原方程，得到

$$
\begin{split}
& 2ik e^{ikx} u' + e^{ikx} u'' = f. \\
\implies& u'' + 2iku' = e^{-ikx}f.
\end{split}
$$

这是关于 $u'$ 的一阶微分方程，可以凑微分了：

$$
\qty(e^{2ikx}u')' = e^{ikx} f.
$$

现在一点儿一点儿积分回去。

$$
\begin{split}
e^{2ikx} u'
&= 0+ \int\limits_0^x \eval{\qty(e^{2ikx}u')'}_\xi \dd{\xi} \\
&= \int\limits_0^x e^{ik\xi} \eval{f}_\xi \dd{\xi}. \\
\end{split}
$$

再来一次。

$$
\begin{split}
u &= 0 + \int\limits_0^x \eval{u'}_\eta \dd{\eta} \\
&= \int\limits_0^x \dd{\eta} e^{-2ik\eta}
    \int\limits_0^\eta \dd{\xi} e^{ik\xi} \eval{f}_\xi \\
&= \int\limits_0^x \dd{\eta} \int\limits_0^\eta \dd{\xi}
    e^{ik (\xi-2\eta)} \eval{f}_\xi.
\end{split}
$$

最后结果……

$$
\int\limits_0^x \dd{\eta} \int\limits_0^\eta \dd{\xi}
    e^{ik (x+\xi-2\eta)} \eval{f}_\xi.
$$

(⊙﹏⊙)

---

还是用冲量法或积分变换法吧……

## B§4 格林函数法

> :material-clock-edit-outline: 2021年11月27日。
>
> :material-eye-arrow-right: [Method of Green’s Functions - 18.303 Linear PDEs](https://ocw.mit.edu/courses/mathematics/18-303-linear-partial-differential-equations-fall-2006/lecture-notes/greensfn.pdf)

### 格林公式

> 此为第二格林公式。

对于 $\R^n \to \R$ 函数 $\phi,\psi$，

$$
\begin{aligned}
\div(\phi \grad\psi ) = \grad\phi \vdot\grad\psi + \phi \laplacian\psi. \\
\div(\psi \grad\phi ) = \grad\psi \vdot\grad\phi + \psi \laplacian\phi. \\
\end{aligned}
$$

两式相减得

$$
\begin{split}
& \div(\phi\grad\psi - \psi\grad\phi) = \phi\laplacian\psi - \psi\laplacian\phi. \\
& \implies \oiint (\phi\grad\psi - \psi\grad\phi) \vdot \vb*{\dd S}
    = \iiint (\phi\laplacian\psi - \psi\laplacian\phi) \dd{V}.
\end{split}
$$

> 二维：
>
> $$
> \oint (\phi\grad\psi - \psi\grad\phi) \vdot \vb*{\dd l}
>     = \iint (\phi\laplacian\psi - \psi\laplacian\phi) \dd{S}.
> $$

### 调和方程的格林函数法

> 无下标表示场点，有下标表示源点。

$$
\left\{\begin{aligned}
\laplacian u &= F & \forall \vb*{x} \in D. \\
u &= f & \forall \vb*{x} \in \partial D.
\end{aligned}\right.
$$

构造辅助的格林函数 $G(\vb* x, \vb* x_0)$，它满足

$$
\left\{\begin{aligned}
\laplacian G &= \eval{\delta}_{\vb* x - \vb* x_0} = \laplacian_0 G
    & \forall \vb*{x}, \vb*{x}_0 \in D. \\
G &= 0 & \forall \vb*{x}, \vb*{x}_0 \in \partial D.
\end{aligned}\right.
$$

> 注意，课上讲的 $G$ 与这里差个负号。

将 $u,G$ 代入格林公式，得

$$
\begin{split}
& \oiint \eval{(u \grad_0 G - G \grad_0 u)}_{\vb* x_0} \vdot \dd{\vb* S_0} \\
&= \iiint \qty(\eval{u}_{\vb* x_0} \eval{\delta}_{\vb* x - \vb* x_0} - \eval{G F}_{\vb* x_0}) \dd{V_0} \\
&= \eval{u}_{\vb* x} - \iiint \eval{G}_{\vb* x, \vb* x_0} \eval{F}_{\vb* x_0} \dd{V_0}.
\end{split}
$$

移项，

$$
\eval{u}_{\vb* x}
= \iiint \eval{G}_{\vb* x, \vb* x_0} \eval{F}_{\vb* x_0} \dd{V_0}
    + \oiint \eval{(u \grad_0 G - G \grad_0 u)}_{\vb* x_0} \vdot \dd{\vb* S_0}.
$$

代入边界条件，得

$$
u = \iiint GF \dd{V_0}
    + \oiint (f \grad_0 G) \vdot \dd{\vb* S_0}.
$$

这样就把原问题转化为求 $G$，而 $G$ 不涉及 $F,f$，只与 $D$ 有关，从而能一劳永逸地解决问题。

### 基本解

先寻找满足 $\laplacian G = \delta = \laplacian_0 G$ 的特解，暂时忽略 $D$ 的问题。

找简单的解即可：设解的形式为 $G = \eval{\bar G}_{r}$，其中 $r = \abs{\vb* x - \vb* x_0}$。解得

$$
\begin{aligned}
\bar G &= - \frac{1}{2\pi} \ln\frac{1}{r} & \text{in $\R^2$}. \\
\bar G &= - \frac{1}{4\pi} \frac{1}{r^2} & \text{in $\R^3$}.
\end{aligned}
$$

### 格林函数

现在考虑 $D$ 的问题。设 $G = \bar G + g$，则 $g$ 满足

$$
\left\{\begin{aligned}
\laplacian g &= 0
    & \forall \vb*{x}, \vb*{x}_0 \in D. \\
g &= 0 & \forall \vb*{x}, \vb*{x}_0 \in \partial D.
\end{aligned}\right.
$$

对于简单的 $D$，这样的 $g$ 可用初等的电像法给出。

## B§4 格林函数法2

> :material-clock-edit-outline: 2021年12月12日。

第一类边界条件调和方程：

$$
\begin{cases}
\laplacian u = 0. & (\forall M \in D) \\
u = \eval{f}_M. & (\forall M \in \partial D) \\
\end{cases}
$$

其解为

$$
\eval{u}_M = - \oint\limits_{\partial D}
\eval{f}_{M_0} \grad_0 \eval{G}_{M,M_0} \vdot \dd{\vb*{\sigma}_0}
$$

其中 $\laplacian G = -\delta(M-M_0)$。

“积分得到的是边界上的源所产生的场，积分是针对边 界处的源点的积分。”

用电像法构造 $G$。考试时只要求将解用定积分和一阶偏导数表示。

## B§5 贝塞尔函数

### 背景

> :material-clock-edit-outline: 2021年11月27日。

解波动方程、扩散方程时，若分离变量，会遇到 Helmholtz 方程

$$
\laplacian V = - \lambda V.
$$

若为圆域，用极坐标进一步分离变量，会导出贝塞尔方程

$$
x^2 \dv[2]{y}{x} + x \dv{y}{x} + (x^2-n^2)y = 0.
$$

该方程的两个级数解称为（第一类）$\pm n$ 阶贝塞尔函数 $J_{\pm n}$。

$$
J_n = \qty(\frac{x}{2})^n \sum_{m\in\N} \frac{1}{m!\ (n+m)!} \qty(-\frac{x^2}{4})^m,
\quad n \in \R.
$$

> $n\in \Z^-$ 时，$\frac{1}{n!}$ 按 $0$ 算。

$n \notin \Z$ 时 $J_n$ 与 $J_{-n}$ 线性独立；$n \in \Z$ 时不再独立（$J_{-n} = (-1)^n J_n$），需要构造另一个特解：第二类贝塞尔函数 $Y_n$。

$$
Y_n = \lim_n \frac{J_n \cos{n\pi} - J_{-n}} {\sin{n\pi}}.
$$

### 性质

> :material-clock-edit-outline: 2021年11月27日。

> 这里的性质只在 $n \in \N$ 时认真检验过。

- 定义

  $$
  x^2 J_n'' + x J_n' + (x^2-n^2) J_n = 0.
  $$

- 幂级数的次数

  - $J_n$ 的最低次项是 $x^n$，并且系数是正的。
  - $J_n$ 要么只有偶次幂，要么只有奇次幂。

- 导数递推

  这两个是最基本的性质，可导出以下所有性质。

  $$
  \begin{aligned}
  \dv{x}(x^n J_n) &= x^n J_{n-1}. \\
  \dv{x} \frac{J_n}{x^n} &= -\frac{J_{n+1}}{x^n}. \\
  \end{aligned}
  $$

  > 第一式左右最低次项都是 $x^{2n-1}$，第二式左右最低次项都是 $x$。

  特别地，$\dv{x} J_0 = -J_1$，$\dv{x}(xJ_1) = xJ_0$。

- 降阶

  $$
  \frac{J_{n-1} + J_{n+1}}{2} = \frac{n J_n}{x}.
  $$

  另外 $J_{n+1} - J_{n-1}= -2\dv{x} J_n$。

- 近似

  $$
  J_n + iY_n \approx \sqrt{\frac{2}{\pi x}} \exp(i \qty(x - \frac\pi4 - \frac{n\pi}{2})).
  $$

  > 上式在 $x \to +\infty$ 时渐近，在 $x = \pm \frac12$ 时余项为零。
  >
  > 左端是 Hankel 函数。

### 从贝塞尔方程证明导数递推性质

> :material-clock-edit-outline: 2021年11月27–28日。

> 我们相信这是可以做到的，尽管尚未做到。

设 $L_n = x^2\dv[2]{x} + x\dv{x} + (x^2-n^2)$，则 $L_n J_n = 0$。

设 $P = x\dv{x}$，则 $L_n = P^2 + (x^2-n^2)$。

由 $L_i - L_j = j^2-i^2$，

$$
\begin{split}
L_i J_j
&= (L_i - L_j)J_j + L_jJ_j \\
&= (j^2-i^2)J_j + 0 = (j^2-i^2)J_j.
\end{split}
$$

再翻回来得到 $P^2J_j = (L_i^2 - x^2+i^2)J_j = (j^2-x^2)J_j$。

又 $P x^k = k x^k$，$P^2 x^k = k Px^k = k^2 x^k$。

因此，

$$
\begin{split}
P^2(x^k J_j)
&= (P^2x^k)J_j + 2(Px^k)(PJ_j) + x^k P^2 J_j \\
&= x^k (k^2 + 2k P + P^2) J_j \\
&= x^k (k^2 + 2kP + j^2-x^2) J_j.
\end{split}
$$

$$
\begin{split}
x^{j+1}J_{j-1}
&\overset?= P(x^jJ_j) \\
&= (Px^j)J_j + x^j PJ_j \\
&= x^j (j + P) J_j.
\end{split}
$$

---

设 $R = \frac{1}{x} \dv{x}$，则需证 $R(x^nJ_n) = x^{n-1}J_{n-1}$ 和 $R(x^{-n}J_n) = -x^{n+1}J_{n+1}$。

$$
\begin{split}
R^2
&= \qty(R\frac{1}{x})\dv{x} + \frac{1}{x}R\dv{x} \\
&= -\frac{1}{x^3} \dv{x} + \frac{1}{x^2} \dv[2]{x}.
\end{split}
$$

$$
\begin{split}
RP
&= \qty(Rx)\dv{x} + xR\dv{x} \\
&= R + \dv[2]{x}.
\end{split}
$$

$$
\begin{split}
PR
&= \qty(P\frac{1}{x})\dv{x} + \frac{1}{x}P\dv{x} \\
&= -R + \dv[2]{x}.
\end{split}
$$

### 用递推性质验证贝塞尔方程

> :material-clock-edit-outline: 2021年11月28日。

替换下标，得 $J_n$ 与 $J_{n+1}$ 的关系

$$
\begin{aligned}
\dv{x}(x^{n+1} J_{n+1}) &= x^{n+1} J_n. \\
\dv{x} \frac{J_n}{x^n} &= -\frac{J_{n+1}}{x^n}. \\
\end{aligned}
$$

将第二式代入第一式，得

$$
\begin{split}
-x^{n+1} J_n
&= \dv{x} (x^{2n+1} \dv{x}\frac{J_n}{x^n}) \\
&= \dv{x} (-nx^n J_n + x^{n+1} J_n') \\
&= -n^2 x^{n-1} J_n -nx^n J_n' + (n+1)x^n J_n' + x^{n+1}J_n'' \\
&= -n^2 x^{n-1} J_n + x^n J_n' + x^{n+1}J_n''.
\end{split}
$$

整理得

$$
x^2 J_n'' + x J_n' = (n^2-x^2) J_n.
$$

证毕。

# 后备箱

- 辐角<u>多值</u>，主辐角单值。
- 区分数列收敛与部分和收敛。
- 求级数的和函数、将函数展开为幂级数时注意<u>收敛域</u>。
- $\oint \frac{\dd{z}}{z} = 2\pi i$，$\oint = 2\pi i \sum\Res$，有个 $2\pi i$。
- 注意微分方程及初始、边界条件中自变量的<u>范围</u>。
- 结果的分母不能保留$i$。
- 行波法中，特征方程 $A(\dd{y})^2 - 2B\dd{x}\dd{y} + C(\dd{x})^2 = 0$ 中交叉项有个负号。
- 强调特征函数系的来源（边界条件的类型）。
- 使用 Cauchy – Riemann 条件时，强调四个偏导数存在且连续。
- 描述多值函数时，写清参数的范围。
- 一般的 $a^b$ 指多值函数 $\exp(b \operatorname{Ln}a)$。
- 调和函数的“共轭”不具有对称性，解析函数的虚部是实部的共轭调和函数。
- 求共轭调和函数时，先检验确实是调和函数。
- 将函数展开成泰勒级数，用比值法或者根值法计算收敛半径或收敛域可能得到不合理的结果。
- Laurent 级数是在环域内展开，题目未指明时，要自己分区。

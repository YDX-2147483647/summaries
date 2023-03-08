# 工科数学分析1

$$
\def\N{\mathbb{N}}
\def\Z{\mathbb{Z}}
\def\Q{\mathbb{Q}}
\def\R{\mathbb{R}}
\def\C{\mathbb{C}}
%
\def\i{\mathrm{i}}
\def\e{\mathrm{e}}
%
\def\d{\mathop{}\!\mathrm{d}}
\def\const{\mathrm{Const.}}
%
\def\arsinh{\operatorname{arsinh}}
\def\arcosh{\operatorname{arcosh}}
\def\artanh{\operatorname{artanh}}
$$

## 1 函数、极限与连续

> :material-clock-edit-outline: 2020年11月12日、2020年11月14日。

### 记号

$$
\displaylines{
N(a, \delta) \triangleq (a-\delta, a+\delta) \\
N^0_+(a, \delta) \triangleq (a,a+\delta)
}
$$

同理定义 $N^0_-(a,\delta),\ N_\pm(a,\delta)$ 。

$$
\forall x\in\R,\quad \lfloor x\rfloor \in\Z\ \land\ \lfloor x\rfloor \leq x \lt \lfloor x\rfloor + 1
$$

### 函数

> 一些特殊而又一般的函数：
> 
> $$
> \operatorname{Dirichlet}(x) = \begin{cases}
> 1& x\in\Q \\
> 0& x\notin\Q
> \end{cases}
> $$
> 
> 在任意点不连续， $Dirichlet(x)\cdot\Pi_i(x-x_i)$ 只在 $x_i$ 处连续。
> 
> $$
> \operatorname{Riemann}(x) = \begin{cases}
> \frac 1q & x=\frac pq \in \Q \\
> 0 & x \notin\Q
> \end{cases}
> $$
> 
> 在有理点间断而在无理点连续。

性质：有界（bounded）性、单调（monotonic）性、对称性（奇偶性（parity）、周期（period）性）。

基本初等函数：常函数，幂函数、指数函数、对数函数，三角函数、反三角函数。

### 三角函数和双曲函数

#### 同角函数关系

$$
\begin{array}%
\sin & \cos  \\
\tan & 1 & \cot \\
 & \sec & \csc
\end{array}
$$

> 向下一格相当于除以$\cos$，向右下一格相当于除以$\sin$。
>
> 再结合 $\sin^2 x + \cos^2 x=1$ 可得到所有的同角三角函数关系。

#### 双曲函数的定义

$$
\displaylines{
\sinh x \triangleq \frac{\e^x-\e^{-x}}2 \\
\cosh x \triangleq \frac{\e^x+\e^{-x}}2 \\
\tanh x \triangleq \frac{\sinh x}{\cosh x}
}
$$

> $\arcsin$ 的“arc”是arc（弧）， $\arsinh$ 的“ar”是area（面积）。

$$
\displaylines{
\arsinh x = \ln(x + \sqrt{x^2+1}) \\
\arcosh x = \ln(x + \sqrt{x^2-1}) \\
\artanh x = \frac{\ln(1+x) - \ln(1-x)}2
}
$$

#### 双曲函数与三角函数的对应

$$
\begin{array}.
\sin x = \frac{\sinh(\i x)}{\i} & \sinh x = \i \sin\frac{x}{\i} \\
\cos x = \cosh(\i x) & \cosh x = \cos\frac{x}{\i}
\end{array}
$$

> 2021年4月23日：
>
> 事实上双曲函数与三角函数的关系和反关系一样。例如
> 
> $$
> \sinh x 
> = \i \sin\frac x\i
> = \i \sin\frac{\i x}{\i^2}
> = \i \sin(-\i x)
> = -\i \sin(\i x)
> = \frac{\sin(\i x)}{\i}
> $$
> 
> 这与 $\sin x =\frac{\sinh(\i x)}{\i}$ 完全一致。 

#### 一些等式

$$
\begin{array}%
\cos^2 x + \sin^2 x = 1 & \cosh^2 x - \sinh^2 x = 1 \\
1 + \tan^2 x = \sec^2 x & 1 - \tanh^2 x = \frac{1}{\cosh^2 x}\\
\\
\d\sin x = \cos x\d x & \d\sinh x = \cosh x\d x \\
\d\cos x = -\sin x\d x & \d\cosh x = \sinh x\d x \\
\d\tan x = \sec^2 x \d x & \d\tanh x = \frac{\d x}{\cosh^2 x} \\
\\
\d\arcsin x = \dfrac{\d x}{\sqrt{1-x^2}} & \d\arsinh = \dfrac{\d x}{\sqrt{1+x^2}} \\
\d\arccos x = -\dfrac{\d x}{\sqrt{1-x^2}} & \d\arcosh = \dfrac{\d x}{\sqrt{x^2-1}} \\
\d\arctan x = \dfrac{\d x}{1+x^2} & \d\artanh = \dfrac{\d x}{1-x^2} \\
\end{array}
$$

另外， $\d\cot x = -\csc^2 x\d x,\ \d\sec x=\sec x\tan x \d x,\ \d\csc x = -\csc x\cot x\d x$ 。

### 极限

#### 定义与性质

若 $f(x)$ 在某 $N^0(x_0)$ 内有定义，则“ $f(x)$ 在 $x_0$ 的极限是$L$”，等价于

$$
\forall\varepsilon >0, \exists \delta >0, \forall x \in N^0(x_0,\delta),\quad f(x) \in N(L, \varepsilon)
$$

记作

$$
\lim_{x\to x_0} f(x) = L
$$

> $\lim = +\infty, -\infty, \infty$ 的，称作有“非正常极限”，但不算存在极限。

极限具有唯一性、局部有界性（对于数列，是全局有界性）、局部保号性、保序性、归并性（Heine定理）、绝对值性质。

若**极限都存在**，则极限的四则运算等于四则运算的极限。（除法还要求分母的极限不为零）

复合函数 $x_1 \mathop{\rightarrow}^{f_{12}} x_2 \mathop{\rightarrow}^{f_{23}} x_3 \\$ 的极限：

$$
\lim_{x_1\to L_1} f_{12}(x_1) = L_2 \land
f_{12}(x_1)\neq L_2 \land 
\lim_{x_2\to L_2} f_{23}(x_2) = L_3 
\quad\Rightarrow\quad
\lim_{x_1\to L_1} f_{23}\circ f_{12} \circ x_1 = L_3
$$

迫敛性，单调有界准则。

#### 例子

$$
\lim_{x\to 0} \dfrac{\sin x}{x} = 1 \\
\lim_{x\to \infty} \left(1+\frac 1x \right)^x = \e
$$

$\exp \dfrac 1x$ 在 $0^-,0^+,\infty$ 的极限分别是 $0,+\infty,1$ 。

#### 无穷小

$$
\lim f = L \quad\Leftrightarrow\quad f=L+\alpha,\quad \alpha \to 0
$$

高阶（更快，$o(\ )$），同阶（$\mathcal O(\ )$），等价（$\sim$）。

> 不是所有无穷小都可比较： $x\to0$ 时的 $\frac 1x$ 与 $\frac{\sin x}{x}$ 。

与标准无穷小的$k$次幂等价的无穷小称作$k$阶无穷小。

求极限时，作为因子的无穷小可作等价替换，其它情况有时可通过四则运算转化出无穷小因子。

> $x\to0$ 时，
> 
> $$
> \dfrac{\tan x - \sin x}{x^3} = \dfrac{\tan x}{x} \cdot\dfrac{1-\cos x}{x^2} = \dfrac{x}{x} \cdot \dfrac{\frac{x^2}2}{x^2} = \frac 12
> $$
> 
> 但
> 
> $$
> \dfrac{\tan x - \sin x}{x^3} = \dfrac{\tan x}{x^3} -\dfrac{\sin x}{x^3} = \infty - \infty
> $$
> 
> 无法进一步求解。

等价无穷小的例子：

$$
\begin{align}
x &\sim \sin x \sim \tan x \sim \sinh x \sim \arcsin x \sim \cdots \\
x &\sim \ln(1+x) \sim \e^x-1 \\
\alpha x &\sim (1+x)^\alpha -1\\
\dfrac{x^2}2 &\sim1 - \cos x
\end{align}
$$

### 连续

#### 定义与性质

$$
\lim f = f
$$

存在定义，存在极限，相等。

> 以上为单点的连续，区间上的连续类似。

- 连续：如上。
- 第一类间断点：左、右极限都存在。
  - 可去间断点：存在双侧极限，但函数值无定义或与极限值不相等。
  - 跳跃间断点：左、右极限不相等。
- 第二类间断点：左或右极限不存在。
  - 无穷型：例如 $\exp\frac 1x$ 在$0$处。
  - 振荡型：例如 $\sin\frac 1x$ 在$0$处。
  - 其它：例如 $\operatorname{Dirichlet}(x)$ 。

连续的性质可类比极限的性质。

另外，闭区间上的连续函数有如下性质。

- 有界，最值定理。
- 零点存在性定理，介值定理。

#### 例子

初等函数在其任意有定义的区间内连续。

### 求极限的方法

先判断极限类型。

#### 简单情况

（直接上例子）

> $$
> \displaylines{
> \lim 0 = 0 \\
> \lim_{x\to x_0} (ax^2+b\ln x+ c\sin x+\cdots) = (\cdots)|_{x=x_0}
> }
> $$

#### $\dfrac 00$

除以零因子。整式也可分解成无理式。

> $$
> \displaylines{
> x\to1:\quad
> \frac{x(x-1)}{x-1} = x \to 1 \\
> 
> x\to1:\quad
> \frac{x-1}{\sqrt x-1}
> = \lim_{x\to1}\frac{(\sqrt x+1)(\sqrt x-1)}{\sqrt x-1}
> = \cdots \\
> 
> \lim_{x\to a} \frac{x-a}{\sqrt[3]x - \sqrt[3]a}
> = \lim_{X=\sqrt[3]x \to \sqrt[3]a = A} \frac{X^3-A^3}{X-A}
> = \lim_{X\to  A} (X^2 + XA + A^2)
> = 3A^2 = 3a^{\frac 23}
> }
> $$

等价无穷小替换。由于更为熟悉 $x\to0$ 时的无穷小，所以可借助换元。不完全分解（如 $(1-\alpha\beta) = (1-\beta) + \beta(1-\alpha)$ ）有时也有帮助。

> $$
> \displaylines{
> x\to0:\quad
> \dfrac{\tan x - \sin x}{x^3} = \dfrac{\tan x}{x} \cdot\dfrac{1-\cos x}{x^2} \to \dfrac{x}{x} \cdot \dfrac{\frac{x^2}2}{x^2} = \frac 12 \\
> 
> \lim_{x\to\frac{\pi}4} \tan(2x)\tan(\frac{\pi}4-x)
> = \lim_{h = \frac\pi4-x \to 0} \tan(\frac{\pi}2 - 2h)\tan h
> = \lim_{h\to0} \frac{\tan h}{\tan(2h)}
> = \lim_{h\to0} \frac{h}{2h}
> = \frac 12 \\
> 
> x\to1:\quad
> \frac{x-1}{\sqrt x-1}
> = \frac{x-1}{(1+(x-1))^{1/2}-1}
> \to \frac{x-1}{\frac12(x-1)}
> = 2 \\
> }
> $$

#### $1^\infty,\ 0^\infty$

$1^\infty$型极限往往可利用 $\lim_{x\to\infty} (1+\frac 1x)^x$ 。

$$
\displaylines{
\alpha \to 0,\ \beta \to \infty,\ \alpha\beta \to L \\
\Rightarrow (1+\alpha)^\beta 
= (1+\alpha)^{\frac{1}{\alpha} \cdot \alpha\beta}
= \left( (1+\alpha)^{\frac 1\alpha}\right) ^ {\alpha\beta}
\to \e^L
}
$$

> $$
> n\to\infty:\quad
> \tan^n \left(\frac\pi4 + \frac 1n \right)
> = \dfrac{\left(1 + \tan\frac 1n \right)^n}{\left(1 - \tan\frac 1n\right)^n}
> \to \dfrac{\exp 1}{\exp(-1)}
> = \e^2
> $$

$\infty^0$型有时可转化为$1^\infty$型。

> $$
> (1+2^x)^{\frac 1x} = 2 \cdot (1+2^{-x})^{\frac 1x}
> $$

#### 无穷级数

> 利用Cauchy收敛原理可证明极限的存在性。

公式。

> $$
> \lim_{n\to\infty} \prod_{i=1}^n (1 - \frac1{(i+1)^2})
> = \lim_{n\to\infty} \prod_{i=1}^n \frac{(i+2)i}{(i+1)^2}
> = \lim_{n\to\infty} \frac{n+1}{2n}
> = \frac 12
> $$

迫敛性。

转化为积分。

#### 杂项

对于 $x \to f(x)$ 迭代而成的数列的极限，证明极限存在（可用单调有界准则等）后，利用 $\lim f(x) = \lim x$ 求极限。

有些题目可能需要分别求左、右极限。

#### L’ Hospital法则与各种方法结合

> :material-clock-edit-outline: 2021年1月14日。

> $$
> \begin{split}
> \lim_{x\to0} \frac{\sqrt{1+x}+\sqrt{1-x}-2}{x^2}
> &= \lim_{x\to0} \frac{\frac{1}{2\sqrt{1+x}} - \frac{1}{2\sqrt{1-x}}}{2x} \\
> &= \lim_{x\to0} \frac{\sqrt{1-x}-\sqrt{1+x}}{2x} \cdot \frac{1}{4\sqrt{1-x^2}} \\
> &= \lim_{x\to0} \frac{-\frac1{2\sqrt{1-x}}-\frac1{2\sqrt{1+x}}}{2} \cdot \frac14 \\
> &= -1 \cdot \frac14
> = - \frac14
> \end{split}
> $$

#### 带Peano余项的Taylor展开

> :material-clock-edit-outline: 2021年1月14日。

>$$
>\begin{split}
>\lim_{x\to0} \frac{\sqrt{1+x}+\sqrt{1-x}-2}{x^2}
>&= \lim_{x\to0} \frac{\left(1 +\frac{x}2 -\frac{x^2}{8} + o(x^2) \right) +
>\left(1 +\frac{-x}2 -\frac{(-x)^2}{8} + o(x^2) \right) - 
>2}{x^2} \\
>&= \lim_{x\to0} \frac{-\frac{x^2}4 + o(x^2)}{x^2}
>= -\frac14
>\end{split}
>$$

## 3 微分中值定理与导数的应用

### Taylor级数

> :material-clock-edit-outline: 2021年1月14日。

（以下的$i$如无说明，皆为 $i=0,1,\cdots$ ）

$$
\begin{align}
\e^x &= \sum_i \frac{x^i}{i!} &= 1 +x +\frac{x^2}2 +\frac{x^3}{6} +\cdots \\
\ln(1+x) &= \sum_{i=1}^{\infty} \frac{(-x)^i}{i} &= x -\frac{x^2}2 +\frac{x^3}3 \pm\cdots \\
\sin x &= \sum_i (-1)^i\frac{x^{2i+1}}{(2i+1)!} &= x -\frac{x^3}{6} +\frac{x^5}{120} \pm\cdots \\
\cos x &= \sum_i (-1)^i\frac{x^{2i}}{(2i)!} &= 1 -\frac{x^2}{2} +\frac{x^4}{24} \pm\cdots \\
\tan x &&= x + \frac{x^3}3 + \frac{2x^5}{15} + \cdots \\
\\
\sqrt{1+x} &= \sum_i \binom{\frac12}{i} x^i &= 1 + \frac{x}2 - \frac{x^2}8 - \cdots \\
(1+x)^n &= \sum_i \binom{n}{i} x^i &= 1 +nx +\frac{n(n-1)x^2}2 +\cdots \\
\end{align}
$$

## 4 不定积分等

> 2020年12月15日\~2020年12月16日。

### 基本

$$
\displaylines{
\int\frac{\d x}{\cos^2x} = \tan x + \const \\
\int\frac{\d x}{\sin^2 x} = \cot x + \const \\
\int\frac{\d x}{\sqrt{1-x^2}} = \arcsin x + \const = -\arccos x + \const \\
\int\frac{\d x}{\sqrt{x^2+1}} = \arsinh x + \const = \ln(x + \sqrt{x^2+1}) + \const \\
\int\frac{\d x}{\sqrt{x^2-1}} = \arcosh x + \const = \ln(x - \sqrt{x^2-1}) + \const \\
\int\frac{\d x}{x^2 + 1} = \arctan x + \const \\
}
$$

> 一些变形：
> 
> $$
> \displaylines{
> \int\frac{\d x}{\sqrt{a^2x^2 \pm b^2}} = \frac{1}{a} \ln(ax + \sqrt{a^2x^2 \pm b^2}) + \const \\
> \int\frac{\d x}{a^2x^2 + b^2} = \frac{1}{ab} \cdot \arctan \frac{ax}{b} + \const \\
> }
> $$

### 将有理真分式分解为简单分式的和

#### 目的

简单分式是形如 $\dfrac{c}{(x-\xi)^\lambda},\ \lambda\in\N_+$ 或 $\dfrac{c_1x + c_0}{(x^2 - 2\alpha x + \beta)^\mu},\ 0\leq\alpha^2<\beta\ \land\ \mu\in\N_+$ 的分式。因为$\int \d x$是线性的，所以可通过计算简单分式的积分来计算有理真分数的积分。

$$
\displaylines{
\int\dfrac{c \d x}{(x-\xi)^\lambda}
= c\int\dfrac{\d(x-\xi)}{(x-\xi)^\lambda}
\rightarrow
\int \dfrac{\d x}{x^\lambda} = \begin{cases}
\ln x & \lambda = 1 \\
- \frac 1{(\lambda-1) x^{\lambda-1}} & \lambda \geq 2 \\
\end{cases}
\\

\begin{split}
\int \dfrac{c_1x + c_0}{(x^2 - 2\alpha x + \beta)^\mu} \d x
&= \int \dfrac{c_1(x-\alpha) + c_1\alpha + c_0}{((x-\alpha)^2 + \beta - \alpha^2)^\mu} \d x \\
&= \frac{c_1}{2(\beta-\alpha^2)^{\mu-1}} \cdot \int\frac{\d \frac{(x-\alpha)^2}{\beta-\alpha^2}} {\left(\frac{(x-\alpha)^2}{\beta-\alpha^2} + 1 \right)^\mu} + 
\frac{c_1\alpha + c_0}{(\beta-\alpha^2)^{\mu-\frac12}} \cdot \int\frac{\d \frac{x-\alpha}{\sqrt{\beta-\alpha^2}}} {\left(\frac{(x-\alpha)^2}{\beta-\alpha^2} + 1 \right)^\mu} \\
&\rightarrow
\int \frac{\d u}{(u+1)^\mu} + \int \frac{\d x}{(x^2+1)^\mu}
\end{split}
}
$$

> 第二项可用三角换元 $x = \tan \theta, \d x = \frac{\d\theta}{\cos^2 \theta}$ 求出：
> 
> $$
> \begin{split}
> \int \frac{\d x}{(x^2 + 1)^\mu}
> &= \int \frac{\sec^2\theta \d \theta}{(\tan^2 \theta + 1)^\mu} \\
> &= \int \cos^{2(\mu-1)}\theta \d\theta
> \end{split}
> $$
> 
> $\cos^{2n}x$ 可降幂为 $\sum_{i=0}^n a_{i,n}\cos(2ix)$ （第一类切比雪夫多项式），逐项积分后再升幂为 $\cos x$ 的函数，然后代入 $\cos^2\theta = \frac 1{1 + x^2}$ 及 $\theta = \arctan x$ 即可。
>
> 或者利用 $m\int\cos^nx \d x = \sin x \cos^{m-1}x + (m-1) \int\cos^{m-2}x\d x$ 逐渐求出。
>
> 也可直接分部积分得出递推式，从而求出：
> 
> $$
> \displaylines{
> I_1 = \int \frac{\d x}{x^2+1} = \arctan x + \const \\
> \begin{split}
> \forall \mu \in \N_+, \quad
> I_\mu = \int \frac{\d x}{(x^2+1)^\mu}
> &= \frac{x}{(x^2+1)^\mu} - \int x \d\frac1{(x^2+1)^\mu} \\
> &= \frac{x}{(x^2+1)^\mu} - \int x \frac{2x}{(x^2+1)^{\mu+1}} \d x \\
> &= \frac{x}{(x^2+1)^\mu} - 2\mu \int \frac{x^2+1-1}{(x^2+1)^{\mu+1}} \d x \\
> &= \frac{x}{(x^2+1)^\mu} - 2\mu \int \frac{\d x}{(x^2+1)^\mu} + 2\mu \int\frac{\d x}{(x^2+1)^{\mu+1}}\\
> &= \frac{x}{(x^2+1)^\mu} - 2\mu I_\mu + 2\mu I_{\mu+1}
> \end{split}
> \\
> \therefore \forall \mu \in \N_+, \quad 2\mu I_{\mu+1} = (1+2\mu)I_\mu - \frac{x}{(x^2+1)^\mu}
> }
> $$
> 
> 然而一般题的次数都不高，所以很可能用不到这些。

#### 一般

设有理真分式为 $\frac{p(x)}{q(x)}$ ，其中 $q(x)$ 是最高次项系数为一的实系数$n$次多项式， $p(x)=\sum_{k=0}^{n-1} a_k x^k$ 。

故 $q(x)$ 在$\C$内有$n$个根，且 $q(z)=0 \Leftrightarrow q(\bar z) = 0$ ，故其中的复根成对。因此可将 $q(x)$ 分解：

$$
\begin{split}
q(x)
&= \prod_{\xi_i\in\R}(x-\xi_i) \cdot \prod_{\Re\eta_j > 0}(x-\eta_j)(x - \overline{\eta_j}) \\
&= \prod_{\xi_i\in\R}(x-\xi_i) \cdot \prod_{\Re\eta_j > 0}(x^2 - 2\Re\eta_j  + |\eta_j|^2) \\
&= \prod_i (x-\xi_i)^{\lambda_i} \cdot \prod_j(x^2 - 2\alpha_j x + \beta_j)^{\mu_j}
\qquad (\forall j,\quad 0 \leq \alpha_j^2 < \beta_j) \\
\end{split}
$$

那么可待定系数$c$：

$$
\dfrac{\sum_{k=0}^{n-1} a_k x^k}{q(x)}
=
\sum_i \sum_{k=1}^{\lambda_i} \dfrac{c_{1,i,k}}{(x-\xi_i)^k} +
\sum_j \sum_{k=1}^{\mu_j} \dfrac{c_{2,j,k,1}x+c_{2,j,k,0}}{(x^2 - 2\alpha_j x + \beta_j)^{\mu_k}}
$$

左侧有$n$个参数，右侧有 $\sum_i \lambda_i + \sum_j 2\mu_j$ 个参数。考察$\lambda,\mu$的定义，可知两侧参数数量相等。因此，解线性方程组即可确定$c$。

#### 特殊

（$\beta>\alpha^2$）

$$
\begin{split}
\int \frac{c_1x + c_0}{x^2 - 2\alpha x + \beta} \d x
&= \frac{c_1}2 \ln(x^2 - 2\alpha x + \beta) + \int \frac{c_1 \alpha + c_0}{x^2 - 2\alpha x + \beta}\d x \\
&= \frac{c_1}2 \ln(x^2 - 2\alpha x + \beta) + 
\frac{c_1\alpha+c_0}{\sqrt{\beta-\alpha^2}}\cdot \arctan \frac{x-\alpha}{\sqrt{\beta - \alpha^2}} +
\const
\end{split}
$$

（$\beta\leq\alpha^2$时可以配方）

### 三角有理式

万能代换（$x = \tan\frac\theta2$）。

> $$
> \int \sin^5 x \d x = \int (1-\cos^2 x)^2 \d \cos x = \cdots
> $$

只含有 $\sin^2 x, \sin x\cos x, \cos^2 x$ 等（可与$\tan x$一一对应的三角函数）的，可化为 $\int f(\tan^2 x) \sec^2 x \d x = \int f(\tan^2 x) \d \tan x$ 。

有时直接进行恒等变形即可。

> $$
> \displaylines{
> \int \tan^2 x\d x = \int (\sec^2 x - 1)\d x = \tan(x) - x + \const \\
> \begin{split}
> \int \frac{x\d x}{1+\cos x} 
> &= \int \frac{x}{2} \sec^2\frac{x}{2} \d x 
> = \int x\d \tan\frac{x}{2} \\
> &= x \tan\frac{x}{2} - \int \tan\frac{x}{2}\d x  \\
> &= x \tan\frac{x}{2} + 2\ln \cos\frac{x}{2} + \const
> \end{split}
> }
> $$

### 应用

#### 绕$x$轴的旋转体的体积

$$
\displaylines{
V = \int_0^{x_0} \pi y^2 \d x \\
V = \int_{\frac\pi2}^0 \pi \rho^2 \sin^2\theta \d(\rho\cos\theta)
= \pi \int_0^{\frac\pi2} \rho^2\sin^2\theta \cdot \left( \rho\sin\theta - \frac{\d\rho}{\d\theta}\cos\theta \right) \d\theta \\
V = \int_0^{\frac\pi2} \frac13 \cdot 2\pi\rho\sin\theta \cdot \rho \cdot \rho\d\theta
= \frac{2\pi}3 \int_0^{\frac\pi2} \rho^3\sin\theta \d\theta \\
}
$$

> $$
> \displaylines{
> \begin{split}
> \frac{V}{\pi}
> &= \int_0^{\frac\pi2} \rho^2\sin^2\theta \cdot \left( \rho\sin\theta - \frac{\d\rho}{\d\theta}\cos\theta \right) \d\theta \\
> &= \int_0^{\frac\pi2} \left( \rho^3\sin^3\theta - \rho^2\frac{\d\rho}{\d\theta}\sin^2\theta\cos\theta \right) \d\theta \\
> &= \int \rho^3\sin^3\theta \d\theta -
> \frac13 \int \sin^2\theta\cos\theta \cdot \frac{\d \rho^3}{\d\theta} \d\theta \\
> \end{split} \\
> 
> \begin{split}
> \text{in which}
> & \int_0^{\frac\pi2} \sin^2\theta\cos\theta \cdot \frac{\d \rho^3}{\d\theta} \d\theta \\
> &= \rho^3\sin^2\theta\cos\theta \Big|_0^{\frac\pi2} - \int_0^{\frac\pi2} \rho^3 \d(\sin^2\theta \cos\theta) \\
> &= 0 - \int_0^{\frac\pi2} \rho^3 (2\sin\theta\cos^2\theta - \sin^3\theta) \d\theta \\
> &= - \int_0^{\frac\pi2} \rho^3 \sin\theta (2\cos^2\theta-\sin^2\theta) \d\theta \\
> &= - \int_0^{\frac\pi2} \rho^3 \sin\theta (2-3\sin^2\theta) \d\theta \\
> \end{split} \\
> 
> \begin{split}
> \therefore \frac{V}{\pi}
> &= \int_0^{\frac\pi2} \rho^3\sin^3 \d\theta + \frac13 \int_0^{\frac\pi2} \rho^3 \sin\theta (2-3\sin^2\theta) \d\theta \\
> &= \int_0^{\frac\pi2} \rho^3 \left( \sin^3 + \frac{2\sin\theta - 3\sin^3\theta}3 \right) \d\theta \\
> &= \int_0^\frac\pi2 \rho^3 \sin^3\theta \d\theta
> \end{split} \\
> }
> $$

## 零点存在性问题

> :material-clock-edit-outline: 2021年1月28日。

已知函数$f$满足若干条件，求证： $\exists \xi, F(x,f,f',\cdots)|_{x=\xi} = 0.$

有多个“$\exists\xi_i$”的，分别用定理表示，联立。

### 依据

- 闭区间上连续函数的性质

  - 零点存在性定理
  - 介值定理

- 微分中值定理

  设 $\varphi(x,f,\cdots)$ ，对它应用定理。

  - Rolle’s
  - Lagrange’s
  - Cauchy’s

- Taylor中值定理

- 积分中值定理

  - $\exists\xi, f(\xi) = \bar f.$
  - $\exists\xi,\quad \int fg\d x = f(\xi) \int g\d x.$

### 手法

- $F=\lambda f' + \mu f'',\quad \lambda,\mu\in\const$

  $\varphi = \lambda f + \mu f'$

- $F=u(x) f + v(x) f'$

  设 $\varphi = C(x) f,\quad C\not\equiv 0$ ，那么 $\varphi' = C'f + C f'$ 。要让$\varphi$是$F$的倍数，即 $C'v-Cu=0$ 。这是关于$C$的微分方程，解出来即可。注意，即使$u,v$不是具体函数，$C$也能解出。

  > 对于$F=f+f'$，可设$\varphi=\e^x f$，保证$\varphi=0$时$F=0$。

- $F=\lambda f + \mu f''$

  一般可找出一个含$f,f’$的函数，使$F$是它与它的导数的组合。

# 注意

注意求切线还是法线。

$\lim_{x\to\infty}$是<u>双侧</u>极限。

$\sqrt{x^2}=|x|=\pm x$ ，要分类。

> $$
> \lim_{x\to\pm\infty} (\sqrt{2x^2+x} - \sqrt{2x^2+1})
> = \lim_{x\to\pm\infty} \frac{1-x}{\sqrt{2x^2+x} + \sqrt{2x^2+1}}
> = \pm\frac1{2\sqrt2}
> $$

求极限时取对数后记得再取回去。

导数不存在点也可能是极值点。

不定积分加 $\const$ 。

注意积分区间（顺序、变化）。

换元法求<u>不定积分</u>时，答案要==换回原变量==；解微分方程组时，结果要写明所有的函数。

求定积分时，可能涉及 $\sqrt{\pm x}$ 一类的问题，也可能有瑕点。

微分方程可能有奇解，要检验。

# 后备箱

二阶微分不具有形式不变性。

恰当方程。

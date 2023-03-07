---
relevant:
  - ./physics-1.md
  - ./probability-and-statistics.md
---

# 物理2

$$
\def\R{\mathbb{R}}
$$

## §2 导体与电介质

### 大平板的紧邻处

> :material-clock-edit-outline: 2021年10月19日。

#### 试验

$$
\begin{split}
    & \lim_{h\to 0^+} \int\limits_0^{+\infty} \frac{\eval{\sigma}_r rh \dd{r}}{\sqrt{r^2+h^2}^3} \\
    &= \lim_{h\to 0^+} \int\limits_0^{\frac\pi2} \frac{\eval{\sigma}_{h\tan\varphi} \tan\varphi \sec[2]\varphi \dd{\varphi}}{\sec[3]\varphi} \\
    &= \lim_{h\to 0^+} \int\limits_0^{\frac\pi2} \eval{\sigma}_{h\tan\varphi} \sin\varphi \dd{\varphi}. \\
\end{split}
$$

$$
\begin{array}{c|c}
    \sigma_r & \lim \\
    \hline
    \sqrt{r} & 0 \\
    1 & 1 \\
    e^{-r} & 1 \\
    e^{-r^2} & 1 \\
    \frac{1}{1+r} & 1 \\
    \frac{1}{1+r^2} & 1 \\
    1-\frac2\pi \arctan r & 1 \\
\end{array}
$$

#### 总结

设无限大平板 $(x,y)$ 处的电荷面密度是 $\eval{\sigma}_{x,y}$，则 $(0,0)$ 处正下方距离 $z_0$ 处的电场强度

$$
\vb*{F}
= \iint\limits_{\R^2} \frac {- \qty(x \vu*{x} + y \vu*{y} + z_0 \vu*{z}) \eval{\sigma}_{x,y} \dd{x}\dd{y}} {\qty(x^2 + y^2 + z_0^2)^{3/2}}.
$$

为简化式子，设一个 $\R^3 \to \R^3$ 的函数 $\eval{\vb*{f}}_{x,y,z} = -\qty(x \vu*{x} + y \vu*{y} + z_0 \vu*{z}) / (x^2+y^2+z_0^2)^{3/2}$，这样

$$
\vb*{F} = \iint_{\R^2} \eval{\vb*{f}}_{x,y,z_0} \eval{\sigma}_{x,y} \dd{x}\dd{y}.
$$

现在换元 $x = z_0 x', y = z_0 y'$：

$$
\vb*{F} = \iint_{\R^2} \eval{\vb*{f}}_{z_0(x',y',1)} \eval{\sigma}_{z_0(x',y')} z_0^2 \dd{x'}\dd{y'}.
$$

由于 $\vb*{f}$ 其实是单位点电荷附近的电场，满足平方反比律 $\eval{\vb*{f}}_{z_0(x',y',1)} \propto 1/z_0^2$，故

$$
\begin{split}
    & \vb*{F} = \iint_{\R^2} \eval{\vb*{f}}_{x',y',1} \eval{\sigma}_{z_0(x',y')} \dd{x'}\dd{y'}. \\
    &\implies \lim_{z_0 \to 0^+} \vb*{F} = \iint_{\R^2} \eval{\vb*{f}}_{x',y',1} \eval{\sigma}_{0,0} \dd{x'}\dd{y'} = \frac{\eval{\sigma}_{0,0}}{2\varepsilon_0}. \\
\end{split}
$$

——无限大平板紧邻处的电场相当于“以此处电荷面密度为面密度的”均匀无限大平板旁的电场，

### 电位移、电场强度、极化强度

> :material-clock-edit-outline: 2021年10月29日。

$$
\begin{aligned}
& \frac{\vb*{D}}{\varepsilon_r} = \frac{\varepsilon_0 \vb*{E}}{1} = \frac{\vb*{P}}{\chi} . \\
& \varepsilon_r = 1 + \chi.
\end{aligned}
$$

### 电势叠加原理

- 球面上不均匀的电荷在球心产生的电势易求。
- 外电场让（接地或不接地的）导体球感应电荷，则球心的电势可以代表整个导体球的电势。

### 电偶极矩

> :material-clock-edit-outline: 2021年9月23日。

#### 记号

用 $q_1$ 表示 $+q$，$q_2$ 表示 $-q$，则 $\sum_i q_i = 0$。

以 $-q$ 所在处为原点，电偶极矩 $\boldsymbol p$ 就是 $\sum_i q_i \boldsymbol r_i$。其实不论原点怎么选，$\sum_i q_i \boldsymbol r_i$ 都是 $p$，因为 $\sum_i q_i (\boldsymbol r_i + \boldsymbol s) = \sum_i q_i \boldsymbol r_i + \left(\sum_i q_i \right) \boldsymbol s = \boldsymbol p + \boldsymbol 0$。

---

取 $O$ 为这些 $q_i$ 附近一点，$P$ 为要讨论场强的地方。（$q_i$ 的范围相对 $OP$ 很小）

类似书上 22 页图 1-17（但方向不同），设 $\boldsymbol r_0 = \overrightarrow{PO}$，设 $\boldsymbol \delta_i$ 为从 $O$ 到 $q_i$ 处的向量，$\boldsymbol r_i$ 为从 $P$ 到 $q_i$ 处的向量，则 $\boldsymbol r_i = \boldsymbol r_0 + \boldsymbol \delta_i$。

#### 计算场强

现在讨论 $P$ 处的场强 $\boldsymbol E$。由叠加原理，

$$
4\pi\varepsilon_0 \boldsymbol E = -\sum_i \frac{q_i}{r_i^3} \boldsymbol r_i.
$$

##### 用 $\delta_i \ll r_0$ 近似

$$
\begin{split}
    r_i
    &= \sqrt{r_0^2 + \left( 2 \boldsymbol r_0 \cdot \boldsymbol\delta_i + \delta_i^2 \right)} \\
    &= r_0 +\frac12 {2\boldsymbol r_0 \cdot \boldsymbol\delta_i + \delta_i^2 \over r_0}
    	- \cdots \\
    &\approx r_0 + \boldsymbol{\hat r_0} \cdot \boldsymbol \delta_i.
\end{split}
$$

> $\boldsymbol{\hat x}$ 表示 $\boldsymbol x/\abs{x}$。

所以

$$
\begin{split}
    r_i^{-3}
    &\approx (r_0 + \boldsymbol{\hat r_0} \cdot \boldsymbol\delta_i)^{-3} \\
    &= r_0^{-3} - 3 r_0^{-4}\ \boldsymbol{\hat r_0} \cdot \boldsymbol\delta_i \pm \cdots \\
    &\approx r_0^{-3} - 3 r_0^{-4}\ \boldsymbol{\hat r_0} \cdot \boldsymbol\delta_i.
\end{split}
$$

##### 代回

$$
\begin{split}
    -4\pi\varepsilon_0 r_0^4 \boldsymbol E 
    &\approx \sum_i q_i \left( r_0 - 3 \boldsymbol{\hat r_0} \cdot \boldsymbol\delta_i \right) \boldsymbol r_i \\
    &= r_0 \sum_i q_i \boldsymbol r_i 
        - 3 \sum_i q_i \left( \boldsymbol{\hat r_0} \cdot \boldsymbol\delta_i \right) \boldsymbol r_i \\
    &= r_0 \boldsymbol p
        - 3 \sum_i q_i \left( \boldsymbol{\hat r_0} \cdot \boldsymbol\delta_i \right) \boldsymbol r_0
        - 3 \sum_i q_i \left( \boldsymbol{\hat r_0} \cdot \boldsymbol\delta_i \right) \boldsymbol\delta_i \\
    &\approx r_0 \boldsymbol p
        - 3 \sum_i q_i \left( \boldsymbol{\hat r_0} \cdot \boldsymbol\delta_i \right) \boldsymbol r_0 \\
    &= r_0 \boldsymbol p
        - 3 \left( \boldsymbol{\hat r_0} \cdot \left(\sum_i q_i \boldsymbol\delta_i \right) \right) \boldsymbol r_0 \\
    &= r_0 \boldsymbol p
        - 3 \left( \boldsymbol{\hat r_0} \cdot \boldsymbol p \right) \boldsymbol r_0 \\
    &= r_0\left( \boldsymbol p - 3 (\boldsymbol{\hat r_0} \cdot \boldsymbol p) \boldsymbol{\hat r_0} \right).
\end{split}
$$

因此

$$
\boldsymbol E = {- \boldsymbol p + 3 (\boldsymbol{\hat r_0} \cdot \boldsymbol p) \boldsymbol{\hat r_0} \over 4\pi\varepsilon_0 r_0^3}.
$$

### 电偶极矩——用电势叠加原理

> :material-clock-edit-outline: 2021年10月5日。
>
> “由于电势是标量，用叠加原理来计算比计算场强矢量简便得多。”（《新概念·电磁学》41页）

#### 等量异种点电荷远处

$$
\begin{split}
    U &= \frac{q}{4\pi\varepsilon_0} \qty(\frac{1}{r_+} - \frac{1}{r_-}) \\
    &\approx \frac{q}{4\pi\varepsilon_0} \dv{\frac1r}{r} \qty(r_+ - r_-) \\
    &= \frac{1}{4\pi\varepsilon_0} \frac{\vb*{p} \cdot \vu*{r}}{r^2}
    = \frac{1}{4\pi\varepsilon_0} \frac{\vb*{p} \cdot \vb*{r}}{r^3}.
\end{split}
$$

再求负梯度。

$$
\begin{split}
    \vb*{E} &= - \grad{U} \\
    &= \frac{1}{4\pi\varepsilon_0} \qty( - \qty(\vb*{p} \cdot \vb*{r}) \frac{3}{r^4} \vu*{r} + \frac{\vb*{p}}{r^3} \cdot I) \\
    &= \frac{1}{4\pi\varepsilon_0} \frac{\vb*{p} - 3(\vb*{p} \cdot \vu*{r}) \vu*{r}}{r^3}.
\end{split}
$$

## §3 静磁场

### 带电旋转圆环所受力矩

> :material-clock-edit-outline: 2021年11月14日。

设一右手系。$Oxy$面内有一均匀带电圆环，电荷线密度为$\lambda$，半径为$R$。圆环匀速旋转，角速度 $\vb*{\omega} = \omega \vu*z$。外界有匀强磁场 $\vb*B = B \vu*x$，问磁场给圆环的力矩。

#### 按电流算

$I \vb*{\dd{l}}$ 相当于 $\dd{q} \vb*{v}$，故 $I = \lambda \omega R$，进而磁矩 $\vb*m = I \vb*S = IS \vu*z$。

因此力矩 $\vb*M = \vb*m \cp \vb*B = ISB \vu*y = \lambda \omega \pi R^3 B \vu*y$。

#### 按运动电荷算

使用微元法。$\vb*r = R(\cos\theta, \sin\theta, 0)$ 处附近有电荷 $\dd{q} = \lambda R\dd{\theta}$，其速度 $\vb*{v} = \vb*\omega \cp \vb*r = v(-\sin\theta, \cos\theta, 0)$。

按这种方法，合力为零不是显然的。所受洛伦兹力 $\dd{\vb*f} = \dd{q} \vb*v \cp \vb*B = - f_m \cos\theta \vu*z$，其中 $f_m = \lambda R v B$。合力

$$
\vb*f = \oint \dd{\vb*f} = -f_m \int\limits_0^{2\pi} \cos\theta \dd{\theta} \vu*z = \vb*0.
$$

现在计算力矩 $\vb*M$。以 $O$ 为参考点，则 $\dd{\vb*M} = \vb*r \cp \dd{\vb*f} = Rf_m \cos\theta (-\sin\theta, \cos\theta, 0)$。因此合力矩

$$
\begin{split}
\vb*M 
&= \oint \dd{\vb*M} \\
&= R f_m \int\limits_0^{2\pi} (-\sin\theta, \cos\theta, 0) \cos\theta \dd{\theta} \\
&= R f_m \pi \vu*y
= \lambda \omega \pi R^3 B \vu*y.
\end{split}
$$

### 无限长带电圆柱面

> :material-clock-edit-outline: 2022年11月6日。

有一无限长均匀带电圆柱面，绕轴转动，请问管内外磁场分布怎样？

注意此场景就是“无限长载流直螺线管”，可参考教材206页 §3.4.3 例3–9。

书上是从极限过程分析的，逻辑少，容易理解；然而未免有插科打诨嫌疑。这里从对称性严格分析一下。（对称性是电磁学的一大主题，在平时多思考思考无碍。）

#### 对称性

> 对称性有两种论证思路。
>
> - 找对称的两点，考虑它们作用之和。
> - 做某种对称操作，考虑操作前后的变化。
>
> 这里按第二种来。

> 电流分布有柱对称性，下面所说的径向、切向、轴向分别指 $\hat \rho$、$\hat \varphi$、$\hat z$。

- 切向：

  1. <u>绕轴旋转</u>对称性 ⇒ $\rho,z$ 相同时，切向分量与 $\varphi$ 无关。
  2. **安培环路定律**（环路取 $\rho = \rho_0$，$z = z_0$） ⇒ $\oint \vb*{B} \vdot \vb*{\dd{l}} = 0$ ⇒ 切向分量为零。

- 径向：

  1. 绕轴旋转对称性 ⇒ $\rho,z$ 相同时，径向分量与 $\varphi$ 无关。

  2. 对称性：<u>电流反向</u>，再<u>绕任意半径旋转</u>半周后，场景不变。

     电流反向 ⇔ $\vb*{B}$ 反向；由 1. 绕任意半径旋转半周相当于没变。

     因此这一对称性 ⇒ 无径向分量。

- 轴向：

  - 沿轴<u>平移</u>对称性 ⇒ $\rho,\varphi$ 相同时，轴向分量与 $z$ 无关。
  - 类似207页图3-53，在 $\varphi$ 平面找一矩形环路，但不跨越圆柱面，运用**安培环路定律** ⇒ $\rho,\varphi$ 相同时，轴向分量在管内外分别与 $\rho$ 无关。

以上推理说明：

- 无论在管内管外，$\vb*{B}$ 都最多有轴向分量。
- $\vb*{B}$ 在管内、管外分别匀强。

至此，$\vb*B$ 在全空间只有管内、管外强度两个变量待定。

#### 物理实际

上面只考虑了对称，下面来考虑一点物理实际。（也就是207页剩下的部分）

##### 管外磁感应强度为零

取特殊点 $\rho \to +\infty$。因为远离所有电流，磁感应强度为零。

> 由 BSL 定律，$\abs{\vb*{B}}$ 最差也是按 $1/\rho$ 衰减的。

再根据管外匀强，整个管外 $\vb*{B}$ 都是零。

##### 管内磁感应强度为 $\mu_0 I_s$

> $I_s$ 是面电流线密度。

在 $\varphi$ 平面找一矩形环路，但**跨越圆柱面**，运用安培环路定律 ⇒ 管内管外磁感应强度之差是 $\mu_0 I_s$。

结合上一节可得结论。

---

// 电荷均匀分布于无限长圆柱面，“绕轴匀速转动”（无限长螺线管）和“沿轴匀速平移”（无限长空心导线）是两个典型模型，结课后最好达到“做梦都能梦清楚”的程度。

## §4 电磁感应和电磁场

### 感生电动势

> :material-clock-edit-outline: 2022年1月2日。

除了用 $\dd{\mathcal{E}} = \vb*E \vdot \dd{\vb*r}$ 计算，还可以构造闭合回路。

例如长螺线管中有均匀变化的电流，另有一导线从无穷远到无穷远，且不进入螺线管，则导线上的感生电动势只取决于导线在无穷远处的方向（以及绕了几圈），而与它在螺线管附近的情况无关。构造另一直折导线与此导线构成闭合回路，且经过中心轴。由于感生电场处处与新导线垂直，从而新导线上无电动势，故回路中电动势等于原导线的电动势。再结合法拉第电磁感应定律可得结论。

## 讨论区

### 环路定理用不到平方反比

> :material-clock-edit-outline: 2021年10月2日。
>
> [第九讲讨论](https://www.icourse163.org/learn/BIT-20020?tid=1464961443#/learn/content?type=detail&id=1243646592&cid=1267148225)：在证明高斯定理时，说电力必须与 $r^2$ 成反比，那么在环路定理的证明中是否也必须要求与 $r^2$ 成反比？在证明静电场高斯定理时，只用到平方反比律、与电量成正比、可叠加性，并不需要径向性和球对称性；那么在证明静电场环路定理时，平方反比律、与电量成正比、可叠加性、径向性和球对称性是否都需要用到呢。

不。用到了可叠加性、径向性（径向性就是球对称性吧？）。

事实上随便设一个 $\vb*{F} = \eval{\lambda}_r \vb*{r}$都行：

$$
\begin{split}
    \curl\vb*{F}
    &= \lambda \curl \vb*{r} + \grad{\lambda} \cross \vb*{r} \\
    &= \lambda \vb*{0} + \pdv{\lambda}{r} \frac{\vb*{r}}{\norm{\vb*{r}}} \cross \vb*{r} \\
    &= \vb*{0} + \pdv{\lambda}{r} \frac{\vb*{0}}{\norm{\vb*{r}}} \\
    &= \vb*{0}.
\end{split}
$$

> 2021年10月5日补。

库仑定律中的“平方反比”意味着立体角，从而有高斯定理。上面随便设的场是有心力场（方向为径向，大小只与距离有关）。

### 关于爱因斯坦的成就

> :material-clock-edit-outline: 2021年12月26日。
>
> [第二周第八讲讨论](https://www.icourse163.org/spoc/learn/BIT-1465203161?tid=1466118443#/learn/forumdetail?pid=1324087822)：
>
> 爱因斯坦因为提出光子说而成功的解释了光电效应的实验结果而获得了1921年的诺贝尔物理学奖，试讨论爱因斯坦所取得一下代表性成就中，哪一个意义更大，哪一个更该获得诺贝尔物理学奖：
>
> 光子学说及波粒二象性、狭义相对论及质能关系、广义相对论、以及关于布朗运动的理论。

- 光子学说及波粒二象性：爱因斯坦对光子的理解比普朗克更深，这是开创性、概念性的工作；不过彼时量子论已经呼之欲出了。
- 狭义相对论及质能关系：就历史而言，爱因斯坦也许算集大成者，不是首创者。
- 广义相对论：没有爱因斯坦，可能二战后才广义相对论，相关数学也不会发展得这么好。
- 关于布朗运动的理论：单看这篇可能微不足道的，但“据说”这是爱因斯坦后续在黑体辐射方面的工作的铺垫。

综上所述，爱因斯坦在**广义相对论**方面的工作起的是关键作用，他在这方面对人类的意义最大。

不过，诺贝尔奖不负责奖励绝妙的想法，它要奖励实验验证过的确凿无疑的东西。在当时，无疑只有光电效应和布朗运动，而布朗运动本身恐怕不值得，于是还是给**光电效应**罢。

# 后备箱

- 电场、电势都能跨物体作用。
- 区分外力做功（克服场力做功）与场力做功。
- 极化电荷影响电位移，但不影响其散度。
- 电容被击穿后相当于导线。
- 算磁链时记得考虑匝数。
- 运动物体的光周期与观测到的光周期不同，因为后发出的光要走更远才能被观测到。
- 区分无限长与半无限长。
- 平方反比力二体系统的总能量是负的。
- 原子受激辐射出来的是光子，不是电子。
- 氢原子自发辐射时，区分发出谱线的条数与发出可见光谱线的条数。
- 电介质可以带电，并且使用叠加原理时应当只拆分电荷，而不移走介质。
- 注意向量的<u>方向</u>。
- 波函数的模方才是概率密度。
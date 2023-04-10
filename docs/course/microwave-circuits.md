---
relevant:
  - ./semiconductor-physics.md
  - ./electromagnetic-field-and-wave.md
---

# 微波电路与系统

$$
\def\R{\mathbb{R}}
$$

## 无源器件和半导体器件

### Smith 圆图上的变换

> :material-clock-edit-outline: 2023年3月8日。

$z = \frac{Z_\text{in}}{Z_c}$，$\Gamma = \frac{z-1}{z+1}$。（一种 [Möbius 变换](https://en.wikipedia.org/wiki/M%C3%B6bius_transformation))

|  情况  |     $z$     |       $\Gamma$        |
| :----: | :---------: | :-------------------: |
|  短路  |     $0$     |         $-1$          |
|  开路  |  $\infty$   |          $1$          |
|  匹配  |     $1$     |          $0$          |
| 纯驻波 | $j\times\R$ | $e^{j\times[0,2\pi)}$ |

<figure markdown='span'>
![](../assets/Smith_chart_explanation.svg)
<figcaption markdown='1'>Smith圆图｜[Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Smith_chart_explanation.svg)</figcaption>
</figure>

|                     变换                     |         $\Gamma$ 的效果         | 解释                                |
| :------------------------------------------: | :-----------------------------: | ----------------------------------- |
| 沿传输线移动 $l$<br>（$+l$ 为“源→负载”方向） | 绕 $\Gamma = 0$ 旋转 $2\beta l$ | 入射、反射波分别转动 $\pm\beta l$。 |
|                  串联纯电抗                  |  沿内切于 $\Gamma=1$ 的圆转动   | $z$ 变化纯虚数                      |
|                  串联纯电阻                  |  沿正交于 $\Gamma=1$ 的圆转动   | $z$ 变化实数                        |
|                  并联纯电抗                  |  沿内切于 $\Gamma=-1$ 的圆转动  | $z^{-1}$ 变化纯虚数                 |
|                  并联纯电阻                  |  沿正交于 $\Gamma=-1$ 的圆转动  | $z^{-1}$ 变化实数                   |

!!! note "Möbius 变换的复合"

    $z \leftrightarrow \Gamma$，则 $z^{-1} \leftrightarrow -\Gamma$。

    $$
    \frac{z^{-1}-1}{z^{-1}+1}
    = \frac{1-z}{1+z}
    = - \frac{z-1}{z+1}.
    $$

### 用微带线实现集总电容、电感

> :material-clock-edit-outline: 2023年3月7–8日。

对于宽 $W$、厚 $d$ 的平板传输线，（传播方向）单位长度的电容、电感

$$
L_0 = \mu \frac{d}{W},\quad
C_0 = \varepsilon \frac{W}{d}.
$$

!!! note "平板传输线理想模型"

    电磁场方向、传播方向相互垂直。电磁场局限在平板之间的长方体中，并且均匀分布。
    
    此时 $E d = U$（电势定义），$H W = I$（安培环路定律）。

从而特性阻抗

$$
Z_c = \sqrt{\frac{L_0}{C_0}}
= \sqrt{\frac{\mu}{\varepsilon}} \frac{d}{W},
$$

以及传播速率

$$
\frac{\omega}{\beta} = \frac{1}{\sqrt{L_0 C_0}} = \frac{1}{\sqrt{\mu\varepsilon}} = c.
$$

#### 微带

由物理参数，可得以下近似。

|   $W/d$   |   $Z_c$   | 短线双端口特性 |
| :-------: | :-------: | :------------: |
|   $0^+$   | $+\infty$ |  仅有串联电感  |
| $+\infty$ |   $0^+$   |  仅有并联电容  |

!!! note "短线"

    以上“短线”是指传播方向上的长度小于 $\frac18 \lambda$。

也可从[转移参数](https://en.wikipedia.org/wiki/Two-port_network#ABCD-parameters)（输出电压电流 ↦ 输入电压电流）理解。

取 $+z$ 为“源→负载”方向，$\theta = \beta z$，则微带线的转移参数为

$$
\begin{bmatrix}
    \cos\theta & j \sin\theta Z_c \\
    j \sin\theta / Z_c & \cos\theta \\
\end{bmatrix}.
$$

!!! note "观察"

    - 行列式为一 ⇔ 倒易（reciprocal）。
    - 主对角线上两数相等 ⇔ 对称。（取逆再统一正方向后不变）
    - 主对角线纯实，反对角线纯虚 ⇐ 倒易 ∧ 无耗。
    - 特征值为 $\exp(\pm j\theta)$，特征向量分别是 $U = \pm I Z_c$。

对比串联电感、并联电容的转移参数

$$
\begin{bmatrix}
    1 & j\omega L \\
      & 1 \\
\end{bmatrix},
\quad
\begin{bmatrix}
    1 \\
    j\omega C  & 1 \\
\end{bmatrix},
$$

即得 $\theta \approx 0$，$Z_c \to +\infty$、$Z_c \to 0^+$ 下的近似。

#### 微带支线

除了用作双端口器件，还可用作支线（支线一端短路或开路，另一端接入电路），这相当于与负载**并联**一段传输线。（传输线的输入阻抗可由 Smith 圆图判断）

### P–N结

> :material-clock-edit-outline: 2023年3月25–26日。

!!! note "结与二极管"

    应当区分结（junction）与二极管（diode），前者更微观。然而这里只写大致原理，并不太区分。

P、N区交界处（空间电荷区）扩散作用导致平衡时出现 N→P 方向内建电场。外部加正向电场（P→N）时减弱内建电场，导通；加反向电场时加强空间电荷区，截止。

Shockley diode equation:

$$
I \propto e^u - 1,
$$

其中 $u = q V / \qty(k_B T)$，有时还要除以一个（略大于一的）修正因子。

> :material-eye-arrow-right: [`ECE531-Fall-19-Lecture-07-PN Junctions Electrostatics.pdf`](https://web.eecs.utk.edu/~azeumaul/courses/ee531/fall2019/lecturenotes/ECE531-Fall-19-Lecture-07-PN Junctions Electrostatics.pdf).

这很大程度上是经验公式，不过也能推导。考虑突变结，采用耗尽层假设（空间电荷区多子耗尽，电荷密度分别等于杂质浓度，从而电荷分别均匀分布），电势在突变处两侧分别为半抛物线状分布。

!!! info "势垒区电容"

    势垒区电势为半抛物线状分布，$\abs{Q} \propto \sqrt{\abs{V_\text{势垒}}}$，$C \propto 1/\sqrt{\abs{V_\text{势垒}}}$。

扩散—漂移运动：

1. 扩散取决与浓度负梯度（与 $E_v - E_F$ 或 $E_F - E_c$ 负梯度一致，参考[“载流子浓度公式记忆技巧”中的箭头](./semiconductor-physics.md#重制版)）。
2. 漂移取决于电势负梯度（电子的电势能、真空能级、$E_c$ 或 $E_v$ 之间只差固定常数，负梯度一致）。
3. 两种运动共同效果是 electron/hole exchange is determined by the relative position of the Fermi energies。

<figure markdown='span'>
    ![](../assets/Diode_quasi-fermi_levels.svg)
    <figcaption markdown='1'>Quasi-fermi levels in p-n diode in forward bias｜[Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Diode_quasi-fermi_levels.svg)</figcaption>
</figure>

无外电场时，平衡后两区 $E_F$ 一致，内建电场 N→P，能带（导带底、价带顶或真空能级）P区高于N区。这个电势差记作 $V_D$。

有偏压时，分析恒定电场：

1. 电势仍降落在势垒区（上图中空白区）上，P区、N区远处 $E_F$ 的差等于 $-qV$，远处 $E_c$、$E_v$ 或真空能级的差则是 $q(V_D - V)$。
2. 势垒区由于持续注入非平衡载流子，Fermi 能级分化为两个准 Fermi 能级，$E_{F,p},\, E_{F,n}$ 都不随空间变化。
3. 与其同时，这些非平衡载流子逸出到扩散区（上图中空白区以外），若这里只考虑复合、扩散，则载流子浓度（从边界到远处）按指数变化到平衡浓度。
4. 由于非平衡载流子的影响总以少子为主，可认为扩散区多子的准 Fermi 能级不随空间变化。

!!! info "扩散区电容"

    扩散区 $Q \propto e^u$，$C \propto e^u$。

现在分析电流。

1. 势垒区没有合电流（因为准 Fermi 能级无梯度），但其边界决定了扩散区情况。

    势垒区两端电势能之差等于 $q(V_D - V)$，$E_{F,n} - E_{F,p} = qV$。

    再看载流子浓度。对每一种载流子，在它是多子的一侧，它的浓度就是平衡时浓度；在它是少子的一侧，根据 $E_{F,n} - E_c$ 或 $E_v - E_{F,p}$ 的情况，按 Maxwell–Boltzmann 分布，它的浓度是另一侧浓度再乘 $\exp(q(V_D-V) / (k_B T))$。

    也可直接考虑每一侧。对每一种载流子，在它是少子的一侧，平衡时 $E_F$ 就等于这里多子的准 Fermi 能级，因此它的浓度等于平衡时浓度再乘 $\exp(\Delta E_F / (k_B T)) = \exp(qV / (k_B T)) \eqqcolon e^u$。

    总之，边界处少子有非平衡载流子，浓度等于平衡时浓度再乘 $(e^u - 1)$。

2. 扩散区没有漂移电流（因为电势无梯度），但非平衡载流子指数分布，它有扩散电流。

    指数分布时，扩散电流密度正比于非平衡载流子浓度。（系数是 $qD/L$，其中 $D,L$ 分别是这种载流子的扩散系数、扩散长度）

    因此，$I \propto e^u - 1$。

!!! abstract "一言以蔽之"

    - 正偏压下，势垒降低，势垒区持续注入非平衡载流子，扩散区非平衡少子形成正向扩散电流，导通。
    - 反偏压下，势垒升高，Fermi 能级仍然分化，但效果是减少势垒区的载流子，扩散区非平衡少子仍形成反向电流，但这点~儿~载流子太少了，截止。反偏压较高后，势垒区几乎完全没有载流子，再升高势垒也没用，反向电流于是饱和了。

!!! info "总电容"

    电荷有扩散区、势垒区两部分。两种电容都随电压变化。正偏时扩散区电容很大，为主；反偏时扩散区电容很小，势垒区电容为主。

!!! info "击穿"

    反向电压较高时，反向电流可能突破饱和。

    - 热击穿：反向电流、电压都较大，电热效应明显，再加上热激发载流子恶性循环，最终烧毁。
    - 电击穿
      - 雪崩击穿（又名硬击穿）：反向电压较高时，势垒区电场很强，载流子动能很高，碰撞电离增加载流子浓度，从而反向电流雪崩式增大。
      - Zener 击穿（又名软击穿）：P、N区都重掺杂时，空间电荷区很薄就杂质就能提供足够多电荷达到平衡，因而反向电压不太高时内建电场就很强，存在内部场致发射，增大反向电流。

### M–S结

> :material-clock-edit-outline: 2023年3月26日。

Metal–Semiconductor 结又名 Schottky 结，制成的二极管叫 Schottky barrier diode（SBD）。

M–S结中金属内部均一，接触表面有势垒，半导体内部有缓一些的势垒。外偏压影响半导体内部势垒，决定载流子浓度分布，形成整流特性；接触表面的势垒因钉扎（半导体表面态密度非常高，电子填不过来）而几乎不变。

与P–N结不同，M–S结有整流特性是因为多子在表面附近的势垒，与非平衡载流子、少子关系不大。因此与比P–N结相比，M–S结一般电容更小（没有少子积累），反向饱和电流更大。输运原理不同也导致M–S结略更偏离 $e^u -1$，正向导通电压更小。

制作半导体器件时，金属引线与半导体天然形成的M–S结有害，这时可在半导体表面附近重掺杂，减薄势垒，实现欧姆接触。

### 各种二极管的特性

> :material-clock-edit-outline: 2023年3月26日。

- **变容管**

  主要利用P–N结反向工作时的电容特性。

  对于突变结，$C \propto 1 / \sqrt{\phi - V}$，其中 $\phi$ 是P–N结接触电压。缓变结的$C$对$V$更不敏感，$C \propto 1 / \qty(\phi - V)^m$，$m \approx \frac13$。

  实际还能制造出 $m = 2$ 的超突变结（用于线性调频：$\omega \propto 1 / \sqrt{C} \propto \phi - V$），以及 $m \approx 0^+$ 的阶跃恢复结（正向导通，反向固定电容）。

- **阶跃恢复管**（step recovery diode）

  P⁺–N–N⁺。正偏时低阻，同时在N–N⁺界面积累大量电荷，大电容；反偏时高阻，同时仅P⁺–N势垒区有小电容。非平衡少子寿命很长，与一般P–N结不同。

- **P⁺–I–N⁺管**

  低频时，具有与P–N管类似的整流特性，但耗尽层人为加厚，电容更小且更恒定，反向击穿电压更高。

  高频时I区复合跟不上，是否导通取决于低频分量及相应整流特性。——可利用低频信号控制高频信号通断。

- **雪崩管**（又名 Read 管、放大芯片）

  全名 impact ionization avalanche transit-time（IMPATT）diode。

  原初版为N⁺–薄P–厚I–P⁺，可在N⁺–P发生雪崩，然后向P⁺渡越。这种管可实现放大，且峰值落后于输入交变电压，对外可呈现负阻。

  实用版的薄P–厚I可合并为一个区。为让两种载流子都漂移，还可对称过去做P⁺–P–N–N⁺（双漂移区）。

  大功率时，还可改用 trapped plasma avalanche triggered transit（TRATT）管，P⁺–N–N⁺，整个N区雪崩击穿。

- **转移电子效应管**（transfer electron diode）

  第三代半导体产物。利用多能谷材料的 Gunn 氏效应天然产生振荡。（这种二极管无需结）

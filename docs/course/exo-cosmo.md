---
relevant:
  - ./physics-1.md
  - ./physics-2.md
---

# Exoplanets & Cosmology

!!! info "课程名称"

    本课跨校，有多个名字。

    - 宇宙的诞生与天文学中的地外行星
    - Introduction to Cosmology and Exoplanets
    - 外星探索的机制与案例——NASA的地外行星与生命探索

## Cosmology

### Radiation dilution in the expanding universe

> 2023年5月1日。

空间膨胀时，辐射（如光）的能量除了分布范围扩大（与物质一样），还会直接减少（与物质不同）—— $E = h c / \lambda$，$\lambda$ 会变。

这导致——

- 辐射能量稀释得比物质更快。
- luminosity distance ∝ comoving distance / scale factor.

### Virial 定理

> 2023年4月30日。
>
> :material-eye-arrow-right: [2.11: Virial Theorem - Physics LibreTexts](https://phys.libretexts.org/Bookshelves/Classical_Mechanics/Variational_Principles_in_Classical_Mechanics_(Cline)/02%3A_Review_of_Newtonian_Mechanics/2.11%3A_Virial_Theorem).

#### Etymology

The word *virial* derives from *vis*, the Latin word for “force” or “energy”, and was given its technical definition by Rudolf Clausius in *On a Mechanical Theorem Applicable to Heat* (1870).

#### Derivation

稳定质点系的平均总动能、势能有限制关系。动能太小则坍缩，动能太大则崩解。

构造

$$
G \coloneqq \sum \vb*{p} \vdot \vb*{r}.
$$

稳定系统的 $G$ 保持有界，从而 $\dv{G}{t}$ 的时间平均为零。


$$
\begin{split}
\dv{G}{t}
&= \sum \vb*{p} \vdot \dv{\vb*r}{t}
  + \sum \dv{\vb*p}{t} \vdot \vb*{r} \\
&= \sum \vb*{p} \vdot \vb*{v}
  + \sum \vb*F \vdot \vb*{r}.
\end{split}
$$

注意总动能 $T = \sum \frac12 m v^2 = \frac12 \sum \vb*{p} \vdot \vb*{v}$。因此时间平均后，

$$
\overline{T} = -\frac{1}{2} \overline{\sum \vb*F \vdot \vb*r},
$$

其中 RHS 称作 the virial of the system。

若 $\vb*F$ 保守，且势能 $U$ 与 $\vb*r$ 关系为幂律，则 $\vb*F \vdot \vb* r = \vb*r \vdot \pdv{U}{\vb*r} \propto U$。平方反比时，比例系数正是一，从而

$$
\overline{T} = - \frac{1}{2} \overline{U}.
$$

#### Application

星系组成的星系团（cluster）可看作这种系统。

至少数量级上，$\overline{T} \approx \frac12 M \overline{v^2}$，$\overline{U} \approx -G M^2 / r$，其中 $M$ 为星系团总质量，$r$ 为尺寸——由 virial 定理可确定 $M, r, \overline{v^2}$ 关系。

观测可知 $\overline{v^2}, r$，得 $M$。对于后发座星系团（Coma cluster），结果是 $10^{15} M_\text{sun}$。然而观测到的星系总质量只有 $10^{13} M_\text{sun}$，加上 IGM（intergalactic medium）则是 $10^{14} M_\text{sun}$，怎么算都不够。因此一定存在大量暗物质，不然星系团将崩解。

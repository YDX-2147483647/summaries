---
relevant:
  - ./digital-signal-processing-advanced.md
  - ./stochastic-signal-processing.md
  - ./physics-2.md
---

# 非平稳信号处理

## §2 典型的时频分析

### 短时Fourier变换面面观

> :material-clock-edit-outline: 2024年11月28日。

- 以加窗单频信号为基。
- 先乘窗，再以单频信号为基（Fourier变换）。
- 先解调指定频率，然后低通滤波。
- 先带通滤波选出指定频率，然后解调以平衡相位。
- 在时频平面上划分栅格。

其实这些理解大多比较片面，有些并非是理解变换整体，而是理解变换结果里的一点。

### Wigner–Ville分布

> :material-clock-edit-outline: 2024年11月28日。

波函数 $ψ$ 不可观测；density matrix $ρ$ 可观测，并且包含了所有可观测的信息。$ψ$ 只能描述纯态，$ρ$ 也能描述混态。

对于纯态，$ψ$ 到 $ρ$ 大致是二次函数，$ρ$ 相当于 $ψ$ 的瞬“时”自相关（对于位置表象，“时”是空间），即 $ρ = \dyad{ψ}$。对于若干纯态经典叠加成的混态，$ρ$ 是每个纯态的density matrix按概率的线性组合。

注意 $ρ$ 是矩阵，相当于二元函数。$ρ$ 的一点涉及 $ψ$ 在两处的值，因此 $ρ$ 有这两处的中心、差两个自变量（分别对应主对角线和反对角线方向）。将差这个自变量Fourier变换（对于位置表象，变换完是动量），就是Wigner–Ville分布。

:material-eye-arrow-right: [PHYS771 Lecture 9: Quantum](https://www.scottaaronson.com/democritus/lec9.html)

一般的概率分布满足概率和为一，其中“和”是一范数。而对于复函数 $ψ$，“和”是二范数。Wigner–Ville分布可看作相空间内的分布，也可写出Schrödinger方程那样的演化方程；但它的值域只能保证在实数范围内，并不保证非负，因此只叫 quasiprobability distribution。

## §3 Cohen类时频分布

> :material-clock-edit-outline: 2024年11月28日。

$ν ↔ t,\ τ ↔ f$，则瞬时相关 $R_{tτ}$、Wigner–Ville分布 ${R_t}^f$、模糊函数 ${R^ν}_τ$、点谱相关 $R^{νf}$ 是Fourier变换对。

很多各种时频分析工具都可理解为给 ${R^ν}_τ$ 乘窗。例如Choi–Williams分布就是乘 $e^{-j (2\pi ντ)^2 / σ}$。

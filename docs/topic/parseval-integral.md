# 用 DTFT 的 Parseval 关系计算定积分

> :material-clock-edit-outline: 2023年4月9日，2023年4月15日。

> 为简便，$z \coloneqq e^{jw}$。可见 $z^* = 1/z$。

## 问题

徒手计算下式。

$$
\int\limits_0^\pi \frac{\dd{w}}{3.25 - 3 \cos w}.
$$

!!! info "另法"

    留数定理。

## 解

若 $\abs{\alpha}<1$，则

$$
\alpha^n u \leftrightarrow \frac{1}{1 - \alpha /z}.
$$

由 Parseval 定理，

$$
\int_0^\pi \abs{\frac{1}{1-\alpha /z}}^2 \dd{w} = \pi \sum_n \abs{\alpha^n u}^2 = \frac{\pi}{1-\abs{\alpha}^2}.
$$

---

$$
\begin{split}
\abs{\frac{1}{\beta-\alpha /z}}^2
&= \frac{1}{\beta^2 + \alpha^2 - \alpha\beta/z - \alpha\beta z} \\
&= \frac{1}{\beta^2 + \alpha^2 - 2\alpha\beta \cos w}. \\
\end{split}
$$

> 注意 $1$ 变成了 $\beta$。

现在令上式等于题目中的被积函数，即

$$
\begin{cases}
    \alpha^2+\beta^2 &= 3.25. \\
    2\alpha\beta &= 3.
\end{cases}
$$

然后可知

$$
\begin{cases}
    (\alpha+\beta)^2 &= \alpha^2+\beta^2 + 2\alpha\beta = 6.25. \\
    (\alpha-\beta)^2 &= \alpha^2+\beta^2 - 2\alpha\beta = 0.25. \\
\end{cases}
$$

因此

$$
\begin{cases}
    \abs{\alpha+\beta} &= 2.5. \\
    \abs{\alpha-\beta} &= 0.5.
\end{cases}
$$

解得 $(\alpha,\beta) \in \qty{\pm(1.5, 1),\ \pm(1, 1.5)}$。

取哪组解呢？

$$
\abs{\frac{1}{\beta-\alpha /z}}^2 = \frac{1}{\abs{\beta}^2} \abs{\frac{1}{1 - \frac\alpha\beta/z}}^2,
$$

要想 $\qty(1 - \frac\alpha\beta/z)^{-1}$ 的反变换是最开始的形式，必须 $\abs{\alpha/\beta} <1$。那我们取 $\alpha = 1,\  \beta = 1.5$。（注意结果与 $\pm$ 无关）

于是原式等于

$$
\frac{1}{1.5^2} \times \frac{\pi}{1 - \frac{1}{1.5^2}} = \frac{4\pi}{5}.
$$

> 看起来并不用具体解出 $\alpha,\beta$，因为答案等于 $\pi / \abs{\beta^2-\alpha^2}$，而
> 
> $$
> \begin{split}
> (\beta^2-\alpha^2)^2
> &= \qty(\beta^2+\alpha^2)^2 - 4\beta^2\alpha^2 \\
> &= 3.25^2 - 3^2 \\
> &= \frac{13^2 - 12^2}{4^2} \\
> &= \frac{5^2}{4^2}.
> \end{split}
> $$

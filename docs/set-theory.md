# 集合论——开启理性思维的钥匙

## 对称差

> :material-clock-edit-outline: 2022年3月8日。

给全集 $X$ 中任意集合 $A$ 定义一个函数 $f_A: X \to \{0,1\}$：

$$
f_A(x) := \begin{cases}
    1 & x \in A. \\
    0 & x \notin A. \\
\end{cases}
$$

这是个双射：

$$
\forall A \in \mathcal{P}(X),\quad\{ x \in X \mid f_A(x) = 1 \} = A.
$$

根据 $A \oplus B$ 的定义，可以验证

$$
f_{A \oplus B} \equiv f_A + f_B. \pmod{2}
$$

现在，

$$
\begin{split}
    f_{(A \oplus B) \oplus C}
    &\equiv f_{A \oplus B} + f_C \\
    &\equiv \qty(f_A + f_B) + f_C \\
    &= f_A + \qty(f_B + f_C) \\
    &\equiv f_A + f_{B \oplus C} \\
    &\equiv f_{A \oplus (B \oplus C)}.
    \pmod{2}
\end{split}
$$

由于 $f$ 的值域是 $\{0,1\}$，所以等式两边不只同余，而且相等。因此 $(A \oplus B) \oplus C = A \oplus (B \oplus C)$。

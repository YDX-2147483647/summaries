---
relevant:
  - ./linear-algebra.md
  - ./calculus-2.md
---

# 人工智能导论

## Bias vs. Variance

> :material-clock-edit-outline: 2022年4月23日，2023年10月12日。

Mean squared error = variance + bias squared.

$y$ is the true value, and $\hat{y}$ is a random variable or a list of variables.

$$
\begin{split}
\overline{(\hat y - y)^2}
&= \overline{(\hat y)^2 + y^2 - 2 \hat y y} \\
&= \overline{(\hat y)^2} + {y^2} - 2 \overline{\hat y} y \\
&= \overline{(\hat y)^2} - \overline{\hat y}^2
  + \qty(\overline{\hat y}^2 + y^2 - 2 \overline{\hat y} y) \\
&= \overline{(\hat y - \overline{\hat y})^2}
  + \qty(\overline{\hat y} - y)^2. \\
\end{split}
$$

## Dual Formulation

:material-eye-arrow-right: [Lagrange Multiplier and Dual Formulation · SVM (gitbooks.io)](https://ai-master.gitbooks.io/svm/content/lagrange-multiplier-and-dual-formulation.html)

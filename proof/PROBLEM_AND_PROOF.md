# Problem and proof

The question asks whether one fixed program can be bounded over Boolean inputs yet unbounded over the tropical semiring. Naive evaluation uses the previous intensional values at every round. The fixed-point round is measured from the additive identity. [Fan, Koutris and Roy, §4](https://arxiv.org/pdf/2504.08914v1#page=10)

    U(x) :- G(x).
    T(x) :- G(x), U(x).
    T(x) :- G(x), E(x,y), T(y).

In Boolean evaluation, $U=G$ in round one, and the guard in both rules forces $T\subseteq G$. Round two fills $T=G$ using the second rule. The two intensional predicates then remain fixed on every input.

For tropical evaluation use the directed path $0,\ldots,n$. Its edges have weight zero, and $G(i)$ has weight $w_i=3^{n-i}$. Every finite derivation of $T(i)$ follows a segment to $j\ge i$ and stops using the second rule. Its weight is $\sum_{k=i}^{j-1}w_k+2w_j$. The two guard occurrences at the stop are on separate branches. This tree has height $j-i+2$. Moving the stop from $j$ to $j+1$ lowers the cost by $w_{j+1}>0$. Therefore the final value at 0 first appears in round $n+2$.

The companion program in the paper has a target whose Boolean value copies one extensional fact. A tropical threshold retains connectivity information, giving square-logarithmic circuit depth by the classical monotone connectivity theorem. The positive-length upper bound uses one actual edge followed by min-plus path doubling. [Full paper](../paper/manuscript.pdf)

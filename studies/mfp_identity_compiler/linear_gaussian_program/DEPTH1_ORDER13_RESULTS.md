# One-hidden-layer identity activation: exact results

## Verdict

The depth-one identity network passes every test through order thirteen
strictly.  More strongly, it has an explicit all-order Stieltjes representing
measure, so every ordinary and shifted Hankel matrix is positive definite at
every finite size.

## Derivatives through order thirteen

\[
(F_1^{(r)}(0))_{r=0}^{13}
=(0,2,0,8,0,32,0,128,0,512,0,2048,0,8192).
\]

In fact,

\[
F_1(t)=\sinh(2t),
\qquad
F_1^{(2k)}(0)=0,
\qquad
F_1^{(2k+1)}(0)=2^{2k+1}.
\]

## Moments

With

\[
K_1(y)=F_1'\!\left(F_1^{-1}(y)\right)=2\sqrt{1+y^2},
\]

the first six moments are

| moment | exact value |
|---|---:|
| \(\mu_0\) | \(1\) |
| \(\mu_1\) | \(1/4\) |
| \(\mu_2\) | \(1/8\) |
| \(\mu_3\) | \(5/64\) |
| \(\mu_4\) | \(7/128\) |
| \(\mu_5\) | \(21/512\) |

The all-order formula is

\[
\boxed{\mu_r=\frac{C_r}{4^r}},
\]

where \(C_r\) is the Catalan number.

## Complete order-thirteen minor audit

All six moment signs are positive.  The thirteen distinct accessible
two-by-two Hankel minors are:

| condition | exact value |
|---|---:|
| \(\mu_0\mu_2-\mu_1^2\) | \(1/16\) |
| \(\mu_0\mu_3-\mu_1\mu_2\) | \(3/64\) |
| \(\mu_0\mu_4-\mu_1\mu_3\) | \(9/256\) |
| \(\mu_0\mu_5-\mu_1\mu_4\) | \(7/256\) |
| \(\mu_0\mu_4-\mu_2^2\) | \(5/128\) |
| \(\mu_0\mu_5-\mu_2\mu_3\) | \(1/32\) |
| \(\mu_1\mu_3-\mu_2^2\) | \(1/256\) |
| \(\mu_1\mu_4-\mu_2\mu_3\) | \(1/256\) |
| \(\mu_1\mu_5-\mu_2\mu_4\) | \(7/2048\) |
| \(\mu_1\mu_5-\mu_3^2\) | \(17/4096\) |
| \(\mu_2\mu_4-\mu_3^2\) | \(3/4096\) |
| \(\mu_2\mu_5-\mu_3\mu_4\) | \(7/8192\) |
| \(\mu_3\mu_5-\mu_4^2\) | \(7/32768\) |

The four distinct accessible three-by-three minors are:

| moment-index matrix | exact determinant |
|---|---:|
| \(\begin{psmallmatrix}0&1&2\\1&2&3\\2&3&4\end{psmallmatrix}=H_2\) | \(1/4096\) |
| \(\begin{psmallmatrix}0&1&2\\1&2&3\\3&4&5\end{psmallmatrix}\) | \(5/16384\) |
| \(\begin{psmallmatrix}0&1&2\\2&3&4\\3&4&5\end{psmallmatrix}\) | \(3/32768\) |
| \(\begin{psmallmatrix}1&2&3\\2&3&4\\3&4&5\end{psmallmatrix}=H_2^+\) | \(1/262144\) |

Therefore all 23 accessible square Hankel minors are strictly positive and

\[
H_0,H_1,H_2,H_0^+,H_1^+,H_2^+\succ0.
\]

## All-order certificate

The moments are represented by

\[
d\nu(x)=\frac2\pi\sqrt{\frac{1-x}{x}}
\mathbf1_{(0,1)}(x)\,dx,
\]

because

\[
\int_0^1x^r\,d\nu(x)=\frac{C_r}{4^r}=\mu_r.
\]

Since this density is positive on an interval,
\(H_d\succ0\) and \(H_d^+\succ0\) for every \(d\ge0\).  This is an
all-order theorem for depth-one identity only, not for the deeper identity
models.


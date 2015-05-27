# EM invariants

To derive the field equations of electromagnetism (EM), we need to find Lorentz
invariants that use the electric (E) and magnetic (B) fields of EM that then
get plugged into the Euler-Lagrange equation.

An invariant is something all observers can agree on.  The Egyptions fiture out
one long ago:

![3 squared plus 4 squared equals 5 squared](../images/EM/EM_invariants/32+42_eq_52.png)

This was the basis for surveying in the flood plains of the Nile. It remains
true today.  The 3D Egyptions know we could also include a third spacial
dimension:

![a squared plut b squared plus c squared equals R
squared](../images/EM/EM_invariants/a2+b2+c2_eq_R2.png)

Einstein showed that Egyptions in rockets could only agree on the inverval
between events.

![d tau squared equals d t squared minus d R squared over the speed of light c
squared](../images/EM/EM_invariants/dtau2_eq_dt2-dR2.png)


Accelerating or spinning is alright for observing events is you can figure out
the right sort of functions to put into the interval.

![d tau squared equals the function f times d t squared minus the function g times d R squared over the speed of light c
squared](../images/EM/EM_invariants/dtau2_eq_f_dt2-g_dR2.png)

Masters of general relativity can figure out the dynamic functions for _f_ and _g_
in only a few special cases because the math remains so difficult. The proposal
described in this site, quaternion gravity, should make this issue tractable
since then one has an algebra problem instead of ten nonliner differential
equations to solve.  For the rest of the discussion of EM, it is assumed f and
g are equal to one since it makes the math simple.

The first term of a quaternion product is a Lorentz invariant scalar. Couple
the current with the potential by multiplying them together:

![J times A equals rho, J times phi, A equals r phi minus J dot A, phi A plus J
phi plus the cross product of J and A](../images/EM/EM_invariants/current_coupling.png)

The electric and magentic fields can be written in terms of differential
operators acting on a potential. Form the product:

![The differential times the potential A equals the time
derivative, Del times phi A equals the time derivative of phi minus the
divergence of A, the time derivative of A plus the gradient of phi plus the
curl of A](../images/EM/EM_invariants/DA.png)

The first term is a gauge term.  EM has gauge symmetry.  Set this to zero in a
way that assures that no matter what gauge we pick - terms involving the time
derivative of phi or divergence of A - the other terms are unchanged.

![One half Del times A minus the conjugate of Del times A equals zero the time
derivative of A plus the gradient of phi plus the curl of
A](../images/EM/EM_invariants/DA_no_scalar.png)

There are two times of 3-vectors.  An axial vector will not change if the the
order of the product is reverse.  A polar vector will flip signs by changing
the order.  That is a property of cross products and curls.  Here are the two
possibilities:

![One half Del times A minus the conjugate of Del times A equals zero the time
derivative of A plus the gradient of phi plus the curl of
A](../images/EM/EM_invariants/DA_no_scalar.png)

![One half A times Del minus the conjugate of A times Del equals zero the time
derivative of A plus the gradient of phi minus the curl of
A](../images/EM/EM_invariants/AD_no_scalar.png)

These should both be as "long" as each other, but will point in a different
direction so long as the magnetic field B is not zero.  Zero is an invariant,
so take the difference of the norms of both of these, and that will always,
necssarily, be equal to zero.

![The norm of minus E plus B equals E squared minus 2 E dot B plus B squared.
The norm of minus E minus B equals E squared plus 2 E dot B plus B squared. The
second norm minus the first is 4 E dot
B](../images/EM/EM_invariants/norms_of_E_B.png)

The dot product of the electric and magnetic field will be used to derive the
homogenous Maxwell equations, the no monopoles and Faraday's law.

The product of the two ways to multiply a differential and a potential also
form an invariant:

![0, minus E plus B times 0, minus E minus B equals B squared minus E squared,
2 E cross B](../images/EM/EM_invariants/B2-E2.png)

This Lorentz invariant quantity will be used when deriving the Maxwell source
equations, Gauss' and Ampere's laws.

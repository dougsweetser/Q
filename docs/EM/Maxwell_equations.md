#  Classical Electrodynamics

Maxwell speculated that someday quaternions would be useful in the analysis of
electromagnetism.  Hopefully after a 130 year wait, in this notebook we can
begin that process.  This approach relies on a judicious use of commutators
and anticommutators.

##  The Maxwell Equations

The Maxwell equations are formed from a combinations of commutators and
anticommutators of the differential operator and the electric and magnetic
fields E and B respectively (for isolated charges in a vacuum.

![even\(\(d by dt, Del\), \(0, B\)\) + odd\(\(d by dt, Del\), \(0, E\)\) = \(-
div B,  Curl E + B dot\) = \(0, 0\)](../images/EM/Maxwell_equations/s_gr_1.gif)

![odd\(\(d by dt, Del\), \(0, B\)\) - even\(\(d by dt, Del\), \(0,E\)\) =
\(div E ,  Curl  B - E dot\) = 4 pi \(rho, J\)](../images/EM/Maxwell_equations/s_gr_2.gif)

![where   even\(A, B\) = \(AB + BA\) , odd\(A, B\) = \(AB -
BA\)](../images/EM/Maxwell_equations/s_gr_3.gif)

The first quaternion equation embodies the homogeneous Maxwell equations.  The
scalar term says that there are no magnetic monopoles.  The vector term is
Faraday's law.  The second quaternion equation is the source term.  The scalar
equation is Gauss' law.  The vector term is Ampere's law, with Maxwell's
correction.

##  The 4-Potential A

The electric and magnetic fields are often viewed as arising from the same
4-potential A.  These can also be expressed easily using quaternions.

![E = vector\(even\(\(d by dt, - Del\),\(phi, - A\)\)\) = \(0, - A dot - Grad
phi\)](../images/EM/Maxwell_equations/s_gr_4.gif)

![B = odd\(\(d by dt, - Del\),\(phi, - A\)\) = \(0,  Curl A
\)](../images/EM/Maxwell_equations/s_gr_5.gif)

The electric field E is the vector part of the anticommutator of the
conjugates of the differential operator and the 4-potential.  The magnetic
field B involves the commutator.

These forms can be directly placed into the Maxwell equations.

![even\(\(d by dt, Del\), odd\(\(d by dt, - Del\), \(phi, - A\)\)\) + odd\(\(d
by dt, Del\), vector\(even\(\(d by dt, - Del\), \(phi, - A\)\)\)\)
=](../images/EM/Maxwell_equations/s_gr_6.gif)

![= \(- div BCurl A ,Curl A dot - Curl A dot - Curl  Grad phi\) = \(- div B, B
dot +  Curl E\) = \(0, 0\)](../images/EM/Maxwell_equations/s_gr_7.gif)

![odd\(\(d by dt, Del\),odd\(\(d by dt, - Del\),\(phi,A\)\)\) - even\(\(d by
dt, Del\), vector\(even\(\(d by dt, - Del\), \(phi, -A\)\)\)\) =
](../images/EM/Maxwell_equations/s_gr_8.gif)

![= \(- Laplacian phi - div A dot,  Curl   Curl A  + A double dot + Grad phi
dot\) = \(Del.E,  Curl  B - E dot\) = 4 pi \(rho,
J\)](../images/EM/Maxwell_equations/s_gr_9.gif)

The homogeneous terms are formed from the sum of both orders of the commutator
and anticommutator.  The source terms arise from the difference of two
commutators and two anticommutators.

##  The Lorentz Force

The Lorentz force is generated similarly to the source term of the Maxwell
equations, but there a small game required to get the signs correct for the
4-force.

![odd\(\(gamma, gamma Beta\),\(0, B\)\) - even\(\(-gamma, gamma Beta\),
\(0,E\)\) = \(gamma Beta dotE, gamma E  + gamma Beta Cross
B\)](../images/EM/Maxwell_equations/s_gr_10.gif)

This is the covariant form of the Lorentz force.  The additional minus sign
required may be a convention handed down through the ages.

##  Conservation Laws

The continuity equation--conservation of charge--is formed by applying the
conjugate of the differential operator to the source terms of the Maxwell
equations.

![scalar\(\(d by dt, - Del\) acting on \(div E,  Curl  B - E dot\)\) =  \(the
time derivative of div E - div E dot + div Curl B, 0\)
=](../images/EM/Maxwell_equations/s_gr_11.gif)

![= scalar\(\(d by dt, - Del\), 4 pi \(rho, J\)\) = 4 pi \(E dot j +d rho by
dt, 0\)](../images/EM/Maxwell_equations/s_gr_12.gif)

The upper is zero, so the dot product of the E field and the current density
plus the rate of change of the charge density must equal zero.  That means
that charge is conserved.

Poynting's theorem for energy conservation is formed in a very similar way,
except that the conjugate of electric field is used instead of the conjugate
of the differential operator.

![scalar\(\(0, -E\)\(div E,  Curl  B - E dot\)\) = \(E dot Curl  B - E dot E
dot, 0\)](../images/EM/Maxwell_equations/s_gr_13.gif)

![= scalar\(\(0, -E\), 4 pi \(rho, J\)\) = 4 pi\(E dot J,
0\)](../images/EM/Maxwell_equations/s_gr_14.gif)

Additional vector identities are required before the final form is reached.

![E dot \(Curl  B\) =  B dot \(Curl E\) + Del dot \(B Cross
E\)](../images/EM/Maxwell_equations/s_gr_15.gif)

![Curl E = - B dot](../images/EM/Maxwell_equations/s_gr_16.gif)

![E dot E dot = 1 over 2 E squared  dot](../images/EM/Maxwell_equations/s_gr_17.gif)

![ B dot B dot = 1 over 2 B squared  dot](../images/EM/Maxwell_equations/s_gr_18.gif)

Use these equations to simplify to the following.

![4 pi\(E dot J, 0\) = \(div\(B Cross E\) - 1 over 2 E squared dot - 1 over 2
B squared dot, 0\)](../images/EM/Maxwell_equations/s_gr_19.gif)

This is Poynting's equation.

##  Implications

The foundations of classical electrodynamics are the Maxwell equations, the
Lorentz force, and the conservation laws.  In this notebook, these basic
elements have been written as quaternion equations, exploiting the actions of
commutators and anticommutators.  There is an interesting link between the E
field and a differential operator for generating conservation laws.  More
importantly, the means to generate these equations using quaternion operators
has been displayed.  This approach looks independent from the usual method
which relies on an antisymmetric 2-rank field tensor and a U(1) connection.


#  The Lorentz Force

The Lorentz force acts on a moving charge.  The covariant form of this law is,
where W is work and P is momentum:

![\(d Work/d tau, d P/d tau\) = gamma e\(Beta dot E, E + Beta Cross
B\)](../images/EM/Lorentz_force/s_gr_1.gif)

In the classical case for a point charge, beta is zero and the E = k e/r^2, so
the Lorentz force simplifies to Coulomb's law.  Rewrite this in terms of the
potentials phi and A.

![\(d W by d tau, d P by d tau\) = gamma e \(Beta dot\(- A dot - Grad phi\), -
A dot - Grad phi + Beta Cross\(Del Cross
A\)\)](../images/EM/Lorentz_force/s_gr_2.gif)

In this notebook, I will look for a quaternion equation that can generate this
covariant form of the Lorentz force in the Lorenz gauge.  By using potentials
and operators, it may be possible to create other laws like the Lorentz force,
in particular, one for gravity.

##  A Quaternion Equation for the Lorentz Force

The Lorentz force is composed of two parts.  First, there is the E and B
fields.  Generate those just as was done for the Maxwell equations

![\(d by dt, Del\) acting on \(phi, A\) = \(phi dot - div A, A dot + Grad phi
+ Curl A\)](../images/EM/Lorentz_force/s_gr_3.gif)

Another component is the 4-velocity

![V = \(gamma, gamma Beta\)](../images/EM/Lorentz_force/s_gr_4.gif)

Multiplying these two terms together creates thirteen terms, only 5 of whom
belong to the Lorentz force.  That should not be surprising since a bit of
algebra was needed to select only the covariant terms that appear in the
Maxwell equations.  After some searching, I found the combination of terms
required to generate the Lorentz force.

![\(d by dt, - Del\) acting on \(phi, - A\)\(gamma, - gamma Beta\) - \(gamma,
- gamma Beta\)\(d by dt, Del\) acting on \(phi, A\)
=](../images/EM/Lorentz_force/s_gr_5.gif)

![](../images/EM/Lorentz_force/s_gr_6.gif)

This combination of differential quaternion operator, quaternion potential and
quaternion 4-velocity generates the covariant form of the Lorentz operator in
the Lorenz gauge, minus a factor of the charge e which operates as a scalar
multiplier.

##  Implications

By writing the covariant form of the Lorentz force as an operator acting on a
potential, it may be possible to create other laws like the Lorentz force.
For point sources in the classical limit, these new laws must have the form of
Coulomb's law, F = k e e'/r^2.  An obvious candidate is Newton's law of
gravity, F = - G m m'/r^2.  This would require a different type of scalar
potential, one that always had the same sign.


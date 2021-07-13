#  Quaternion Analysis

Complex numbers are a subfield of quaternions.  My hypothesis is that complex
analysis should be self-evident within the structure of quaternion analysis.

The challenge is to define the derivative in a non-singular way, so that a
left derivative always equals a right derivative.  If quaternions would only
commute...  Well, the scalar part of a quaternion does commute.  If, in the
limit, the differential element converged to a scalar, then it would commute.
This idea can be defined precisely.  All that is required is that the
magnitude of the vector goes to zero faster than the scalar.  This might
initially appears as an unreasonable constraint.  However, there is an
important application in physics.  Consider a set of quaternions that
represent events in space-time.  If the magnitude of the 3-space vector is less
than the time scalar, events are separated by a timelike interval.  It
requires a speed less than the speed of light to connect the events.  This is
true no matter what coordinate system is chosen.

##  Defining a Quaternion

A quaternion has 4 degrees of freedom, so it needs 4 real-valued variables to
be defined:

![q = \(a0, a1, a2, a3\)](../images/Math/analysis/s_gr_1.gif)

Imagine we want to do a simple binary operation such as subtraction, without
having to specify the coordinate system chosen.  Subtraction will only work if
the coordinate systems are the same, whether it is Cartesian, spherical or
otherwise.  Let e~0~, e~1~, e~2~, and e~3~ be the shared, but unspecified, basis.  Now
we can define the difference between two quaternion q and q' that is
independent of the coordinate system used for the measurement.

![dq = q prime  - q = \(\(a0 prime  - a0\) e0, \(a1 prime  - a1\) e1/3, \(a2
prime  - a2\) e2/3, \(a3 prime  - a3\) e3/3\)](../images/Math/analysis/s_gr_2.gif)

What is unusual about this definition are the factors of a third.  They will
be necessary later in order to define a holonomic equation later in this
section.  Hamilton gave each element parity with the others, a very reasonable
approach.  I have found that it is important to give the scalar and the sum of
the 3-vector parity.  Without this "scale" factor on the 3-vector, change in
the scalar is not given its proper weight.

If dq is squared, the scalar part of the resulting quaternion forms a metric.

![dq squared = \(da0 squared e0 squared + da1 squared e1 squared over 9 + da2
squared e2 squared over 9 + da3 squared e3 squared over 9, 2 da0 da1 e0 e1
over 3, 2 da0 da2 e0 e2 over 3, 2 da0 da3 e0 e3 over 3\)](../images/Math/analysis/s_gr_3.gif)

What should the connection be between the squares of the basis vectors?  The
amount of intrinsic curvature should be equal, so that a transformation
between two basis 3-vectors does not contain a hidden bump.  Should time be
treated exactly like space?  The Schwarzschild metric of general relativity
suggests otherwise.  Let e~1~, e~2~, and e~3~ form an independent, dimensionless,
orthogonal basis for the 3-vector such that:

![- 1 over e1 squared = - 1 over e2 squared = - 1 over e3 squared = e0
squared](../images/Math/analysis/s_gr_4.gif)

This unusual relationship between the basis vectors is consistent with
Hamilton's choice of 1, i, j, k if e~0~^2^ = 1.  For that case, calculate the
square of dq:

![dq squared = \(da0 squared e0 squared - da1 squared over 9 e0 squared - da2
squared over 9 e0 squared - da3 squared over 9 e0 squared, 2 da0 da1 over 3, 2
da0 da2 over 3, 2 da0 da3 over 3\) ](../images/Math/analysis/s_gr_5.gif)

The scalar part is known in physics as the Minkowski interval between two
events in flat space-time.  If e~0~^2^ does not equal one, then the metric would
apply to a non-flat space-time.  A metric that has been measured experimentally
is the Schwarzchild metric of general relativity.  Set e~0~^2^ = (1 - 2 GM/c^2^
R), and calculate the square of dq:

![dq squared = \(da0 squared \(1 - 2 G M over c squared r\) - dA dot dA over 9
\(1 - 2 G M over c squared r\) , 2 da0 da1 over 3, 2 da0 da2 over 3, 2 da0 da3
over 3\) ](../images/Math/analysis/s_gr_6.gif)

This is the Schwarzchild metric of general relativity.  Notice that the
3-vector is unchanged (this may be a defining characteristic).  There are very
few opportunities for freedom in basic mathematical definitions.  I have
chosen this unusual relationships between the squares of the basis vectors to
make a result from physics easy to express.  Physics guides my choices in
mathematical definitions :-)

##  An Automorphic Basis for Quaternion Analysis

A quaternion has 4 degrees of freedom.  To completely specify a quaternion
function, it must also have four degrees of freedom.  Three other linearly-
independent variables involving q can be defined using conjugates combined
with rotations:

![q conjugated = \(a0 e0, - a1 e1 over 3, - a2 e2 over 3, - a3 e3 over
3\)](../images/Math/analysis/s_gr_7.gif)

![q conjugated first is defined to be \(- a0 e0,  a1 e1 over 3, - a2 e2 over
3, - a3 e3 over 3\) = \(e1 q e1\) conjugated](../images/Math/analysis/s_gr_8.gif)

![q conjugated second is defined to be \(- a0 e0, - a1 e1 over 3,  a2 e2 over
3, - a3 e3 over 3\) = \(e2 q e2\) conjugated](../images/Math/analysis/s_gr_9.gif)

The conjugate as it is usually defined (q^*^) flips the sign of all but the
scalar.  The q^*1^ flips the signs of all but the e~1~ term, and q^*2^ all but the
e~2~ term.  The set q, q^*^, q^*1^, q^*2^ form the basis for quaternion analysis.  The
conjugate of a conjugate should give back the original quaternion.

![\(q conj\) conj = q, \(q conjugated first\) conjugated first = q, \(q
conjugated second\) conjugated second = q](../images/Math/analysis/s_gr_10.gif)

Something subtle but perhaps directly related to spin happens looking at how
the conjugates effect products:

![\(q times q prime\) conjugated first = q prime  conjugated first times q
conjugated first](../images/Math/analysis/s_gr_11.gif)

![\(q times q prime\) conjugated first = - q prime  conjugated first times q
conjugated first, \(q times q prime\) conjugated second = - q prime conjugated
second times q conjugated second](../images/Math/analysis/s_gr_12.gif)

![\(q times q prime times q times q prime\) conjugated first = q prime
conjugated first times q conjugated first times q prime conjugated first times
q conjugated first](../images/Math/analysis/s_gr_13.gif)

The conjugate applied to a product brings the result directly back to the
reverse order of the elements.  The first and second conjugates point things
in exactly the opposite way.  The property of going "half way around" is
reminiscent of spin.  A tighter link will need to be examined.

##  Future Timelike Derivative

Instead of the standard approach to quaternion analysis which focuses on left
versus right derivatives, I concentrate on the ratio of scalars to 3-vectors.
This is natural when thinking about the structure of Minkowski space-time,
where the ratio of the change in time to the change in 3-space defines five
separate regions: timelike past, timelike future, lightlike past, lightlike
future, and spacelike.  There are no continuous Lorentz transformations to
link these regions.  Each region will require a separate definition of the
derivative, and they will each have distinct properties.  I will start with
the simplest case, and look at a series of examples in detail.

Definition: The future timelike derivative:

Consider a covariant quaternion function f with a domain of H and a range of
H.  For a future timelike derivative to be defined, the 3-vector must approach
zero faster than the positive scalar.  If this is not the case, then this
definition cannot be used.  Implementing these requirements involves two limit
processes applied sequentially to a differential quaternion D.  First the
limit of the three vector is taken as it goes to zero, (D - D^*^)/2 -&gt; 0.
Second, the limit of the scalar is taken, (D + D^*^)/2 -&gt; +0 (the plus zero
indicates that it must be approached with a time greater than zero, in other
words, from the future).  The net effect of these two limit processes is that
D-&gt;0\.

![d f\(q, q conjugated, q conjugated first, q conjugated second\) over d q
=](../images/Math/analysis/s_gr_14.gif)

![= the limit as the scalar d approaches zero from the positive direction of
\(the limit as \(d, D\) approaches the scalar \(d, 0\) of \(f\(q + \(d, D\), q
conjugated, q conjugated first, q conjugated second\) - f\(q, q conjugated, q conjugated first, q conjugated second\) times \(d, D\) inverted\)\)](../images/Math/analysis/s_gr_15.gif)

The definition is invariant under a passive transformation of the basis.

The 4 real variables a0, a1, a2, a3 can be represented by functions using the
conjugates as a basis.

![f\(q, q conjugated, q conjugated first, q conjugated second\) = a0 = e0 \(q
+ q conjugated\) over 2](../images/Math/analysis/s_gr_16.gif)

![f = a1 = e1 \(q + q conj 1\) over \(-2 over 3\) = \(q + q conjugated first\)
e1 over \(-2 over 3\)](../images/Math/analysis/s_gr_17.gif)

![f = a2 = e2 \(q + q conjugated second\) over \(-2 over 3\) = \(q + q
conjugated second\) e2 over \(-2 over 3\)](../images/Math/analysis/s_gr_18.gif)

![f = a3 = e3 times \(q + q conjugated + q conjugated first + the second
conjugated of q\) over \(2 over 3\) = \(q + q conjugated + q conjugated first
+ the second conjugated of q\) times e3 over \(2 over 3\)](../images/Math/analysis/s_gr_19.gif)

Begin with a simple example:

![f = a0 = \(q + q conjugated\) over 2](../images/Math/analysis/s_gr_20.gif)

![d a0 by d q = da0 by d q conjugated = the limit of \(the limit of\(\(e0\(q +
\(d, D\) + q conjugated\) - \(q + q conjugated\)\) times the inverse of
\(2\(d, D\)\)\)\) = e0 over 2](../images/Math/analysis/s_gr_21.gif)

![ d a0 by d q conjugated first = da0 by d q conjugated second =  0
](../images/Math/analysis/s_gr_22.gif)

The definition gives the expected result.

A simple approach to a trickier example:

![f = a1 = e1 \(q + q conjugated first\) over \(- 2 over 3\)
](../images/Math/analysis/s_gr_23.gif)

![d a1 by d q = d a1 by d q conjugated = the limit of \(the limit of\(e1 times
\(\(q + \(d, D\) + q conjugated first\) - \(q + q conjugated first\)\) times
the inverse of \(-2 over 3 \(d, D\)\)\)\) = - 3 e1 over 2](../images/Math/analysis/s_gr_24.gif)

![d a1 over d q conjugated  = d a1 over d q conjugated second =
0](../images/Math/analysis/s_gr_25.gif)

So far, the fancy double limit process has been irrelevant for these identity
functions, because the differential element has been eliminated.  That changes
with the following example, a tricky approach to the same result.

![f = a1 = \(q + q conjugated first\) times e1 over \(-2 over 3\)
](../images/Math/analysis/s_gr_26.gif)

![d a1 by d q  =  d a1 by d q conjugated first =](../images/Math/analysis/s_gr_27.gif)

![= the  limit of\(the limit of\(\(\(q + \(d, D\) + q conjugated first\) - \(q
+ q conjugated first\)\) times e1 \(-2 over 3 \(d, D\)\) inverted\)\)
=](../images/Math/analysis/s_gr_28.gif)

![= the limit of\(the limit of\(\(d, D\) times e1 \(-2 over 3 \(d, D\)\)
inverted\)\) =](../images/Math/analysis/s_gr_29.gif)

![= the limit of \(\(d, 0\) times e1 times \(-2 over 3 \(d, 0\)\) inverted\) =
- 3 over 2 e1](../images/Math/analysis/s_gr_30.gif)

Because the 3-vector goes to zero faster than the scalar for the differential
element, after the first limit process, the remaining differential is a scalar
so it commutes with any quaternion.  This is what is required to dance around
the e~1~ and lead to the cancellation.

The initial hypothesis was that complex analysis should be a self-evident
subset of quaternion analysis.  So this quaternion derivative should match up
with the complex case, which is:

![z = a + b i, y = \(Z - Z conjugated\) over 2 i](../images/Math/analysis/s_gr_31.gif)

![d b by d z = - i over 2 = - d b by d Z
conjugated](../images/Math/analysis/s_gr_32.gif)

These are the same result up to two subedits.  Quaternions have three
imaginary axes, which creates the factor of three.  The conjugate of a complex
number is really doing the work of the first quaternion conjugate q^*1^ (which
equals -z^*^), because z^*^ flips the sign of the first 3-vector component, but no
others.

The derivative of a quaternion applies equally well to polynomials.

![let f = q squared](../images/Math/analysis/s_gr_33.gif)

![d f by d q = the limit of\(the limit of \(\(\(q + \(d, D\)\) squared - q
squared\) times \(d, D\) inverted\)\) =](../images/Math/analysis/s_gr_34.gif)

![= the limit of \(the limit of \(\(q squared + q times \(d, D\) + \(d, D\)
times q + \(d, D\) squared - q squared\) times \(d, D\) inverted\)\)
=](../images/Math/analysis/s_gr_35.gif)

![= the limit of \(the limit of \(\(q + \(d, D\) times q times \(d, D\)
inverted + \(d, D\)\)\) =](../images/Math/analysis/s_gr_36.gif)

![= the limit of \(2 q + \(d, 0\)\) = 2 q](../images/Math/analysis/s_gr_37.gif)

This is the expected result for this polynomial.  It would be straightforward
to show that all polynomials gave the expected results.

Mathematicians might be concerned by this result, because if the 3-vector D
goes to -D nothing will change about the quaternion derivative.  This is
actually consistent with principles of special relativity.  For timelike
separated events, right and left depend on the inertial reference frame, so a
timelike derivative should not depend on the direction of the 3-vector.

##  Analytic Functions

There are 4 types of quaternion derivatives and 4 component functions.  The
following table describes the 16 derivatives for this set

![Reading each derivative for the 4 components a0, a1, a2, a3 in a row, the
derivatives with respect to q are e~0~/2, - 3 e~1~/2, - 3 e~2~/3, 3 e~3~/3; the
derivatives with respect to q conj are e~0~/2, 0, 0, 3 e~3~/3;the derivatives with
respect to q conj1 are 0, - 3 e~1~/2, 0, 3 e~3~/3;the derivatives with respect to
q conj2 are 0, 0, - 3 e~2~/2, 3 e~3~/3;](../images/Math/analysis/s_gr_38.gif)

This table will be used extensively to evaluate if a function is analytic
using the chain rule.  Let's see if the identity function w = q is analytic.

![Let w = q = \(a0 e0,  a1 e~1~ over 3, a2 e2 over 3, a3 e3 over
3\)](../images/Math/analysis/s_gr_39.gif)

Use the chain rule to calculate the derivative will respect to each term:

![d w by d a0 times d a0 by d q = e0 e0 over 2 = 1
half](../images/Math/analysis/s_gr_40.gif)

![d w by d a1 time d a1 by d q = e1 over 3 times e1 over \(-2 over 3\) = 1
half](../images/Math/analysis/s_gr_41.gif)

![d w by d a2 times d a2 by d q = e2 over 3 times e2 over \(-2 over 3\) = 1
half](../images/Math/analysis/s_gr_42.gif)

![d w by d a3 times d a3 by d q = e3 over 3 times d e3 over \(2 over 3\) = - 1
half](../images/Math/analysis/s_gr_43.gif)

Use combinations of these terms to calculate the four quaternion derivatives
using the chain rule.

![d w by d q = d w by d a0 times d a0 by d q + d w  by d a1 times d a1 by d q
+ d w by d a2 times d a2 by d q + d w by d a3 times d a3 by d q = 1 half + 1
half + 1 half - 1 half = 1](../images/Math/analysis/s_gr_44.gif)

![d w by d q conj   =d w by d a0 times d a0 by d q conj +d w by d a3 times d
a3 by d q conj = 1 half - 1 half = 0](../images/Math/analysis/s_gr_45.gif)

![d w by d q conjugated first = d w by d a1 times d a1 by d q conjugated first
+ d w by d a3 times d a3 by d q conjugated first = 1 half - 1 half =
0](../images/Math/analysis/s_gr_46.gif)

![d w by d q conjugated second = d w by d a2 times d a2 by d q conjugated
second + d w by d a3 times d a3 by d q conjugated second = 1 half - 1 half =
0](../images/Math/analysis/s_gr_47.gif)

This has the derivatives expected if w=q is analytic in q.

Another test involves the Cauchy-Riemann equations.  The presence of the three
basis vectors changes things slightly.

![Let u = \(a0 e0, 0, 0, 0\) , V = \(0, a1 e1 over 3, a2 e2 over 3, a3 e3 over
3\) ](../images/Math/analysis/s_gr_48.gif)

![d u by d a0 times e1 over 3 = d V by d a1 e0, d u by d a0 times e2 over 3 =
d V by d a2 times e0, d u by d a0 times e3 over 3 = d V by d a3 times
e0](../images/Math/analysis/s_gr_49.gif)

This also solves a holonomic equation.

![the scalar part of \(d u by d a0, d V by d a1, d V by d a2, d V by d a3\)
times \(e0, e1, e2, e3\)\) = e0 times e0 + e1 times e1 over 3 + e2 times e2
over 3 + e3 times e3 over 3 = 0 ](../images/Math/analysis/s_gr_50.gif)

There are no off diagonal terms to compare.

This exercise can be repeated for the other identity functions.  One
noticeable change is that the role that the conjugate must play.  Consider the
identity function w = q^*1^.  To show that this is analytic in q^*1^ requires that
one always works with basis vectors of the q^*1^ variety.

![Let u = \(- a0 e0, 0, 0, 0\), V = \(0, a1 e1 over 3, - a2 e2 over 3, - a3 e3
over 3\)](../images/Math/analysis/s_gr_51.gif)

![d u by d a0 times \(-e1 over 3 \)= d V by d a1 times e0, d u by d a0 times
e2 over 3 = d V by d a2  times e0, d u by d a0 times e3 over 3 = d V by d a3
times e0](../images/Math/analysis/s_gr_52.gif)

This also solves a first conjugate holonomic equation.

![\(d u by d a0 + d V by d a1 + d V by d a2 + dV by d a3\) dot \(e0 + e1 + e2
+ e3\) = e0  e0  + e1 over 3 times e1 + e2 over 3 time e2 + e3 over 3 times e3
= 0](../images/Math/analysis/s_gr_53.gif)

Power functions can be analyzed in exactly the same way:

![Let w = q squared  = \(a0 squared times e0 squared + a1 squared times e1
squared over 9 + a2 squared times e2 squared over 9 + a3 squared times e3
squared over 9, 2 a0 a1 e0 e1 over 3, 2 a0 a2 e0 e2 over 3, 2 a0 a3 e0 e3 over 3\) ](../images/Math/analysis/s_gr_54.gif)

![u = \(a0 squared e0 squared + a1 squared e1 squared over 9 + a2 squared e2
squared over 9 + a3 squared e3 squared over 9, 0, 0,
0\)](../images/Math/analysis/s_gr_55.gif)

![V = \(0, 2 a0 a1 e0 e1 over 3, 2 a0 a2 e0 e2 over 3, 2 a0 a3 e0 e3 over
3\)](../images/Math/analysis/s_gr_56.gif)

![d u by d a0 e1 over 3 = 2 a0 e0 squared e1 over 3 = d  V by d a1
e0](../images/Math/analysis/s_gr_57.gif)

![d u by d a0 e2 over 3 = 2 a0 e0 squared e2 over 3 = d  V by d a2
e0](../images/Math/analysis/s_gr_58.gif)

![d u by d a0 e3 over 3 = 2 a0 e0  e3 squared over 3 = d  V by d a3
e0](../images/Math/analysis/s_gr_59.gif)

This time there are cross terms involved.

![- d u by d a1 3 times e0 = - 2 a1 e0 e1 squared over 9 = d V1 by d a0 e1
over 3](../images/Math/analysis/s_gr_60.gif)

![- d u by d a2 3 e0 = - 2 a2 e0 e2 squared over 9 = d V2 by d a0 e2 over
3](../images/Math/analysis/s_gr_61.gif)

![d u by d a3 e0 = - 2 a3 e0 e3 squared over 9 = - d V3 by d a0 e3 over
3](../images/Math/analysis/s_gr_62.gif)

At first glance, one might think these are incorrect, since the signs of the
derivatives are suppose to be opposite.  Actually they are, but it is hidden
in an accounting trick :-)  For example, the derivative of u with respect to
a1 has a factor of e~1~^2^, which makes it negative.  The derivative of the first
component of V with respect to a0 is positive.  Keeping all the information
about signs in the e's makes things look non-standard, but they are not.  

Note that these are three scalar equalities.  The other Cauchy-Riemann
equations evaluate to a single 3-vector equation.  This represents four
constraints on the four degrees of freedom found in quaternions to find out if
a function happens to be analytic.

This also solves a holonomic equation.

![\(d u by d a0 + d V over a1 + d V by d a2 +d V by d a3 \) dot \(e0 +e1 + e2
+ e3\) =](../images/Math/analysis/s_gr_63.gif)

![= 2 a0 e0 cubed  + 2 a0 e1 over 3 e1 + 2 a0 e2 over 3 e2 + 2 a0 e3 over 3 e3
= 0](../images/Math/analysis/s_gr_64.gif)

Since power series can be analytic, this should open the door to all forms of
analysis.  (I have done the case for the cube of q, and it too is analytic in
q).

##  4 Other Derivatives

So far, this work has only involved future timelike derivatives.  There are
five other regions of space-time to cover.  The simplest next case is for past
timelike derivatives.  The only change is in the limit, where the scalar
approaches zero from below.  This will make many derivatives look time
symmetric, which is the case for most laws of physics.

A more complicated case involves spacelike derivatives.  In the spacelike
region, changes in time go to zero faster than the absolute value of the
3-vector.  Therefore the order of the limit processes is reversed.  This time
the scalar approaches zero, then the 3-vector.  This creates a problem,
because after the first limit process, the differential element is (0, D),
which will not commute with most quaternions.  That will lead to the
differential element not cancelling.  The way around this is to take its norm,
which is a scalar.

A spacelike differential element is defined by taking the ratio of a
differential quaternion element D to its 3-vector, D - D^*^.  Let the norm of
D approach zero.  To be defined, the three vector must approach zero faster
than its corresponding scalar.  To make the definition non-singular
everywhere, multiply by the conjugate.  In the limit D D^*^/((D - D^*^)(D - D^*^))*
approaches (1, 0), a scalar.

![the norm of the partial derivative of f with respect to q =](../images/Math/analysis/s_gr_65.gif)

![= the limit as the 3-vector \(0, D\) goes to 0 of \(the limit as the
quaternion differential element \(d, D\) goes to the 3-vector \(0, D\) of
\(f\(q + \(d, D\), q conjugated, q conjugated first, q conjugated second\) - f\(q, q conjugated, q conjugated first, q conjugated second\) times \(d, D\) inverted\)\) times the preceding difference conjugated\)\)](../images/Math/analysis/s_gr_66.gif)

To make this concrete, consider a simple example, f = q^2.  Apply the
definition:

![the norm of d q squared by d q = the limit as \(0, D\) goes to 0 of \(the
limit as \(d, D\) goes to \(0, D\)](../images/Math/analysis/s_gr_67.gif)

![\(\(\(\(a, B\) + \(d, D\)\) squared - \(a, B\) squared\) times \(d, D\)
inverted times the conjugate of the preceding difference
=](../images/Math/analysis/s_gr_68.gif)

![= the limit of \(\(\(a, B\) + \(0, D\) times \(a, B\) times \(0, D\)
conjugated over the norm of \(0, D\) + \(0, D\)\) times the preceding sum
conjugated\) =](../images/Math/analysis/s_gr_69.gif)

The second and fifth terms are unitary rotations of the 3-vector B.  Since the
differential element D could be pointed anywhere, this is an arbitrary
rotation. Define:

![\(a, B prime\) = \(0, D\) times \(a, B\) times \(0, -D\) over the norm of
\(0, D\)](../images/Math/analysis/s_gr_70.gif)

Substitute, and continue:

![= the limit of \(\(\(a, B\) + \(a, B prime\) + \(0, D\)\) times \(\(a, B\) +
\(a, B prime\) + \(0, D\)\) conjugated\) =](../images/Math/analysis/s_gr_71.gif)

![= the limit of \(4 times a squared + 2 B squared + 2 B dot B prime + 2 D dot
B + 2 D dot B prime, 0\)](../images/Math/analysis/s_gr_72.gif)

![= \(4 a squared + 2 B squared + 2 B dot B prime, 0\) is less than 2 q
absolute value squared](../images/Math/analysis/s_gr_73.gif)

Look at how wonderfully strange this is!  The arbitrary rotation of the
3-vector B means that this derivative is bound by an inequality.  If D is in
direction of B, then it will be an equality, but D could also be in the
opposite direction, leading to a destruction of a contribution from the
3-vector.  The spacelike derivative can therefore interfere with itself.  This
is quite a natural thing to do in quantum mechanics.  The spacelike derivative
is positive definite, and could be used to define a Banach space.

Defining the lightlike derivative, where the change in time is equal to the
change in space, will require more study.  It may turn out that this
derivative is singular everywhere, but it will require some skill to find a
technically viable compromise between the spacelike and timelike derivative to
synthesis the lightlike derivative.


#  Unifying the Representation of Spin and Angular Momentum

I will show how to represent both integral and half-integral spin within the
same quaternion algebraic field.  This involves using quaternion
automorphisms.  First a sketch of why this might work will be provided.
Second, small rotations in a plane around two axes will be used to show how
the resulting vector points in an opposite way, depending on which involution
is used to construct the infinitesimal rotation.  Finally, a general identity
will be used to look at what happens under exchange of two quaternions in a
commutator.

##  Automorphism, Rotations, and Commutators

Quaternions are formed from the direct product of a scalar and a 3-vector.
Rotational operators that act on each of the 3 components of the 3-vector act
like integral angular momentum.  I will show that a rotation operator that
acts differently on two of the three components of the 3-vector acts like
half-integral spin.  What happens with the scalar is irrelevant to this
dimensional counting.  The same rotation matrix acting on the same quaternion
behaves differently depending directly on what involutions are involved.

Quaternions have 4 degrees of freedom.  If we want to represent quaternions
with automorphisms, 4 are required:  They are the identity automorphism, the
conjugate anti-automorphism, the first conjugate anti-automorphism, and the
second conjugate anti-automorphism:

![The identity automorphism I maps q into
q](../img/QM/spin_and_angular_momentum/s_gr_1.gif)

![The conjugate anti-automorphism * maps q into
q*](../img/QM/spin_and_angular_momentum/s_gr_2.gif)

![The first conjugate anti-automorphism *1 maps q into
q*1](../img/QM/spin_and_angular_momentum/s_gr_3.gif)

![The second conjugate anti-automorphism *2 maps q into
q*2](../img/QM/spin_and_angular_momentum/s_gr_4.gif)

where

![q*1 is defined to be \(e1 q
e1\)*](../img/QM/spin_and_angular_momentum/s_gr_5.gif)

![q*2 === \(e2 q e2\)*](../img/QM/spin_and_angular_momentum/s_gr_6.gif)

e1, e2, e3 are orthogonal basis vectors

The most important automorphism is the identity.  Life is stable around small
permutations of the identity:-) The conjugate flips the signs of the each
component in the 3-vector.  These two automorphisms, the identity and the
conjugate, treat the 3-vector as a unit.  The first and second conjugate flip
the signs of all terms but the first and second terms, respectively.
Therefore these operators act on only the two of the three components in the
3-vector.  By acting on only two of three components, a commutator will behave
differently.  This small difference in behavior inside a commutator is what
creates the ability to represent integral and half-integral spins.

##  Small Rotations

Small rotations about the origin will now be calculated.  These will then be
expressed in terms of the four automorphisms discussed above.

I will be following the approach used in J. J. Sakurai's book "Modern Quantum
Mechanics", chapter 3, making modifications necessary to accommodate
quaternions.  First, consider rotations about the origin in the z axis.
Define:

![Rotation around e3 at zero by theta is defined to be \(cosine theta e0, 0,
0, sine theta e3 over 3\)](../img/QM/spin_and_angular_momentum/s_gr_7.gif)

![if q = \(0, a1 e1/3, a2 e2/3,
0\)](../img/QM/spin_and_angular_momentum/s_gr_8.gif)

![Rotation around e3 acting on q = q prime= \(0, \(a1 cosine theta-a2 sine
theta\) e0 e1 over 3, \(a2 cosine theta+a1 sine theta\) e0 e2 over 3,
0\)](../img/QM/spin_and_angular_momentum/s_gr_9.gif)

Two technical points.  First, Sakurai considered rotations around any point
along the z axis.  This analysis is confined to the z axis at the origin, a
significant but not unreasonable constraint.  Second, these rotations are
written with generalized coordinates instead of the very familiar and
comfortable x, y, z.  This extra effort will be useful when considering how
rotations are effected by curved spacetime.  This machinery is also necessary
to do quaternion analysis (please see that section, it's great :-)

There are similar rotations around the first and second axes at the origin;

![Rotation around e1 at zero by theta = \(cosine theta e0, sine theta e1 over
3, 0, 0\)](../img/QM/spin_and_angular_momentum/s_gr_10.gif)

![Rotation around e2 at zero by theta = \(cosine theta e0, 0, sine theta e2
over 3, 0\)](../img/QM/spin_and_angular_momentum/s_gr_11.gif)

Consider an infinitesimal rotation for these three rotation operators.  To
second order in theta,

![sine theta = theta + errors of the order of theta cubed, cosine theta = 1 -
theta squared over 2 + errors of the order of theta
cubed](../img/QM/spin_and_angular_momentum/s_gr_12.gif)

![Rotation around e1 at zero by theta much less than 1 = \(\(1 - theta squared
over 2\) e0, theta e1 over 3, 0, 0\) + errors of the order of theta
cubed](../img/QM/spin_and_angular_momentum/s_gr_13.gif)

![Rotation around e12at zero by theta much less than 1 = \(\(1 - theta squared
over 2\) e0, 0, theta e2 over 3, 0\) + errors of the order of theta
cubed](../img/QM/spin_and_angular_momentum/s_gr_14.gif)

![Rotation around e3 at zero by theta much less than  1 = \(\(1 - theta
squared over 2\) e0, 0, 0, theta e3 over 3\) + errors of the order of theta
cubed](../img/QM/spin_and_angular_momentum/s_gr_15.gif)

Calculate the commutator of the first two infinitesimal rotation operators to
second order in theta:

![The commutator of a rotation around e1, rotation around e2 = \(\(1 - theta
squared over 2\) e0, theta e1 over 3, 0, 0\) times \(\(1 - theta squared over
2\) e0, 0, theta e2 over 3, 0\)
-](../img/QM/spin_and_angular_momentum/s_gr_16.gif)

![- \(\(1 - theta squared over 2\) e0, 0, theta e2 over 3, 0\) times \(\(1 -
theta squared over 2\) e0,theta e1 over 3, 0, 0\)
=](../img/QM/spin_and_angular_momentum/s_gr_17.gif)

![= \(\(1 - theta squared\) e0 squared, theta e0 e1 over 3, theta e0 e2 over
3, theta squared e1 e2 over 9\) - \(\(1 - theta squared\) e0 squared, theta e0
e1 over 3, theta e0 e2 over 3, - theta squared e1 e2 over 9\)
](../img/QM/spin_and_angular_momentum/s_gr_18.gif)

![= 2 \(0, 0, 0, theta squared e1 e2 over 9\) = 2 \(Re3=0 \(theta squared\) -
R\(0\)\)](../img/QM/spin_and_angular_momentum/s_gr_19.gif)

To second order, the commutator of infinitesimal rotations of rotations about
the first two axes equals twice one rotation about the third axis given the
squared angle minus a zero rotation about an arbitrary axis (a fancy way to
say the identity). Now I want to write this result using anti-automorphic
involutions for the small rotation operators.

![The commutator of a rotation around e1 conjugated, a rotation around e2
conjugated = \(\(1-theta squared over 2\) e0, - theta e1 over 3, 0, 0\) times
\(\(1 - theta squared over 2\) e0, 0, - theta e2 over 3, 0\)
-](../img/QM/spin_and_angular_momentum/s_gr_20.gif)

![ - \(\(1 - theta squared over 2\) e0, 0, - theta e2 over 3, 0\) times \(\(1
- theta squared over 2\) e0, - theta e1 over 3, 0, 0\)
=](../img/QM/spin_and_angular_momentum/s_gr_21.gif)

![= \(\(1 - theta squared\) e0 squared, - theta e0 e1 over 3, - theta e0 e2
over 3, theta squared e1 e2 over 9\) - \(\(1 - theta squared\) e0 squared, -
theta e0 e1 over 3, - theta e0 e2 over 3, - theta squared e1 e2 over 9\)
=](../img/QM/spin_and_angular_momentum/s_gr_22.gif)

![= 2 \(0, 0, 0, theta squared e1 e2 over 9\) = 2 \(Re3=0 \(theta squared\) -
R\(0\)\)](../img/QM/spin_and_angular_momentum/s_gr_23.gif)

Nothing has changed.  Repeat this exercise one last time for the first
conjugate:

![The commutator of a rotation around e1 first conjugated, a rotation around
e2 first conjugated = \(-\(1 - theta squared over 2\) e0, theta e1 over 3, 0,
0\) times \(-\(1 - theta squared over 2\) e0, 0, - theta e2 over 3, 0\)
-](../img/QM/spin_and_angular_momentum/s_gr_24.gif)

![- \(-\(1 - theta squared over 2\) e0, 0, - theta e2 over 3, 0\) times \(-\(1
- theta squared over 2\) e0, theta e1 over 3, 0, 0\)
=](../img/QM/spin_and_angular_momentum/s_gr_25.gif)

![= \(\(1 - theta squared\) e0 squared, - theta e0 e1 over 3, - theta e0 e2
over 3, theta squared e1 e2 over 9\) - \(\(1 - theta squared\) e0 squared, -
theta e1 over 3, - theta e2 over 3, - theta squared e1 e2 over 9\)
=](../img/QM/spin_and_angular_momentum/s_gr_26.gif)

![= 2 \(0, 0, 0, theta squared e1 e2 over 9\) = 2 \(Re3=0 \(theta squared\) -
R\(0\)\)](../img/QM/spin_and_angular_momentum/s_gr_27.gif)

This points exactly the opposite way,even for an infinitesimal angle!

This is the kernel required to form a unified representation of integral and
half integral spin. Imagine adding up a series of these small rotations, say 2
pi of these.  No doubt the identity and conjugates will bring you back exactly
where you started.  The first and second conjugates in the commutator will
point in the opposite direction.  To get back on course will require another 2
pi, because the minus of a minus will generate a plus.

##  Automorphic Commutator Identities

This is a very specific example.  Is there a general identity behind this
work?  Here it is:

![The commutator of q, q prime = the commutator of q conjugate, q prime
conjugated = the first conjugate of the commutator of q first conjugated, q
prime first conjugated = the second conjugate of the commutator of q second
conjugated, q prime second
conjugated](../img/QM/spin_and_angular_momentum/s_gr_28.gif)

It is usually a good sign if a proposal gets more subtle by generalization :-)
In this case, the negative sign seen on the z axis for the first conjugate
commutator is due to the action of an additional first conjugate.  For the
first conjugate, the first term will have the correct sign after a 2 pi
journey, but the scalar, third and forth terms will point the opposite way.  A
similar, but not identical story applies for the second conjugate.

With the identity, we can see exactly what happens if q changes places with q'
with a commutator.  Notice, I stopped right at the commutator (not including
any additional conjugator).  In that case:

![The commutator of q conjugate, q prime = - the commutator of q prime, q =
the commutator of q conjugated, q prime conjugated = - the commutator of q
prime conjugated, q conjugated =](../img/QM/spin_and_angular_momentum/s_gr_29.gif)

![= \(0, a2 a3 e2 e3 over 9 + a3 a2 e3 e2 over 9, a3 a1 e3 e1 over 9 + a1 a3
e1 e3 over 9, a1 a2 e1 e2 over 9 + a2 a1 e2 e1 over
9\)](../img/QM/spin_and_angular_momentum/s_gr_30.gif)

![The commutator of q first conjugated, q prime first conjugated = - the
commutator of q prime first conjugated, q first conjugated
=](../img/QM/spin_and_angular_momentum/s_gr_31.gif)

![= \(0, a2 a3 e2 e3 over 9 + a3 a2 e3 e2 over 9, - a3 a1 e3 e1 over 9 - a1 a3
e1 e3 over 9, - a1 a2 e1 e2 over 9 - a2 a1 e2 e1 over
9\)](../img/QM/spin_and_angular_momentum/s_gr_32.gif)

![The commutator of q first conjugated, q prime first conjugated = - the
commutator of q prime first conjugated, q first conjugated
=](../img/QM/spin_and_angular_momentum/s_gr_33.gif)

![= \(0, a2 a3 e2 e3 over 9 + a3 a2 e3 e2 over 9, - a3 a1 e3 e1 over 9 - a1 a3
e1 e3 over 9, - a1 a2 e1 e2 over 9 - a2 a1 e2 e1 over
9\)](../img/QM/spin_and_angular_momentum/s_gr_34.gif)

Under an exchange, the identity and conjugate commutators form a distinct
group from the commutators formed with the first and second conjugates.  The
behavior in a commutator under exchange of the identity automorphism and the
anti-automorphic conjugate are identical.  The first and second conjugates are
similar, but not identical.

There are also corresponding identities for the anti-commutator:

![The anti-commutator of q, q prime = the conjugate of the anti-commutator of
q conjugated, q prime conjugated = - the first conjugate of the anti-
commutator of q first conjugated, q prime first conjugated = - the anti-
commutator of q second conjugated, q prime second
conjugated](../img/QM/spin_and_angular_momentum/s_gr_35.gif)

At this point, I don't know how to use them, but again, the identity and first
conjugates appear to behave differently that the first and second conjugates.

##  Implications

This is not a super-symmetric proposal.  For that work, there is a super-
partner particle for every currently detected particle.  At this time, not one
of those particles has been detected, a serious omission.

Three different operators had to be blended together to perform this feat:
commutators, conjugates and rotations.  These involve issue of even/oddness,
mirrors, and rotations.  In a commutator under exchange of two quaternions,
the identity and the conjugate behave in a united way, while the first and
second conjugates form a similar, but not identical set.  Because this is a
general quaternion identity of automorphisms, this should be very widely
applicable.


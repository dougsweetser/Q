* Quaternions versus Space-time Numbers

The history of the 4D division algebra know as quaternions will be lightly
sketched. Are these good enough to describe all the patterns of events in
space-time? I will argue that two specific issues dealing with the rules of
addition and multiplication require a variation on quaternions I call
"space-time numbers." It is simple enough to convert a space-time number into a
quaternion (but not the reverse).

** The Multiple Discoveries of Quaternions

A quaternion is a division algebra like the real and complex numbers, but with
four degrees of freedom. Gauss was the first to work out the algebra in one of
his notebooks. He did not publish the results, possibly thinking they were not
interesting enough. Today, most practical physicists do not consider
quaternions to be worthy of much study.

Rodrigues figured out how to use quaternions to do rotations in three
dimensional space. There are several technical reasons why rotations should
always be done with quaternions instead of Euler angles, but I will skip a
detailed discussion of that subject. Rotations in 3D space remain the
one-trick-pony use of quaternions by both rocket scientists and game designers.

Hamilton spent a decade trying to figure out a consistent set of rule to add,
subtract, multiply and divide triplets of numbers. The first three are easy,
but making sure division always works cannot be done with triplets. Hamilton
realized on a walk with his wife that a fourth number was required, leading to
a famous bit of vandalism as he carved the rules onto a bridge. The "fourness"
of this new number was such a jump for Hamilton that he included it in the name
itself, the quaternions. Hamilton was so adverse to the 4D nature of
quaternions that the day after his discovery, he created the "pure quaternion"
where the first term was zero. I have not become a scholar of his efforts since
many of his contemporaries where unable to understand his written works.

The rules of quaternion algebra are simple and should be familiar to those who
have worked with complex numbers and vector algebra. A quaternion is a four
dimensional vector space over the real numbers. This means they can be added,
subtracted, or multiplied by a scalar. Care must be used to not call a
quaternion a 4-vector, a term that appears in differential geometry that brings
tangent and cotangent spaces into play. As a vector space over the real
numbers, quaternions are a group with the addition operator. The identity
element is zero.

To andle the multiplication operator, one needs a few rules:

![](quaternion_multiplication_rules.png)

One can make different choices for the signs, but this is the set that Hamilton
used. For use in symbolic math packages, I have found the 4x4 real matrix
representation is useful:

![](quaternion_matrix.png)

The matrix representation has the rules of multiplicaiton built in. Because it
is a matrix, it also has addition and what is necessary to invert the matrix.
The inverse of this matrix is the transpose of the matrix which always
necessarily exists divided by the norm of the matrix which is the sum of the
squares of each real-valued term.

Technical note: I define the norm as the product of a quaternion with its
conjugate:

![](quaternion_norm.png)

Notice the 3 zeroes. What is usually done is not include the three zeroes. They
matter to me for two reasons. First, the product of two quaternions is
necessarily another quaternion. This is obvious when one does programming since
the data structure stays the same. Second, much of calculus is the study of
change near interesting points. There may be times one want to study say q<sup>\*</sup>(q+da), 
then nothing needs to be modified.
[end note]

The norm will only equal zero for the zero quaternion. Therefore a
multiplicative inverse will exist in all cases except for zero, just as is the
case for the real and imaginary numbers.

For completeness, it should be noted that a quaternion can also be represented
by a 2x2 matrix with complex values. In my own experience with Mathematica, the
complex representation led to odd results.

A quaternion can be viewed as a [Clifford algebra](https://en.wikipedia.org/wiki/Clifford_algebra), specifically
Cl<sub>0, 2</sub>(R). Clifford algebras are also know as geometric algebra based
on a modern outreach effort by David Hestenes using the term Clifford did as
being more descriptive. That goal is to have a big tent of algebras, picking
the one that best fits the job at hand. This is different from my own research
work which is to find one structure that is powerful enough to do it all as
Nature does it all. The real and complex numbers are Cl<sub>0, 0</sub>(R) and
Cl<sub>0, 1</sub>(R) respectively. Both the real and complex numbers are
subgroups of quaternions. The real numbers are the diagonal of the matrix
representation. There are three complex numbers in every equations: the
diagonal plus any of the other three terms. One could also lump all three
imaginary numbers together and the result is a complex number. Multiplication
for real and complex numbers commutes, so they are both mathematical fields.
The sum of these parts, the quaternions, by contrast is not a mathematical
field because the order of multiplication matters to the cross product terms
found in a quaternion.

A quaternion with a norm of one is a way to represent the group SU(2), also
known as a unit quaternion. A unit quaternion sits in the middle of the
standard model, U(1)xSU(2)xSU(3). It remains an open riddle why the standard
model has these three particular Lie groups. 


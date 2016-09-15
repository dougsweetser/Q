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

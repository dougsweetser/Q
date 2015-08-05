![E equals gamma m c squared](../images/Index/egmc2.jpg)

# Special relativity using real-valued quaternions only

## Early failures

It was obvious in 1910 that quaternions _should_ be perfect to do the job of
rotating space and time since quaternions have always been the master of doing
rotations in space. This is how a rotation around the x axis is done:

![Rotatio around the x
axix](../images/SR/special_relativity/rotation_around_x.png)

Boosts are rotations involving space and time. There is a well know approach to
doing boosts that uses hypserbolic sines and cosines. Just swapping in the
hyperbolic functions for their counterparts does not work. So the first people
to try this abandoned quaternions and used complex-valued quaternions. The
added imaginary factors allowed them to get a boost that was as compact as
spatial rotations. They did not worry about loosing the properties of being a
division algebra a deal breaker.

The groups for doing spatial rotations versus boosts have a significant
technical difference. The group for doing spatial rotations, SO(3), which is
compact. The group for doing boosts, SO(1, 3), is not compact. We should not
have the expectation that boosts should have the same form as spatial
rotations. 

## An expression that works

I did a hunt for how to represent the Lorentz boost by starting with
a hyperbolic rotation, then seeing what was needed to construct the group
correctly. About a half hour of hunting and pecking in Mathematica reveled the
answer:

![ booost along the x axix](../images/SR/special_relativity/boost_along_x.png)

It is fun to compare the boost to the rotation: the former changes the first
two terms using hyperbolic functions, while the later operates on the final two
terms with the normal trig functions. Some people battle to understand the
factor of two on the angles, but I just accept it as is.

There are several places in the phyisics literature where it is claimed that
only complex-valued quaternions can represent the Lorentz group. Sometimes it
is good to just play until things work.

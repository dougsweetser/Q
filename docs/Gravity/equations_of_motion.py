#!/usr/bin/env python
# coding: utf-8

# # Equations of motion from a line element

# 
# 
# The idea for this notebook is to follow the logic presented at this URL: https://hepweb.ucsd.edu/ph110b/110b_notes/node79.html,
# first using the Schwarzschild metric, then with the exponential escape velocity field I have proposed.
# 
# Write out the Schwarzschild metric in spherical coordinates.
# 
# $$
# d\tau^2=\left(1-2 \frac{GM}{c^2 R}\right)dt^2-1/c^2\left(1-2 \frac{GM}{c^2 R}\right) dR^2-1/c^2 R^2 d\theta^2-1/c^2 R^2 \sin^2(\theta)d\phi^2
# $$
# 
# Divide through by $d\tau^2$:
# 
# $$
# 1=\left(1-2 \frac{GM}{c^2 R}\right)\left(\frac{dt}{d\tau}\right)^2-1/c^2\left(1-2 \frac{GM}{c^2 R}\right) \left(\frac{dR}{d\tau}\right)^2-\frac{1}{c^2} R^2 \left(\frac{d\theta}{d\tau}\right)^2-\frac{1}{c^2} R^2 \sin^2(\theta)\left(\frac{d\phi}{d\tau}\right)^2
# $$
# 
# If you have ever "done time" in a graduate-level math class on calculus, there is a major concern about this step. I will acknowledge, yet continue to go forward despite said concerns.
# 
# There are a few things to notice about this expression. The first is that it is a constant! That fact will be used later.
# 
# Expressions written in spherical coordinates which depends on $t$, $R$, $\theta$, and $\phi$. Notice that both $t$ and $\phi$ are _not in any of the 4 coefficients_. This looks like a squared velocity vector. If it can be put into a Lagrangian for the motion of a particle, then a change in time $t$ or an angle $\phi$ would not alter equations of motion. Where there is a symmetry like this there is a conserved quantity. In these cases, both energy and angular momentum are conserved respectively.
# 
# Without bothering to explain, the author of that web page writes down a Lagrangian:
# 
# $$
# \mathcal{L}_\rm{Schw.} = - m c \sqrt{\left(1-2 \frac{GM}{c^2 R}\right)c^2 \dot{t}^2-\frac{\dot{R}^2}{\left(1-2 \frac{GM}{c^2 R}\right)}-R^2 \dot{\theta}^2- R^2 \sin^2(\theta) \dot{\phi}^2};
# $$
# 
# The derivatives are with respect to the interval $\tau$. The Lagrangian is going to be invariant under a Lorentz transformation, as it typically is. There a three parts: a mass $m$, a constant $c$, and the square root of a velocity squared, so it is an $m \rm{velocity}^2$ expression of energy.Begin the analysis of this Lagrangian by writing it in a symbolic form so derivatives can be taken.

# In[2]:


import sympy as sp
from sympy import init_printing
from sympy import latex
sp.init_session(quiet=True)
init_printing(use_latex='mathjax')
R, θ, tdot, Rdot, θdot, Φdot, c, GM, m = sp.symbols("R, θ, tdot, Rdot, θdot, Φdot, c, GM, m")

c2 = c ** 2
g_factor = (1 - 2 * GM / (c2 * R))

LSch = - m * c * sp.sqrt( g_factor * c2 * tdot ** 2 - Rdot ** 2 / g_factor - R ** 2 * θdot ** 2 - R ** 2 * sp.sin(θ) ** 2 * Φdot ** 2 )
LSch


# The terms get mixed around, but the form looks correct.
# 
# To calculate the energy, take the derivative with respect to tdot.

# In[17]:


dLtdot = diff(LSch, tdot)


# $$ - \frac{c^{3} m \dot{t} \left(- \frac{2 GM}{R c^{2}} + 1\right)}{\sqrt{- R^{2} \dot{Φ}^{2} \sin^{2}{\left (θ \right )} - R^{2} \dot{θ}^{2} - \frac{\dot{R}^{2}}{- \frac{2 GM}{R c^{2}} + 1} + c^{2} \dot{t}^{2} \left(- \frac{2 GM}{R c^{2}} + 1\right)}} $$

# The denominator looks frightening, but recall that it just equals unity. As $M \rightarrow 0$ or $R \rightarrow \infty$, the result is what we expect for special relativity.

# Analyze the angular conservation using the phi dot term.

# In[4]:


dLΦdot = diff(LSch, Φdot)
dLΦdot


# Again the rather complicated expression of unity appears in the denominator. By comparison, the numerator looks simple and reasonable. 
# 
# Is this Lagrangian right? It is true that there is some latitude in picking out a Lagrangian. Since physics uses detivatives of Lagrangians, adding constant values can be done liberally. The two best things about the Lagrangian LSch is that it gets both the conservative quantities correct as confirmed by experimental tests of weak field gravity.
# 
# Many poeple would stop there and claim the case is closed, up to some arbitrary additiona and multiplication factors. Yet there are a number of things that bother me about the Lagrangian LSch. Why should there be a minus sign? Why use the constant veolcity $c$ in $ m c \sqrt{{...}}) $ when one is studying a velocity that changes in a gravity field? A square root function creates complicated relationships.
# 
# To explore LSch in more depth, take a derivative of the energy. Here are three second derivative terms:

# In[5]:


diff(dLtdot, tdot)


# In[6]:


diff(dLtdot, R)


# In[7]:


diff(dLtdot, Rdot)


# All three are complicated. Physics of course allows for complicated situations. Yet this is suppose to be simple, just a particle and a weak, static gravitational source.

# As a possible alternative, construct a new Lagrangian, one that starts from a justified starting spot. Write out a relativistic kinetic energy expressin that uses the same velocity squared, but does not use a square root.

# In[8]:


LKE = 1 - 1/2 * ( g_factor * c2 * tdot ** 2 - Rdot ** 2 / g_factor - R ** 2 * θdot ** 2 - R ** 2 * sp.sin(θ) ** 2 * Φdot ** 2 )
LKE


# Do the same sort of analysis as done before for the same reasons, namely to find the conserved energy and angular momentum.

# In[18]:


dLKEtdot = diff(LKE, tdot)
sp.expand(dLKEtdot)


# In[10]:


dLKEΦdot = diff(LKE, Φdot)
dLKEΦdot


# The "numerator" energy and momentum terms are exactly as before, but there is no complicated denominator. Using the velocity squared means no square root complications. See how that continues through these subsequent derivates of the energy.

# In[11]:


diff(dLKEtdot, tdot)


# In[12]:


diff(dLKEtdot, R)


# In[13]:


diff(dLKEtdot, Rdot)


# Everything is simpler. The last expression may provide the clearest way to distinguish between the two Lagrangians. For LKE, the energy is not a fucntion of Rdot. 

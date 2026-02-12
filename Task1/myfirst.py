#!/usr/bin/env python
# coding: utf-8

# # Coursework Set Week 1

# **Common remarks**:
# 
# * Deadline: Sunday at 23:59h for the week of this task
# * <font color='red'>Keep all the information in this template unaltered!</font>
# 
# **Please fill in the following fields:**
# 
# * Name: Ahmet Kaan Bulut
# * Username: akbulut
# * Student s-number: S6470564
# * Group (AS1, etc.): AS6
# 
# -----

# In[1]:


# Leave unaltered
totalpoints = currentpoints = 0


# ### Kepler's third law (4 pt) <font color='red'><b>COURSEWORK</b></font>
# 
# According to Kepler's third law, the square of the period ``P`` of the orbit of the planet is 
# proportional to the cube of the semi
# major axis (``a``) of an elliptical orbit (which is half the distance of the 
# longest axis of an ellipse).
# After applying Newton's (1642-1727) Laws of Motion and Newton's Law of Gravity 
# one can derive the more general form:
# 
# $$\boxed{P^2 = \frac{4\pi^2}{G(m_1+m_2)} a^3}$$
# 
# where ``G`` is the gravitational constant, ``a`` the distance to the Sun, ``P`` is
# the period for one orbit (i.e. one year), 
# ``m1`` is the mass of the heaviest and ``m2`` is the mass of
# the lighter body.
# 
# Given this information and the code template below, we ask 
# you to calculate an estimate of the mass of Sun and Earth combined. 
# Use Python variables with the same name as in the above formula.
# The answer is in fact the mass of the Sun because the mass of Earth is 
# almost a million times smaller than that of the Sun and therefore negligible.
# 
# Start your code with the line ``from scipy.constants import G, pi``
# to define the values for $G$ and $\pi$.
# 
# Answer: $(m_1+m_2) \approx 2\cdot10^{30}\; \rm{kg}$
#     
# **Your solution**:

# In[3]:


from scipy.constants import G, pi
import math

P = 365.25*24*3600
a = 149597870700
M = ((4*pi**2)*a**3)/(G*P**2)
print(M) #M = m1+m2


# In[11]:


# Leave unaltered
totalpoints += 4
currentpoints += 0


# ### Magnitude calculations (3 pt) <font color='red'><b>COURSEWORK</b></font>
# 
# Astronomers use the term apparent magnitude to describe how bright an object appears in the 
# sky as seen from Earth.  In 150 BC, Hipparchus invented a scale where he assigned 
# an apparent magnitude of 1 to the brightest stars in the sky, and he gave the dimmest 
# stars he could see an apparent magnitude of 6. (Sun, Moon and planets exclude).
# The absolute magnitude is invented later when astronomers realized that the magnitude depends
# on the distance to an object. 
# Therefore the absolute magnitude is defined as the apparent
# magnitude of an object if it was located at a distance of 10 parsecs.
# 
# The relation between absolute magnitude (M), apparent magnitude (m) and distance (d) in parsec is:
# 
# $$m - M = 5 \log_{10} d - 5$$
# 
# when we know the absolute- and apparent magnitude of a star, we calculate the distance
# to that star with the formula:
# 
# $$d(pc) = 10^{\frac{m-M}{5} + 1}$$
# 
# **Note:**  1 parsec is 3.26164 lightyear (ly).
# 
# We can calculate the distance to Sirius in lightyears with the Python code:
# 
# ```python
# # Sirius data
# apparentMagnitude = -1.46
# absoluteMagnitude = 1.45
# 
# # The distance is related to the magnitudes as m-M=5.Log(d/10)
# # 1 Parsec = 3.26164 ly
# 
# m = apparentMagnitude
# M = absoluteMagnitude
# 
# d = 10.0 * pow( 10.0, (m-M)/5.0 ) * 3.26164
# ```
#         
# 1. Copy this to an empty notebook. Expand it with interactive input with ``input()`` for both magnitudes and 
#    print the resulting distance using an f-string in ``print()``.  
#    Include the output for Sirius in your report.
# 2. Create a Python script (download notebook as ``.py`` file).  
#    - Rename the file into ``magnitude.py`` and run it with:  
#    ``python magnitude.py`` on the command line.
#    - Include code and embed a photo or screenshot of its output in your report.
# 
# **Answers**:

# In[ ]:





# In[43]:


# Leave unaltered
totalpoints += 3
currentpoints += 0


# ### Symbolic links (1 pt) <font color='red'><b>COURSEWORK</b></font>
# 
# 1. Create in your home directory a symbolic link to  ``/net/virgo01/data/users/XXXXXXX``, where `XXXXXXX`is your username.
#    This gives the path the alias to `VIRGO01`, which is the student data server.
# 2. Execute command ``ls -l`` in your home directory, make a text copy or screendump of its output and embed it in this notebook.
# 3. Change directory to `VIRGO01`. Make a dummy file with `touch`. Go to your home directory.  
#    List the contents of folder `VIRGO01` and include the listing in your report.
# 
# 
# **Answers**:

# In[ ]:





# In[24]:


# Leave unaltered
totalpoints += 1
currentpoints += 0


# ### (Remote desktop or Kapteyn PC) Configuring Dolphin and (3pt) <font color='red'><b>COURSEWORK</b></font>
# 
# On a Kapteyn PC or in a remote desktop, start application ``dolphin``, which is a file manager. Start Dolphin and configure it according to the image below.
# 
# ![image.png](attachment:image.png)
# 
# Make a screenshot of Dolphin’s window with application `spectacle`, Dolphin should show two panes, and in one of the panes the contents of directory ``PROGNUM/Task1`` should be displayed.
#     
# Embed the image in the coursework notebook.
# 
# **Embedded image**:

# In[ ]:





# In[27]:


# Leave unaltered
totalpoints += 3
currentpoints += 0


# ### Path finding (1 pt) <font color='red'><b>COURSEWORK</b></font>
# 
# * Use Unix command ``which ds9`` to find the Unix path to the application DS9. Write the path in your notebook. If you are working from
#   home, you should use the oVirt remote desktop to be able to use DS9.
# * You can start the programme by typing ``ds9`` on the command line. There is no need to type the whole path. 
# * Download FITS image [m101.fits](https://www.astro.rug.nl/intranet/courses/PROGNUM2023/build/html/Tasks/examples/m101.fits), copy it with
#   Filezilla to the directory PROGNUM/Task1 on your remote desktop, and display it from the command line by entering command ``ds9
#   m101.fits``. 
# * Try different color look up tables in ``ds9``.
# 
# Pixel positions in the image correspond to a position in a World Coordinate System (WCS). ``ds9`` does this transformation for you.
# 
# * Give WCS coordinates $(\alpha, \delta)$ for the approximate centre of the galaxy.
# 
# **Answer**:

# In[ ]:





# In[37]:


# Leave unaltered
totalpoints += 1
currentpoints += 0


# ## Finishing up
# 
# **Please read the section about your report in the task documentation very carefully before submitting it to BrightSpace.**
# 
# ------------

# 
# ## T.A. Grading

# In[45]:


# Leave unaltered
taskgrade = round(10*currentpoints/totalpoints, 1) if totalpoints != 0 else 0
print(f"Total number of points: {totalpoints}. Student score: {currentpoints}.  Task Grade = {taskgrade}")


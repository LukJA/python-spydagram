Future Development Notes
========================

Deciphering V1 Diagram Targets
------------------------------

For a first step, im going to start with the CUED undergraduate databooks, as a guide 
for where to begin and what to include.

In this way its also sort of revision!!

The idea is to build in an extensible system, where new disciplines can be conjoined
cohesively to the existing code space without conflict.

The key is to isolate what is best described as a *sketch* and what requires sufficient
complexity it deserves its own *diagram* subset.

Dump of CUED databooks
----------------------

Mechanics
^^^^^^^^^

1. Kinematics
    - Velocity and acceleration in polar and intrinsic coordinate systems
2. Geometry
    - Ellipse [ Orbits ]
    - Solids of revolution [ arbitrary revolved solid ]
3. Mechanics of Machines
    - **Free body force diagrams**
        - e.g. rope or belt friction on a pulley wheel
    - Cam and gear kinematics [ arbitrary 2d body ]
4. Linear systems, Vibration  and Stability
    - Step and impulse responses of 2nd order linear systems 
    - Harmonic responses of 2nd order linear systems [ a/b/c variants ]
5. Areas, Volume, CoG, MoI
    - Parallel axis theorem [ on an arbitrary lamina ]
    - Moments of inertia
        - Rods
        - Curved Rod
        - lamina
        - Sectoral lamina
        - Elliptical lamina
        - Triangular lamina
        - Polygonal lamina
    - Solids of Revolutions
        - Cylinder
        - Spheroid
        - Cone
        - Hemisphere
        - Toroids
    - Shells of Revolution
        - Cyclidrical
        - Spherical
        - spherical cap
        - conical shell

Structures
^^^^^^^^^^

Materials
^^^^^^^^^

Electrical
^^^^^^^^^^

Thermofluids
^^^^^^^^^^^^

Information
^^^^^^^^^^^

Mathematics
^^^^^^^^^^^

Call Architecture
-----------------

Deciding on the nested/inherited object and call hierarchy is key to ensuring fast and simple
usability.

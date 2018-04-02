# Camera Models

### What is a Pinhole Camera?
- Has no lens, simply a hole
- Hole must not be too small or big -> otherwise blurring effects through diffraction or averaging
- Small set of rays from a point hits the screen

### What is the reason for lenses?
Lenses gather and focus light -> allow for brighter images

### What is the effective diameter of a lens?
Portion of a lens actually reachable by light rays

### How is the field of view defined?
tan w = d / 2 f with d = effective diameter and f = focal length

### How is the depth of field defined?
Range of distances that produce acceptably focussed images

### What are circles of confusion?
The rays from the same point hit the image at different points
Can't be circumvented when imaging objects at different distances -> Tiefenunschärfe 

### What is a vanishing point?
Place where parallel lines meet

### What is vignetting?
When placing lenses in front of each other, parts of them become unused

### What are collinear vanishing points?
Induced by sets of parallel lines on the same plane -> line through vanishing points is the horizon

### What is Orthographic projection? What is its camera matrix?
- Points get mapped onto a lower-dimensional space
- Parallel projection lines, no pin-hole
- 1000, 0100, 0001
- -> Take x and y, ignore z and account for varying projector distances by setting W = T

### What is weak perspective projection? What is its camera matrix?
- Same as orthographic, but with constant scaling factor f / Zavg  
- 1000, 0100, 000Zavg/f

### What is the Perspective Projection Equation for a pinhole?
- (-f*x/z, -f*y/z, -f), where f is the distance between image and origin and x, y, z are the coordinates of the object
- Height of image = - object height * image distance / object distance

### What are homogeneous coordinates?
Have additional dimension to account for the fact that if the distance between projector (object) and screen (image) increases, the screen coordinates increase as well. The additional dimension captures the distance, which is set to 1 for the correct coordinates.

### What is the Projective Camera matrix?
- Maps a 3D point to a 2D point on a pinhole camera image
- 1, 1, 1/f
- 3D point's HC coordinates have T as additional dimension
- Resulting 2D point's HC coordinates need to be divided by additional dimension to get 2D position

### What transformations does a camera apply to the original point in HC?
1. Transformation representing extrinsic parameters (camera may not be at the origin)
2. Transformation representing projection model
3. Transformation representing intinsic parameters (focal length, principal point, aspect ratio etc.)

### How many extrinsic parameters are there for a camera?
6, because we need 3 for the rotation matrix and 3 for the translation vector


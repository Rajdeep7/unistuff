# Path Planning (Apr 17 2018)

### Basic task
- Find path from configuration A to configuration B
- With constraints:
  - Nonholonomic constraints
  - Continuous Curvature
  - Obstacles etc.
  
### Example AD Tasks
- Parking -> space critical, not time critical
- Unstructured environments (Parking lot on farmer's field)
- Highway maneuvers -> safety critical
- Route Planning

## Holonomic vs Nonholonomic constraints (exam!)
- In general: limit the possible state transitions of a robot / car
- Holonomic 
  - Any reachable configuration can be reached by a simple motion (robot can directly drive to a goal configuration)
  - Constraints can be written without using derivatives
  - Example constraints:
    - Constraint on position -> robot can't leave the arena
    - Constraint on 3D position -> robot can't leave the surface of a sphere (x^2+y^2+z^2 = 1)
  - Notes:
    - Can basically drive in every direction (full degree of freedom)
    - Orientation of car != orientation of wheels
- Nonholonomic
  - Reaching configurations may require a combination of motions instead of simple motions
  - Constraints may depend on the derivatives of state variables (x, y, orientation etc.)
  - Can't be integrated to a representation without derivatives
  - Example constraints:
    - A wheel may only move in one direction -> dy/dt = sin(orientation), dx/dt = cos(orientation), dorientation/dt = u
    
## Single Track Model (exam!)


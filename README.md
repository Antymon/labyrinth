Labyrinth Generator
---------
Simple Python one-class randomized maze generator.

Generates mazes based on Depth First Search.

###Example usage:

```python
import time
import numpy as np
from labyrinth import Labyrinth
    
size = 200
x = np.random.randint(1, size)
y = 1
start = (x, y)
l = Labyrinth(size, size, start, straightness_factor=0.1)
l.print('maze_{}.png'.format(time.time()))
```

###Example mazes
Yellow box symbolizes start. Isolated cells are separately highlighted.

[maze_0]: examples/maze.png
[maze_1]: examples/maze_1579792100.5722864.png
[maze_2]: examples/maze_1579792138.850511.png
[maze_3]: examples/maze_1579792164.190318.png
[maze_4]: examples/maze_1579792178.2891562.png

![maze_0]
![maze_1]
![maze_2]
![maze_3]
![maze_4]


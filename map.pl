adjacent(1,2).         adjacent(2,1).   
adjacent(1,3).         adjacent(3,1).   
adjacent(1,4).         adjacent(4,1).   
adjacent(1,5).         adjacent(5,1).   
adjacent(2,3).         adjacent(3,2).   
adjacent(2,4).         adjacent(4,2).   
adjacent(3,4).         adjacent(4,3).   
adjacent(4,5).         adjacent(5,4).  

color(1, orange, x).    color(1, orange, y).  
color(2, pink, x).  color(2, pink, y).  
color(3, purple, x).    color(3, purple, y).  
color(4, red, x).   color(4, pink, y). 
color(5, pink, x).  color(5, purple, y). 

conflict(R1, R2, Coloring) :-  
adjacent(R1, R2),  
color(R1, Color, Coloring),  
color(R2, Color, Coloring).   
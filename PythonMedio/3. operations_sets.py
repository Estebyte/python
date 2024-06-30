set_a = {'col', 'mex', 'bol'}
set_b = {'pe', 'bol'}

# unión de los conjuntos

set_c = set_a.union(set_b)
print(set_c)
print(set_a | set_b) 

# elementos en común

set_c = set_a.intersection(set_b)
print(set_c)
print(set_a & set_b) 

# dejamos sólo los elementos de A

set_c = set_a.difference(set_b)
print(set_c)  
print(set_a - set_b)  

# unión sin los elementos en común

set_c = set_a.symmetric_difference(set_b)
print(set_c) 
print(set_a ^ set_b)
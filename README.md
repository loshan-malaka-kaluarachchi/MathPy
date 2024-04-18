# Mathematic variables

Implementation of classes to model symbolic variables.
Properties of a algebraic variable.

For algebraic terms, $a$ is the coefficient, $x$ is the symbol for the variable and $p$ is the power.
$$ a \cdot x^{p} $$

### Case 1: Variables with equal powers can only be added
$$ a \cdot x^{p} + b \cdot x^{p} = \( a + b\) \cdot x^{p} $$ 

### Case 2: If coefficients and powers equal to one, they can be hidden
$$ 1 \cdot x^{1} = x $$

### Case 3: If coefficient is zero
$$ a = 0; p = ? -> 0 $$

### Case 4: If the index is equal to zero 
$$ a = ?; p = 0 -> a $$

### Case 5: If the coefficient and index is equal to 1
$$ a = 1; p = 1 -> x $$

### Case 6: If the index is equal to 1
$$ a = ?; p = 1 -> ax $$

### Case 7: If both the coefficient and index are neither zero nor one
$$ a = ?; p = ? -> ax^p $$




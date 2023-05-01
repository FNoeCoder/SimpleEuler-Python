from SimpleEuler import SimpleEuler

# Example: y'= 4x-2y;  y(0)=2;  y(0.5);  h= 0.1

equation = "4*x-2*y"
x0 = "0"
y0 = "2"
domain = "0.5"
h = "0.1"

example = SimpleEuler(equation, x0, y0, domain, h)

print(example.getListXY())
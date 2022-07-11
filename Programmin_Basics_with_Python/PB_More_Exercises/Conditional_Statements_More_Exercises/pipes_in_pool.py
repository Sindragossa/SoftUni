v = int(input())
p1 = int(input())
p2 = int(input())
h = float(input())

pipe1 = p1 * h
pepe2 = p2 * h
all_pipes = pipe1 + pepe2

if all_pipes <= v:
    full_percent = (all_pipes / v) * 100
    pipe1_percent = (pipe1 / all_pipes) * 100
    pepe2_percent = (pepe2 / all_pipes) * 100
    print(f'The pool is {full_percent:.2f}% full. Pipe 1: {pipe1_percent:.2f}%. Pipe 2: {pepe2_percent:.2f}%.')
elif all_pipes > v:
    everything = all_pipes - v
    print(f'o	"For {h:.2f} hours the pool overflows with {everything:.2f} liters."')
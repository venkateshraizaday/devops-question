print(f"Code loops to 1000 and prints numbers divisible by 7 and 11")

# begin
n = 1000

for i in range(1, n):
    if i%7==0 and i%11==0:
        print(i)
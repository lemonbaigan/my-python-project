import math 


def calculate_v(u,a,s):
    return math.sqrt(u**2 + 2*a*s)

def calculate_u(v,a,s): 
    return math.sqrt(v**2 - 2*a*s)

def calculate_a(v,a,s):
    return(v**2 - u**2) / (2*s)

def calculate_s(v,u,a):
    return (v**2 - u**2) / (2*a)

print("📘 Equation : v^2 = u^2 + 2as")
print("what do you want to calculate?")
print("1, v (final velocity)")
print("2, u (intial velocity)")
print("3, a (acceleration)")
print("4, s (distance)")


choice = input("enter your choice nigesh (1/2/3/4): ")

if choice == '1': 
    u= float(input("enter inital velocity(u): "))
    a = float(input("Enter acceleration (a): "))
    s = float(input("Enter distance (s): "))
    v = calculate_v(u, a, s)
    print(f"✅ Final velocity (v) = {v:.2f}")
elif choice == '2':
    v = float(input("Enter final velocity (v): "))
    a = float(input("Enter acceleration (a): "))
    s = float(input("Enter distance (s): "))
    u = calculate_u(v, a, s)
    print(f"✅ Initial velocity (u) = {u:.2f}")
elif choice == '3':
    v = float(input("Enter final velocity (v): "))
    u = float(input("Enter initial velocity (u): "))
    s = float(input("Enter distance (s): "))
    a = calculate_a(v, u, s)
    print(f"✅ Acceleration (a) = {a:.2f}")
elif choice == '4':
    v = float(input("Enter final velocity (v): "))
    u = float(input("Enter initial velocity (u): "))
    a = float(input("Enter acceleration (a): "))
    s = calculate_s(v, u, a)
    print(f"✅ Distance (s) = {s:.2f}")
else:
      print("❌ Invalid choice. Try again.")

import random

def estimate_pi(n):
    num_point_circle = 0
    num_point_total = 0
    for i in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        distance = x**2 + y**2
        if distance <= 1:
            num_point_circle = num_point_circle + 1
        num_point_total = num_point_total + 1

    return 4 * num_point_circle / num_point_total

print("The estimation for pi is:")
print(estimate_pi(1000000))
print("cool right?")
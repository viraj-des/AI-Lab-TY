jug4 = 0
jug3 = 0

print("Water Jug Problem\n")

jug3 = 3
print("Step1: 4L =", jug4, "3L =", jug3)

jug4 = jug3
jug3 = 0
print("Step2: 4L =", jug4, "3L =", jug3)

jug3 = 3
print("Step3: 4L =", jug4, "3L =", jug3)

jug3 = jug3 - (4 - jug4)
jug4 = 4
print("Step4: 4L =", jug4, "3L =", jug3)

print("Goal Achieved:", jug3, "Liters")
'''
Created on Tue Aug 29 16:52 2023

Using the Integer Linear Programming

The function in this file is used to matches N patients with K doctors. Each patient is allowed to provide a ranked list 
of their preference for doctors, however, doctors are prohibited from displaying preferences for patients. Thus the code should takes in the following:

- A 2D list of ranked preferences (# of patients X # of doctors) (highest number = most preferred).
- A list of the maximum capacity for each doctor (assume that the total capacity exceeds the number of patients)

Output Return:
- A list of assignments indicating which doctors are to take care of which patients

Assumptions:
@ 09/04/2023:
- Doctors don't have preferences for patients (since they are not displaying their preferences)
- Total capacity exceeds the number of patients
- Each patient provides a rank for every doctor
- Ties are allowed

Summary of the function:
Consider the problem as the Integer Linear Problem. Define the binary variables x_ij that are equal to 1 when patient i is assigned to doctor j and 0 otherwise. 
The objective function is to maximize the sum of preferences. The constraints are that each patient is assigned to exactly one doctor and each doctor has a maximum capacity.

Author: @Nelson Wu, @Sai Koukuntla, @Alexandra Cheng 
'''

from pulp import LpMaximize, LpProblem, LpVariable, lpSum, PULP_CBC_CMD

def ilp_assignment(preferences, doctor_capacity):
    num_patients = len(preferences)
    num_doctors = len(preferences[0])

    # Create the ILP problem
    model = LpProblem(name="doctor-patient-assignment", sense=LpMaximize)

    # Create variables
    x = {}
    for i in range(num_patients):
        for j in range(num_doctors):
            for k in range(doctor_capacity[j]):
                x[i, j] = LpVariable(name=f"x_{i}_{j}", cat="Binary")

    # Objective function: Maximize the sum of preferences
    model += lpSum(preferences[i][j] * x[i, j] for i in range(num_patients) for j in range(num_doctors)), "Total_Preference"

    # Constraint: Each patient is assigned to exactly one doctor
    for i in range(num_patients):
        model += lpSum(x[i, j] for j in range(num_doctors)) == 1, f"Patient_{i}"

    # Constraint: Each doctor has a maximum capacity
    for j in range(num_doctors):
        for k in range(doctor_capacity[j]):
            model += lpSum(x[i, j] for i in range(num_patients)) <= doctor_capacity[j], f"Doctor_{j}_{k}"

    # Solve the problem
    model.solve(PULP_CBC_CMD(msg=0))

    # Extract the assignments
    assignments = [[] for _ in range(num_doctors)]
    for i in range(num_patients):
        for j in range(num_doctors):
            if x[i, j].varValue == 1:
                assignments[j].append(i)

    return assignments

# # Test the function
# preferences = [
#     [5, 2, 1],
#     [4, 3, 1],
#     [3, 2, 4],
#     [1, 5, 2]
# ]
# doctor_capacity = 2

# assignments = ilp_assignment(preferences, doctor_capacity)
# print("Assignments:", assignments)

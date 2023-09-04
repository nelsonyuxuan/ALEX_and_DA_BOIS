'''
Created on Tue Aug 29 16:52 2023

Using the Integer Linear Programming

The function in this file is used to matches N patients with K doctors. Each patient is allowed to provide a ranked list 
of their ppreference for doctors, however, doctors are rohibited from displaying preferences for patinets. Thus the code should takes in the following:

- A list of ranked preferences, 1 list for each patient.
- A maximum capacity for each doctor (can initially assume the same capacity - note that the total capacity should exceed the number of patients)

Output Return:

- A list of assignments indicating which doctors are to take care of which patients

Assumptions:
@ 09/04/2023:
- Doctors don't have preferences for patients (since they are not displaying their preferences)
- Doctors have the same capacity 
- The list of preferences are assumed to be no equals (i.e. no ties). The maximum preference would be equal to the number of doctors (i.e. 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 for 10 doctors).

Summary of the function:
Consider the problem as the Integer Linear Problem. Define the binary variables x_ij that are equal to 1 when patient i is assigned to doctor j and 0 otherwise. 
The objective function is to maximize the sum of preferences. The constraints are that each patient is assigned to exactly one doctor and each doctor has a maximum capacity.

Author: @Nelson Wu 
'''

from pulp import LpMaximize, LpProblem, LpVariable, lpSum

def ilp_assignment(preferences, doctor_capacity):
    num_patients = len(preferences)
    num_doctors = len(preferences[0])

    # Create the ILP problem
    model = LpProblem(name="doctor-patient-assignment", sense=LpMaximize)

    # Create variables
    x = {}
    for i in range(num_patients):
        for j in range(num_doctors):
            x[i, j] = LpVariable(name=f"x_{i}_{j}", cat="Binary")

    # Objective function: Maximize the sum of preferences
    model += lpSum(preferences[i][j] * x[i, j] for i in range(num_patients) for j in range(num_doctors)), "Total_Preference"

    # Constraint: Each patient is assigned to exactly one doctor
    for i in range(num_patients):
        model += lpSum(x[i, j] for j in range(num_doctors)) == 1, f"Patient_{i}"

    # Constraint: Each doctor has a maximum capacity
    for j in range(num_doctors):
        model += lpSum(x[i, j] for i in range(num_patients)) <= doctor_capacity, f"Doctor_{j}"

    # Solve the problem
    model.solve()

    # Extract the assignments
    assignments = [[] for _ in range(num_doctors)]
    for i in range(num_patients):
        for j in range(num_doctors):
            if x[i, j].varValue == 1:
                assignments[j].append(i)

    return assignments

# Test the function
preferences = [
    [5, 2, 1],
    [4, 3, 1],
    [3, 2, 4],
    [1, 5, 2]
]
doctor_capacity = 2

assignments = ilp_assignment(preferences, doctor_capacity)
print("Assignments:", assignments)

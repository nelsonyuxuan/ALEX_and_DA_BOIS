'''
Created on Tue Aug 29 16:52 2023

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

Author: @Nelson Wu 
'''

def rank_order(ranked_preferences, indiv_max_capcity):
    # Import Packages
    import numpy as np
    from scipy.optimize import linear_sum_assignment 
    
    # Read in the number of patients and doctors
    num_patients = len(ranked_preferences)
    num_doctors = len(ranked_preferences[0])

    # Initialize the cost matrix based on the number of patients and doctors
    cost_matrix = -np.array(ranked_preferences)
    
    # Duplicate rows for each doctor based on their capacity
    extended_cost_matrix = np.repeat(cost_matrix, indiv_max_capcity, axis=1)
    
    # Perform the Hungarian algorithm to find the optimal assignment
    row_ind, col_ind = linear_sum_assignment(extended_cost_matrix)
    
    # Create a list to store the assignment of patients to doctors
    assignments = [[] for _ in range(num_doctors)]
    
    for patient, doctor in enumerate(col_ind):
        # Convert extended doctor index to original doctor index
        original_doctor = doctor % num_doctors
        assignments[original_doctor].append(patient)
        
    return assignments

# Example usage
preferences = [
    [5, 2, 1],  # Preferences for patient 0
    [4, 3, 1],  # Preferences for patient 1
    [3, 2, 4],  # Preferences for patient 2
    [1, 5, 2]   # Preferences for patient 3
]
doctor_capacity = 2  # Each doctor can handle 2 patients

assignments = rank_order(preferences, doctor_capacity)
print("Assignments:", assignments)
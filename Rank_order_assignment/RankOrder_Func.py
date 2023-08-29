'''
Created on Tue Aug 29 16:52 2023

The function in this file is used to matches N patients with K doctors. Each patient is allowed to provide a ranked list 
of their ppreference for doctors, however, doctors are rohibited from displaying preferences for patinets. Thus the code should takes in the following:

- A list of ranked preferences, 1 list for each patient.
- A maximum capacity for each doctor (can initially assume the same capacity - note that the total capacity should exceed the number of patients)

Output Return:

- A list of assignments indicating which doctors are to take care of which patients
'''

def rank_order(ranked_preferences, indiv_max_capcity):
    # Import Packages
    import numpy as np
    
    # Read in the number of patients and doctors
    num_patients = len(ranked_preferences)
    num_doctors = len(indiv_max_capcity)

    # Initialize the cost matrix based on the number of patients and doctors
    cost_matrix = -np.array(ranked_preferences, indiv_max_capcity)

    



    return final_assignment
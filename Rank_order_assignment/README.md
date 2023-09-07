## Rank-Order Assignment

## Files:
- **RankOrder_LIP.py** contains the function that implements the Integer Linear Programming method to solve the rank order problem.
- **demo.ipynb** is the demo script that employs the created function.

## RankOrder_LIP.py:
The function in this file is used to matches N patients with K doctors. Each patient is allowed to provide a ranked list 
of their preference for doctors, however, doctors are prohibited from displaying preferences for patients. Thus the code should takes in the following:

- A 2D list of ranked preferences (# of patients X # of doctors) (highest number = most preferred).
- A list of the maximum capacity for each doctor (assume that the total capacity exceeds the number of patients)

Output Return:
- A list of assignments indicating which doctors are to take care of which patients

## Assumptions:
- **Doctor Preferences**: Doctors do not have patient preferences, as they are not allowed to express them.
- **Patient Assignment**: If the total capacity of doctors exceeds the number of patients, every patient is guaranteed an assignment. Otherwise, some patients may not be assigned.
- **Patient Ranking**: Each patient ranks every doctor.
- **Ties**: Ties in rankings are permitted.
- **Doctor Capacity**: Doctors may have varying capacities.
- **Preference Values**: Preferences must be integers, in line with the ILP approach. A patient's maximum preference for any doctor is equal to the total number of doctors, while the minimum is 1.


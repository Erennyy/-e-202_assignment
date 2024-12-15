Student ID: 2022402303

You are expected to formulate a multiple-layer transshipment problem.
Your objective is to satisfy all the demand with the least cost.
All related data are provided at the end of this document.

Use Python and Pulp Package for the questions below. You are expected to upload your code and a report. 
Make sure your code is clear, free of repetitions and unneccesary outputs. Use descriptive comments in your code.
Each of you has unique data for the problem, use the dataset assigned to you. You can either carry out the assignment
individually, or in groups of up to three people. If in a group, using the data of any member is fine. If any resemblence
between two submissions is detected,both parties will be held accountable for plagiarism.

Question 1. Formulate this problem as an LP in Pulp. Name your decision variables and constraints clearly.
Output the model formulation (objective function and the constraints), Solve the model, then output the optimal solution,
the basic variables and the total cost. Draw the solution on the network. You can draw by hand or use the online website draw.io

Question 2. Answer these questions according to the results of question 1 and seperately for each task. 
Firsly argue your expectations with reasoning using economic interpretation of the results without resolving the LP,
then reformulate a seperate model and solve it, inspect the total cost and confirm your expectations.
Do not forget to update and revert the data for each task. Note that the naming of nodes start with 0.
Avoid repetition of similar code. Define functions for similar uses.

    Question 2.a. The capacity of supply node 2 increases by one unit.
    What is the expected change in the total cost?
    Answer using economic interpretation. Then, confirm your expectations with resolving the LP.

    Question 2.b. The capacity of supply node 0 increases by one unit.
    What is the expected change in the total cost?
    Answer using economic interpretation. Then, confirm your expectations with resolving the LP.

    Question 2.c. The demand quantity of demand node 0 increases by one unit.
    What is the expected change in the total cost?
    Answer using economic interpretation. Then, confirm your expectations with resolving the LP.

    Question 2.d. The cost of sending one unit from supply node 0 to first layer transshipment node 0 decreases by one.
    Do you expect a change in the basis? What is the expected change in the cost?
    Answer using economic interpretation. Then, confirm your expectations with resolving the LP.

    Question 2.e. The cost of sending one unit from supply node 0 to first layer transshipment node 2 decreases by one.
    Do you expect a change in the basis? What is the expected change in the cost?
    Answer using economic interpretation. Then, confirm your expectations with resolving the LP.

    Question 2.f. What if the decrease in Question 2.e. was 21?
    Do you expect a change in the basis? What is the change in the cost?
    Confirm your expectations with resolving the LP.

Question 3. Say that supply node 0 cannot ship to first layer transshipment node 0.
Do you think that the total cost will increase or decrease in this case? Explain.
Model the LP and Solve regarding this. Output the basic variables and the optimal cost.

Question 4. Say that the demand of retailer 0 increases.
For how much increase do you think that you will be able to satisfy the demand?
For how much increase you will lose sales?

Hints:
    - You are formulating and solving an LP. Define your decision variables as non-negative and CONTINUOUS.
Otherwise, you won't be able to make economic interpretation.
    - Don't formulate for the transportation simplex. Don't use theta for the transhipment nodes and don't introduce dummy supply/demand.   
    - You will need three sets of decision variables. You can name them X_S_T1, X_T1_T2, X_T2_D.
    - Node IDs start with 0. This is consistent with Python indices. Be careful about this on answering your questions.
    - You can use the makeDict() function of Pulp to prepare data for the LP Models

Data for the Student No: 2022402303
no_of_supply_nodes = 4
no_of_first_layer_transshipment_nodes = 3
no_of_second_layer_transshipment_nodes = 5
no_of_demand_nodes = 4
c_S_T1 = [

[13, 11, 12],
[19, 13, 16],
[22, 21, 22],
[22, 15, 23]]

c_T1_T2 = [

[45, 49, 47, 33, 52],
[34, 36, 44, 67, 60],
[53, 67, 54, 57, 57]]

c_T2_D = [

[17, 14, 15, 12],
[10, 16, 19, 11],
[19, 13, 10, 16],
[11, 10, 19, 16],
[15, 15, 12, 16]]

supply_capacities = [354, 386, 101, 291]
demand_quantities = [281, 203, 355, 171]

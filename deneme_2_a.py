import pulp

no_of_supply_nodes = 4
no_of_first_layer_transshipment_nodes = 3
no_of_second_layer_transshipment_nodes = 5
no_of_demand_nodes = 4

c_S_T1 = [
    [13, 11, 12],
    [19, 13, 16],
    [22, 21, 22],
    [22, 15, 23]
]

c_T1_T2 = [
    [45, 49, 47, 33, 52],
    [34, 36, 44, 67, 60],
    [53, 67, 54, 57, 57]
]

c_T2_D = [
    [17, 14, 15, 12],
    [10, 16, 19, 11],
    [19, 13, 10, 16],
    [11, 10, 19, 16],
    [15, 15, 12, 16]
]

supply_capacities = [354, 386, 101, 291]
demand_quantities = [281, 203, 355, 171]

def transshipment_problem(supply_capacity, demand_quantity, cost_S_T1, cost_T1_T2, cost_T2_D):

    model = pulp.LpProblem("MultiLayer_Transshipment", pulp.LpMinimize)

    # Introducing LP Problem Variables
    X_S_T1 = {}
    X_T1_T2 = {}
    X_T2_D = {}

    # Supply Nodes to First Layer of Transshipment Nodes
    for i in range(no_of_supply_nodes):
        for j in range(no_of_first_layer_transshipment_nodes):
            X_S_T1[(i, j)] = pulp.LpVariable(f"X_S_T1_{i}_{j}", lowBound=0, cat="Continuous")

    # First Layer of Transshipment Nodes to Second Layer of Transshipment Nodes
    for j in range(no_of_first_layer_transshipment_nodes):
        for k in range(no_of_second_layer_transshipment_nodes):
            X_T1_T2[(j, k)] = pulp.LpVariable(f"X_T1_T2_{j}_{k}", lowBound=0, cat="Continuous")

    # Second Layer of Transshipment Nodes to Demand Nodes
    for k in range(no_of_second_layer_transshipment_nodes):
        for l in range(no_of_demand_nodes):
            X_T2_D[(k, l)] = pulp.LpVariable(f"X_T2_D_{k}_{l}", lowBound=0, cat="Continuous")

    # Setting the Objective Function
    model += (
        pulp.lpSum(cost_S_T1[i][j] * X_S_T1[(i, j)] for i in range(no_of_supply_nodes) for j in range(no_of_first_layer_transshipment_nodes)) +
        pulp.lpSum(cost_T1_T2[j][k] * X_T1_T2[(j, k)] for j in range(no_of_first_layer_transshipment_nodes) for k in range(no_of_second_layer_transshipment_nodes)) +
        pulp.lpSum(cost_T2_D[k][l] * X_T2_D[(k, l)] for k in range(no_of_second_layer_transshipment_nodes) for l in range(no_of_demand_nodes))
    )

    # Constraints
    # Supply Quota Restrictions
    for i in range(no_of_supply_nodes):
        model += pulp.lpSum(X_S_T1[(i, j)] for j in range(no_of_first_layer_transshipment_nodes)) <= supply_capacity[i]

    # First Layer Quaota Restrictions
    for j in range(no_of_first_layer_transshipment_nodes):
        model += pulp.lpSum(X_S_T1[(i, j)] for i in range(no_of_supply_nodes)) == pulp.lpSum(X_T1_T2[(j, k)] for k in range(no_of_second_layer_transshipment_nodes))

    # Second Layer Quota Restrictions
    for k in range(no_of_second_layer_transshipment_nodes):
        model += pulp.lpSum(X_T1_T2[(j, k)] for j in range(no_of_first_layer_transshipment_nodes)) == pulp.lpSum(X_T2_D[(k, l)] for l in range(no_of_demand_nodes))

    # Demand Quota Restrictins
    for l in range(no_of_demand_nodes):
        model += pulp.lpSum(X_T2_D[(k, l)] for k in range(no_of_second_layer_transshipment_nodes)) >= demand_quantity[l]

    # Integrated Functions that Solving LP Problem    
    model.solve()

    # 6. Results
    print("Total Cost:", pulp.value(model.objective))
    print("Basic Variables:")
    for v in model.variables():
        if v.varValue > 0:
            print(f"{v.name} = {v.varValue}")
    print("-" * 50)
    return pulp.value(model.objective)

original_cost = transshipment_problem(supply_capacities, demand_quantities, c_S_T1, c_T1_T2, c_T2_D)

# Question 2.a: Supply Node 2 capacity increases by 1
updated_supply = supply_capacities[:]
updated_supply[2] += 1
new_cost = transshipment_problem(updated_supply, demand_quantities, c_S_T1, c_T1_T2, c_T2_D)
print("Cost Change:", new_cost - original_cost)

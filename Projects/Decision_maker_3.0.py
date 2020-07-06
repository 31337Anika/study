values = []
parameters = []

number_of_values = int(input("enter number of values:"))
count_of_values = 0


number_of_parameters = int(input("enter number of parameters:"))
count_of_parameters = 0

while count_of_values < number_of_values:
    value_name = input("enter value's name:")
    values.append(value_name)
    count_of_values += 1

while count_of_parameters < number_of_parameters:
    parameter_name = input("enter parameter's name:")
    parameter_weight = input("enter parameter weight")
    parameters_dict = {'name': parameter_name, 'weight': parameter_weight}
    parameters.append(parameters_dict)

    count_of_parameters += 1

count_of_values = 0
count_of_parameters = 0


print(values)
print(parameters)

result = []
while count_of_values < number_of_values:
    while count_of_parameters < number_of_parameters:
        print(values[count_of_values])
        print("please rate ",values[count_of_values]," in ",parameters[count_of_parameters].get("name"))

        weight = float(parameters[count_of_parameters].get("weight"))
        rating = float(input(":"))
        parameter_cost = rating * weight
        count_of_parameters += 1

        result_value = {"value": count_of_values, "parameter_cost": parameter_cost}
        result.append(result_value)

    count_of_values += 1
    count_of_parameters = 0

output = {}

for value in result:
    i = value.get("value")
    parameter_total_weight = value.get("parameter_cost")
    if i in output:
        weight_old = output[i]
    else :
        weight_old = 0
    weight_sum = weight_old + parameter_total_weight
    dict = {i: weight_sum}
    output.update(dict)

count_of_values = 0
maximum_value, maximum_value_name = 0,""
while count_of_values < number_of_values:
    print(values[count_of_values]," is ",output[count_of_values])
    if output[count_of_values]>maximum_value:
        maximum_value = output[count_of_values]
        maximum_value_name = values[count_of_values]
    count_of_values += 1
print("The best decision is ",maximum_value_name)
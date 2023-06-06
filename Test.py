def print_operation_table(operation, num_rows=6, num_colums=6):
    for i in range(num_rows):
        list_operation = []
        for j in range(num_colums):
            list_operation.append(operation)
        print(list_operation)

print_operation_table("o", 8, 8)
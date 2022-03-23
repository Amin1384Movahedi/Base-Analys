def null_checker(data):
    # Check for null values
    n_nulls = len(data[data.isnull().any(axis=1)])
    print(f'\nnumber of null values in whole DataFrame : {n_nulls}\n')

    for col in data.columns:
        n_null_1 = len(data[data[col] == '?'])
        n_null_2 = len(data[data[col] == ' ?'])
        n_null_3 = len(data[data[col] == '? '])
        n_null_4 = len(data[data[col] == ' ? '])
        n_null_5 = len(data[data[col] == ' '])

        if n_null_1 != 0:
            print(f'==========={col}===========\n')
            print(f'Number of null values which is filled by "?" is : {n_null_1}\n')

        elif n_null_2 != 0:
            print(f'==========={col}===========\n')
            print(f'Number of null values which is filled by " ?" is : {n_null_2}\n')

        elif n_null_3 != 0:
            print(f'==========={col}===========\n')
            print(f'Number of null values which is filled by "? " is : {n_null_3}\n')

        elif n_null_4 != 0:
            print(f'==========={col}===========\n')
            print(f'Number of null values which is filled by " ? " is : {n_null_4}\n')

        elif n_null_5 != 0:
            print(f'==========={col}===========\n')
            print(f'Number of null values which is filled by " ? " is : {n_null_5}\n')
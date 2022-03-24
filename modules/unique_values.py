# Show unique values from each column that have less than 20 unique values
def unique_values(data):
    for col in data.columns:
        temp = data[col]
        n_unique = temp.nunique()

        if n_unique < 20:
            print(f'=========== Unique values of {col} column ===========\n')
            for unique in temp.unique():
                print(unique)
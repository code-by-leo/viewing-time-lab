def clean_data(data):
    """
    TODO: Implement your "clean_heartrate_data" function from TLAB #1 & #2
    within this module. Note that this code will be *slightly* different
    from your original function.

    we need to skip the 1st row aka the 0th 
    """
    clean_data = []
    for row in data:
        #skip the 0th line
        if row != "minutes\n":
            #why name the type? | Append to the clean_data list as a float
            clean_data.append(float(row.strip()))
            #return clean data to use where you call the function
    return clean_data
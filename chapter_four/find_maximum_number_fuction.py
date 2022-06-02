def maximum(value1, value2, value3):
    """to find the maximum_value"""
    max_value = value1
    if value2 > max_value:
        max_value = value2
    if value3 > max_value:
        max_value = value3
    return max_value


print(maximum(6,89,14))

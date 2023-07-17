def find_max_value(data: dict):
    """
    Return the maximum int or float value in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The maximum value in the dictionary.
    """
    keys= []
    for i in data.values():
        if type(i) == int:
            keys.append(i)
        
    max = keys[0]
    for mx in keys:
        if max < mx:
            max = mx
    return max
data  = {
    'a' : 4, 
    'b' : -10, 
    'c' : 0
  }
print(find_max_value(data))
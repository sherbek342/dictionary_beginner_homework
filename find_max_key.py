def find_max_key(data: dict):
    """
    Return the maximum int or float key in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The maximum key in the dictionary.
    """
    
    keys= []
    for i in data:
        if type(i)==int or type(i)==float:
            keys.append(i)
        max = keys[0]
        for mx in keys:
            if max < mx:
                max = mx
    return max

data = {
    1.4 :'a', 
    7.8 :'b', 
    8.4 : 'c'
  }
print(find_max_key(data))
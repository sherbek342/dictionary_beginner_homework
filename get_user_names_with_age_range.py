def get_user_names_with_age_range(data:list, min_age:int, max_age:int) -> list:
    """
    Return a list of users with a given age range

    Args:
        data (dict): A dictionary of values
        min_age (int): The minimum age to search for
        max_age (int): The maximum age to search for
    Returns:
        list: A list of users with the given age range
    """
    keys= []
    names =[]
    for i in data:
        if type(i['age']) == int:
            keys.append(i['age'])
            names.append(i['name'])
        
    min = keys[0]
    for mx in keys:
        if min > mx:
            min = mx
    return names[keys.index(min)]


data = [
  {
    'name': 'John', 
    'age': 20
  }, 
  {
    'name': 'Mary', 
    'age': 17
  },
  {
    'name': 'Ban', 
    'age': 23
  },
  {
    'name': 'John', 
    'age': 27
  }
]
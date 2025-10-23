'Melissa Kushner'
'Date Created:10/14/2025'
'Last Modified: 10/31/2025'
'Python Version 1.0'
'Description: Takes your postage data and prints the cost'
def get_data():
    '''
    Gets the length, height, thickness, startzip and enzip of the user 
    Args:
        None
    Returns:
        length (float)
        height (float)
        thickness  (float)
        startzip (int)
        endzip (int)
     '''  
    data = input("Enter your postage data in order of length, height, thickness, starzip and endzip:  ")  
    data = data.split(',')
    return float(data[0]), float(data[1]), float(data[2]), int(data[3]), int(data[4])
   
def get_type (length, height, thickness):
    '''
    Gets Postage type 
    Args:
        length (float): The length of there postage
        height (float): The height of there postage
        thickness (float): The thickness of there postage
    Returns:
        post_type (str)
    '''  
    if 3.5 <= length <= 4.25 and 3.5 <= height <= 6 and .007 <= thickness <= .016:
        return "Regular Post Card" 
    elif 4.25 < length < 6 and  6 < height < 11.5 and .007 <= thickness <=.015:
        return "Large Post Card"
    elif 3.5 <= length <= 6.125 and  5 <= height <= 11.5 and .016 < thickness <.25:
        return "Envelope"
    elif 6.125 < length < 24 and  11 <= height <= 18 and .25 <= thickness <= .5:
        return "Large Envelope"
    elif 2*(length + height + thickness) <= 84:
        return "Package"
    elif 84 < 2*(length + height + thickness) <= 130:
        return "Large Package"
    else:
        return "Unmailable"

def get_zone(zipcode):
   '''
    Gets zipcode
    Args:
        zipcode(int): The zipcode of there postage
    Returns:
       zone (int)
    '''  
   if 1<=zipcode<=6999:
      return 1
   elif 7000<=zipcode<=19999:
      return 2
   elif 20000<=zipcode<=35999:
      return 3
   elif 36000<=zipcode<=62999:
      return 4
   elif 63000<=zipcode<=84999:
      return 5
   elif 85000<=zipcode<=99999:
      return 6
   else:
      return -1
    
def get_distance(startzip, endzip):
    '''
    Gets the distance between startzip and endzip 
    Args:
         startzip(int): The startzip of there zipcode 
         endzip(int): The endzip of there zipcode
    Returns:
        distance (int)
    '''     
    startzone = get_zone(startzip)
    endzone = get_zone(endzip)
    return abs(endzone - startzone)

def get_cost(post_type, distance):
   '''
   Gets cost of the postage type
   Args:
        post_type(int) 
        distance(int)
    Returns:
        cost(float)
   '''
   if post_type == 'Unmailable' or distance == -1:
      return 'Unmailable'
   if post_type == 'Regular Post Card':
        return .20 + .03*distance  
   elif post_type == 'Large Post Card':
        return .37 + .03*distance  
   elif post_type == 'Envelope':
        return .37 + .04*distance  
   elif post_type == 'Large Envelope':
        return .60 + .05*distance  
   elif post_type == 'Package':
        return 2.95 + .25*distance  
   elif post_type == 'Large Package':
        return 3.95 + .35*distance  




def main():
    '''
    Print the answer 
    Args:

    Returns
    Cost(float)
    '''

    length, height, thickness, startzip, endzip = get_data()
    post_type = get_type(length, height, thickness)
    distance = get_distance(startzip, endzip)
    cost = get_cost(post_type, distance)
    cost = f"{cost:.2f}"
    cost = cost.lstrip('0')
    print(cost)
main()
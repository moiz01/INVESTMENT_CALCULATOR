""" This module will have function to calculate lumpsum return
    Auther: Moiz
    Date: 8-Jul-2024
"""
def returns(
        principal,
        interest_rate,
        time_in_years,
        n=1):
    """ This function calculate lumpsum and return
    Arg:
        principal: Present value
        interest_rate: Rate of return
        time_in_years: Duration of investment
        n: Number of compounded interests in a year
    Return:
        Estimated return
    """
    result=principal*(1+(interest_rate/100)/n)**(n*time_in_years)


    
    formatted_number = "{:,}".format(round(result))
    formatted_number = formatted_number.replace(',', ',', 1)  # Replace the first ',' to ',' format 
    formatted_number = formatted_number.replace(',', ',')  
    

    return formatted_number
    
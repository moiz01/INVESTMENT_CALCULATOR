"""This function calculate the sip
"""
def sip(principal,interest_rate,time_in_years):
    i=(interest_rate*0.01)/12
    n=time_in_years*12
    num=principal*(((1+i)**n)-1)*(1+i)
    den=i
    
    return round(num/den)
#print(sip(total_investment_amount=25000,anual_rate=10,years_of_investment=5))
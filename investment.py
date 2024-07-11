import sys
import argparse
from calculator.lumpsum import lumpsum
def argument_parser():
    parser=argparse.ArgumentParser(description="investment calculator")
    parser.add_argument('lumpsum',type=str,help='present value of investment')
    parser.add_argument('total_investment',type=int,help='present value of investment')
    parser.add_argument('intrest_rate',type=int,help='rate of interes')
    parser.add_argument('time_in_years',type=int,help='time in years')
    return parser
    

# def main(arguments):
#     principal=int(arguments[0])
#     interest_rate=int(arguments[1])
#     time_in_years=int(arguments[2])
#     print(round(lumpsum(principal,interest_rate,time_in_years,n=1)))
    
#     # total_value=principal*(1+(interest_rate/100))**time_in_years
#     # print(round(total_value))

if __name__=="__main__":
    # main(sys.argv[1::])
   args= argument_parser().parse_args()
#    print(args)
result=lumpsum(principal=args.total_investment,interest_rate=args.intrest_rate,time_in_years=args.time_in_years)
print(f"Investesment amount:{args.total_investment}\nYears: {args.time_in_years}\nRate of Interest: {args.intrest_rate}% \nReturn: {round(result)} " )
import sys
import argparse
from calculator.lumpsum import returns as lumpsum_returns
from calculator.sip import returns as sip_returns
def argument_parser():
    parser=argparse.ArgumentParser(description="investment calculator")
    parser.add_argument('investment_type',type=str,choices=['lumpsum','sip'],help='present value of investment')
    # parser.add_argument('total_investment',type=int,help='present value of investment')
    # parser.add_argument('intrest_rate',type=int,help='rate of interes')
    # parser.add_argument('time_in_years',type=int,help='time in years')
    parser.add_argument('-p','--principal',type=int,required=True,help='present value of investment')
    parser.add_argument('-r','--rate',type=int,required=True,help='rate of interest')
    parser.add_argument('-t','--time',type=int,required=True,help='time in years')
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
   if args.investment_type=='lumpsum':
       result=lumpsum_returns(principal=args.principal,interest_rate=args.rate,time_in_years=args.time)
       print(f"Investment amount:{args.principal}\nYears: {args.time}\nRate of Interest: {args.rate}% \nReturn: {result} " )
   elif args.investment_type=='sip':
       result=sip_returns(principal=args.principal,interest_rate=args.rate,time_in_years=args.time)
       print(f"Investment amount:{args.principal}\nYears: {args.time}\nRate of Interest: {args.rate}% \nReturn: {result} " )
          
#    print(args)
# result=lumpsum(principal=args.total_investment,interest_rate=args.intrest_rate,time_in_years=args.time_in_years)
# print(f"Investesment amount:{args.total_investment}\nYears: {args.time_in_years}\nRate of Interest: {args.intrest_rate}% \nReturn: {round(result)} " )
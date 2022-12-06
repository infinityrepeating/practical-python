# pcost.py
#
# Exercise 1.27

import sys
import csv

def portfolio_cost(filename):
    final_cost = 0.0
    
    with open(filename, "rt") as file:
        rows = csv.reader(file)
        headers = next(file)
        
        for row in rows:
            try:
                nshares, price = int(row[1]), float(row[2])
                final_cost += nshares*price
                print(f"Total cost for {row[0]}: {round(nshares*price, 1)}")
                
            # this catches error in int() and float() conversions
            except ValueError:
                print(f"Bad row: {row[0]}")

    print(f"\nFinal cost: {final_cost}")

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

portfolio_cost(filename)
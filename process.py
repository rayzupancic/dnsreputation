######################################
# name: process.py 
# purpose: process the DNS debug logs to find the age and reputation of queried domains
# author: rayz
# Last Modified:
# 070616: created
#
######################################

import re


#####################################
# name: main
# purpose: main routine
#####################################
def main():

    filename = '/home/rzupancic/winlog/dns/queries.log'

    with open(filename) as fd:
        for line in fd:
            fields = line.split()
            if len(fields) == 16:
                print len(fields) 
                mdy= fields[0]
                time = fields[1]
		domainRaw = fields[15]
                # take out the leading and trailing character count
		domainRaw= re.sub(r'^\(\d+\)','',domainRaw)
                # ^ beginning of line, \( escape the paren, \d+ one or more digits
		domainRaw= re.sub(r'\(\d+\)$','',domainRaw)
                # take out the middle character count
		domain	= re.sub(r'\(\d+\)','.',domainRaw)
                print domain
		
            

               



if __name__ == "__main__":
   main()

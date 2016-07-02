############################################################
# name: domainage.py
# purpose; determine information regarding a domain
#
# author: rayz
# Last Modified: 20160701
############################################################

import sys
import os
import getopt
import whois
import logging

##############
#  name: usage()
#  purpose: print usage information
##############
def usage():
   logging.info( "usage: domainage -a <domain-name>")



#############################
# name: initialize_logger(outputDir)
# input: outputDir str
# output: na
# purpose: a generic routine handle logging streams
#############################
def initialize_logger(logDir):
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # create console handler and set level to info
    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter("%(levelname)s - %(message)s")
    logger.addHandler(handler)

    # create error file handler and set level to error
    handler = logging.FileHandler(os.path.join(logDir, "error.log"),"w", encoding=None, delay="true"
)
    handler.setLevel(logging.ERROR)
    formatter = logging.Formatter("%(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # create debug file handler and set level to debug
    handler = logging.FileHandler(os.path.join(logDir, "all.log"),"w")
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)

####################
#  name: main()
#  purpose: main routine
##############
def is_domain_new(wi):
    now = datetime.datetime.now()
    thresholdDate = now - datetime.timedelta(days=60)
    


####################
#  name: main()
#  purpose: main routine
##############
def main():
    # logging dir
    logDir = os.path.join('.','log')
    initialize_logger(logDir)

    logging.debug( sys.argv)
    logging.debug( "length: " + str( len(sys.argv)))
    if len(sys.argv) < 2 :
        usage()
        sys.exit(1)



    try:
        opts, args = getopt.getopt(sys.argv[1:],"a:h")
    except getopt.GetoptError:
        logging.info( "domainage.py -a <domainname>")
        sys.exit(2)

    for opt,arg in opts:
        logging.debug( "opt: " + opt + " arg =" + arg)
        if opt == "-h":
            usage()
            sys.exit(2)
        if opt == "-a":
            logging.debug(arg)
            domain = arg
            domainInfo = whois.whois(arg)

    logging.info( "domain is: " + domain)

    # use whois info to find domain creation date
    w whois.whois(domain)

    # use datetime to return a threshold decision
    if is_domain_new(w.creation_date)

if __name__ == "__main__":
    main()

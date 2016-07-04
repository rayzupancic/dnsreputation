############################################################
# name: domainage.py
# purpose; determine whether the creation date of a domain
# is less than X days old
#
# author: rayz
# Last Modified: 20160702
############################################################

import sys
import os
import getopt
import whois
import logging
import datetime

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
# name: is_domain_new(dt)
# purpose: calculate the age of a domain creation relative
#           to threshold
# input: datetime object
# output boolean
##############
def is_domain_new(dt):
    now = datetime.datetime.now()
    thresholdDate = now - datetime.timedelta(days=60)
    if  thresholdDate < dt :
        status = True
    else:
        status = False
    return status 

####################
# name: log_domain(dom, dt)
# purpose: put domains under threshold in a log file for parsing by Splunk
# input: dom string, dt datetime object, filen str file name
# output na
##############
def log_domain(dom, dt, filen):
    fd = open(filen,'a')
    # get the current time and date
    now = datetime.datetime.now()

    fd.write(str(now) + ': ' + dom + ',' +  dt + '\n')
    fd.close

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

    # how old should a domain be
    thresholdAge = 60

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

    logging.info( "domain entered: " + domain)

    # use whois info to find domain creation date
    domainInfo = whois.whois(domain)

    # use datetime to return a threshold decision
    if is_domain_new(domainInfo.creation_date[0]):
        domLogFile = os.path.join(logDir, "newdomains.log")
        log_domain(domain, str(domainInfo.creation_date[0]), domLogFile)

if __name__ == "__main__":
    main()

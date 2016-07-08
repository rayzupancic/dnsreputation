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
import initlogger as il

##############
#  name: usage()
#  purpose: print usage information
##############
def usage():
   logging.info( "usage: domainage -a <domain-name>")


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

    # get the process name and create a dir for logging
    proc = sys.argv[0]
    procName = proc.split('.')
    # set up logging path
    logDir = os.path.join('./log',procName[0])
    # create logdir if it doesn't exist
    if not os.path.exists(logDir):
        os.makedirs(logDir)
    il.initialize_logger(logDir)

    #logging.debug( sys.argv)
    #logging.debug( "length: " + str( len(sys.argv)))
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

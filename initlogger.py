############################################################
# name: initlog.py
# purpose: setup logging
#
# author: rayz - adapted from various routines found on Internet
# Last Modified: 20160707
############################################################

import os
import logging


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


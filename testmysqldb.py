###########################################
# name: testmysqldb.py
# purpose: test out odbc connectivity
# author: rayz
#
#########################

import MySQLdb
import time

#########################
# name: insert_values_to_db()
# input: str, oldaddress, str, newaddress, float lat, float lng
# output na
# purpose: connect to SQLServer and insert values
#
#########################
def insert_values_to_db(dom, date ):

    print date
    # build the connect string
    db = MySQLdb.connect("localhost","domainlookup","domainlookup","domainlookup" )
    #print connStr

    # get the connection

    cursor = db.cursor()

    # SQL query to INSERT a record into the database.
    sql = """INSERT INTO domains_tbl(domain_name, domain_create_date) VALUES(%s,%s)"""

    try:
        cursor.execute(sql,(dom, date,)) 
        db.commit()
    except Exception, e:
      
        print "rolling back: "  + repr(e)
        db.rollback()


    db.close()
    return()

#########################
# name: get_values_from_db()
# input: str, oldaddress
# output na
# purpose: connect to SQLServer and retrieve values
#
#########################
def get_values_from_db(domain):


    # get the connection and cursor
    db = MySQLdb.connect("localhost","domainlookup","domainlookup","domainlookup" )
    cursor = db.cursor()

    # build the SQL Query
    sql = "SELECT * FROM domain_tbl WHERE domain = %s " 
    try:
       for row in cursor.execute(sql,domain):
           print row
    except: 
       print "error in db"
    # close it off
    db.close()

    return row


#################
def main():

    domain = "google.com"
    dt = time.strptime('07/21/1997','%m/%d/%Y')
    insert_values_to_db(domain, time.strftime('%Y-%m-%d',dt))
    #insert_values_to_db(domain, dt)
    #get_values_from_db(addressStr)



if  __name__ == "__main__":
    main()

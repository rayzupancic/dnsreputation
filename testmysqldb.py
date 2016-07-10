###########################################
# name: testmysqldb.py
# purpose: test out odbc connectivity
# author: rayz
#
#########################

import MySQLdb

#########################
# name: insert_values_to_db()
# input: str, oldaddress, str, newaddress, float lat, float lng
# output na
# purpose: connect to SQLServer and insert values
#
#########################
def insert_values_to_db( oldAddress,newAddress, lat, lng):
    # build the connect string
    connStr = 'Driver={SQL Server};Server=sqlserver;Database=geocoding;uid=sa;pwd=rayzrayz'
    #print connStr

    # get the connection
    connection = pyodbc.connect(connStr)
    connection.autocommit = False

    cursor = connection.cursor()

    # build the SQL Query
    SQL = """
    INSERT INTO geocoding(cobra_old_address, cobra_cleaned_address, cobra_latitude, cobra_longitude)
  VALUES (?,?,?,?)
    """
    try:
        cursor.execute(SQL,oldAddress, newAddress,lat,lng)
        connection.commit()
    except pyodbc.IntegrityError:
        print('row exists:' + newAddress)


    cursor.close()
    del cursor
    connection.close()
    return()

#########################
# name: get_values_from_db()
# input: str, oldaddress
# output na
# purpose: connect to SQLServer and retrieve values
#
#########################
def get_values_from_db(oldAddress):

    # build the connect string
    connStr = 'Driver={SQL Server};Server=sqlserver;Database=geocoding;uid=sa;pwd=rayzrayz'
    #print connStr

    # get the connection and cursor
    db = MySQLdb.connect("localhost","domainlookup","domainlookup","domainlookup" )
    cursor = db.cursor()

    # build the SQL Query
    SQL = "SELECT * FROM domain_tbl WHERE domain = ? "
    try:
       for row in cursor.execute(SQL,oldAddress):
           print row
           print row
    except pyodbc.Error, err:
        print err

    # close it off
    cursor.close()
    del cursor
    connection.close()

    return row


#################
def main():

    cleanedAddressStr = '3901 S. Sherman St, Englewood CO'
    addressStr = '3901 S. Sherman St. Englewood, Co 80113'
    insert_values_to_db(addressStr, cleanedAddressStr, lat, lng)
    #get_values_from_db(addressStr)



if  __name__ == "__main__":
    main()

# Add data bases corresponding to the query here. Each query can run on a different data base 
# Key - Query identifier from the queries dictionary. Value is the database identifier
# Database properties (host, database name, user, pw, port etc. are defined in the configuraiton file)
#databases = {
#           'count_date_range': 'salesdb',
#           'item_date_range': 'salesdb',
#           'item_count_date_range': 'salesdb',
#           'item_count': 'salesdb',
#           'inventory_count': 'inventorydb'
#          }
# Add new queries to the dictionary. Query Name is unique and query needs to be evaluated for syntax 
# and correctness before adding to the dictionary 
# Queries are templatized where ever needed / possible
#queries = { 
#           'count_date_range': "select count(*) from orders where orderDate between %(fromDate)s AND %(toDate)s", 
#           'item_date_range': "select * from orders where itemType=%(itemType)s AND orderDate between %(fromDate)s AND %(toDate)s",
#           'item_count_date_range': "select itemType, count(*) from orders where orderDate between %(fromDate)s AND %(toDate)s group by itemType",
#           'item_count': "select itemType, count(*) from orders group by itemType",
#           'inventory_count': "select itemType, count(*) from inventory group by itemType"
#        }

# Class to provide an abstaction for templatized queries. Queries are added during initialization. 
# TODO: Load queries from a file instead of initializing them here

class sqlqueries:

    __queries = { 
        'item': "select * from orders where itemType=%(itemType)s AND orderDate between %(fromDate)s AND %(toDate)s",
        'item_male': "select * from orders where itemType=%(itemType)s AND gender='Male' AND orderDate between %(fromDate)s AND %(toDate)s",
        'item_female': "select * from orders where itemType=%(itemType)s AND gender='female' AND orderDate between %(fromDate)s AND %(toDate)s",
        'item_count': "select itemType, count(*) from orders where orderDate between %(fromDate)s AND %(toDate)s group by itemType",
        'item_count_male': "select itemType, count(*) from orders where gender='Male' AND orderDate between %(fromDate)s AND %(toDate)s group by itemType",
        'item_count_female': "select itemType, count(*) from orders where gender='Female' AND orderDate between %(fromDate)s AND %(toDate)s group by itemType",
        'inventory_count': "select itemType, count(*) from inventory group by itemType"
    }

    def __init__(self):
        pass
       
    def addquery(self, qname, query):
        if qname is not None and query is not None: 
            #TODO: check for duplicate before adding
            self.__queries.add(qname, query)

    def deletequery(self, qname):
        if qname is not None:
           if qname in self.__queries:
               self.__queries.delete(qname) 

    def getquery(self, qname):
        if qname is not None and qname in self.__queries:
            return self.__queries[qname]
        else:
            return None
    

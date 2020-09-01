from mysql.connector import Error
from parse.parseargs import parse_cli_args
from dbdao.mysqldb import mysqldb
from dbdao.sqlqueries import sqlqueries

def execute_query(args):

    queries = sqlqueries()

    query = queries.getquery(args.queryname)

    if query is not None:
       print(query)
    else:
       print("Query Name provided does not exist in the list: %s" % args.queryname)
       return;

    param_dict = { "itemType": args.itemtype,
                   "fromDate": args.startdate,
                   "toDate":  args.enddate}

    db = None

    try:
        db = mysqldb()
        db.execute(query, param_dict)

        # passing query name to create output file with query name extension
        db.fetchrows(args.queryname)
	
    except Error as e:
        print(e)

    finally:
        if db is not None:
            db.close();

if __name__ == '__main__':
    args = parse_cli_args()

    execute_query(args) 

# Credit to users confused00 and bsa on stack exchange for this bit of code 

import redis, csv, json, sys


redis_host = "localhost"
redis_port = 6379
redis_password = ""

def read_csv_data(csv_file, ik, iv):
    with open(csv_file, encoding='utf-8') as csvf:
        csv_data = csv.reader(csvf)
        return [(r[ik], r[iv]) for r in csv_data]

def store_data(conn, data):
    for i in data:
        conn.setnx(i[0], i[1])
    return data

def main():
    if len(sys.argv) < 2:
        sys.exit(
            "Usage: %s file.csv [key_column_index, value_column_index], where key_column_index and value_column_index are zero-based ints (0,1,2,3) for first second third csv column etc.."
            % __file__
        )
    columns = (0, 1) if len(sys.argv) < 4 else (int(x) for x in sys.argv[2:4])
    data = read_csv_data(sys.argv[1], *columns)
    conn = redis.Redis(redis_host)
    print (json.dumps(store_data(conn, data)))

if '__main__' == __name__:
    main()

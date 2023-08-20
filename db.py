UNI_DB_USERNAME = "db_reader"
UNI_DB_PASSWORD = "reader_pass"
UNI_DB_HOST = "nc13.jinr.ru"
UNI_DB_NAME = "bmn_db"

requested_period = 7
requested_run = 2076

import psycopg2
import subprocess

if __name__ == "__main__":
    try:
        conn = psycopg2.connect(user=UNI_DB_USERNAME, password=UNI_DB_PASSWORD, host=UNI_DB_HOST, database=UNI_DB_NAME)
        print(conn)
        cursor = conn.cursor()
        cursor.execute(f"SELECT geometry_id FROM run_ WHERE period_number={requested_period} AND run_number={requested_run}")
        record = cursor.fetchone()
        geometry_id = record[0]
        print(f"geometry_id = {geometry_id}")
        cursor.execute(f"SELECT root_geometry FROM run_geometry WHERE geometry_id={geometry_id}")
        record = cursor.fetchone()
        print(record)
        filename = f"geometry_{requested_period}_{requested_run}.root"
        with open(filename, "wb") as f:
            f.write(record[0]) 
    finally:
        conn.close()
        cursor.close()

    print(filename)

    shell = subprocess.Popen(["/bin/bash"], 
                        shell=False,
                        stdin =subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        universal_newlines=True,
                        bufsize=0)
    r = shell.communicate(
         "cd /scratch1/pklimai/bmnroot/build/ \n"+
         ". config.sh \n" + 
         "cd /scratch1/pklimai/visapi \n" + 
         "root get_geometry_json.C"
         )
    print(r[0])
        


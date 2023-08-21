import psycopg2
import subprocess

UNI_DB_USERNAME = "db_reader"
UNI_DB_PASSWORD = "reader_pass"
UNI_DB_HOST = "nc13.jinr.ru"
UNI_DB_NAME = "bmn_db"

def get_geometry_json(requested_period, requested_run):
    try:
        conn = psycopg2.connect(user=UNI_DB_USERNAME, password=UNI_DB_PASSWORD, host=UNI_DB_HOST, database=UNI_DB_NAME)
        # print(conn)
        cursor = conn.cursor()
        cursor.execute(f"SELECT geometry_id FROM run_ WHERE period_number={requested_period} AND run_number={requested_run}")
        record = cursor.fetchone()
        geometry_id = record[0]
        # print(f"geometry_id = {geometry_id}")
        cursor.execute(f"SELECT root_geometry FROM run_geometry WHERE geometry_id={geometry_id}")
        record = cursor.fetchone()
        # print(record)
        filename = f"geometry_{requested_period}_{requested_run}.root"
        with open(filename, "wb") as f:
            f.write(record[0]) 
    finally:
        conn.close()
        cursor.close()

    # print(filename)

    shell = subprocess.Popen(["/bin/bash"], 
                        shell=False,
                        stdin =subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        universal_newlines=True,
                        bufsize=0)
    output = shell.communicate(
         "cd /scratch1/pklimai/bmnroot/build/ \n"+
         ". config.sh \n" + 
         "cd /scratch1/pklimai/visapi \n" + 
         f"""root 'get_geometry_json.C({requested_period}, {requested_run}, "{filename}")'"""
         )
    return "\n".join(output[0].splitlines()[15:])
        

if __name__ == "__main__":
    print(get_geometry_json(7, 2076))


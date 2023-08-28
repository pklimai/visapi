import psycopg2
import subprocess

from config import *

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
        # TODO - temp directory must be configurable
        filename = f"geometries/geometry_{requested_period}_{requested_run}.root"
        # print(filename)
        with open(filename, "wb") as f:
            f.write(record[0]) 
    except Exception as e:
        return f'{{"error": "{str(e)}"}}'
    finally:
        conn.close()
        cursor.close()

    shell = subprocess.Popen(["/bin/bash"], shell=False,
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            universal_newlines=True, bufsize=0)
    output = shell.communicate(
         f"""source {SOURCE_FILE_1} \n
             source {SOURCE_FILE_2} \n
             root 'get_geometry_json.C({requested_period}, {requested_run}, "{filename}")' \n
         """)
    return "\n".join(output[0].splitlines()[17:])


def get_event_json(event_idx: int):
    shell = subprocess.Popen(["/bin/bash"], shell=False,
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            universal_newlines=True, bufsize=0)
    output = shell.communicate(
         f"""source {SOURCE_FILE_1} \n
             source {SOURCE_FILE_2} \n
             root 'get_event_json.C("{EVENTS_FILENAME}", {event_idx})' \n
         """)
    return "\n".join(output[0].splitlines()[19:-1])



if __name__ == "__main__":
    # Testing ROOT communication:
    #print(get_geometry_json(7, 2076))
    #print(get_geometry_json(8, 8000))
    print(get_event_json(3))

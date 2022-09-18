import time
import psycopg2
from psycopg2.extras import RealDictCursor
#from config import settings
from rich.console import Console

console = Console()

while True:
    try:
        conn = psycopg2.connect(
            database="db",
            user="postgres",
            password="KiipX5dq"
        )
        cr = conn.cursor()
        break
    except psycopg2.DatabaseError:
        console.print("[bold red]FAILED : Connection To Database Failed")
        print("Trying Again...")
        time.sleep(3)

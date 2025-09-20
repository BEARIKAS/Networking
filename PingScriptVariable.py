import sys
import subprocess
from concurrent.futures import ThreadPoolExecutor

def load_hosts(filename):
    "Load hosts from a text file (one host/IP per line)."
    with open(filename) as f:
        return [line.strip() for line in f if line.strip()]

def ping_host(host):
    "Ping a single host using subprocess."
    try:
        result = subprocess.run(
            ["ping", "-n", "1", host],  
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        if result.returncode == 0:
            return f"[UP]   {host} is reachable"
        else:
            return f"[DOWN] {host} is not reachable"
    except Exception as e:
        return f"[ERROR] Could not check {host}: {e}"

if __name__ == "__main__":
    args = sys.argv[1:]

    # Case 1: no args → use defaults
    if not args:
        hosts = ["8.8.8.8", "1.1.1.1"]

    # Case 2: single argument ending with .txt → treat as file
    elif len(args) == 1 and args[0].endswith(".txt"):
        hosts = load_hosts(args[0])

    # Case 3: otherwise → treat args as host list
    else:
        hosts = args

    # Running pings concurrently
    with ThreadPoolExecutor(max_workers=10) as executor:
        results = executor.map(ping_host, hosts)

    for res in results:
        print(res)
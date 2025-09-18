import subprocess

# List of IPs to ping
hosts = [
    "8.8.8.8",   # Google DNS
    "1.1.1.1",   # Cloudflare DNS
]

for host in hosts:
    try:
        
        output = subprocess.run(
            ["ping", "-n", "1", host],  # 1 echo request
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        
        if output.returncode == 0:
            print(f"[UP]   {host} is reachable")
        else:
            print(f"[DOWN] {host} is not reachable")

    except Exception as e:
        print(f"[ERROR] Could not check {host}: {e}")
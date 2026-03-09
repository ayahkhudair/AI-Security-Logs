import random
import datetime
import pandas as pd

"""
This script generates 2,000 simulated server logs.
It includes normal traffic and a fake hacker attack pattern:
- Hacker IP: 192.168.1.99
- Attack time: Night hours (00:00 - 04:00)
- Attack method: POST
- Attack size: 5,000 to 20,000 bytes
"""

NUM_LOGS = 2000
HACKER_IP = "192.168.1.99"
NORMAL_IP_RANGE = 50  # Simulated IPs: 192.168.1.1 - 192.168.1.50
logs = []

for _ in range(NUM_LOGS):
    hour = random.randint(0, 23) # Random hour of the day
    
    # Normal traffic defaults
    ip = f"192.168.1.{random.randint(1, NORMAL_IP_RANGE)}"
    status = 200
    method = "GET"
    size = random.randint(200, 800)
    
    # Simulate hacker attack during night hours
    if 0 <= hour <= 4 and random.random() < 0.4:
        ip = HACKER_IP
        status = random.choice([401, 403])
        method = "POST"
        size = random.randint(5000, 20000)
    
    # Generate timestamp for log
    timestamp = datetime.datetime.now().replace(hour=hour, minute=0, second=0).strftime("%Y-%m-%d %H:%M:%S")

    logs.append([timestamp, ip, method, status, size])

# Convert to DataFrame and save as CSV (no headers, to mimic server logs)
df = pd.DataFrame(logs, columns=['timestamp', 'ip', 'method', 'status', 'size'])
df.to_csv('server_logs.txt', index=False, header=False)

print(f"Success! {NUM_LOGS} server logs generated.")
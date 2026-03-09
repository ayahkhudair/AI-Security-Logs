import pandas as pd
import plotly.express as px
from sklearn.ensemble import IsolationForest

# 1.Load Server Logs
df = pd.read_csv('server_logs.txt', names=['timestamp', 'ip', 'method', 'status', 'size'])
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Extract useful features
df['hour'] = df['timestamp'].dt.hour
df['method_code'] = df['method'].map({'GET': 0, 'POST': 1}).fillna(2)

# 2.Detect anomalies using Isolation Forest
model = IsolationForest(contamination=0.05, random_state=42)
df['anomaly_score'] = model.fit_predict(df[['status', 'method_code', 'size', 'hour']])

# Filter only anomalies
anomalies = df[df['anomaly_score'] == -1].copy()

# 3.Categorize risk levels based on features
def get_risk(row):
    """
    Assigns a risk level based on log features:
    - HIGH: Large data transfer (possible data theft)
    - MEDIUM: Failed access attempts (possible brute force)
    - LOW: Other suspicious activity
    """
    if row['size'] > 15000:
        return "HIGH (Data Theft)"
    if row['status'] == 401:
        return "MEDIUM (Brute Force)"
    return "LOW (Suspicious)"

anomalies['risk_level'] = anomalies.apply(get_risk, axis=1)

# 4.Interactive Dashboard
print(f"--- SECURITY BREACH REPORT ---\nFound {len(anomalies)} potential threats.")

fig = px.scatter(
    anomalies,
    x="timestamp",
    y="size",
    color="risk_level",
    hover_data=['ip', 'status'],
    title="AI Security Dashboard"
)
fig.show()
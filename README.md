# AI-Security-Logs

<h2>📖 Overview</h2>
<p>
  This project is an unsupervised machine learning tool designed to detect cybersecurity anomalies in server logs. It uses the <b>Isolation Forest</b> algorithm to identify suspicious patterns, such as brute-force attempts and data exfiltration, that traditional systems might miss.
</p>



<h2>🚀 Key Features</h2>
<ul>
  <li><b>Synthetic Log Generation:</b> Simulates 2,000 lines of realistic server traffic, including sophisticated "Night-time" attack patterns (00:00 - 04:00).</li>
  <li><b>AI Anomaly Detection:</b> Implements <code>Scikit-Learn</code> to score and isolate threats based on status codes, request methods, payload sizes, and time-of-day.</li>
  <li><b>Interactive Dashboards:</b> Features a dynamic scatter plot built with <code>Plotly</code> for real-time time-series analysis.</li>
  <li><b>Risk Categorization:</b> Automatically labels detected threats as <b>High, Medium, or Low risk</b> for prioritized incident response.</li>
</ul>



<h2>🛠️ Tech Stack</h2>
<table>
  <tr>
    <td><b>Language</b></td>
    <td>Python 3.14.3</td>
  </tr>
  <tr>
    <td><b>Data Science</b></td>
    <td>Pandas, Scikit-Learn</td>
  </tr>
  <tr>
    <td><b>Visualization</b></td>
    <td>Plotly Express</td>
  </tr>
  <tr>
    <td><b>Version Control</b></td>
    <td>Git/GitHub</td>
  </tr>
</table>

<h2>💻 How to Run</h2>
<pre>
<code>
# 1. Install dependencies
pip install pandas scikit-learn plotly

# 2. Generate logs
python generator.py

# 3. Launch the AI Detector
python detector.py
</code>
</pre>

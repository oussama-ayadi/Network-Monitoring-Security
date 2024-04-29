import pandas as pd
from jinja2 import Template

# Load CSV data or generate data
data = {
    'severity': 'Critical',
    'incident_id': 'IR001',
    'datetime': '2024-04-25 15:30:00',
    'incident_type': 'Network Anomaly',
    'incident_description': 'Anomaly detected in network traffic.',
    'customers_impacted': 'Customer A, Customer B',
    'root_cause': 'Packet loss due to network congestion',
    'recovery_actions': 'Implemented QoS policies, optimized network routing.',
    'techniques_and_tools': 'Network monitoring tools, configuration management.',
    'pcapng_file': 'incident_capture.pcapng'
}

# Read the Jinja2 template file
with open('incident_response_template.html', 'r') as f:
    template_content = f.read()

# Create a Jinja2 template
template = Template(template_content)

# Render the template with data
rendered_html = template.render(data=data)

# Save the rendered HTML to a file
with open('incident_response_report.html', 'w') as f:
    f.write(rendered_html)

print("HTML report generated successfully.")

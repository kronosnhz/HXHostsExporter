import requests, json, csv, urllib3
from msvcrt import getch
urllib3.disable_warnings()

hx_host = "https://[YOUR HX ADDRESS]"
hx_port = "[HX PORT]"
username = "[YOUR USERNAME]"
password = "[YOUR PASSWORD]"
API_BASE_ROUTE = "/hx/api/v3"

csv_headers =["Hostname", "IP Address", "OS", "Agent Version"]

url = hx_host + ":" + str(hx_port)
url = url + API_BASE_ROUTE + "/hosts"

print("Connecting with Fireeye Endpoint Security...")
print("HOST: " + hx_host + " PORT: " + hx_port)

try:
    response = requests.get(url, params = {"limit":"10000"}, auth = (username, password), verify=False)
    print("Downloading hosts...")
except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')
else:
    hosts = response.json()['data']['entries']
    print("Writing CSV...")
    with open('hx_all_hosts.csv', 'w', newline='') as hosts_file:
        csv_writer = csv.writer(hosts_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        
        line_count = 0
        for host in hosts:
            if line_count == 0:
                # Header column
                csv_writer.writerow(csv_headers)
                line_count +=1
            else:
                # Attributes to find
                rowValues = [
                    host['hostname'],
                    host['primary_ip_address'],
                    host['os']['product_name'],
                    host['agent_version']
                    ]

                # Write host row
                csv_writer.writerow(rowValues)
                
                line_count +=1

        print(f'Printed {line_count} lines.')
    print('Success!')
print('Press any key to exit...')
getch()
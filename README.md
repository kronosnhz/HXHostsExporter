# Fireeye Hosts Extractor
 Extract programatically all hosts in Fireeye Endpoint Security Platform.

## Prerequisites
* Python 3 [Official Download](https://www.python.org/downloads/)
* Requests Python Library with `pip3 install requests`

## How to run
1. Set `hx_host `, `hx_port`, `username` and `password` variable values in the script 
1. Execute `py HXHostsExctractor.py` in a shell

The script will create a new CSV file named `hx_all_hosts.csv` with all hosts in the platform.

## Downloaded fields
The script will download these fields per host: `hostname`, `primary_ip_address`, `os` and `agent_version` but It can be customized to extract any other just adding them in the `rowValues` variable.
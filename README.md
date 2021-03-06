# Fireeye Hosts Extractor
 Extract programatically all hosts in Fireeye Endpoint Security Platform.

## Prerequisites
* Install Python 3 [Official Download](https://www.python.org/downloads/) (uncheck Install for all users to not require Administrator rights)
* Install `Requests Python Library` executing `py -m pip install requests` in your shell (I recommend PowerShell in Windows)

## How to run
1. Open with a text editor the script `HXHostsExtractor.py` and set `hx_host `, `hx_port`, `username` and `password` variable values 
1. Execute `py HXHostsExtractor.py` in a shell (I recommend PowerShell in Windows)

The script will create a new CSV file named `hx_all_hosts.csv` with all hosts in the platform.

## Downloaded fields
The script will download these fields per host: `hostname`, `primary_ip_address`, `os` and `agent_version` but It can be customized to extract any other just adding them in the `rowValues` variable.

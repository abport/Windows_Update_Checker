# Windows Update Checker

A Python script to check if a specific Windows update is installed on one or multiple computers.


## Prerequisites

-   Python 3 installed on the computer you will run the script from
-   Windows Management Instrumentation (WMI) enabled on the remote computers
-   The hostnames or IP addresses of the remote computers
-   The KB number of the update you want to check

## Usage

### Remote execution using Windows Management Instrumentation (WMI)

1.  Clone the repository to your computer
```bash
git clone https://github.com/abport/Windows_Update_Checker.git
```
2.  Navigate to the repository directory
```bash
cd Windows_Update_Checker
```
3. Edit the `check_update_wmi.py` script and replace `hosts` with the hostnames or IP addresses of the remote computers you want to run the script on.
```python
hosts = ["host1", "host2", "host3"]
```
4.  Run the script and enter the KB number of the update you want to check when prompted.
```code
python check_update_wmi.py
```
5.  The script will output the results for each computer, indicating whether the update is installed or not.
```python
Update is installed on host1.
Update is not installed on host2.
Update is installed on host3.
```
### Batch script

1.  Clone the repository to your computer
```bash
git clone https://github.com/abport/Windows_Update_Checker.git
```
2.  Navigate to the repository directory
```bash
cd Windows_Update_Checker
```
3.  Create a text file named `computers.txt` in the repository directory and list the hostnames or IP addresses of the remote computers you want to run the script on, one per line.
```python
host1
host2
host3
```
4.  Run the `check_update_batch.bat` script.
```python
check_update_batch.bat
```
5.  The script will run the `check_update_wmi.py` script for each computer in the `computers.txt` file, outputting the results to the Command Prompt window.
```python
Checking update on host1...
Update is installed on host1.
Checking update on host2...
Update is not installed on host2.
Checking update on host3...
Update is installed on host3.
```
## Troubleshooting

-   If you receive an error when running the script, make sure that WMI is enabled on the remote computers and that you have the necessary permissions to connect to the remote computers and execute the code.
-   If you receive an error when running the batch script, make sure that you have Python installed on the computer and that the path to the Python executable is set correctly in the `check_update_batch.bat` script.
-   If you receive an error when entering the KB number, make sure that you enter the KB number in the correct format (e.g. "123456").

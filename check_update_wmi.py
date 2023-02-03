import wmi

def is_update_installed(host, kb_number):
    c = wmi.WMI(computer=host)
    for update in c.Win32_QuickFixEngineering():
        if update.HotFixID == "KB" + kb_number or update.HotFixID == "Q" + kb_number:
            return True
    return False

hosts = ["host1", "host2", "host3"]  # Replace with the hostnames or IP addresses of the computers you want to run the script on
kb_number = input("Enter the KB number of the update: ")

for host in hosts:
    if is_update_installed(host, kb_number):
        print(f"Update is installed on {host}.")
    else:
        print(f"Update is not installed on {host}.")

import wmi

c = wmi.WMI()

def is_update_installed(kb_number):
    for update in c.Win32_QuickFixEngineering():
        if update.HotFixID == "KB" + kb_number or update.HotFixID == "Q" + kb_number:
            return True
    return False

kb_number = input("Enter the KB number of the update: ")

if is_update_installed(kb_number):
    print("The update is installed.")
else:
    print("The update is not installed.")

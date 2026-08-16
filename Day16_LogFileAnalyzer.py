#Log File Analyzer

with open("app_logs.txt", "r") as file:
    lines = file.readlines()

info_count = 0
warning_count = 0
error_count = 0

for line in lines:
    if "INFO" in line:
        info_count += 1
    elif "WARNING" in line:
        warning_count += 1
    elif "ERROR" in line:
        error_count += 1

print(f"Total INFO messages: {info_count}")
print(f"Total WARNING messages: {warning_count}")
print(f"Total ERROR messages: {error_count}")

if info_count > warning_count and info_count > error_count:
    print("INFO is the most common log type")
elif warning_count > info_count and warning_count > error_count:
    print("WARNING is the most common log type")
else:
    print("ERROR is the most common log type")

for line in lines:
    if "ERROR" in line:
        print(line)
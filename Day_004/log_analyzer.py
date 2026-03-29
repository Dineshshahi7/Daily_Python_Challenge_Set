'''
# Log Analyzer (String + File + Loops)
You are given a log file (log.txt) with entries like:
- INFO User logged in
- ERROR Invalid password
- WARNING Disk almost full
- INFO File uploaded
- ERROR Server crashed

i) Requirements:
- Read file

ii) Count:
- INFO messages
- ERROR messages
- WARNING messages

iii) Extract:
- All ERROR messages

iv) Print:
- Summary report

v) Bonus:
- Save report to new file (report.txt)
'''

FILE_NAME = "log.txt"


def analyze_logs():
    info_count = 0
    error_count = 0
    warning_count = 0
    error_messages = []

    try:
        with open(FILE_NAME, "r") as f:
            for line in f:
                line = line.strip()

                if line.startswith("INFO"):
                    info_count += 1

                elif line.startswith("ERROR"):
                    error_count += 1
                    error_messages.append(line)

                elif line.startswith("WARNING"):
                    warning_count += 1

        # Print report
        print("\n----- Log Report -----")
        print("INFO count:", info_count)
        print("ERROR count:", error_count)
        print("WARNING count:", warning_count)

        print("\nError Messages:")
        for msg in error_messages:
            print(msg)

        # Save to file (bonus)
        with open("report.txt", "w") as f:
            f.write("----- Log Report -----\n")
            f.write(f"INFO: {info_count}\n")
            f.write(f"ERROR: {error_count}\n")
            f.write(f"WARNING: {warning_count}\n\n")

            f.write("Error Messages:\n")
            for msg in error_messages:
                f.write(msg + "\n")

        print("\nReport saved to report.txt")

    except FileNotFoundError:
        print("log.txt file not found.")


analyze_logs()
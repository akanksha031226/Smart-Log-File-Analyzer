from log_analyzer import analyze_log
import os
print("===== SMART LOG FILE ANALYZER =====")
filename = input("Enter log file name:") 
if not os.path.exists(filename):
    print("Error: Log file not found!")
    exit()
info, warnings, errors, error_details = analyze_log(filename)
print("\n===== ANALYSIS REPORT =====")
print("INFO messages:", info)
print("WARNING messages:", warnings)
print("ERROR messages:", errors)
print("\n===== ERROR DETAILS =====")
for error, count in error_details.items():
    print(error, "->", count,"time(s)")
with open("report.txt", "w") as report:
    report.write("===== SMART LOG FILE ANALYZER =====\n")
    report.write(f"INFO messages: {info}\n")
    report.write(f"WARNING messages: {warnings}\n")
    report.write(f"ERROR messages: {errors}\n")
    report.write("\n===== ERROR DETAILS =====\n")
    for error, count in error_details .items():
        report.write(f"{error} -> {count} time(s)\n")
if error_details:
    most_frequent_error = max(error_details, key=error_details.get)

    print("\nMost frequent error:", most_frequent_error)
    print("Frequency:", error_details[most_frequent_error],"time(s)")

    with open("report.txt", "a") as report:
        report.write(f"\nMost frequent error: {most_frequent_error}\n")
        report.write(f"Frequency: {error_details[most_frequent_error]} time(s)\n")
else:
    print("\nNo errors found in the log file.")
print("\nAnalysis completed!")    
print("Report saved successfully in report.txt")
total = info+warnings+errors
print("Total log entries analyzed:", total)


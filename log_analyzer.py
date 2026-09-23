def analyze_log(filename):
    info_count = 0
    warning_count = 0
    error_count = 0
    errors = {}
    with open(filename, "r") as file:
        for line in file:
            if "INFO:" in line:
                info_count += 1
            elif "WARNING:" in line:
                warning_count += 1
            elif "ERROR:" in line:
                error_count += 1
                error_message = line.replace("ERROR:" , "").strip()
                if error_message in errors:
                    errors[error_message] += 1
                else:
                    errors[error_message] = 1
    print("CHECK:", info_count, warning_count, error_count)                
    return info_count, warning_count, error_count,errors
                         
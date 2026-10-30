
import re
from collections import Counter
from urllib.parse import urlsplit


# Function to parse a single log line
def parse_log_line(line):
    pattern = r'(\S+) \S+ \S+ \[([^\]]+)\] "([A-Z]+) (.*?) HTTP/[\d.]+" (\d{3}) (\S+)'

    match = re.match(pattern, line)

    if not match:
        return None

    ip_address = match.group(1)
    method = match.group(3)
    endpoint = match.group(4)
    status_code = int(match.group(5))

    # Remove query parameters from endpoint
    endpoint = urlsplit(endpoint).path

    return {
        "ip": ip_address,
        "method": method,
        "endpoint": endpoint,
        "status": status_code
    }


# Function to analyze the log file
def analyze_log_file(filename):

    ip_counts = Counter()
    endpoint_counts = Counter()
    status_counts = Counter()

    total_requests = 0
    error_count = 0
    malformed_lines = 0

    try:
        with open(filename, "r") as file:

            for line in file:

                line = line.strip()

                if not line:
                    continue

                log_data = parse_log_line(line)

                if log_data is None:
                    malformed_lines += 1
                    continue

                total_requests += 1

                ip_counts[log_data["ip"]] += 1
                endpoint_counts[log_data["endpoint"]] += 1
                status_counts[log_data["status"]] += 1

                # Count error responses (4xx and 5xx)
                if log_data["status"] >= 400:
                    error_count += 1

        # Display analysis report
        print("\n========== SERVER LOG ANALYSIS REPORT ==========")

        print("\nTotal Requests:", total_requests)
        print("Total Error Responses:", error_count)
        print("Malformed Log Lines:", malformed_lines)

        # Display status code summary
        print("\n---------- HTTP STATUS CODES ----------")

        if status_counts:
            for status, count in status_counts.most_common():
                print(f"Status {status}: {count} requests")
        else:
            print("No valid status codes found.")

        # Display most frequent IP addresses
        print("\n---------- TOP IP ADDRESSES ----------")

        if ip_counts:
            for ip, count in ip_counts.most_common(5):
                print(f"{ip} : {count} requests")
        else:
            print("No IP addresses found.")

        # Display most requested endpoints
        print("\n---------- MOST REQUESTED ENDPOINTS ----------")

        if endpoint_counts:
            for endpoint, count in endpoint_counts.most_common(5):
                print(f"{endpoint} : {count} requests")
        else:
            print("No endpoints found.")

        print("\n===============================================")

        # Save summary report to a file
        with open("summary_report.txt", "w") as report:

            report.write("SERVER LOG ANALYSIS REPORT\n")
            report.write("==========================\n")

            report.write(f"Total Requests: {total_requests}\n")
            report.write(f"Error Responses: {error_count}\n")
            report.write(f"Malformed Lines: {malformed_lines}\n")

            report.write("\nHTTP STATUS CODES:\n")
            for status, count in status_counts.most_common():
                report.write(f"{status}: {count}\n")

            report.write("\nTOP IP ADDRESSES:\n")
            for ip, count in ip_counts.most_common(5):
                report.write(f"{ip}: {count}\n")

            report.write("\nMOST REQUESTED ENDPOINTS:\n")
            for endpoint, count in endpoint_counts.most_common(5):
                report.write(f"{endpoint}: {count}\n")

        print("\nSummary report saved as summary_report.txt")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

    except PermissionError:
        print("Error: Permission denied while reading the file.")

    except OSError as error:
        print("File error:", error)


# Main function
def main():

    print("================================")
    print("       LOG FILE ANALYZER")
    print("================================")

    filename = input("Enter log file name (example: access.log): ").strip()

    if not filename:
        print("Please enter a valid file name.")
        return

    analyze_log_file(filename)


if __name__ == "__main__":
    main()

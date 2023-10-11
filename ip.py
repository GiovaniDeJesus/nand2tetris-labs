import socket

# Input and output file names
input_file = "input.txt"
output_file = "output.txt"

# Open input and output files
with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    for line in infile:
        # Remove leading/trailing whitespaces and newline characters
        line = line.strip()

        # Check if the line is an IP address
        try:
            ip_address = socket.gethostbyname(line)
            outfile.write(ip_address + "\n")
        except socket.gaierror:
            # If it's not a valid domain, assume it's an IP address
            outfile.write(line + "\n")

print("Resolution complete. Results written to", output_file)

import datetime

def create_timestamp_file():
    # Get current timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    # Create file with timestamp as filename
    filename = f"{timestamp}.txt"
    
    # Write timestamp content to file
    with open(filename, 'w') as file:
        file.write(timestamp)

        
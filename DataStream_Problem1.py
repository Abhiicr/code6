class DataStream:
    def __init__(self):
        #to store the last printed timestamp for each unique string
        self.last_printed_timestamp = {}
    
    def should_output_data_str(self, timestamp, data_str):
        # Check if the string has been printed before
        if data_str not in self.last_printed_timestamp:
            self.last_printed_timestamp[data_str] = timestamp
            return True
        # Check if 5 seconds have passed since the last time this string was printed
        if timestamp - self.last_printed_timestamp[data_str] >= 5:
            self.last_printed_timestamp[data_str] = timestamp
            return True
        # If less than 5 seconds have passed
        return False

# Test 
def test_data_stream():
    data_stream = DataStream()
    results = [
        data_stream.should_output_data_str(timestamp=0, data_string="hello"),
        data_stream.should_output_data_str(timestamp=1, data_string="world"),
        data_stream.should_output_data_str(timestamp=6, data_string="hello"),
        data_stream.should_output_data_str(timestamp=7, data_string="hello"),
        data_stream.should_output_data_str(timestamp=8, data_string="world")
    ]
    print(results)

# Running test
test_data_stream()

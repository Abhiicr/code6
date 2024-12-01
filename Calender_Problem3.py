class Calendar:
    def __init__(self):
        # List to store booked events as [start, end) intervals
        self.booked_events = []
    
    def schedule(self, start, end):
        # Validate input: ensure end time is after start time
        if start >= end:
            return False
        
        # Check for overlap with existing events
        for event_start, event_end in self.booked_events:
            # Overlap conditions:
            if start < event_end and end > event_start:
                return False
        # No overlaps found, add the event
        self.booked_events.append([start, end])
        return True

# Test 
def test_calendar():
    # Test case 
    calendar = Calendar()
    test_cases = [
        (5, 10),   # First event, should return True
        (8, 13),   # Overlaps with first event, should return False
        (10, 15),  # Back-to-back with first event, should return True
        (0, 5),    # No overlap, should return True
        (3, 7),    # Overlaps with first event, should return False
    ]
    results = []
    
    for start, end in test_cases:
        result = calendar.schedule(start, end)
        results.append(result)
        print(f"Scheduling event [{start}, {end}): {result}")
    
    return results

# Run the tests
test_results = test_calendar()

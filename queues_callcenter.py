from collections import deque

class CallCenter:
    def __init__(self):
        self.queue = deque()

    def add_request(self, request):
        """Adds a new customer service request to the queue."""
        self.queue.append(request)
        print(f"Request '{request}' added to the queue.")

    def handle_next_request(self):
        """Handles the next customer service request in the queue."""
        if self.queue:
            request = self.queue.popleft()
            print(f"Handling request: {request}")
        else:
            print("No requests to handle.")

# Example usage
call_center = CallCenter()

# Adding requests
call_center.add_request("Request 1: Password reset")
call_center.add_request("Request 2: Account locked")
call_center.add_request("Request 3: Billing issue")

# Handling requests
call_center.handle_next_request()  # Output: Handling request: Request 1: Password reset
call_center.handle_next_request()  # Output: Handling request: Request 2: Account locked
call_center.handle_next_request()  # Output: Handling request: Request 3: Billing issue
call_center.handle_next_request()  # Output: No requests to handle.
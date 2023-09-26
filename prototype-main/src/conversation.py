```python
class Conversation:
    
    def __init__(self, user_id):
        self.user_id = user_id
        self.history = []
        
    def start_conversation(self):
        self.history = []
        
    def generate_response(self, input):
        return "Model response goes here"
    
    def save_conversation(self):
        # TODO: Save conversation history to database
        pass
```
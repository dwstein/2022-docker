from pydantic import BaseModel
from typing import List, Optional

class Message(BaseModel):
    role: str  # 'user' or 'llm'
    content: str

class Conversation(BaseModel):
    messages: List[Message] = []

    def add_message(self, role: str, content: str):
        self.messages.append(Message(role=role, content=content))

    def get_history(self):
        return self.messages

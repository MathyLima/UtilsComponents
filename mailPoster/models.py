from dataclasses import dataclass

@dataclass
class MailPayload:
    receiver: str
    subject: str
    body: str
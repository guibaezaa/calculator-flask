from abc import ABC, abstractmethod

class NotificationSender(ABC):
    @abstractmethod
    def send_notification(self, recipient: str, message: str) -> None:
        """Send a notification to the specified recipient with the given message."""
        pass

class EmailNotificationSender(NotificationSender):
    def send_notification(self, recipient: str, message: str) -> None:
        print(f"Sending email to {recipient}: {message}")

class SMSNotificationSender(NotificationSender):
    def send_notification(self, recipient: str, message: str) -> None:
        print(f"Sending SMS to {recipient}: {message}")


class Notificator:
    def __init__(self, notication_sender: NotificationSender) -> None:
        self.__notification_sender = notication_sender

    def send(self, recipient: str, message: str) -> None:
        self.__notification_sender.send_notification(recipient, message)

obj = Notificator(EmailNotificationSender())
obj.send("Message via Email", "Hello via Email!")
obj = Notificator(SMSNotificationSender())
obj.send("Message via SMS", "Hello via SMS!") 

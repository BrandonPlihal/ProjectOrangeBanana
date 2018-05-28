from collections import OrderedDict
import sys

class Task:
    def __init__(self, assigned_from, assigned_to, subject, message):
        self.assigned_from = assigned_from
        self.assigned_to = assigned_to
        self.subject = subject
        self.message = message


    def __getattr__(self, attr):
        return self.data[attr]

    def to_dict(self):
        return OrderedDict({'assigned_from': self.assigned_from,
                            'assigned_to': self.assigned_to,
                            'subject': self.subject,
                            'message': self.message})

    def sign_transaction(self):
        pass

    def bytes(self):
        return sys.getsizeof(self.assigned_to) + sys.getsizeof(self.assigned_from) + \
               sys.getsizeof(self.subject) + sys.getsizeof(self.message)
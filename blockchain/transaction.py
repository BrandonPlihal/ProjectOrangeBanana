import time
import sys

class Transaction:
    def __init__(self, assigned_to, assinged_from, subject, task):
       '''

       :param assigned_to:
       :param assinged_from:
       :param subject:
       :param task:
       :param size:
       '''

        self.assigned_to = assigned_to
        self.assigned_from = assinged_from
        self.subject = subject
        self.task = task
        self.size = self._get_size()

    def _get_size(self):
        return sys.getsizeof(self.assigned_to) + sys.getsizeof(self.assigned_from) + sys.getsizeof(self.subject) + sys.getsizeof(self.task)


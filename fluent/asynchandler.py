# -*- coding: utf-8 -*-

from .handler import FluentHandler
from .asyncsender import FluentSender

class FluentHandler(FluentHandler):
    '''
    Asynchronous Logging Handler for fluent.
    '''

    def getSenderClass(self):
        return FluentSender

    def close(self):
        self.acquire()
        try:
            try:
                self.sender.close()
            finally:
                super(FluentHandler, self).close()
        finally:
            self.release()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

from gevent import Greenlet
from gevent.queue import Queue

import Dokka.Messages


class GeventActor(Greenlet):
    def __init__(self):
        super(GeventActor, self).__init__()
        self._inbox = Queue()
        self._running = False

    def tell(self, message):
        self._inbox.put(message)

    def on_receive(self, message):
        raise NotImplementedError()

    def _run(self):
        self._running = True
        while self._running:
            message = self._inbox.get()
            if not isinstance(message, Dokka.Messages.Message):
                continue
            if isinstance(message, Dokka.Messages.StopActor):
                self._running = False
            self.on_receive(message)

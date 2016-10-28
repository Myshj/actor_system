from multiprocessing import Process, Queue

import Dokka.Messages


class ProcessActor(Process):
    def __init__(self):
        super(ProcessActor, self).__init__()
        self._inbox = Queue()
        self._running = False

    def on_received(self, message):
        raise NotImplementedError()

    def tell(self, message):
        self._inbox.put(message)

    def run(self):
        self._running = True

        while self._running:
            message = self._inbox.get()
            if not isinstance(message, Dokka.Messages.Message):
                continue
            elif isinstance(message, Dokka.Messages.StopActor):
                self._running = False
            self.on_received(message)

import ntpath
# pip3 install pydispatcher --user
from pydispatch import dispatcher
import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


MYHANDLER_SENDER = 'myhandler_sender'
MYHANDLER_SIGNAL = 'myhandler_signal'
TEST_FILE = 'test_data.csv'
TEST_DIR = '/home/bill/data/documents/infolab2/progs/jupyter_notebooks/pyqtgraph/test_data/'
THRESHOLD_TIME = 0.01


class MyHandler(FileSystemEventHandler):
    ''' handle events from the file system '''
    def __init__(self):
        self.start_time = time.time()

    def on_modified(self, event):
        now_time = time.time()
        # filter out multiple modified events occuring for a single file operation
        if (now_time - self.start_time) < THRESHOLD_TIME:
            print('repeated event, not triggering')
            return
        changed_file = ntpath.basename(event.src_path)
        if changed_file == TEST_FILE:
            print('changed file: {}'.format(changed_file))
            print('event type: {}'.format(event.event_type))
            print('do something...')
            # print(event)
            message = '{} changed'.format(changed_file)
            dispatcher.send(message=message, signal=MYHANDLER_SIGNAL, sender=MYHANDLER_SENDER)
        self.start_time = now_time


def main():
    dispatcher.connect(dispatcher_receive, signal=MYHANDLER_SIGNAL, sender=MYHANDLER_SENDER)
    observer = Observer()
    observer.schedule(event_handler, path=TEST_DIR, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

def dispatcher_receive(message):
    print('received dispatch: {}'.format(message))
    # read in the altered file

if __name__ == "__main__":
    event_handler = MyHandler()
    main()
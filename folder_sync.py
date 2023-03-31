from dirsync import sync
import logging
import schedule
import time


def synchronize():
    sync('E:\\folder_a', 'E:\\folder_test', 'sync', purge=True)  # this sync override the files in the second folder
    logging.basicConfig(filename="log.txt", level=logging.DEBUG,
                    format="%(asctime)s %(message)s")
    logging.debug("Debug logging test ...")
    logging.info("Program sync as expected")
    logging.warning("This event was logged")


schedule.every(20).seconds.do(synchronize)

while True:
    schedule.run_pending()
    time.sleep(2)

import Bottle_credentials_interface
import from_queue_to_drive
import Add_To_Calender
import multiprocessing
import Course_parsed
import  send_injection

def web_interface():
    Bottle_credentials_interface.webpage()


if __name__=="__main__":
    multiprocessing.Process(target=Add_To_Calender.process_event).start()
    multiprocessing.Process(target=from_queue_to_drive.setup_queue_consumer).start()
    multiprocessing.Process(target=web_interface).start()
    #multiprocessing.Process(target=Course_parsed.get_campus()).start()


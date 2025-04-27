from threading import Thread, Lock
import time
import sys

# Override print for thread-safe output
print = lambda x: sys.stdout.write("%s\n" % x)

# Global Lock
lock = Lock()

def render_3D_model():
    print("Rendering waiting for lock...⏳")
    lock.acquire()
    print("Rendering got lock...rendering...♻️")
    
    time.sleep(2)  # heavy computation
    
    lock.release()
    print("Rendering released lock...👍")

def upload_model_dbms():
    print("DBMS uploader waiting for lock...⏳")
    lock.acquire()
    print("DBMS uploader got lock...transferring data...⬆️")
    
    time.sleep(5)  # heavy computation
    
    lock.release()
    print("DBMS uploader released lock...👍")

# Making the threads  
t1 = Thread(target=render_3D_model)
t2 = Thread(target=upload_model_dbms)
t3 = Thread(target=render_3D_model)
t4 = Thread(target=render_3D_model)
t5 = Thread(target=upload_model_dbms)
t6 = Thread(target=upload_model_dbms)

# Start threads
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()

# Wait for threads to complete
t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()

print("Main Thread ended")

import threading,subprocess,shutil
def exit_thread(server:subprocess.Popen):
    threading.main_thread().join()
    print("Shutting down server...")
    server.kill()
    print("Cleaning up...")
    shutil.rmtree("/dev/shm/mcminigame",ignore_errors=True)
def exit_handler(server:subprocess.Popen):
    thread = threading.Thread(target=exit_thread,args=(server,))
    thread.start()
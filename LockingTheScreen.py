import ctypes
def log_the_screen():
 ctypes.windll.user32.LockWorkStation()
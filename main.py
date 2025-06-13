"""
Główny moduł uruchamiający aplikację GUI księgarni internetowej.
"""


import gui_module

def __main__():
    try:
        gui_module.run_gui()
    except Exception as e:
        print("Error",e)

if __name__ == "__main__":
    __main__()
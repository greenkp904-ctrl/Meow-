#logic.py

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Models.models import *
from Database_Management import *
from GUI.gui_main import *

def run_logic():
    setup_database()
    print("=================================================\n"
          "============| Chettikkulangara Bank |============\n"
          "=================================================\n\n")
    
    app = BankApp()
    app.mainloop() 
    
if __name__ == "__main__":
    run_logic()
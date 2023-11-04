import os
try:
    import pyautogui, time, keyboard
    # pip install opencv-python
except ImportError:
    os.system("pip install pyautogui")
    os.system("pip install keyboard")



while True:
    buy = pyautogui.locateCenterOnScreen('buy.png', confidence=0.84)
    if buy:
        time.sleep(0.06)
        pyautogui.moveTo(buy)
        pyautogui.click()
        time.sleep(0.09)
        pyautogui.click()
        print(f"Clicked buy button on {buy}")
    else:
        ok = pyautogui.locateCenterOnScreen('ok.png', confidence=0.88)
        if ok:
            pyautogui.moveTo(ok)
            pyautogui.click()
            time.sleep(0.05)
            pyautogui.click()
            print(f"Clicked ok button on {ok}")
    time.sleep(0.07)
    
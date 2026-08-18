from meme_rendering import render_gif
import random
import os
import asyncio
import pyautogui
from email_handeling import send_email
memes=os.listdir('./memes')
print(memes)
sms=None
keyboard_controls = [
        'w', 'a', 's', 'd'
        # ,'space', 'shift', 'ctrl',
        # 'tab', 'esc',
        # 'q', 'e'
    ]

mouse_controls = [
    'left',
    'right',
    'middle'
]

mouse_movements = [
        'x',
        'y'
        #'mouse-scroll'
    ]





def activate_keys(keys):
    for i in keys:
        if i in keyboard_controls:
            pyautogui.keyDown(i)
        elif i in mouse_controls:
            pyautogui.mouseDown(i)
        elif i in mouse_movements:
            x, y = pyautogui.position()

            if i == 'x':
                new_x = random.randint(0, pyautogui.size()[0] - 1)
                pyautogui.moveTo(new_x, y)

            elif i == 'y':
                new_y = random.randint(0, pyautogui.size()[1] - 1)
                pyautogui.moveTo(x, new_y)


            
    

async def punish_level_1():
    play_time=random.randint(9,20)
    meme=random.choice(memes)
    print(meme,play_time)
    
    render_gif(filename=meme,time_play=play_time)
    sleep_time=random.randint(1,30)
    await asyncio.sleep(sleep_time)

activated_keys=[]

def deactivate_keys(keys):
    for i in keys:
        if i in keyboard_controls:
            pyautogui.keyUp(i)

        elif i in mouse_controls:
            pyautogui.mouseUp(button=i)

async def punish_level_2():
    global activated_keys
    
    controls=[keyboard_controls]
    chosen_control=random.choice(controls)
    key_to_activate=random.choice(chosen_control)
    activated_keys.append(key_to_activate)
    print(key_to_activate)
    activate_keys(keys=activated_keys)
    sleep_time=random.randint(1,30)
    await asyncio.sleep(sleep_time)
    deactivate_keys(activated_keys)
    activated_keys=[]

        
    
async def punish_level_3():
    global sms
    
    if sms is None:
        message="Still Playing Game"
        send_email(message=message)
        sleep_time=random.randint(1,30)
        await asyncio.sleep(sleep_time)
        sms=True

async def main():
    await punish_level_1()

if __name__=='__main__':
    asyncio.run(main())
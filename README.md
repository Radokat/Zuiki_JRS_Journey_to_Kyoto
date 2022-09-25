# Zuiki_JRS_Journey_to_Kyoto
Zuiki "support" for Japanese Rail Sim: Journey to Kyoto via keyboard events.

Required Python packages:  
pyautogui  
pygame  
  
Download the .py file and run via: python.exe .\Zuiki_JRS_Journey_to_Kyoto.py   
Alternatively you can now also download a executable release that was created with py2exe.  
  
At the start you will need to select the line you want to drive, as the train on the Eizan line maps notches differently.  
Once you are in the cabin, sync the controller up by putting it into the EB settin.  
  
The inputs will be buffered, so there is a delay if you move many notches at once.  
This is by design, as the game only accepts keyboard inputs separated by a pause.  

 
 
## Make sure to disable Steam Input for the game, otherwise the controller will behave incorrectly.  
  
  
Lever and most buttons are working.  
There is no support for the electric brake, as there are not enough notes on the controller.
  
Button mappings:
 

| Controller  | Game |
| :-------------: | :-------------: |
| D-pad left  | D-pad left  |
| D-pad right  | D-pad right  |
| D-pad up   | D-pad up   |
| D-pad down   | D-pad down   |
| A  | Enter (Confirm)  |
| B  | ESC (Cancel)  |
| Y  | Z (Retry)  |
| Home  | Tab(Pause)  |
| L  | L  |
| R  | Horn  |  

Horn is hard mapped, as the game still recognizes some of the buttons in game.  
That's why it's also important to use all buttons, with the exception of Home and R, only while the game is paused or in menus.

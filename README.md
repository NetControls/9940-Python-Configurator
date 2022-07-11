# 9940-Python-Configurator
Configurator for 9904/9940 Motion Controllers

Python Version: 3.10.2

PySerial Version: 3.5

ToDo:

  List serial ports so user can select which port to open, i.e. 1,2,3...
  
  Option to open/close serial port so it is more graceful.
  
  Switch to key strokes for user entery using F1-F12 (Hint need "keyboard" module")
  
  Implement test: F keys to move the motor +/-51200 counts to test 1 rotation in each direction
  
    For encoder motors, read out the encoder value and check what it should be for one rotation +/-...i.e. if enc_cpr == 800, then is should be =/- 800...
    
    Encoder CPR can be read using the "E" command, i.e. :1E<CR>
    
 
    
 

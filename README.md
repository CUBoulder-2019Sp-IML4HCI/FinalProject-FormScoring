# Form Scoring Utility Instructions  
## Step 1: Hardware Setup
#### 1a - Receiver Setup. 
Plug microbit receiver into USB port on computer.
#### 1b - Upper Arm Accessory. 
Attach upper arm mount to arm  such that the microbit rests near the center of the deltoid. The exact position is not critical, but a greater distance between the upper arm microbit and the hand mircobit is preferred. When satisfied with the position of the upper arm mount, fasten the hook and loop closure such that the band does not slip, but circulation is not obstructed. Articulate your arm to ensure the band is not restrictive. If there is any restirction, loosen the hook and loop closure. Do not exercise with an armband that is too tight.
#### 1c - Glove Accessory. 
Put on glove, and articulate the hand and wrist to ensure a full range of motion is possible without restriction. If the battery pack limits the motion of the hand, reposition the battery pack to a different location on the cuff of the glove, and perform articulation test again. Repeat position testing until a comfortable and non-restrictive position for the battery pack is found.
## Step 2: Starting Wekinator  
#### Open WekinatorProject.wekproj in Wekinator 
(WekinatorProject.wekproj can be found in FinalProject-FormScoring/WekinatorProject)  
## Step 3: Starting gui.py
#### Run gui.py
Using Unix Terminal:  
~/FinalProject-FormScoring$ python gui.py
## Step 4: Using the GUI
![Image of GUI](https://github.com/CUBoulder-2019Sp-IML4HCI/FinalProject-FormScoring/blob/master/img/gui_instructions.png)
### Training the Model
1. Using the dropdown (displayed above with 'Still'), select the form/failure you wish to train.
2. Using the demo animation as a guide, record a single rep of the form/failure by clicking 'Start/Stop Recording' at the beginning of the rep, and again when the rep is complete.
3. Record at least 2 samples for each form/failure.
4. Repeat until all form/failure modes have been trained.

### Using the Model
To use the model, click 'Start/Stop Running' when beginning a set, and again when you complete your set.

### Reading the Results
The frequency of good reps and failures will be displayed at the bottom of the GUI. 

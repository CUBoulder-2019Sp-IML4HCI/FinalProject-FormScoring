Ian Wilkins, Garrett Sippel
CSCI 4889

# IML4HCI Final Project - Exercise Form Scoring
## Final Report

### The Idea and Mission Statement:
Our goal was to create an interactive, wearable, accessory that can be trained to recognize proper form for a given exercise, and then score future motions of that exercise against the proper form. This system has implications in improving exercise quality, monitoring training progress, and preventing malform injury. The user will be able to train the model to their needs, including but not limited to, movement restraints for post injury physical therapy, speed restraints due to different movement arms from people of different shapes and sizes, and provide live feedback on form for people who are unable to monitor their movements due to constraint, injury, or disability.

### UX Example - Bicep Curl
Understanding the Curl: A standard bicep curl has 2 primary modes of failure: failure to pronate the wrist (not rotating the wrist to achieve a full contraction of the bicep), and failure to complete the full range of motion for the rep (performing a half rep).

Interactive User Accessories: The user will wear a glove and an armband equipped with microbits to track the motion of the arm in 3D space. These accessories capture motion data specific to the user, and safely track user motion without impeding circulation or range of motion.

![Image of Glove and Armband Acessories](https://github.com/CUBoulder-2019Sp-IML4HCI/FinalProject-FormScoring/blob/master/accessories.png)

Interactive User Training: The user must train 4 states for a bicep curl model: a still (the state reached in between/at the bottom of a rep), a rep with proper form (full range of motion and pronation of the wrist), a rep with pronation failure, and a half rep.

![Image of GUI](https://github.com/CUBoulder-2019Sp-IML4HCI/FinalProject-FormScoring/blob/master/gui_pic.PNG)

In order to guide the user through the training process, an animation of a trainer performing the exercise and each failure mode will be displayed based on what the user has selected to train. Id est, if the user selects to train pronation failure, an animation of a rep that fails to pronate the wrist will be played.

User Feedback: Dynamic time warping is used to identify and classify the failure modes trained. The upon completing a set, the GUI will provide the user with feedback on the frequency of failure modes detected.
[Insert image of UI Feedback]


 



## Greatest Challenges:
### Physical Challenges:
As initially predicted, the greatest physical challenge was designing an accessory that can be repeatedly secured in place for the duration of the exercise. A dynamic time warping model uses distance between the input path and the training data as a loss function. In order to reliably classify the input path, the general shape of the path in n-dimensional space must be repeatable, and unique. In the case of pronation failure in a bicep curl, the 
#### Glove Design
The first iteration of our glove used a leather work glove as the base, and nylon chicago screws for mounting the microbit.

What was learned: The rigidity of leather gloves makes them easier to mount the microbit to, but limit dexterity. Looser fitting gloves were comfortable, and secured the microbit well, but posed a safety risk due to reduced grip and slippage. Furthermore, a leather glove does not stretch very much, limiting the size of hand that can be accommodated. 12 individuals were asked to try the glove, it was only a comfortable fit for 3 of them.

The second iteration of the glove used a thin and stretchy glove as a base, and thread as the mechanism to constrain the microbit.

What was learned: This glove had less restriction to dexterity, but was hard to mount a microbit to. The stretch factor made static mounting points less feasible. The glove was tested by 7 individuals (not many people want to help with random glove tests, while working out. Next time we will bring free food to attract interest.). Just stitching through the auxiliary pin holes (constraining only 1 edge) would detect movement when the fabric was stretched (like when a fist is closed) in 4 of the testers. Stitching through the auxiliary pin holes, the power input, and the buttons, caused the button stitching to snap when the fabric was stretched in 3 of the testers. A Stitch through the auxiliary pin holes and the battery input constrained the microbit well in 3D space, and did not snap any threads for all 7 testers. The testing in the gym also revealed that a repositional battery pack was a practical necessity to safe and comfortable function.

The third and final iteration of the glove constrained the microbit with the auxiliary pins parallel to the knuckles on the ulnar side of the glove, and a slightly slackened thread through the power input connecting to the space between the tendon of the thumb and the tendon of the forefinger provides adequate constraint, handles stretching well, and does not feel awkward during use. A glove was found with a cuff material that adheres well to the hook side of a hook and loop patch. The battery pack now has a hook patch added so it can be easily positioned anywhere on the cuff of the glove without adding extra bulk.


#### Armband Design
The first iteration of the upper arm mount used a compression sleeve cut to a band about 4” wide as a base, and nylon chicago screws to affix the microbit. 

What we learned: The chicago screws are not very comfortable when pressed against the upper arm (even when the smooth side is facing the skin), and the battery pack is heavy enough that securing it in place is problematic. It is very easy to create an overly-restrictive arm cuff, which is neither comfortable nor safe in use.

The second iteration of the arm band used a longer section of a compression sleeve in order to increase the contact area without increasing the tension of the cuff, and fine stitching to affix the microbit to the sleeve to avoid abbrading the upper arm.

What we learned: This armband seemed very promising until it was taken to the gym: the microbit is not removable, and it is used on a part of the body with heavy perspiration. The second iteration of the arm band and the glove were tested at the same time, however, the armband got really sweaty and gross, and no one (ourselves included) wanted to continue the testing on it at that point. Therein, only 3 people gave feedback on the second iteration of the armband. The microbit could not be removed in order to wash the band, and the section of the band covered by the microbit took longer to dry.

The third iteration of the upper arm cuff used chicago screws to secure the microbit such that it could be detached for cleaning. Using what was learned in the previous iterations, the nylon chicago screws need to have the heads modified to feel more natural against the arm (this was done by abbrading the inward facing side until a significantly flatter shape was achieved). The cuff needed to have grommets added to prevent fraying in the areas that the chicago screws went through. 

What we learned: The modified chicago screws felt fine, the grommets were irritating during use. 


The fourth iteration of the upper arm cuff, used a physical therapy light-duty compression sleeve, that was modified with a stretch compensated pocket for the microbit and battery pack.

What we learned: A standard upper arm compression sleeve is easily torn by the microbit. Additionally, the microbit is very uncomfortable when held in a pocket or folded cuff of the compression sleeve (the current pocket design adds extra fabric to form a pocket. This additional fabric increases the tension of the sleeve, and pushes the microbit too firmly against the body.).

### Computational Challenges:
As predicted, the greatest computational challenge was capturing and processing the input features such that our system is sensitive to subtle changes in form. In the case of the bicep curl, there are two classes of form change: orientation and distance.

Orientation Sensitivity
The glove did a great job constraining the microbit, and the accelerometer values from the glove microbit were very sensitive to changes in roll, pitch, and yaw. However, not all orientation of the microbit relative to the accessory are equally effective.

#### Glove Orientation Sensitivity:
Much of the orientation sensitivity testing was used as an evaluation metric for the final design of the glove, and so a standard procedure set was created. The procedures were as follows:
 [The following procedures assume the usage of the left hand]

![Ikea-Style Diagram of Roll, Pitch, and Yaw Testing](https://github.com/CUBoulder-2019Sp-IML4HCI/FinalProject-FormScoring/blob/master/roll_pitch_yaw_diagram.png)

Roll Test: Place a carpenters speed square on a table such that the square rests on one of the short edges, and the long edge rises from left to right. Put on the microbit glove and place your hand palm-down on the table. Start recording the feed, and pronate your wrist such that the plane of your palm is parallel with the long edge of the square, then return hand to table. This set of action is meant to standardize the testing of roll (wrist rotation in this case).

Pitch Test: Place a carpenters speed square on a table such that the square rests on one of the short edges, and the long edge rises from proximal to distal to you. Put on the microbit glove and place your hand palm-down on the table. Start recording the feed, and tilt your wrist/hand such that the plane of your palm is parallel with the long edge of the square, then return wrist/hand to table. This set of action is meant to standardize the testing of pitch (tilt of the wrist/hand in this case).

Yaw Test: Place a carpenters speed square on a table such that the lip of the square references the edge of the table proximal to you, and such that the left end of the long edge is more proximal to you than the right end.  Put on the microbit glove and place your hand on the square such that you middle finger is touching the the distal corner of the square, and your middle finger is parallel with the right edge. Start recording the feed, and tilt your wrist/hand such that your middle finger is parallel with the long edge of the square, then return wrist/hand to starting position. This set of action is meant to standardize the testing of yaw.

Roll, Pitch, Yaw Results: The best orientation of the microbit relative to the glove is with the edge of auxiliary pins parallel to the knuckles, and the side with the power input facing the skin.

#### Distance Sensitivity
The distance between the delt and the hand is long enough to tell large differences in arm position, but lacks the ability to detect more subtle changes. Experiments on signal strength were conducted in order to determine if a reduction in strength would provide more sensitivity. Reducing signal strength did not change performance very much when microbits have a clear line of sight between each other, but did improve the detection of bodies blocking the line of sight between microbits. Not all exercises position the body such that the signal between the microbits is obscured, but the ones that do may see a benefit from the reduced signal strength. In the case of the bicep curl used to demo this project, pronation of the wrist causes the arm to cut the line of sight. Further experimentation revealed that within a range of a meter, the overall performance across all signal strengths was not significantly different, however, the sensitivity to obstruction increased inversely to signal strength. Since there was no reduction of performance when a clear line of sight exists, but potentially improved performance when the body obstructs the signal, the final microbit hex has a reduced signal strength of 1. 

### Technologies Used:
#### Hardware:
This system involves the usage of three microbits, one microbit to act a receiver for a laptop, and two microbits in wearable accessories to constrain the microbits to the user.

#### Software:
Our OSC server and GUI were written in Python, our Dynamic Time Warping (DTW) utilizes Wekinator. The Python backend handles interactions with the GUI to send the appropriate control messages to Wekinator, and then listens to Wekinator’s outputs to display the appropriate results to the user. 

### Risks to Failure: 
The greatest risk to failure was the ability to determine subtle changes in form. In order for the user to have a custom interactive experience, the system must be able to capture small changes in form between users. Experimentation and refinement of feature extraction largely handled this issue, though there are still some types of changes that are still quite difficult to capture. Perhaps the greatest failure mode to classify is the half rep. The motion of a half rep is essentially a scaled down version of a full rep, and it requires a lot of sensitivity to distinguish between half and full reps. Our final product was able to distinguish between half and full reps for all of the users tested thus far, but it is unknown how easy it will be to extend it to other exercises where the difference is even more subtle.


### Ethical questions - Human and Infrastructural:
#### Hardware Ethical Concerns:
The development of accessories was approached with a great concern for user safety; the user could potentially injure themself while working out.  The final accessories cause minimal restriction to dexterity, minimal restriction to movement, minimal restriction to circulation, minimal abrasion, and the greatest level of comfort feasibly possible. 

#### Training Ethical Concerns:
This project has always involved a concern that the user might not know proper form. Instead of assuming the user understand proper form, and common modes of failure, our final product includes gifs of the actions being performed when the user selects a movement to train. This reduces the likelihood that the user will train incorrect form, and clarify each failure mode.

### Open Source Components:
#### Project Repo:
GitHub Repo: https://github.com/CUBoulder-2019Sp-IML4HCI/FinalProject-FormScoring

#### Python:
Anaconda Python Platform: https://www.anaconda.com/distribution/  
Python-OSC Package: https://pypi.org/project/python-osc/

#### Mirobit:
Microbit MakeCode Platform: https://makecode.microbit.org/ 

#### Final Video:
https://youtu.be/Ze9NPAPZrT4


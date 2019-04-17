## Changelog  
# 03-06-2019 Ian Wilkins: 
- Finish project proposal draft
                        
# 03-07-2019 Ian Wilkins: 
- Begin prototyping microbit chain.
- Create initial mircobit reciever (receive -> write to serial) hex
- Create initial microbit middle link (receive -> package -> send) hex
- Create initial microbit end link (send via radio) hex
- Create initial python OSC server
                                          
# 03-12-2019 Ian Wilkins: 
- Update microbit middle link (receive -> package -> send) hex
                      
# 03-13-2019 Ian Wilkins: 
- Add link to GitHub repo to project proposal
- Add acceptance criteria to project milestones in project proposal
- Make final revisions to project proposal and submit to Moodle
                        
# 03-14-2019 Ian Wilkins: 
- After meeting with Ben, I have been shown that a microbit chain is not going to be as feasible as 2 microbits communicating independently with the receiver.
- Begin prototyping signal strength reading
- Begin new python OSC server to handle new message format.
                        
# 03-14-2019 Garrett Sippel:
- Wrote ocs handler

# 03-17-2019 Ian Wilkins: 
- Create first working microbit 'a' and 'b' hex
- Update python OSC server to interpret messages from microbit 'a' and 'b'
                        
# 03-20-2019 Both:        
- Created youtube video
- Link: https://youtu.be/LxvbDUXSePE

# 03-25-2019 Ian Wilkins: 
- Create first glove and armband mount for 'a' and 'b' microbits. The following discoveries were made from these prototypes:
  1. Thick/robust work gloves are more rigid (and therein easier to mount a microbit to), but limit                                dexterity during exercises, making them less ideal.
  2. A loose fitting glove feels less awkward when a microbit is mounted, but poses potential safety                              issues when dealing with heavy weights (maximum grip strength is reduced).
  3. It is VERY EASY to make an arm band that cuts off circulation. The current battey pack weighs                                enough that supporting it is problematic. Potential solutions include decreasing tension of the                              cuff, but increasing the total contact surface area.


# 03-27-2019 Ian Wilkins: 
- Create second glove and armband mount for 'a' and 'b' microbits. The following discoveries were made from these prototypes:
    1. Thin and stretchy gloes have less restriction to dexterity, but are heard to mount a microbit                                to. The strech factor complicates using static mounting points. Too much stiching will snap when                              the glove is stretched, but too little stiching will not adequately constrain the microbit in 3D                              space.
    2. A tight fitting glove holds the microbit mounting method closer to the skin. In order to reduce                              irritation, fine thread was used to adhere the microbit.
    3. The battery pack is bulky, and position preference seems to change with each user. I need to                                find a way to have a repositional battery pack that is still safely secured. 
    4. The next iteration of the upper arm cuff seemed promising until it was taken to the gym. An                                  unforseen problem was realized: the microbit needs to be able to be detached so the band can be                              cleaned (the band band will absorb sweat during a workout. Current material and design is not                                well suited for easy washing.

# 03-31-2019 Garrett Sippel:
- Create initial GUI.

# 04-01-2019 Garrett Sippel:
- Experiment with threading GUI and server class together.


# 04-01-2019 Ian Wilkins:
- At this point in the project, we have reasonable mounts for the microbits (though more development is needed on the upper arm mount), we have a basic GUI, we have basic data handling, and we have all the components talking to each other. We have confirmed that we can recieve and process the XYZ acceleration values and signal stength between microbits, and that the signal strength is in fact reasonable different at different stages of our test exercises. The next step is to implement the DTW. Today involved reasearch on available DTW libraries and what option is most applicable to our project.

# 04-02-2019 Ian Wilkins: 
- Create third glove and armband mount for 'a' and 'b' microbits. The following discoveries were made from these prototypes:
    1. Constraining the microbits with the auxillary pins parallel to the knuckles on the ulnar side of                              the glove, and a slightly slackened thread through the power inpit connecting to the space                                    between the tendon of the thumb and the tendon of the forefinger provides adequate constraint,                                handles stretching well, and does not feel awkward during use.
    2. A glove was found with a cuff material that adheres well to the hook side of a hook and loop                                  patch. The battery pack now has a hook patch added so it can bea easily repositioned anywhere on                              the cuff of the glove without adding extra bulk.
    3. The glove is almost done, it now needs a way for the microbit to be detached when the glove is                                whashed.
    4. The next iteration of the upper arm cuff used chicago screws to secure the microbit such that it                              could be detached for cleaning. The cuff needed to have gromets added to prevent fraying in the                              areas that the chicago screws went through. The gromets chose were very irritating during use.                                For the next iteration of the upper arm cuff, I plan on using a physical therapy light-duty                                  compression sleeve, and sewing a stretch compensated pocket for the microbit and battery pack.

# 04-04-2019 Both:
- After discovering microbit radio latency/message chain issues during in class demos, the source of this latency was pinpointed and corrected.
- The source of the error was we updated both microbits to an old hex that did not inclide the global variable for last received message time, which were needed to restart the message chain if a deadlock was reached.

# 04-04-2019 Garrett Sippel:
- Research options for using GUI to send control messages to Wekinator. This may be a simpler option than implementing our own DTW. If the GUI can be used to send control messages, Wekinator can handle the processing, and the GUI can display the outputs.

# 04-06-2019 Ian Wilkins:
- Create fourth armband mount for 'b' bicrobit. The following discoveries were made from this prototype:
    1.  A standard upper arm compression sleeve is easily torn by the microbit. Additionally, the microbit is very                    uncomfortable when held in a pocket or folded cuff of the compression sleeve (the current pocket design causes the            microbit to abbrade the upper arm, which wears down the compression sleeve and is uncomfortable for the user).
    2.  The next design must not press the microbit against the body. The proposed next design will have a more loosely               affixed pocket for the microbit, and some additional padding to prevent abbrasion against the arm.
    
# 04-09-2019 Both:
- Problem 1 (FIXED): Sending control messages to Wekinator stops Wekinator from receiving the microbit data input. The following fixes were made:
    1.  Update OSC server class to handle the Wekinator control signals and the microbit data input. This involved changing the GUI class such that the server access state variables of the GUI class to indicate when Wekinator control messages should be sent.
    2. There was an additional space ('\s') in the message address/prefix that was short circuiting Wekinator, and forcing it to stop listening to the input port.
    
- Problem 2: Wekinator is receiving input vectors populated with 0.0. The following debudding steps have been taken:
    1.  Print Wekinator input immediately before it is sent to Wekinator via OSC server. The printed messages look good.
    2.  Set input as a variable and then send the variable. Variable prints as expected.
    3.  Change the initialization and data structure of the input.
   
# 04-10-2019 Both:
- FIXED Problem 2 Described in last update. Input was being mapped to an incorrect data type, a new function to be applied during the serial read map was written.
- New Update Video. https://youtu.be/Cuhxcn72vcI

# 04-11-2019 Both:
- Experiment with changes in signal strength. Reducing signal strength did not change performance very much when microbits have a clear line of sight between eachother, but did improve the detection of bodies blocking the line of sight between microbits. Not all exercises position the body such that the signal between the microbits is obscured, but the ones that do may see a benefit from the reduced signal strength. 
- New Microbit hex files with reduced signal strength.

# 04-12-2019 Both:
- EPIPHANY: Providing the user with a 0-100 score is not useful for users looking to understand and improve their form. The regressor score indicates how good or bad the user's form was, without any additional information as to what they did wrong. A regressor score is not particularly meaningful to real-world health and fitness endeavors. A meaningful output should inform the user of the modes of failure in their form such that the user can make corrections. As such, our model will now classify/identify failures in form, and report to the user what aspects need improvement.

# 04-13-2019 Both:
- Continued field testing has revealed the following issues and potential solutions:
    1. Every full rep is classified as a half rep before the rep is completed. A half rep can be identified by the following gesture patterns:
        - half rep, half rep ... (if the true half rep is not the last rep of a set, then the true half rep will be followed by a half)
        - half rep, end set (if the true half rep is the last rep of the set, then the true half rep will be followed by the end of the set)
    2. Some failures may not be detectable immediately after the completion of the rep, and instead require an indication that the a new rep is being started. Ex: Excessive retraction/extension at the rest position will only be detected after the proper motion of the rep has been completed.  
    
# 04-17-2019 Both:
- New Update Video. https://youtu.be/99L_uTlZNxg
               

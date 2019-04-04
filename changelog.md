03-06-2019 Ian Wilkins: -Finish project proposal draft
                        
03-07-2019 Ian Wilkins: -Begin prototyping microbit chain.
                        -Create initial mircobit reciever (receive -> write to serial) hex
                        -Create initial microbit middle link (receive -> package -> send) hex
                        -Create initial microbit end link (send via radio) hex
                        -Create initial python OSC server
                                          
03-12-2019 Ian Wilkins: -Update microbit middle link (receive -> package -> send) hex
                      
03-13-2019 Ian Wilkins: -Add link to GitHub repo to project proposal
                        -Add acceptance criteria to project milestones in project proposal
                        -Make final revisions to project proposal and submit to Moodle
                        
03-14-2019 Ian Wilkins: -After meeting with Ben, I have been shown that a microbit chain is not going to be as feasible as 
                         2 microbits communicating independently with the receiver.
                        -Begin prototyping signal strength reading
                        -Begin new python OSC server to handle new message format.
                        
03-14-2019 Garrett Sippel:-Wrote ocs handler

03-17-2019 Ian Wilkins: -Create first working microbit 'a' and 'b' hex
                        -Update python OSC server to interpret messages from microbit 'a' and 'b'
                        
03-20-2019 Both:        -Created youtube video
                        -Link: https://youtu.be/LxvbDUXSePE

03-25-2019 Ian Wilkins: - Create first glove and armband mount for 'a' and 'b' microbits. The following discoveries were made                             from these prototypes:
                          1. Thick/robust work gloves are more rigid (and therein easier to mount a microbit to), but limit                                dexterity during exercises, making them less ideal.
                          2. A loose fitting glove feels less awkward when a microbit is mounted, but poses potential safety                              issues when dealing with heavy weights (maximum grip strength is reduced).
                          3. It is VERY EASY to make an arm band that cuts off circulation. The current battey pack weighs                                enough that supporting it is problematic. Potential solutions include decreasing tension of the                              cuff, but increasing the total contact surface area.


03-27-2019 Ian Wilkins: - Create second glove and armband mount for 'a' and 'b' microbits. The following discoveries were                               made from these prototypes:
                          1. Thin and stretchy gloes have less restriction to dexterity, but are heard to mount a microbit                                to. The strech factor complicates using static mounting points. Too much stiching will snap when                              the glove is stretched, but too little stiching will not adequately constrain the microbit in 3D                              space.
                          2. A tight fitting glove holds the microbit mounting method closer to the skin. In order to reduce                              irritation, fine thread was used to adhere the microbit.
                          3. The battery pack is bulky, and position preference seems to change with each user. I need to                                find a way to have a repositional battery pack that is still safely secured. 
                          4. The next iteration of the upper arm cuff seemed promising until it was taken to the gym. An                                  unforseen problem was realized: the microbit needs to be able to be detached so the band can be                              cleaned (the band band will absorb sweat during a workout. Current material and design is not                                well suited for easy washing.
                          
04-02-2019 Ian Wilkins: - Create third glove and armband mount for 'a' and 'b' microbits. The following discoveries were                               made from these prototypes:
                          1. Constraining the microbits with the auxillary pins parallel to the knuckles on the ulnar side of                              the glove, and a slightly slackened thread through the power inpit connecting to the space                                    between the tendon of the thumb and the tendon of the forefinger provides adequate constraint,                                handles stretching well, and does not feel awkward during use.
                          2. A glove was found with a cuff material that adheres well to the hook side of a hook and loop                                  patch. The battery pack now has a hook patch added so it can bea easily repositioned anywhere on                              the cuff of the glove without adding extra bulk.
                          3. The glove is almost done, it now needs a way for the microbit to be detached when the glove is                                whashed.
                          4. The next iteration of the upper arm cuff used chicago screws to secure the microbit such that it                              could be detached for cleaning. The cuff needed to have gromets added to prevent fraying in the                              areas that the chicago screws went through. The gromets chose were very irritating during use.                                For the next iteration of the upper arm cuff, I plan on using a physical therapy light-duty                                  compression sleeve, and sewing a stretch compensated pocket for the microbit and battery pack.
               

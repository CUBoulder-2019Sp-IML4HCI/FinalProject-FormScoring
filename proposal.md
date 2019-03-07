# FinalProject-FormScoring


Ian Wilkins, Garrett Sippel
CSCI 4889
IML4HCI Final Project Proposal: Form Scoring Regressor

The Idea and Mission Statement:
Our goal is to create an interactive, wearable, accessory that can be trained to recognize proper form for a given exercise, and then score future motions of that exercise against the proper form. This system has implications in improving exercise quality, monitoring training progress, and preventing malform injury. The user will be able to train the model to their needs, including but not limited to, movement restraints for post injury physical therapy, speed restraints due to different movement arms from people of different shapes and sizes, and provide live feedback on form for people who are unable to monitor their movements due to constraint, injury, or disability.

Challenges you think you will have to overcome: 
There are 2 classes of challenge, physical and computational.

The greatest physical challenge will be designing an accessory that can be repeatedly secured in place, and stay in place during the movement of the exercise. If the user is unable to secure the accessory accurately and repeatedly, then the measurements may change due to movement of the device.

The greatest computational challenge will be capturing and processing the input features such that our regressor is sensitive to subtle changes in form. Many injuries and inefficiencies are from small changes in form, and our model must be able to detect these subtle changes to provide beneficial feedback and scoring to the user.

The technologies you think you will need:
At least three microbits, and a way to secure them to the user. Armbands are our initial thought. The software we will use is microbit’s Makecode. Python and something like scikit learn or keras for the ML portion. We will use Andriod Studio to make an app for the user to interact with the software. 

Risks to failure: 
The greatest risk of failure is the ability to determine subtle changes in form. Small changes in form must be capturable and distinguishable in order to accurately score the user’s exercise form. Furthermore, different users may have subtle changes in exercise form and exercise goals, and in order for the user to have a custom interactive experience, the system must be able to capture small changes in for between users.



Ethical questions - Human and Infrastructural:
People could potentially injure themselves while working out. Our current idea is to trust the user to know proper form while they are training the model. Once they are actually working out we will help them detect improper form based on their given proper form. A user could potentially train the model wrong and we would be telling the they are performing the exercise properly when they are not. Another problem is that they could train the model to an exercise where the improper form is too similar to the proper form for our model to tell. Then the program will keep telling them they are doing it correctly when they are not.

Open Source and Closed Source Components:
All of our code is open source, or at least not closed source.

The Timeline

The Concept Phase:
We started with two ideas whose infrastructures would be similar. First was the idea being out lined so far, which is to detect proper form for an exercise. The second would be to detect what trick was performed on a skateboard. If looking for proper form becomes to suddel of a change we may consider the trick idea.

Milestones:
Week 8 - Decide how our project will be customizable to the user, utilize embedded machine learning, and utilize sensors beyond standard computer peripherals.

The Planning Phase:
There are 2 goals of the planning phase: write a proposal to document our concept from the concept phase, and interview potential users about what exercises need the most form critique in order to determine what exercises should be used to evaluate our system.

Milestones:
Week 8 - Finish initial proposal draft by midnight at Wednesday.
Week 9 - Decide what exercises and exercise movement features will be used for evaluation. 

The Design & Development Phase:
The primary objectives of our design and development phase are to prototype and refine our physical accessory based on user testing, refine data handling and modelling based on evaluation metrics decided during planning, and to refine an accessible user interface.

Milestones:
Week 10 - Create rough accessory and begin data handling
Week 11 - First trained models with prototype accessory
Week 12 - Begin creating user interfaces, refine prototype accessory based on evaluation metrics
Week 13 - Finish user interfaces, finalize physical accessory
Week 14 - Full assembly evaluation. All pieces together and working.
Week 15 - Polish and finalize full system

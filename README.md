# thief-detector 

After watching Python courses, I've decided to put in practice some of the new knowledge that I acquired. That is the reason why I created this project. It has some functions and libraries that I used in these courses. Thief-Detector is a program which has the goal of make easier for the stores to detect if someone in the store is a recognized thief that stole in the past. This program has three different status for every person: no suspect, caution and warning. 

### Status - 🟢 

**No suspect**: Are the people who the store has not pictures in the files, that's mean, the person who is caught in the camera never stole something from the store and that's the reason why he/she will be shown with the green borders. It's important let know that maybe this person has never stolen in the store before but he/she can do it in the same moment that is in the store, in this case, the owner program can take the picture used before to save it to the future. - 🟠 

**Caution**: It is used for the people who have a similar aspect with some of the thief saved. It can be calculated thanks for the function "`face_distance()`" that give to the program the percentage of similarities between two photos. The people caught in this status will have the orange borders for alert to the store security of the person who entered. For make easier the comparison, the program will show two photo of the person who entered and another of the most similar thief. - 🔴 

**Warning**: Are the thieves, this status will be in the program only if the suspect is a thief saved in the files of the program and the program as caution's status happened, will be two photo, the registered and the taken in the moment. In this case the photo borders will be red. ## About policy This project hasn't any commercial purpose, it was done only to practice my knowledge that I acquired in the past and show it to the world, the use of celebrities pictures is only to make funnier this program with these examples. 

## How start the project After all this theoretical plan, the requirements that you need to use this project are: > ⚠️ 

**IMPORTANT** This project strictly use Python 3.10 to libraries compability 1. Install these packages if you didn't before: `pip install opencv-python face-recognition numpy` 2. Create a production environment: `py -3.10 -m venv venv >> .\venv\Scripts\activate` 3. Let's start the program: `py .\main.py`
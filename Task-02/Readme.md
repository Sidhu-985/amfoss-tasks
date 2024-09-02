# Terminal Chaos 

Oh boy oh boy this task was filled with chaos as it says. It took a long time but I finally managed ti crack the secret code and decode it to get  the github link which will lead to the goal of success. 

## Steps Taken To Complete the task:

### **Part 1**:
- This part is super easy we just navigate through the files of Arrakis-dex directory.
- Then I used the ```find``` command to find a file named parchment.txt and use ```cat``` command to print out the contents of that file in the terminal.

### **Part 2**:
- Use ```git checkout <branch-name>``` to change the branch from main to light-to-the-realm branch to find files that find all the files that contains both "good" and "holy" using ```grep -rlZ "good" * | xargs -0 grep -l "holy"```.
- Then I followed other regular steps asked on part 2.

### **Part 3**:
- Navigate to dark-Realm branch - Dark-Realm-I and Dark-Realm-II.
- Used command ```tree``` to find file named Celestial Veil Amulet.txt and print out the contents of the file to read the secret code inside it.

### **Part 4**:
- After finding and stroing all the codes in the **Handbook** directory we decode it using ``` echo <file-name> | base64 -d``` to get a github link.
- I navigated to that repository to find my next step.
- After cloning the new found repo I had to use ```git log``` to find history of commits taken place in this repository. While navigating through this after a long time I found a text containing another secret code. I copied that and decoded it to get a new repository. And this one finally lead to the portal of victory.
- After cloning this new repo I quickly activated the holy-spell using python command and completed my journey.

## Technical Difficulties:
- Consumed alot of time on part 2.
- Incorrect usage of certain commands.

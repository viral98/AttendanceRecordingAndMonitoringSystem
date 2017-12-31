# AttendanceRecordingAndMonitoringSystem
A attendance recording and monitoring system based off RFID's.

## Motivation
Consistency in attendance recording proves to be a difficult task in most institutes. On an average, lecturers spend 10 minutes per lecture behind taking attendace and chores related to it. These 10 minutes add up to hours when looking at the entire semester. Our project aims at reducing the time wasted in taking attendace and utilizing it towards the teaching learning process.
Further, we provide an intuitive user interface for the lecturers to manage and edit any records if needed.

## Problems we aim to tackle
- **Lack in consistency of attendance data collection**
    Often lecturers take attendance on a peice of paper and then later write it down on ledgers. These ledgers too lack consistency
    depending from institute to institute. We provide an optimized schema for storing all the attendance data in a consistent manner.
- **Time spent behind taking attendance**
    As mentioned above, on an average it takes close to 10 minutes per lecture behind logging down attendance. This time can be utilized in fruitful manner behind the actual teaching learnign process
- **Time spent behind processing the attendance data**
    The ledgers are used to manually calculate whether a student is a defaulter in a particular subject. This is a time consuming process and requires using human resources which could have been optimally used for other tasks. 
    All the processing on the attendance data can be done at a click of a button by the respective subject teacher or the head of the department.
    
## Detail
- **Data collection**
    The attendance data is collected using RFID tags which are assigned to each student just like their ID cards, these tags need to be swiped
    in front of a RFID reader connected a Raspberry Pi (Model 2) which is present in every Lecture room and practical Lab. Each Raspberry Pi has a locally
    hosted database which stores the timetable for the particular lecture room. 
- **Data storage**
    Each Raspberry Pi is connected wirelessly to a central MySQL server which has student data pre loaded against which these Raspberry Pi's mark Absent/Present.
    This data storage (a database commit) happens only after a teacher reads his/her card. This is to ensure that the data gets committed only on the lecturer's consent. 
- **Data Retrival**
    Data can be retrived by a locally hosted web application which is built using PHP, HTML & CSS. Material design guidelines have been followed to ensure the best UI/UX. 
    Data can be retrived in any manner the teacher demands, various drill down and roll up options are provided.
 
## About Us
We are a team of 3 students from Shri Bhagubhai Mafatlal Polytechnic (At the time of making this project), Mumbai.
The team members are named, Maithili Bhuta, Monil Shah and Viral Tagdiwala

Viral is a third year student who specializes in network security. He also has keen interests in web development.

Monil is a third year student who also specializes in backend web development in PHP.

Maithili is a third year student who has keen interests in web development specializing in front-end web development and PHP.
    




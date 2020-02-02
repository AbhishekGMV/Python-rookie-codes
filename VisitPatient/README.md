### Description

Idea of this project is to facilitate a better way of visiting a patient in a hospital general ward, It avoids crowding of visitors in general ward which may disturb the patient in anyway.
Following steps occur in the process:
  • Receptionist maintains information of the in-patients of the hospital.
  • Visitor enquires the receptionist about the patient, If the patient is admitted
  • Receptionist enquires visitor for necessary information.
  • Generates a QR code based on bed number of respective patients.
  • SMS will be sent to visitor’s phone number about the visiting time.
  • An access device is maintained at the entrance of the ward which scans the QR code. (But this was quite beyond scope of this             project, it involves programming of hardware like Arduino board and raspberry pi.)
  • Visitor will receive an automated call before 5 minutes of end of visiting time.
  
  
  
### Actors on the scene

•	Receptionist – Maintains record of patient, communicates to visitor for information and generates QR code and facilitates automated SMS and Call services
•	Visitor –   Enquires receptionist for details of patient and visits patient.



### Tech stack used

[Twilio Rest API](https://www.twilio.com/)

*Twilio SMS and call services* were utilized to alert user about visiting time to visitor.
The phone number has to be a Registered to Twilio account and obtain SID, token and a ‘from’ number (had to be provided as input to the program).



### Advantages
 Reduces paper work! (Eco-friendly)
	QR will be sent to visitor’s phone number.
	In worst case (visitor who doesn’t have a phone), Hard copy of QR code will be provided.

 Improves Quality of business
	Technology helps reduce Man power.
	Reduces cost of maintenance.


### Instructions to run the program 

Program takes in following inputs upon running:
•	Number of patients to be registered and,
•	Name of the patient
•	Bed number
•	Status (0 - admitted or 1 - discharged) respectively 

Above input maintain Register of patients. Now the visitor enquires the receptionist about the patient, receptionist takes following input to check and facilitate the visit if patient is admitted.

•	Name of the patient 
•	Phone number 
•	SID, Authorization token and a from number (Twilio Account) 
•	Visiting time in minutes

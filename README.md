# CS-340-Module-Four
CS 340 README 

About the Project/Project Title
CRUD Python Module for Grazioso Salvare
This project is a Python-based CRUD module developed as part of CS 340 for the Grazioso Salvare project. The module provides an interface for interacting with a MongoDB database using Python. At this stage, the module supports Create and Read operations, allowing records to be inserted into and retrieved from the database securely and efficiently.
The goal of this module is to separate database logic from application logic, making the system easier to maintain, test, and extend as additional functionality is added in later milestones.

Motivation
The motivation behind this project is to create a reusable and maintainable data access layer that follows software engineering best practices. By isolating database operations in a dedicated module, the application becomes more secure, easier to debug, and simpler to scale.
This approach also prepares the project for future enhancements, including Update and Delete functionality, without requiring major changes to the existing application structure.

Getting Started
To get a local copy up and running, follow these simple steps.
This project requires a MongoDB database with authentication enabled and a Python environment configured with the appropriate libraries. The CRUD module connects to the database using a non-admin user account created during the Module Three milestone.
Before running the module, ensure that MongoDB is running and that the user credentials used in the connection string have read and write permissions on the target database.

Installation
Required Tools
•	Python 3
Used as the primary programming language due to its readability and strong support for database integration.
•	MongoDB
Used as the NoSQL database for storing and managing animal shelter data.
•	PyMongo
The official MongoDB driver for Python, used to connect to and interact with the database.
•	Codio Development Environment
Used for development and testing as provided by SNHU.
Installation Steps
1.	Install Python 3 if it is not already installed.
2.	Install the PyMongo library using pip: pip install pymongo
3.	Ensure MongoDB is running with authentication enabled.
4.	Place the CRUD Python module file in your project directory.





Usage
The CRUD module is used by importing the class and calling its methods to perform database operations.
Create Operation Example
from CRUD_Python_Module import AnimalShelter

shelter = AnimalShelter()

test_doc = {
    "animal_id": "CS340TEST01",
    "animal_type": "Dog",
    "name": "TestDog",
    "breed": "Mixed",
    "outcome_type": "Adoption"
}

print("Create result:", shelter.create(test_doc))

results = shelter.read({"animal_id": "CS340TEST01"})
print("Records found:", len(results))
print(results[:1])

Code Example
The following example demonstrates the core functionality of the module by showing how data is created and retrieved from the database using a clean and simple interface.
shelter = AnimalShelter("aacuser", "password")
shelter.create({"animal_type": "Cat", "name": "Whiskers"})
animals = shelter.read({"animal_type": "Cat"})
This example highlights how the module abstracts database logic while remaining easy to use.

Tests
Test results are shown in the Screenshots section, confirming successful insertion and retrieval of records.
 <img width="975" height="339" alt="image" src="https://github.com/user-attachments/assets/e3685fe6-de34-482e-afd9-4ff5aac06122" />






Screenshots
The screenshot below demonstrates successful execution of the Create and Read operations. A test document is inserted into the MongoDB collection, and a query confirms that matching records are returned from the database.
<img width="975" height="633" alt="image" src="https://github.com/user-attachments/assets/14d8a2dd-b513-4db1-b199-cc48d7b7a694" />


 


Contact
Your name: ADIL PATEL

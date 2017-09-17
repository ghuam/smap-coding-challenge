=========================================
SMAP Energy Coding Challenge
Submitted by: Amitabh Ghuwalewala (ghuam)
=========================================

Architecture:
	Front-end:
		The front-end is dependant on CanvasJS to draw the required line chart.
		2 files:
		
		- layout.html (links to CanvasJS)
		- summary.html (invokes CanvasJS)
		
		are resposible for handling the "consumption" app's "summary" view.
		CanvasJS is responsible for visualizing the total consumption by user
		data. This information is also tabulated below the line chart.
	
	Back-end:
		The function which handles the "summary" view simply fetches the total
		consumption data by user. It is dependant on the User and Consumption
		models (defined in models.py).
		
		The SQLite DB is populated a priori by calling the Django management
		command:
		
		python manage.py import
		
		in the project directory. The Django management command will read the CSV
		files and insert the data into the SQLite DB using Django's ORM.

The optional "detail" view has not been implemented.
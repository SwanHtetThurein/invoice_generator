# Flask Invoice Generator

This is a simple Flask web application that generates PDF invoices based on user input. It uses the WeasyPrint library to convert HTML templates to PDF files.

## Features

- Dynamic generation of invoices with customizable details.
- Responsive HTML template for clean and professional-looking invoices.
- PDF generation using WeasyPrint.
- Supports both JSON data and form data input.

## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.x
- Flask
- WeasyPrint
- Other dependencies (specified in requirements.txt)

## Usage
Clone the Repository. Open your terminal or command prompt and navigate to the Project Directory and install the dependencies using 
````pip install -r requirements.txt.````
Then type
````python app.py````
and the app will create a pdf file in your folder. 

## Customization
Invoice Template: The default template is located in the templates/invoice.html file. Customize this file to change the layout of your invoices.
Default Data: You can modify the default data in app.py to set initial values for the invoice.

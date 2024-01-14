from flask import Flask, render_template, send_file, request
from datetime import datetime
from weasyprint import HTML 
import io
import os 

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    # Extract JSON data from the request or use an empty dictionary if not present
    posted_data = request.get_json() or {}
    
    # Get the current date
    today = datetime.today().strftime("%B %-d, %Y")

    # Default data for the invoice
    default_data = {
        'duedate': 'August 1, 2019',
        'from_addr': {
            'addr1': '12345 Sunny Road',
            'addr2': 'Sunnyville, CA 12345',
            'company_name': 'Python Tip'
        },
        'invoice_number': 123, 
        'items': [
            {
                'charge': 300.0,
                'title': 'website design'
            },
            {
                'charge': 75.0,
                'title': 'Hosting(3 months)'
            },
            {
                'charge': 10.0,
                'title': 'Domain name (1 year)'
            }
        ],
        'to_addr': {
            'company_name': 'Acme Corp',
            'person_email': 'john@example.com',
            'person_name': 'John Dilly'
        }
    }

    # Extract data from the request or use default values
    duedate = posted_data.get('duedate', default_data['duedate'])
    from_addr = posted_data.get('from_addr', default_data['from_addr'])
    to_addr = posted_data.get('to_addr', default_data['to_addr'])
    invoice_number = posted_data.get('invoice_number', default_data['invoice_number'])
    items = posted_data.get('items', default_data['items'])

    # Calculate the total charge for items
    total = sum([i['charge'] for i in items])

    # Render the HTML template using Jinja variables
    rendered = render_template('invoice.html',
                               date=today,
                               from_addr=from_addr,
                               to_addr=to_addr,
                               items=items,
                               total=total,
                               invoice_number=invoice_number,
                               duedate=duedate)
    
    # Print the rendered HTML for debugging (optional)
    print(rendered)

    # Convert HTML template to PDF using WeasyPrint 
    html = HTML(string=rendered)
    rendered_pdf = html.write_pdf()  # No arguments were passed to render PDF in memory (instead of writing to disk)

    # Send the generated PDF to the client 
    return send_file(
        io.BytesIO(rendered_pdf),
        attachment_filename='invoice.pdf'
    )

if __name__ == '__main__':
    # Set the port to the environment variable PORT or default to 5000
    port = int(os.environ.get("PORT", 5000))
    # Run the Flask app
    app.run(host='0.0.0.0', port=port)

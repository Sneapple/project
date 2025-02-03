import logging

# Set up logging
logging.basicConfig(
    level=logging.DEBUG,  # You can set it to INFO or ERROR depending on your needs
    format='%(asctime)s - %(levelname)s - %(message)s',  # Log format
    handlers=[
        logging.StreamHandler(),  # Logs to console
        logging.FileHandler('app.log')  # Logs to a file 'app.log'
    ]
)

def generate_report(data):
    """
    Function to generate a report based on provided data.
    """
    try:
        logging.info("Starting to generate the report.")
        # Your report generation code here
        if not data:
            logging.warning("No data provided for report generation.")
        else:
            # Logic to generate report
            logging.info(f"Report generated successfully with {len(data)} items.")
    except Exception as e:
        logging.error(f"Error generating the report: {e}")
        raise

def main():
    """
    Main function where the report is generated.
    """
    logging.info("Program started.")
    sample_data = ["item1", "item2", "item3"]
    generate_report(sample_data)
    logging.info("Program finished.")
    
if __name__ == '__main__':
    main()

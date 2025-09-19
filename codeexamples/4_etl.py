# Extract data from the raw_data.csv file
def extract(file_name):
  return pd.read_csv(file_name)
  
  # Write cleaned_data to a CSV using file_name
  data_frame.to_csv(file_name)
  print(f"Successfully loaded data to {file_name}")

extracted_data = extract(file_name="raw_data.csv")

# Transform the extracted_data
def transform(data_frame):
  return data_frame.loc[:, ["industry_name", "number_of_firms"]]
try:
    clean_sales_data = transform(extracted_data)
    logging.info("Successfully filtered DataFrame by 'Total Price'")
except KeyError as ke:
    logging.warning(f"{ke}: Cannot filter DataFrame by 'Total Price'")

transformed_data = transform(data_frame=extracted_data)

# Load the transformed_data to cleaned_data.csv

def load(data_frame, file_name):
  data_frame.to_csv(file_name)

cleaned_data = load(data_frame=transformed_data, target_table="cleaned_data")

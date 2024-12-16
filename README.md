# **Census-Data-Standardization-and-Analysis-Pipeline**

### *Project Overview*  
This project is designed to standardize, process, and analyze census data to ensure its uniformity, accuracy, and accessibility for advanced analysis and visualization. By leveraging Python, Pandas, SQL, MongoDB, and Streamlit, this pipeline cleans, processes, and organizes raw census data into a structured format suitable for deriving insights and making data-driven decisions.

##  <ins>*Key Features:*</ins> 
  
  ### Data Cleaning and Standardization:
  ##### *Column Renaming:*
  * *Standardize column names for better consistency and readability.* 
  ##### State/UT Name Formatting:
  * *Normalize state and union territory names to ensure uniformity across datasets.*
### Handling State/UT Formation:
* *Account for the formation of new states like Telangana (2014) and Ladakh (2019) by appropriately renaming districts in the dataset based on their updated state/UT affiliation.*
### Missing Data Processing:
* *Identify missing data and calculate the percentage of incomplete data for each column.*
* *Fill missing values using logical relationships within the data (e.g., population = sum of male and female populations).*
* *Compare missing data statistics before and after the data-filling process.*
### Data Storage and Integration:
* *Save cleaned data into a MongoDB collection named census.*
* *Fetch data from MongoDB and upload it into a relational database with appropriate table structures, including primary and foreign key constraints.*
### Interactive Querying and Visualization:
* *Perform SQL queries on the relational database to derive meaningful insights.*
* *Display query results and visualizations using Streamlit, enabling easy exploration and analysis of the data.*

## Task 1: Rename Columns
* *Rename columns to ensure consistent and meaningful naming conventions, ensuring no name exceeds 60 characters.*
<br/>

## Task 2: Rename State/UT Names
* *Format state and UT names in Title Case, replace & with and, and follow specific capitalization rules for words like "and".*
<br/>

## Task 3: Handle New State/UT Formations
* *Rename districts based on their affiliation to newly formed states/UTs like Telangana and Ladakh.*
<br/>

## Task 4: Handle Missing Data
* *Calculate missing data percentages, fill missing values logically, and compare pre- and post-filling statistics.*
<br/>

## Task 5: Save Data to MongoDB
* *Store the cleaned dataset in a MongoDB collection named census.*
<br/>

## Task 6: Database Connection and Upload
* *Fetch data from MongoDB and upload it to a relational database, maintaining proper schema structure with constraints.*
<br/>

## Task 7: Streamlit Dashboard
* *Run complex SQL queries on the data and visualize results interactively using Streamlit.*
<br/>

# <ins> *Technologies Used*<ins>
##### * *Python :  Data processing and integration.*
##### * *Pandas :  Data cleaning and transformation.*
##### * *SQL :   Querying and relational database management.*
##### * *MongoDB :  NoSQL database for storing processed data.*
##### * *Streamlit :  Interactive data visualization and dashboarding.*


<br/>
 

  ### How to Run the Project
  #### <ins> *Set up the Environment:* </ins>
  *Install required Python libraries using pip install python, pandas, sql, mongodb, streamlit  requirements.txt.*
  #### <ins> *Run the Pipeline:* </ins>
*Clean and process the data by running the provided Python scripts in sequential order.*
  #### <ins>*Data Storage:*</ins>
*Ensure MongoDB and the relational database are set up for data storage.*
  #### <ins>*Streamlit Dashboard:*</ins>
*Launch the Streamlit dashboard with streamlit run app.py for data exploration and visualization.*

















  

# Install necessary libraries

# pip install pandas
# pip install docx2txt
# pip install mysql-connector-python
# pip install pymongo
# pip install flask_sqlalchemy
# pip install mysql
# pip install streamlit as st
# python -m pip install "pymongo[srv]"

# import necessary libraries like pandas as numpy
import pandas as pd
from turtle import st
import docx2txt
import pymongo  # noqa: F401


df=pd.read_csv(r"D:\census\Input\census_2011.csv")


# Rename each column and commiting the changes using inplace
df.rename(columns = {'State name':'State/UT'},inplace=True)  
df.rename(columns = {'District name':'District'},inplace=True)
df.rename(columns = {'Male_Literate':'Literate_Male'},inplace=True)
df.rename(columns = {'Female_Literate':'Literate_Female'},inplace=True)
df.rename(columns = {'Rural_Households':'Households_Rural'},inplace=True)
df.rename(columns = {'Urban_Households':'Households_Urban'},inplace=True)
df.rename(columns = {'Age_Group_0_29':'Young_and_Adult'},inplace=True)
df.rename(columns = {'Age_Group_30_49':'Middle_Aged'},inplace=True)
df.rename(columns = {'Age_Group_50':'Senior_Citizen'},inplace=True)
df.rename(columns = {'Age not stated':'Age_Not_Stated'},inplace=True)

# Display all the columns that are renamed
# df[['State/UT','District','Literate_Male','Literate_Female','Households_Rural','Households_Urban',
#     'Young_and_Adult','Middle_Aged','Senior_Citizen','Age_Not_Stated']]

# Rename all the State/UT according to the task
def format(state):
  a=state.split()
  b=[]
  for i in a:
    if i.lower()=='and':
      b.append('and')
    else:
      b.append(i.capitalize())
  return ' '.join (b)

df['State/UT'] = df['State/UT'].apply(format)
# Display all distinct State/UT and check if they are renamed accordingly
df.filter(items=['State/UT']).drop_duplicates()

#Read the Telangana_file
Telangana_file = docx2txt.process(r"D:\Downloads\Telangana.docx")

# Function to change the State/UT according to the District
def remake(district):
  if district['State/UT'] == 'Andhra Pradesh' and district['District'] in Telangana_file:
    return 'Telangana'
  return district['State/UT']

df['State/UT'] = df.apply(remake, axis=1)
# To check if they are changed accordingly
df1=df[df['State/UT'].str.contains('Telangana')]
df1.filter(items=['State/UT', 'District']).drop_duplicates()

ladakh_districts = ['Leh(Ladakh)','Kargil']
# Function to change the State/UT according to the District
def updated(districts):
  if districts['State/UT'] == 'Jammu and Kashmir' and districts['District'] in ladakh_districts:
    return 'Ladakh'
  return districts['State/UT']

df['State/UT'] = df.apply(updated, axis=1)
df2 = df[df['State/UT'].str.contains('Ladakh')]
df2.filter(items=['State/UT', 'District']).drop_duplicates()

df['Population'] = df['Population'].fillna(df['Male'] + df['Female'])
df['Male'] = df['Male'].fillna(df['Population'] - df['Female'])
df['Female'] = df['Female'].fillna(df['Population'] - df['Male'])
df['Population'] = df['Population'].fillna(df['Middle_Aged'] + df['Senior_Citizen']+df['Age_Not_Stated']+df['Young_and_Adult'])

df['Literate'] = df['Literate'].fillna(df['Literate_Male'] + df['Literate_Female'])
df['Literate_Male'] = df['Literate_Male'].fillna(df['Literate'] - df['Literate_Female'])
df['Literate_Female'] = df['Literate_Female'].fillna(df['Literate'] - df['Literate_Male'])

df['SC'] = df['SC'].fillna(df['Male_SC'] + df['Female_SC'])
df['Female_SC'] = df['Female_SC'].fillna(df['SC'] - df['Male_SC'])
df['Male_SC'] = df['Male_SC'].fillna(df['SC'] - df['Female_SC'])

df['ST'] = df['ST'].fillna(df['Male_ST'] + df['Female_ST'])
df['Female_ST'] = df['Female_ST'].fillna(df['ST'] - df['Male_ST'])
df['Male_ST'] = df['Male_ST'].fillna(df['ST'] - df['Female_ST'])

df['Workers'] = df['Workers'].fillna(df['Male_Workers'] + df['Female_Workers'])
df['Female_Workers'] = df['Female_Workers'].fillna(df['Workers'] - df['Male_Workers'])
df['Male_Workers'] = df['Male_Workers'].fillna(df['Workers'] - df['Female_Workers'])

df["Main_Workers"]= df['Main_Workers'].fillna(df['Population']-(df["Non_Workers"]+ df["Cultivator_Workers"]+ df["Agricultural_Workers"]+ df["Household_Workers"]+ df["Other_Workers"]))
df["Non_Workers"]= df['Non_Workers'].fillna(df['Population']-(df["Main_Workers"]+ df["Cultivator_Workers"]+ df["Agricultural_Workers"]+ df["Household_Workers"]+ df["Other_Workers"]))
df["Cultivator_Workers"]= df['Cultivator_Workers'].fillna(df['Population']-(df["Non_Workers"]+ df["Main_Workers"]+ df["Agricultural_Workers"]+ df["Household_Workers"]+ df["Other_Workers"]))
df["Agricultural_Workers"]= df['Agricultural_Workers'].fillna(df['Population']-(df["Non_Workers"]+ df["Cultivator_Workers"]+ df["Main_Workers"]+ df["Household_Workers"]+ df["Other_Workers"]))
df["Household_Workers"]= df['Household_Workers'].fillna(df['Population']-(df["Non_Workers"]+ df["Cultivator_Workers"]+ df["Agricultural_Workers"]+ df["Main_Workers"]+ df["Other_Workers"]))
df["Other_Workers"]= df['Other_Workers'].fillna(df['Population']-(df["Non_Workers"]+ df["Cultivator_Workers"]+ df["Agricultural_Workers"]+ df["Household_Workers"]+ df["Main_Workers"]))

df["Hindus"]= df["Hindus"].fillna(df["Population"]-(df["Muslims"]+ df["Christians"]+ df["Sikhs"]+ df["Buddhists"]+ df["Jains"]+ df["Others_Religions"]+ df["Religion_Not_Stated"]))
df["Muslims"]= df["Muslims"].fillna(df["Population"]-(df["Hindus"]+ df["Christians"]+ df["Sikhs"]+ df["Buddhists"]+ df["Jains"]+ df["Others_Religions"]+ df["Religion_Not_Stated"]))
df["Christians"]= df["Christians"].fillna(df["Population"]-(df["Muslims"]+ df["Hindus"]+ df["Sikhs"]+ df["Buddhists"]+ df["Jains"]+ df["Others_Religions"]+ df["Religion_Not_Stated"]))
df["Sikhs"]= df["Sikhs"].fillna(df["Population"]-(df["Muslims"]+ df["Christians"]+ df["Hindus"]+ df["Buddhists"]+ df["Jains"]+ df["Others_Religions"]+ df["Religion_Not_Stated"]))
df["Buddhists"]= df["Buddhists"].fillna(df["Population"]-(df["Muslims"]+ df["Christians"]+ df["Sikhs"]+ df["Hindus"]+ df["Jains"]+ df["Others_Religions"]+ df["Religion_Not_Stated"]))
df["Jains"]= df["Jains"].fillna(df["Population"]-(df["Muslims"]+ df["Christians"]+ df["Sikhs"]+ df["Buddhists"]+ df["Hindus"]+ df["Others_Religions"]+ df["Religion_Not_Stated"]))
df["Others_Religions"]= df["Others_Religions"].fillna(df["Population"]-(df["Muslims"]+ df["Christians"]+ df["Sikhs"]+ df["Buddhists"]+ df["Jains"]+ df["Hindus"]+ df["Religion_Not_Stated"]))
df["Religion_Not_Stated"]= df["Religion_Not_Stated"].fillna(df["Population"]-(df["Muslims"]+ df["Christians"]+ df["Sikhs"]+ df["Buddhists"]+ df["Jains"]+ df["Others_Religions"]+ df["Hindus"]))

df["Total_Education"] = df['Total_Education'].fillna(df["Literate_Education"]+df["Illiterate_Education"])
df["Literate_Education"] = df['Literate_Education'].fillna(df["Total_Education"]-df["Illiterate_Education"])
df["Illiterate_Education"] = df['Illiterate_Education'].fillna(df["Total_Education"]-df["Literate_Education"])

df['Households'] = df['Households'].fillna (df['Households_Rural']+df['Households_Urban'])
df['Households_Rural'] = df['Households_Rural'].fillna (df['Households']-df['Households_Urban'])
df['Households_Urban'] = df['Households_Urban'].fillna (df['Households']-df['Households_Rural'])

Population = df['Population'].isnull().sum() * 100 / len(df)
Male = df['Male'].isnull().sum() *100 / len(df)
Female = df['Female'].isnull().sum() *100 /len(df)

Literate = df['Literate'].isnull().sum() * 100 / len(df)
Literate_Male = df['Literate_Male'].isnull().sum() * 100 / len(df)
Literate_Female = df['Literate_Female'].isnull().sum() * 100 / len(df)

SC = df['SC'].isnull().sum() * 100 / len(df)
Male_SC= df['Male_SC'].isnull().sum() * 100 / len(df)
Female_SC = df['Female_SC'].isnull().sum() * 100 / len(df)

ST = df['ST'].isnull().sum() * 100 / len(df)
Male_SC= df['Male_ST'].isnull().sum() * 100 / len(df)
Female_SC = df['Female_ST'].isnull().sum() * 100 / len(df)

Workers = df['Workers'].isnull().sum() * 100 / len(df)
Male_Workers= df['Male_Workers'].isnull().sum() * 100 / len(df)
Female_Workers= df['Female_Workers'].isnull().sum() * 100 / len(df)

Main_Workers = df['Main_Workers'].isnull().sum() * 100 / len(df)
Non_Workers= df['Non_Workers'].isnull().sum() * 100 / len(df)
Cultivator_Workers= df['Cultivator_Workers'].isnull().sum() * 100 / len(df)
Agricultural_Workers = df['Agricultural_Workers'].isnull().sum() * 100 / len(df)
Household_Workers= df['Household_Workers'].isnull().sum() * 100 / len(df)
Other_Workers= df['Other_Workers'].isnull().sum() * 100 / len(df)

Hindus = df['Hindus'].isnull().sum() * 100 / len(df)
Muslims= df['Muslims'].isnull().sum() * 100 / len(df)
Christians= df['Christians'].isnull().sum() * 100 / len(df)
Sikhs = df['Sikhs'].isnull().sum() * 100 / len(df)
Buddhists= df['Buddhists'].isnull().sum() * 100 / len(df)
Jains= df['Jains'].isnull().sum() * 100 / len(df)
Others_Religions = df['Others_Religions'].isnull().sum() * 100 / len(df)
Religion_Not_Stated = df['Religion_Not_Stated'].isnull().sum() * 100 / len(df)

Total_Education = df['Total_Education'].isnull().sum() * 100 / len(df)
Literate_Education = df['Literate_Education'].isnull().sum() * 100 / len(df)
Illiterate_Education = df['Illiterate_Education'].isnull().sum() * 100 / len(df)

Households = df['Households'].isnull().sum() * 100 / len(df)
Households_Rural = df['Households_Rural'].isnull().sum() * 100 / len(df)
Households_Urban = df['Households_Urban'].isnull().sum() * 100 / len(df)

# MongoDB connection
from pymongo.mongo_client import MongoClient  # noqa: E402
from pymongo.server_api import ServerApi  # noqa: E402

uri = "mongodb+srv://Rameeza:1040@cluster0.mfh68.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
    
# Create Database
mongo_db = client['Census_Data']

# Create collection
mongo_collection = mongo_db['Census']

df_dict =df.to_dict('records')

# Insert the data in your collection
mongo_collection.insert_many(df_dict)

mongo_data = list(mongo_collection.find({},{"_id":0}))

# Convert MongoDB data to DataFrame
df_mongo = pd.DataFrame(mongo_data)

df.rename(columns = {'Households_with_TV_Computer_Laptop_Telephone_mobile_phone_and_Scooter_Car':'household_with_tv'},inplace=True)

df.rename(columns = {'Main_source_of_drinking_water_Other_sources_Spring_River_Canal_Tank_Pond_Lake_Other_sources__Households':'Main_source_of_drinking_water_Other_sources'},inplace=True)

df.rename(columns = {'Main_source_of_drinking_water_Other_sources_Spring_River_Canal_Tank_Pond_Lake_Other_sources__Househo':'Main_source_of_drinking_water'},inplace=True)

df.rename(columns = {'Main_source_of_drinking_water_Other_sources_Spring_River_Canal_Tank_Pond_Lake_Other_sources__Househo':'Main_source'},inplace=True)

df.rename(columns = {'Main_source_of_drinking_water_Handpump_Tubewell_Borewell_Households':'Main_source_of_drinking_water'},inplace=True)

df.rename(columns = {'Type_of_latrine_facility_Night_soil_disposed_into_open_drain_Households':'Type_latrine_facility_soildisposed'}, inplace = True)

df.rename(columns = {'Type_of_latrine_facility_Flush_pour_flush_latrine_connected_to_other_system_Households':'Type_latr_flush_otherhouseholds'},inplace=True)

df.rename(columns = {'Not_having_latrine_facility_within_the_premises_Alternative_source_Open_Households':'Not_having_latrine_premise'},inplace=True)

import mysql.connector  # noqa: E402
import sqlalchemy  # noqa: E402, F401
import pandas as pd  # noqa: E402
from sqlalchemy import create_engine  # noqa: E402

# Replace <PASSWORD> with your actual password
user = "root"
password = "12345"
host = "localhost"
database = "census"


# Create an SQLAlchemy engine
engine = create_engine('mysql+mysqlconnector://root:12345@localhost/census', echo=True)
print('engineConnection:',engine)

def clean_column_name(name):
    # Replace spaces and periods with underscores
    name = name.replace(" ", "_").replace(".", "_")
    # Shorten the name to 64 characters if necessary
    if len(name) > 64:
        name = name[:64]
    return name
df1.columns = [clean_column_name(col) for col in df1.columns]

print('df1.columns:',df1.columns)

# Insert data into MySQL using pandas
df.to_sql("Census_rameeza", con=engine, if_exists="replace", index=False)
print("Data inserted into MySQL successfully!")

import mysql.connector  # noqa: E402, F811
import pandas as pd  # noqa: E402
import streamlit as st  # noqa: E402, F811

# Function to establish database connection
def get_connection():
    return mysql.connector.connect(
        user="root",
        password="12345",
        host="localhost",
        port=3306,
        database="census"
    )

# Function to fetch data from database
def get_data(query, connection):  # noqa: F811
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    return pd.DataFrame(result, columns=columns)
  
# Establish connection
connection = get_connection()

# Query 1: Total Population
st.title("Total Population of Each District")
query = """SELECT District, SUM(Population) AS Total_Population FROM Census_rameeza GROUP BY District;"""
df = get_data(query, connection)
st.dataframe(df)

# Query 2: Literate Males and Females
query_2 = """SELECT District, SUM(Literate_Male) AS Total_Literate_Males, SUM(Literate_Female) AS Total_Literate_Females FROM Census_rameeza GROUP BY District;"""
df = get_data(query_2, connection)
st.title("Literate Males and Literate Females in Each District")
st.dataframe(df)

# Query 3: Males_workers and Females
query_3 = """SELECT District, SUM(Male_Workers + Female_Workers) AS Total_Workers, 
SUM(Population) AS Total_Population, 
ROUND((SUM(Male_Workers + Female_Workers) / SUM(Population)) * 100, 2) AS Percentage_Workers FROM Census_rameeza GROUP BY District;"""
df = get_data(query_3, connection)
st.title("Males_workers and Females_workers in Each District")
st.dataframe(df)

# Query 4:Households have access to LPG or PNG as a cooking fuel in each district
query_4 = """SELECT District, LPG_or_PNG_Households FROM census_rameeza;"""
df = get_data(query_4, connection)
st.title("LPG or PNG as a cooking fuel in each District")
st.dataframe(df)

# Query 5: Religious composition(Hindus, Muslims, Christians, Sikhs, Buddhists, Jains, Others_Religions, Religion_Not_Stated) of each district
query_5 = """SELECT District, Hindus, Muslims, Christians, Sikhs, Buddhists, Jains, Others_Religions, Religion_Not_Stated FROM census_rameeza;"""
df = get_data(query_5, connection)
st.title("Religious composition(Hindus, Muslims, Christians, Sikhs, Buddhists, Jains, Others_Religions, Religion_Not_Stated")
st.dataframe(df)

# Query 6:Households have internet access in each district
query_6 = """SELECT District, Households_with_Internet FROM census_rameeza;"""
df = get_data(query_6, connection)
st.title("Households have internet access in each district")
st.dataframe(df)

# Query 7:The educational attainment distribution(below primary, primary, middle, secondary, etc.)in each district 
query_7 = """SELECT District,Below_Primary_Education,Primary_Education,Middle_Education,Secondary_Education,Higher_Education,Graduate_Education,Other_Education FROM census_rameeza;"""
df = get_data(query_7, connection)
st.title("The educational attainment distribution in each district ")
st.dataframe(df)

# Query 8:Households have access to various modes of transportation (bicycle, car, radio, television, etc.) in each district
query_8 = """SELECT District, Households_with_Bicycle, Households_with_Car_Jeep_Van, Households_with_Scooter_Motorcycle_Moped FROM census_rameeza;"""
df = get_data(query_8, connection)
st.title("Households access to various modes of Transportation")
st.dataframe(df)

# Query 9: The condition of occupied census houses(dilapidated, with separate kitchen, with bathing facility, with latrine facility, etc.) in each district
query_9 = """SELECT District, Condition_of_occupied_census_houses_Dilapidated_Households as Dilapidated,
Households_with_separate_kitchen_Cooking_inside_house as Separate_Kitchen, 
Having_bathing_facility_Total_Households as Bathing_Facility, 
Having_latrine_facility_within_the_premises_Total_Households as Laterin_within_premis,
Not_having_bathing_facility_within_the_premises_Total_Households as Bathing_facility_NotIn_Premises,
Not_having_latrine_premise as Not_latrine_premises FROM census_rameeza;"""
df = get_data(query_9, connection)
st.title("The condition of occupied census houses")
st.dataframe(df)

# Query 10: The Household size distributed (1 person, 2 persons, 3-5 persons, etc.) in each district
query_10 = """SELECT District, Household_size_1_person_Households as 1_Person, Household_size_2_persons_Households as 2_Persons,  Household_size_3_persons_Households as 3_Persons, Household_size_4_persons_Households as 4_Persons, Household_size_5_persons_Households as 5_Persons, Household_size_6_8_persons_Households as 6to8_Persons, Household_size_9_persons_and_above_Households as 9_and_more_Persons FROM census_rameeza;"""
df = get_data(query_10, connection)
st.title("The household size distributed (1 person, 2 persons, 3-5 persons, etc.) in each district")
st.dataframe(df)

# Query 11:The total number of households in each state
query_11 = """SELECT 'State/UT', SUM(Households)as Total_Households FROM census_rameeza GROUP BY 'State/UT';"""
df = get_data(query_11, connection)
st.title("The total number of households in each state")
st.dataframe(df)

# Query 12: Households have a latrine facility within the premises in each state
query_12 = """SELECT 'State/UT', SUM(Having_latrine_facility_within_the_premises_Total_Households) as Premises_Laterine FROM census_rameeza GROUP BY 'State/UT';"""
df = get_data(query_12, connection)
st.title("Households have a latrine facility within the premises in each state")
st.dataframe(df)

# Query 13:The average household size in each state
query_13 = """SELECT 'State/UT', AVG(Household_size_1_person_Households) as "1-Person", 
AVG(Household_size_2_persons_Households) as "2-Persons", 
AVG(Household_size_3_persons_Households) as "3-Persons", 
AVG(Household_size_4_persons_Households) as "4-Persons",
Avg(Household_size_5_persons_Households) as "5-Persons", 
AVG(Household_size_6_8_persons_Households) as "6to8-Persons", 
AVG(Household_size_9_persons_and_above_Households) as "9 and more Persons" FROM census_rameeza GROUP BY 'State/UT';"""
df = get_data(query_13, connection)
st.title("The average household size in each state")
st.dataframe(df)

# Query 14:Households are owned versus rented in each state
query_14 = """SELECT 'State/UT', SUM(Ownership_Owned_Households) as "Owned",
SUM(Ownership_Rented_Households) as "Rented" FROM census_rameeza GROUP BY 'State/UT';"""
df = get_data(query_14, connection)
st.title("Households are owned versus rented in each state")
st.dataframe(df)

# Query 15:The distribution of different types of latrine facilities(pit latrine, flush latrine, etc.) in each state
query_15 = """SELECT 'State/UT', SUM(Type_of_latrine_facility_Pit_latrine_Households) as "Pit_Laterine",
SUM(type_of_latrine_facility_Other_latrine_Households) as "Other_Laterine",SUM(Type_latrine_facility_soildisposed) as "Night_Soil",
SUM(Type_latr_flush_otherhouseholds) as "Flush" FROM census_rameeza GROUP BY 'State/UT';"""
df = get_data(query_15, connection)
st.title("The distribution of different types of latrine facilities")
st.dataframe(df)

# Query 16:households have access to drinking water sources near the premises in each state
query_16 = """SELECT 'State/UT', SUM(Location_of_drinking_water_source_Away_Households) as "Households" FROM census_rameeza GROUP BY 'State/UT';"""
df = get_data(query_16, connection)
st.title("Households have access to drinking water sources near the premises in each state")
st.dataframe(df)

# Query 17:The average household income distribution in each state based on the power parity categories
query_17 = """SELECT 'State/UT', AVG(Power_Parity_Less_than_Rs_45000) as "income < 45000", 
AVG(Power_Parity_Rs_45000_150000) as "income between 45000 to 150000", 
AVG(Power_Parity_Rs_150000_330000) as "income between 150000 to 330000", 
AVG(Power_Parity_Rs_330000_545000) as "income between 330000 to 545000",
AVG(Power_Parity_Above_Rs_545000) as "income > 545000" FROM census_rameeza GROUP BY'State/UT';"""
df = get_data(query_17, connection)
st.title("Average household income distribution in each state based on the power parity-categories")
st.dataframe(df)

# Query 18:The percentage of married couples with different household sizes in each state
query_18 = """SELECT 'State/UT', (SUM(Married_couples_1_Households)/SUM(Married_couples_None_Households +Married_couples_1_Households+Married_couples_2_Households+Married_couples_3_or_more_Households))*100 as "1"  ,
(SUM(Married_couples_2_Households)/SUM(Married_couples_None_Households +Married_couples_1_Households+Married_couples_2_Households+Married_couples_3_or_more_Households))*100 as"2" ,
(SUM(Married_couples_3_or_more_Households)/SUM(Married_couples_None_Households+Married_couples_1_Households+Married_couples_2_Households+Married_couples_3_or_more_Households))*100 as "3" FROM census_rameeza GROUP BY 'State/UT';"""
df = get_data(query_18, connection)
st.title("Percentage of married couples with different household sizes in each state")
st.dataframe(df)

# Query 19:Households fall below the poverty line in each state based on the power parity categories
query_19 = """SELECT 'State/UT',SUM(Power_Parity_Less_than_Rs_45000) as "Households"  FROM census_rameeza GROUP BY 'State/UT';"""
df = get_data(query_19, connection)
st.title("Households fall below the poverty line in each state based on the power parity categories")
st.dataframe(df)

# Query 20:Overall literacy rate (percentage of literate population) in each state
query_20 = """SELECT 'State/UT', (SUM(Literate_Education)/SUM(Total_Education))*100 as Literacy_Rate FROM census_rameeza GROUP BY 'State/UT';"""
df = get_data(query_20, connection)
st.title("Overall literacy rate (percentage of literate population) in each state")
st.dataframe(df)
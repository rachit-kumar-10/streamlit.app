import streamlit as st # type: ignore
from sqlalchemy import create_engine , text
import urllib.parse

db_host = "127.0.0.1"
db_port = "3306"
db_name = "student_database"
db_user = "root"
db_password = urllib.parse.quote("RACHITKUMARXVAYU")


db_url = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
engine = create_engine(db_url)

def fetch_data():
    query = text("SELECT * FROM Student_Data ")
    try:
        with engine.connect() as conn:
            result = conn.execute(query)  # Execute the query
            columns = result.keys()  # Get column names
            data = [dict(zip(columns, row)) for row in result]  # Convert rows into a dictionary using column names
        return data
    except Exception as e:
        st.error(f"Error fetching data: {e}")
        return []  # Return an empty list on error

# Streamlit UI
st.title("View Student Data")

data = fetch_data()  # Fetch data

# Display the data
if data:
    st.table(data)  # Display the data as a table
else:
    st.info("No data found in the database.")
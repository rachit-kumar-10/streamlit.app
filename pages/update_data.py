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


def update_data(student_id, field, new_value):
    query = text(f"UPDATE Student_Data SET {field} = :new_value WHERE id = :student_id")
    with engine.connect() as conn:
        conn.execute(query, { "new_value" : new_value, "student_id" : student_id })
        conn.commit()







st.title ("Update Student Data")
student_id = st.number_input("Enter student ID to Update ", min_value=1 , step=1)
field = st.selectbox("Field to Update ", [ "firstname", "lastname", "title", "age", "nationality", "registration_status", "num_courses", "num_semesters" ])
new_value = st.text_input("New Value")
if st.button ( "Update"):
    try:
        update_data(student_id, field , new_value)
        st.success("Data Successfully updated")
    except Exception as e:
        st.error(f"Error updating data : {e}") 
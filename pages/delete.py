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


def delete_data(student_id):
    query = text("DELETE FROM Student_Data WHERE id = :student_id")
    with engine.connect() as conn:
        conn.execute(query, {"student_id": student_id})
        conn.commit()

st.title("Delete student data")
student_id = st.number_input("Enter student ID to delete", min_value = 1 , step=1)

if st.button("Delete"):
    try:
        delete_data(student_id)
        st.success(f"Data with student_id {student_id} successfully deleted !")
    except Exception as e :
        st.error(f"Error deleting data : {e}")
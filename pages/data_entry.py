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

def insert_data(firstname,lastname, title,age, nationality, registration_status, num_courses , num_semesters):

    query= text(
        """        
        INSERT INTO student_data (firstname , lastname , title , age, nationality , registration_status, num_courses, num_semesters)
        VALUES ( :firstname , :lastname,:title , :age, :nationality , :registration_status, :num_courses, :num_semesters)
        """
    )

    try: 
        with engine.connect() as conn:
            conn.execute(query, {
                "firstname": firstname,
                "lastname": lastname,
                "title": title,
                "age": age,
                "nationality": nationality,
                "registration_status": registration_status,
                "num_courses": num_courses,
                "num_semesters": num_semesters
            })
            # Commit the transaction explicitly
            conn.commit()
    except Exception as e:
        print(f"Error occurred: {e}")
        raise RuntimeError(f"Database operation failed: {e}")


st.title("Student Data Entry Form")

with st.form("data_entry_form"):
    # User info
    st.header("User Information")
    firstname = st.text_input("First Name")
    lastname = st.text_input("Last Name")
    title = st.selectbox("Title", ["", "Mr.", "Ms.", "Dr."])
    age = st.number_input("Age", min_value=18, max_value=110, step=1)
    nationality = st.selectbox(
        "Nationality", ["India", "Africa", "Antarctica", "Asia", "Europe", "North America", "Oceania", "South America"]
    )

    # Course info
    st.header("Course Information")
    registration_status = st.radio(
        "Registration Status", ["Registered", "Not Registered"], index=1
    )
    num_courses = st.number_input("# Completed Courses", min_value=0, step=1)
    num_semesters = st.number_input("# Semesters", min_value=0, step=1)

    # Terms and conditions
    st.header("Terms & Conditions")
    accepted = st.checkbox("I accept the terms and conditions.")

    # Submit button
    submitted = st.form_submit_button("Submit")

    if submitted:
        if accepted:
            if firstname.strip() and lastname.strip():
                try:
                    insert_data(firstname, lastname , title, age , nationality, registration_status,num_courses, num_semesters  )
                    st.success("Data successfully submitted")
                
                except RuntimeError as e:
                    st.error(f"An error occurred: {e}")
            else:
                st.warning("First name and last name are required.")
        else:
            st.warning("You must accept the terms and conditions to proceed.")






    


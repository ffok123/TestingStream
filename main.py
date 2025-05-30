import streamlit as st
import pandas as pd
import matplotlib as plt


# Set up the title and headers for the Streamlit dashboard
st.title("My first Dashboard")
st.header("Name of author: Florence fok")
st.subheader("Course: COMP 4145")
st.text("Lab 2 exercise")

# Add a markdown link and separator
st.markdown("[HKBU email](mailto:wyfok@hkbu.edu.hk)")
st.markdown("---")
st.markdown("**My first** *program*")

# Display a simple text message
# st.json({"a":"1,2,3","b":"4,5,6"})  # Example of JSON display (commented out)
# st.code("""print("Yee")""")  # Example of code display (commented out)
st.write("Hello world")

# File uploader widget to allow users to upload a file
uploaded_file = st.file_uploader("Choose a file", type=["csv", "txt", "xlsx"])

# Check if a file has been uploaded
if uploaded_file is not None:
    # Read the uploaded file into a DataFrame
    df = pd.read_csv(uploaded_file)

    # Display a preview of the data
    st.subheader("data preview")
    st.write(df.head())

    # Display a summary of the data
    st.subheader("data summary")
    st.write(df.describe())

    # Allow users to filter the data by selecting a column and value
    st.subheader("filter data")
    # Get the list of columns from the DataFrame
    columns = df.columns.tolist()
    # Create a dropdown menu for selecting a column to filter the data
    selected_col = st.selectbox("Select column to filter by", columns)
    # Get the unique values from the selected column
    unique_values = df[selected_col].unique()
    # Create a dropdown menu for selecting a value to filter the data
    selected_value = st.selectbox("Select value to filter by", unique_values)


    # Filter the DataFrame based on the selected column and value
    filtered_df = df[df[selected_col] == selected_value]
    # Display the filtered DataFrame
    st.write(filtered_df)

    st.subheader("Plot data")
    # Dropdowns for selecting columns for the x-axis and y-axis
    x_column = st.selectbox("Select x-axis column", columns)
    y_column = st.selectbox("Select y-axis column", columns)

    # Add a button to generate the chart
    #if st.button("Generate Line Chart"):
        # Generate a chart based on the selected columns
        #st.subheader("Generated Line Chart")
        #st.line_chart(filtered_df.set_index(x_column)[y_column])
    if st.button("Generate Bar Chart"):
        # Generate a chart based on the selected columns
        st.subheader("Generated Bar Chart")
        st.bar_chart(filtered_df.set_index(x_column)[y_column])
else:
    # Display a message when no file is uploaded
    st.write("Waiting on file upload..")

    # Example of additional processing (commented out)
    # st.write("File uploaded successfully!")
    # st.write(uploaded_file.name)
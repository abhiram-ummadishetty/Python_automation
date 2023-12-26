import streamlit as st
import pandas as pd
import numpy as np
import currency_converter as cc
import youtube_downloader as yd
import version_control as vc
import Morse_Code_Converter as Mc


st.set_page_config(
    page_title="PYTHON-AUTOMATION",
    page_icon="❄️",
)


st.sidebar.success("Select an Application")
page = 'Home'

page = st.sidebar.selectbox(
    'Automations',
    ('Home','Currency Converter', 'Version Control', 'Youtube Downloader','Morse Code Converter')
)

if page == 'Home':
    st.title('❄️ PYTHON-AUTOMATION ❄️')
    st.markdown(
        """
        Python automation involves using Python programming to perform repetitive tasks automatically without manual intervention.
        This Python automation project performs a series of tasks using Streamlit.

        **👈 Select a app from the sidebar** to see some examples
        of what Python can do!
        ### Key Areas:
        - **Scripting and Batch Processing:** Automating tasks like file management, data processing, and system operations.
        - **Web Automation:** Controlling browsers for tasks like web scraping, testing, or interaction with web applications.
        - **Data Processing and Analysis:** Streamlining data cleaning, analysis, and machine learning workflows.
        - **Task Scheduling:** Automating routine processes at specific intervals or times.

        ### Tools and Libraries:

        - **Selenium:** For browser automation.
        - **Beautiful Soup, Requests:** Web scraping and HTTP requests.
        - **OpenCV:** Image processing and computer vision.
        - **os, shutil:** Built-in file and directory operations.
        - **Task Schedulers (schedule, apscheduler):** Task automation at specified times.

        ### Workflow:

        - **Identify Tasks:** Pinpoint tasks suitable for automation.
        - **Choose Tools:** Select appropriate libraries or tools.
        - **Script Development:** Create Python scripts or programs for automation.
        - **Testing and Execution:** Validate scripts, execute, and monitor performance.

        ### Benefits:

        - **Efficiency:** Reduces manual effort and minimizes errors.
        - **Scalability:** Handles large-scale operations and data volumes.
        - **Flexibility:** Python's libraries cater to diverse automation needs.

        Python automation optimizes workflows, boosts productivity, and enables focus on higher-value tasks by automating repetitive processes efficiently.
    """
    )

elif page == 'Currency Converter':
    st.title('Currency Converter')
    user_input_text = st.text_input("Enter the base currency to be converted","-")
    user_input_text_upper = user_input_text.upper()
    st.write("You entered:", user_input_text)

    user_input_number = st.number_input("Enter the amount that is to be converted",value=1)
    st.write("The number you entered:", user_input_number)

    data_req = cc.convert_currency(user_input_text_upper)
    if data_req:
        for key, value in data_req.items():

            if key == user_input_text_upper:
                pass
            else:
                data = {
                    "Currency" :  [f"{cc.CURRENCIES_list[key]}"],
                    "Value" : [f"{float(value) * user_input_number}"]
                }

                df = pd.DataFrame(data)
                st.dataframe(df)

                # st.write(f"{cc.CURRENCIES_list[key]}: {float(value) * user_input_number}")

elif page == 'Version Control':
    st.title("Version control")
    source_dir = st.text_input("Enter the Directory Location", "")
    destination_dir = st.text_input("Enter the Backup Directory Loaction", "")
    if st.button("BackUp"):
        st.write("BackUp Started")
        vc.copy_folder_to_directory(source_dir, destination_dir)
        st.write("BackUp Ended")

elif page == 'Youtube Downloader':
    st.title('Youtube Downloader')
    user_input_text = st.text_input("Enter the URL", "")
    if st.button('Download'):
        path = yd.path_finder()
        if path:
            st.write("Started download")
            yd.youtube_downloader(user_input_text,path)
            st.write("Download Complete")
        else:
            st.write("Invalid link")

elif page == 'Morse Code Converter':
    st.title('Morse Code Converter')
    text = st.text_input("enter the Text:")
    morse = st.text_input("enter the Morse:")
    code  = Mc.textToMorse(text)
    text_output = Mc.morseToText(morse)
    print(code)
    if st.button("Text To Morse"):
        st.text(code)
    if st.button("Morse To Text"):
        st.text(text_output)






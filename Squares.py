# import streamlit as st
#
# st.header("Basic Calculator")
#
# agree = st.checkbox("Open Calculator")
#
# def calculator(x):
#     return x * x
#
#
# if agree:
#     user_name = st.text_input("Write your name", )
#     if user_name:
#         st.write("Nice to meet you!",user_name)
#         start = st.button("Start", type="primary")
#         if start:
#             st.session_state.number = st.number_input("Insert a number")
#
#         if st.session_state.number:
#             st.session_state.result = calculator(st.session_state.number)
#         calculate = st.button("calculate", type="primary")
#         if calculate:
#             if st.session_state.result:
#                 st.write("The current number is ", st.session_state.result)
# import streamlit as st
#
# st.header("Basic Calculator")
#
# agree = st.checkbox("Open Calculator")
#
#
# def calculator(x):
#     return x * x
#
#
#
# if agree:
#     user_name = st.text_input("Write your name")
#     if user_name:
#         st.write("Nice to meet you!", user_name)
#         start = st.button("Start", type="primary")
#
#         if 'number' not in st.session_state:
#             st.session_state.number = 0
#
#
#         number = st.number_input("Insert a number", value=None, min_value=None, max_value=None, step=10)
#
#         if start:
#
#             st.session_state.result = calculator(number)
#
#         if st.session_state.result:
#             st.write("The result is:", st.session_state.result)
import streamlit as st

st.header("Basic Calculator")

agree = st.checkbox("Open Calculator")


def calculator(x):
    return x * x


if agree:
    user_name = st.text_input("Write your name")

    if user_name:
        st.write("Nice to meet you!", user_name)

        # Initialize session state variables if they don't exist
        if 'number' not in st.session_state:
            st.session_state.number = 0
        if 'result' not in st.session_state:
            st.session_state.result = None

        start = st.button("Start", type="primary")

        if start:

            number = st.number_input("Insert a number", value=st.session_state.number)
            st.session_state.number = number


        if st.button("Calculate"):
            result = calculator(st.session_state.number)
            st.write("The current number is:", result)

import streamlit as st
import functions

todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This is my Todo App.")
st.write("This App is to increase your productivity.")

for todo in todos:
    st.checkbox(todo)


st.text_input("", placeholder="Enter a new todo..")
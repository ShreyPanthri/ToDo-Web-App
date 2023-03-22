import streamlit as st
import functions

todos = functions.get_todos("todos.txt")

def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    functions.write_todos("todos.txt", todos)

st.title("My todo app")
st.subheader("Helps to manage day to day tasks")
st.write("This will increase my productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos("todos.txt", todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')

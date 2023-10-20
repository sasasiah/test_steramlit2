
import streamlit as st
import pandas as pd

def display_tasks(task_list):
    tasks_df = pd.DataFrame(task_list)
    st.table(tasks_df)

def create_task(task_name, task_due_date):
    task = {
        'name': task_name,
        'due_date': task_due_date,
        'completed': False
    }
    return task

def add_task_to_list(task_list, task):
    task_list.append(task)
    return task_list

# Streamlit app
st.title("Calendar To-Do List")

task_list = []

task_name = st.text_input("Enter task name:")
task_date = st.date_input("Enter task date:")

if st.button("Add Task"):
    task_list = add_task_to_list(task_list, create_task(task_name, task_date))

st.header("Tasks:")
display_tasks(task_list)
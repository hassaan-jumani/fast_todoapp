import streamlit as st
import requests
import pandas as pd
from pydantic_practice import Todo_pydantic
# Create a todoap with title add button and delete butto and show all button using streamlit

st.title("Todo App")

local_host = "http://127.0.0.1:8000/"

def getall():
    if st.button("Get all", key="get all todos"):
        r = requests.get(f"{local_host}getall")
        if r.status_code == 200:
            result = r.json()
            df = pd.DataFrame(result)
            st.data_editor(df,column_config={"name": st.column_config.LinkColumn(
            "Todos Title",
            validate=f"{local_host}/get/",
            disabled=True,
            # validate="^https://[a-z]+\.streamlit\.app$",
            # validate=requests.get(f"{local_host}get/{df['id'][0]}"),
        )},
        # hide_index=True,
        )
        else:
            st.error("Something went wrong")

def create_todos():
    todo_name = st.text_input("Enter a todo", key="new_todo name")
    todo_description = st.text_input("Enter a todo Description", key="new_todo description")
    if st.button("Add", key="add_todo"):
        r = requests.post(f"{local_host}create" , json={'name':todo_name,'description':todo_description})
        print(r.json())
        if r.status_code == 200:
            st.success("Todo added successfully")
        else:
            st.error("Something went wrong")

        


if __name__ == "__main__":
    getall()
    create_todos()
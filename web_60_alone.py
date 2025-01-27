import streamlit as st
# from streamlit import checkbox

import functions

todos = functions.get_todos()   # here we get the list of our todos from todos_store.txt file


def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    functions.write_todos(todos)
    print('todo = ', todo, type(todo))

# To stop our web app we should to entered in Terminal next command: CTRL+C
st.title("My Todo App")                                         # Заголовок - крупным жирным шрифтом
st.subheader("This is a subtitle (subheader) of my Todo App.")  # Подзаголовок - средним полужирным шрифтом
st.write("This App is to increase your <b>productivity</b>.", unsafe_allow_html=True)  # Текст мелким (обычным) шрифтом
# где <b>...</b> вместе с аргументом unsafe_allow_html=True -> даёт жирный шрифт (bold font)

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)            # delete the _todo from the todos list
        functions.write_todos(todos)
        del st.session_state[todo]  # delete the _todo from the session_state instance "dictionary"
        st.rerun()                  # перезапуск\обновление веб-страницы для активации изменений

# Отображает поле для ввода текста (обязательно указать либо пустую строку у аргумента label либо заголовок этого поля)
st.text_input(label="New todo:", placeholder="Add a new todo...", on_change=add_todo, key="new_todo")

# st.session_state  # this row displays session_state instance "dictionary" on the web-page
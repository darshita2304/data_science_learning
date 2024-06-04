import streamlit as st

st.title('Hello world')

cuisine = st.sidebar.selectbox(
    "Pick a cousines", ("Indian", "Italian", "Spanish", "Mexican"))


def generate_restaurant_name_and_items(cuisine):
    return {
        'restaurant_name': 'Curry Delight',
        'menu_items': 'Samosa, Paneer Tikka',
    }


if cuisine:
    response = generate_restaurant_name_and_items(cuisine)

    st.header(response['restaurant_name'])
    menu_items = response['menu_items'].split(',')

    st.write("** Menu Items **")

    for item in menu_items:
        st.write("-", item)

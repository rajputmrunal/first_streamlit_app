
import streamlit
import pandas
streamlit.title("my parents new healthy dinner")
streamlit.header("Breakfast menu")
streamlit.text("omega 3 & oatmeal")
streamlit.text("kale,spinach & rocket smothie")
streamlit.text("Hard-boiled free-range egg")
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
fruits_selected=streamlit.multiselect("pick some fruits:",list(my_fruit_list.index),['avacado','strwaberry'])
streamlit.dataframe(my_fruit_list)
# Let's put a pick list here so they can pick the fruit they want to include 


# Display the table on the page.

#my_fruit_list = my_fruit_list.set_index('Fruit')

#fruits_to_show = my_fruit_list.loc[fruits_selected]

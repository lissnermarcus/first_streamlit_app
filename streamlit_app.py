import streamlit
import pandas

streamlit.title("My parents new heathy diner")

streamlit.header("breakfast favorites")

streamlit.text("🥣 omega 3 and blueberry oatmeal etcetc")
streamlit.text("🥗 kale, spinach smoothie")
streamlit.text("🐔 eggs for days")
streamlit.text("🥑🍞 avocado toast")

streamlit.header("🍌🥭 build your own fruit smoothie")
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index("Fruit")
#streamlit.dataframe(my_fruit_list)

# lets put a pick list here so they can pick the fruit they want to include
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ["Avocado", "Strawberries"])
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)
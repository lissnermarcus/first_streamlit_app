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
streamlit.dataframe(my_fruit_list)
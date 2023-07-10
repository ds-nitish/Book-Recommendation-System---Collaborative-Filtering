import streamlit as st
import pickle
import pandas as pd
import numpy as np

# importing all pickle fiile
similarity_score = pickle.load(open('similarity.pkl','rb'))

table = pd.DataFrame(pickle.load(open('table.pkl','rb')))

data = pd.DataFrame(pickle.load(open('data.pkl','rb')))

# Making recommendation function to get recommended books
recommended_book = []
def recommend(book_name):
    index = np.where(table.index == book_name)[0][0]
    data = sorted(list(enumerate(similarity_score[index])),key= lambda x:x[1],reverse=True)[1:11]
    for i in data:
        recommended_book.append(table.index[i[0]])
    return recommended_book

# Creating UI for data input
st.title('Book Recommendation')
selected_book = st.selectbox('Choose Book Name',(data['Book-Title'].unique()))

if st.button('Recommend'):
    books_data = recommend(selected_book)
    for i in books_data:
        st.markdown(f'**{i}**')
        st.image(data[data['Book-Title']==i]['Image-URL-M'].unique()[0])

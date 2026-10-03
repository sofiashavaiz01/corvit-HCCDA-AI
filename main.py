import streamlit as st
st.title('Welcome to Corvit HCCDA-AI')
st.write('We are leaerning Python in Corvit.')
st.text('I am Sofia Shavaiz')
st.write('I have done ADP-CS')
st.success('regestration successful')
st.info('For more information')
st.warning('Warning')
st.error('Error')

st.checkbox('show/hide')
st.checkbox('Male')
st.checkbox('Female')


    
hobbies = st.multiselect('Hobbies',['gaming','writing','singing'])    


st.write('You selected', len(hobbies),hobbies,'hobbies')




     

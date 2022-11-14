import pandas as pd
import numpy as np
import ast

import streamlit as st

class AutomateTest:
    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)
        self.counter = 0

    def get_data(self):
        if self.counter < self.df.shape[0]:
            data = self.df.iloc[self.counter]
            question = data['question']
            answer = data['answer']
            answer = ast.literal_eval(answer)
            image = data['image_src']
            self.counter += 1
            return question, answer, image
        else:
            return 'finished', ['finished'], 'finished'

    def generate_row(self):
        ques, ans, img = auto_test.get_data()
        if ques != 'finished':
            st.write(str(self.counter) + ") " + ques)
            if img!='no_image':
                try:
                    st.image(img)
                except:
                    print('Image cannot be read')
            st.radio('Options are:', tuple(ans), key=ques)
            return True
        else:
            return False
        # next_button = st.button('Next Question', key=ques)
        # return next_button

if __name__ == '__main__':
    file_path = 'cbsstest1.csv'
    next_button = True
    auto_test = AutomateTest(file_path)
    st.title('Comprehensive Basic Science Self-Assessment')

    start_button = st.button("Start Test", key='start')
    if start_button:
        next_button = auto_test.generate_row()
    
    while(next_button):
        next_button = auto_test.generate_row()
    st.write('End of the Test!!!')


    
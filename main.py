import os
import streamlit as st
from merge_split import split

import base64
import time

import shutil

def file_mk_rm(dirname, zipname):
    if(os.path.exists(dirname)):
        shutil.rmtree(dirname)
    os.makedirs(dirname, exist_ok=True)
    if(os.path.exists(zipname)):
        os.remove(zipname)

def file_rm(dirname, zipname):
    if(os.path.exists(dirname)):
        shutil.rmtree(dirname)
    if(os.path.exists(zipname+'.zip')):
        os.remove(zipname+'.zip')

def side():
    st.sidebar.title('pdf-controller')
    mode = st.sidebar.radio('Please select a mode ',['Home' ,'Split mode', 'Merge mode'])
    return mode

def page1(tmpdir, zipname):
    st.subheader('Split mode')
    input = st.file_uploader("", type='pdf')
    selected_item = st.radio('In what format will you save the file?',['pdf', 'zip'])
    try:
        if st.button('RUN'):
            with st.beta_expander('Download link'):
                file_mk_rm(tmpdir, zipname)
                split(input, tmpdir,selected_item, zipname)
    except AttributeError:
        st.error('The file is not selected.')

if __name__ == "__main__":
    mode = side()
    tmpdir = './tmp/'
    zipname = 'tmp_zip'
    
    if mode == 'Split mode':
        page1(tmpdir, zipname)
    file_rm(tmpdir, zipname)
        
    

import os
import PyPDF2
import glob

import base64

import streamlit as st
import shutil

def merge(pdfdir , outdir):
    merger = PyPDF2.PdfFileMerger()
    for filepath in glob.glob(pdfdir + '*.pdf'):
        merger.append(filepath)
    merger.write(outdir + 'merge.pdf')
    merger.close()

def split(filename, outpath,selected_item, zipname):
    reader = PyPDF2.PdfFileReader(filename)
    page_n = reader.getNumPages()
    for page in range(page_n):
        split_page = PyPDF2.PdfFileWriter()
        split_page.addPage(reader.getPage(page))
        savepath = outpath + str(page) + '.pdf'
        with open(savepath, 'wb') as f:
            split_page.write(f)
        if selected_item == 'pdf':
            with open(savepath, 'rb') as f:
                b64 = base64.b64encode(f.read()).decode()
            href = f'<a href="data:application/octet-stream;base64,{b64}" download="str(page) + .pdf">download:{page}.pdf</a>'    
            st.markdown(href, unsafe_allow_html=True)
    if selected_item =='zip':
        shutil.make_archive(zipname,'zip', outpath)
        with open('tmp_zip'+'.zip', 'rb') as f:
            b64 = base64.b64encode(f.read()).decode()
            href = f'<a href="data:application/octet-stream;base64,{b64}" download="pdf-controller.zip">download:zip</a>'    
            st.markdown(href, unsafe_allow_html=True)

if __name__ == "__main__":
    filename = './data/sample.pdf'
    splitpath = './split_out/'
    os.makedirs(splitpath, exist_ok=True)
    split(filename,splitpath)
    mergepath = './merge_out/'
    os.makedirs(mergepath, exist_ok=True)
    merge(splitpath, mergepath)

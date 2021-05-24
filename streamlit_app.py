import streamlit as st
import pandas as pd
from apriori import runApriori, dataFromFile, to_str_results

st.markdown("# Apriori Streamlit by 陳偉銍")

st.sidebar.markdown(
    """The code attempts to implement the following paper:

> *Agrawal, Rakesh, and Ramakrishnan Srikant. "Fast algorithms for mining association rules." Proc. 20th int. conf. very large data bases, VLDB. Vol. 1215. 1994.*
"""
)

default_csv = st.selectbox(
    "Select one of the sample csv files", ("source.csv", "INTEGRATED-DATASET.csv", "tesco.csv")
)

if default_csv == 'INTEGRATED-DATASET.csv':
    st.markdown('''The dataset is a copy of the “Online directory of certified businesses with a detailed profile” file from the 
    Small Business Services (SBS) dataset in the NYC Open Data Sets http://nycopendata.socrata.com/''')
elif default_csv == 'tesco.csv':
    st.markdown('The dataset is a toy dataset contain frequently purchased grocery items')
elif default_csv == 'source.csv':
    st.markdown('This is only for my HOMEWORK from [GD人工智慧在生活的應用]')
    st.markdown('We are going to find out all **frequent itemsets** and **association rules** via <span style="color: #fb0505;">Apriori algorithm</span>', unsafe_allow_html=True)
    st.markdown('The minimum confidence is 60% and minimum support count is 2.')
    # st.markdown('<p style="color: aqua;"> </p>', unsafe_allow_html=True)

st.markdown('Here are some sample rows from the dataset')
csv_file = pd.read_csv(default_csv, header=None, sep="\n", comment='#')
# st.write(csv_file[0].str.split("\,", expand=True).head())
st.write(csv_file[0].str.split("\,", expand=True))

st.markdown('---')
st.markdown("## Inputs")

st.markdown('''
            **Support** shows transactions with items purchased together in a single transaction.
            
            **Confidence** shows transactions where the items are purchased one after the other.''')

st.markdown('Support and Confidence for Itemsets A and B can be represented by formulas')

support_helper = ''' > Support(A) = (Number of transactions in which A appears)/(Total Number of Transactions') '''
confidence_helper = ''' > Confidence(A->B) = Support(AUB)/Support(A)') '''
st.markdown('---')

if default_csv == 'source.csv':
    st.markdown('minimum confidence is 60%')
    st.markdown('<span style="color: orange;">minimum support count is 2</span>', unsafe_allow_html=True)
    minimum_support_helper = ''' > According to the formula, min Support(X)=2, which means we need "0.18" as the threshold."'''
    st.button('Support(A) = (Number of transactions in which A appears)/(Total Number of Transactions)', help=minimum_support_helper)
    # st.markdown('<p style="color: aqua;"> </p>', unsafe_allow_html=True)

support = st.slider("Enter the Minimum Support Value", min_value=0.1,
                    max_value=0.9, value=0.55,
                    help=support_helper)

confidence = st.slider("Enter the Minimum Confidence Value", min_value=0.1,
                       max_value=0.9, value=0.6, help=confidence_helper)

inFile = dataFromFile(default_csv)

items, rules = runApriori(inFile, support, confidence)

i, r = to_str_results(items, rules)

st.markdown("## Results")

st.markdown("### Frequent Itemsets")
st.write(i)

st.markdown("### Frequent Rules")
st.write(r)

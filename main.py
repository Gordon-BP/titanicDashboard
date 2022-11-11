import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("Titanic Survivorship by the Numbers")
with st.container():
    st.header("\"Women and Children First\" is just the tip of the iceberg...")
    st.text("""
    Here's some pretty charts about a sinking ship
    """)


    st.markdown("""
    ## Data key:
    | Variable |                 Definition                 |                       Key                      |
    |:--------:|:------------------------------------------:|:----------------------------------------------:|
    | Survived | Survival                                   | 0 = No, 1 = Yes                                |
    | Pclass   | Ticket class                               | 1 = 1st, 2 = 2nd, 3 = 3rd                      |
    | Sex      | Sex                                        |                                                |
    | Age      | Age in years                               |                                                |
    | SibSp    | # of siblings / spouses aboard the Titanic |                                                |
    | Parch    | # of parents / children aboard the Titanic |                                                |
    | Ticket   | Ticket number                              |                                                |
    | Fare     | Passenger fare                             |                                                |
    | Cabin    | Cabin number                               |                                                |
    | Embarked | Port of Embarkation                        | C = Cherbourg, Q = Queenstown, S = Southampton |
    
    not listed: PassengerId, Name
    """)
train = pd.read_csv("data/train.csv")

st.subheader("Let's see survival by various passenger traits...")

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(['Overall', 'Gender', 'Ticket Class', 'Age', 'Family Size', 'Embarkation'])

with tab1:
    """
        Shows a pie chart of overall passenger survival
    """
    st.header("Overall Survival")
    total_survived = train['Survived'].sum()
    total_perished = len(train) - total_survived
    fig, ax = plt.subplots()
    fig.patch.set_alpha(0)
    ax.pie(
        x = [total_perished, total_survived],
        labels = ['Total Perished', 'Total Survived'],
        colors = ['#1b50b0', '#d2e9e3'],
        startangle = 90,
        autopct="%.2f",
        textprops={'color':"w"}
    )
    st.pyplot(fig)
with tab2:
    """
        Shows two pie charts- one for men's survival rate, another for women's
    """
    st.header("Survival by Gender")
    col1, col2 = st.columns(2)
    survival_by_gender = pd.pivot_table(
        data=train,
        values=['PassengerId'],
        index=[train.Sex, train.Survived],
        aggfunc=len
    )
    with col1:
        st.subheader("Survival rates for women")
        fig, ax1 = plt.subplots()
        fig.patch.set_alpha(0)
        ax1.pie(
            x = survival_by_gender.loc['female']['PassengerId'],
            labels = ['Total Women Perished', 'Total Women Survived'],
            colors = ['#1b50b0', '#d2e9e3'],
            startangle = 90,
            autopct="%.2f",
            textprops={'color':"w"}
        )
        st.pyplot(fig)
    with col2:
        st.subheader("Survival rates for men")
        fig, ax1 = plt.subplots()
        fig.patch.set_alpha(0)
        ax1.pie(
            x = survival_by_gender.loc['male']['PassengerId'],
            labels = ['Total Men Perished', 'Total Men Survived'],
            colors = ['#1b50b0', '#d2e9e3'],
            startangle = 90,
            autopct="%.2d",
            textprops={'color':"w"}
        )
        st.pyplot(fig)
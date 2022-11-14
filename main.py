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
train
st.subheader("Let's see survival by various passenger traits...")

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(['Overall', 'Gender', 'Ticket Class', 'Age', 'Family Size', 'Embarkation'])

with tab1:
    st.header("Overall Survival")
    total_survived = train['Survived'].sum()
    total_perished = len(train) - total_survived
    fig, ax = plt.subplots()
    fig.patch.set_alpha(0)
    ax.pie(
        x = [total_perished, total_survived],
        labels = ['Perished', 'Survived'],
        colors = ['#1C304A', '#046B99'],
        startangle = 90,
        autopct="%.2f",
        textprops={'color':"w"}
    )
    st.pyplot(fig)
with tab2:
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
            labels = ['Perished', 'Survived'],
            colors = ['#1C304A', '#046B99'],
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
            labels=["Perished","Survived"],
            colors = ['#1C304A', '#046B99'],
            startangle = 90,
            autopct="%.2f",
            textprops={'color':"w"}
        )
        st.pyplot(fig)
with tab3:
    st.header("Survival by Ticket Class")
    titleArr = ["First Class", "Second Class", "Third Class"]
    classNums = [1,2,3]
    survival_by_class = pd.pivot_table(
            data=train,
            values=['PassengerId'],
            index=[train.Pclass, train.Survived],
            aggfunc=len
    )
    cols = st.columns(3)
    for i in range(3):
        with cols[i]:
            st.subheader(f"{titleArr[i]} Survival Rates")
            fig, ax1 = plt.subplots()
            fig.patch.set_alpha(0)
            ax1.pie(
                x = survival_by_class.loc[classNums[i]]['PassengerId'],
                labels = ['Perished', 'Survived'],
                colors = ['#1C304A', '#046B99'],
                startangle = 90,
                autopct="%.2f",
                textprops={'color':"w"}
            )
            st.pyplot(fig)
with tab4:
    st.header("Survival by Age")
    survival_ages = train.Age.loc[train.Survived == 1]

    fig, ax1 = plt.subplots()
    fig.patch.set_alpha(0)
    n, bins, patches = ax1.hist(
        x = survival_ages,
        bins=10,
        facecolor = '#046B99',
        alpha=1
    )
    ax1.patch.set_alpha(0)
    # Styling everything for dark mode
    for spine in ax1.spines:
        ax1.spines[spine].set_color("w")
    ax1.tick_params(axis='x', colors='w')
    ax1.tick_params(axis='y', colors='w')
    ax1.set_xlabel("Age Range", color='w')
    ax1.set_xticks(bins)
    ax1.set_xticklabels(np.floor(bins).astype(int))
    ax1.set_ylabel("Number of Survivors", color = 'w')
    ax1.set_ymargin(0.25)
    ax1.grid(True, which='major', axis='y', color='w', alpha=0.33)
    # Add labels to the bars
    for bar, label in zip(patches, n):
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width() / 2, height+0.01, label.astype(int),
            ha='center', va='bottom', color='w')
    st.pyplot(fig)
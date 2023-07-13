# Here is the modified code:

# Imports
import os
from dotenv import load_dotenv
import streamlit as st
from crypto_wallet import generate_account, get_balance, send_transaction
from web3 import Web3

# Load environment variables
load_dotenv()

# Initialize a Web3 instance
w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))

# Database of KryptoJobs2Go candidates including their name, digital address, rating and hourly cost per Ether.
candidate_database = {
    "Lane": [
        "Lane",
        "0xaC8eB8B2ed5C4a0fC41a84Ee4950F417f67029F0",
        "4.3",
        0.20,
        "Images/lane.jpeg",
    ],
    "Ash": [
        "Ash",
        "0x2422858F9C4480c2724A309D58Ffd7Ac8bF65396",
        "5.0",
        0.33,
        "Images/ash.jpeg",
    ],
    "Jo": [
        "Jo",
        "0x8fD00f170FDf3772C5ebdCD90bF257316c69BA45",
        "4.7",
        0.19,
        "Images/jo.jpeg",
    ],
    "Kendall": [
        "Kendall",
        "0x8fD00f170FDf3772C5ebdCD90bF257316c69BA45",
        "4.1",
        0.16,
        "Images/kendall.jpeg",
    ],
}

# A list of the KryptoJobs2Go candidates first names
people = ["Lane", "Ash", "Jo", "Kendall"]

def get_people():
    """Display the database of KryptoJobs2Go candidate information."""
    db_list = list(candidate_database.values())

    for number in range(len(people)):
        st.image(db_list[number][4], width=200)
        st.write("Name: ", db_list[number][0])
        st.write("Ethereum Account Address: ", db_list[number][1])
        st.write("KryptoJobs2Go Rating: ", db_list[number][2])
        st.write("Hourly Rate per Ether: ", db_list[number][3], "eth")
        st.text(" \n")

# Streamlit Code
st.markdown("# KryptoJobs2Go!")
st.markdown("## Hire A Fintech Professional!")
st.text(" \n")

# Streamlit Sidebar Code - Start
st.sidebar.markdown("## Client Account Address and Ethernet Balance in Ether")

# Generate account and display account address and balance
account = generate_account()
st.sidebar.write("Account Address: ", account.address)
st.sidebar.write("Account Balance: ", get_balance(w3, account.address), "ETH")

# Create a select box to chose a FinTech Hire candidate
person = st.sidebar.selectbox("Select a Person", people)

# Create a input field to record the number of hours the candidate worked
hours = st.sidebar.number_input("Number of Hours")

st.sidebar.markdown("## Candidate Name, Hourly Rate, and Ethereum Address")

# Identify the FinTech Hire candidate
candidate = candidate_database[person][0]
st.sidebar.write("Name: ", candidate)

# Identify the KryptoJobs2Go candidate's hourly rate
hourly_rate = candidate_database[person][3]
st.sidebar.write("Hourly Rate (ETH): ", hourly_rate)

# Identify the KryptoJobs2Go candidate's Ethereum Address
candidate_address = candidate_database[person][1]
st.sidebar.write("Ethereum Address: ", candidate_address)

# Calculate wage
wage = hourly_rate * hours
st.sidebar.markdown("## Total Wage in Ether")
st.sidebar.write(wage)

# Call the send_transaction function and pass it 3 parameters: Your account, the candidate_address, and the wage as parameters
if st.sidebar.button("Send Transaction"):
    # Send transaction and get transaction hash
    transaction_hash = send_transaction(w3, account, candidate_address, wage)

    # Display transaction hash
    st.sidebar.markdown("#### Validated Transaction Hash")
    st.sidebar.write(transaction_hash)

    # Celebrate your successful payment
    st.balloons()

# The function that starts the Streamlit application
# Writes KryptoJobs2Go candidates to the Streamlit page
get_people()

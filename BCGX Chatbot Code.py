#Press ⇧ Shift + ⌘ Cmd + P (Command Palette) to access the python interpreter
import pandas as pd
df = pd.read_csv('/Users/vibodharyajampale/Library/CloudStorage/OneDrive-Personal/W_Desktop/Vibodharya Courses Material/Microsoft_Tesla_Apple Financial Analysis.csv')

Input= input("Enter Your Query: Choose between What is the total revenue?, What is the total assets?, What is the liabilities?, or What is the Net Profit?: ")
Company = input("Enter the Company Name: ")
Year= input("Enter the Year 2022, 2023, 2024: ")

def chatbot_response(Input, Company, Year):
    # Placeholder for the chatbot logic
    # In a real application, this would involve processing the input and generating a response
    # Filter the dataframe based on input
    
    Company = Company.strip().title()
    Year = int(Year)

    row = df[(df['Company'] == Company) & (df['Year'] == Year)]

    if row.empty:
        return f"❌ No data found for {Company} in {Year}."

    if Input == "What is the total revenue?":
        revenue = row['Total Revenue'].values[0]
        output= f"The total revenue for {Company} in {Year} is: {revenue}"

    elif Input == "What is the total assets?":
        assets = row['Total Assets'].values[0]
        output= f"The total assets for {Company} in {Year} is: {assets}"

    elif Input == "What is the liabilities?":
        liabilities = row['Total Liabilities'].values[0]
        output= f"The total liabilities for {Company} in {Year} is: {liabilities}"

    elif Input == "What is the Net Profit?":
        net_profit = row['Net Income'].values[0]
        output= f"The net profit for {Company} in {Year} is: {net_profit}"

    else:
        return "❓ Sorry, I didn't understand your query. Please try again with a valid question."
    
    return output
    
    
print(chatbot_response(Input,Company,Year))

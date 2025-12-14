#importing pandas for data manipulation
import pandas as pd

#importing chain to to flatten the data list into a single  list
from itertools import chain

#importing apriori algorithm and association rule generator
from mlxtend.frequent_patterns import apriori, association_rules


#Loading the transaction dataset in rows
data = {
    "Transaction_ID": [1,2,3,4,5,6,7,8,9,10],
    "Items": [
        "Bread, Milk, Eggs",
        "Bread, Butter",
        "Milk, Diapers, Beer",
        "Bread, Milk, Butter",
        "Milk, Diapers, Bread",
        "Beer, Diapers",
        "Bread, Milk, Eggs, Butter",
        "Eggs, Milk",
        "Bread, Diapers, Beer",
        "Milk, Butter"
    ]
}

#Dataset is converted into a pandas dataframe
df = pd.DataFrame(data)

#Creating a transaction format for Apriori
#Split the 'Items' string column into a list of individual items
df["Items_liSplit the 'Items' string column into a list of individual itemsst"] = df["Items"].str.split(r",\s*")

#Encoding the data into one-hot format
#Flatten all item lists and extract unique items, then sort them
unique_items = sorted(set(chain.from_iterable(df["Items_list"])))

#Creating a column for each unique item
for item in unique_items:
    df[item] = df["Items_list"].apply(lambda x: 1 if item in x else 0)

#Selection the one-hot encoded item columns
transactions = df[unique_items]


# Apply Apriori algorithm

#Finding the frequent itemset which satisfy the min_sup 0f 20%
frequent_itemsets = apriori(transactions, min_support=0.2, use_colnames=True)

# Generating association rules
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.5)

rules = rules[["antecedents", "consequents", "support", "confidence", "lift"]]

#Displaying the results
print("\n Original Dataset with Transaction Lists ")
print(df[["Transaction_ID", "Items", "Items_list"]])

print("\n One-Hot Encoded Transaction Data (Suitable for Apriori) ")
print(df[["Transaction_ID"] + unique_items])

print("\n Frequent Itemsets (Support >= 0.2) ")
print(frequent_itemsets)

print("\n Association Rules (Confidence >= 0.5) ")
print(rules)

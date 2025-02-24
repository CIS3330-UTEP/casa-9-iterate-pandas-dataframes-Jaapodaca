import pandas as pd 

file_content = "big-mac-full-index.csv" 
df = pd.read_csv(file_content) 

print("\nMethod 1:()") 
for index, row in df.head().iterrows():
    price = row["local_price"] - row["dollar price"]
    print(f"On {row["date"]} in {row["name"]}, price difference: ${price:.2f}")

print ("\nMethod 2:()") 
def calculate_price(row):
      return f"On {row["date"]} in {row["name"]}, price difference: ${row["local_price"] - row["dollar_price"]:.2f}" 

result = df.apply(calculate_price, axis=1)
for res in result.head():
     print(res)
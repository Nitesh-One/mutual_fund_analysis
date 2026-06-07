import pandas as pd
nav_history = pd.read_csv('data/raw/02_nav_history.csv')

print(nav_history.columns)

nav_history['date'] = pd.to_datetime(nav_history['date'])

# print(nav_history.dtypes)

nav_history = nav_history.sort_values(by = ['amfi_code', 'date'])

print(nav_history.duplicated().sum())

nav_history = nav_history.drop_duplicates()

print(nav_history.isnull().sum())

nav_history['nav'] = nav_history.groupby('amfi_code')['nav'].ffill()

invalid_nav = nav_history[nav_history['nav'] <= 0]
print(invalid_nav)
print("Invalid NAV Records:", len(invalid_nav))

nav_history = nav_history[
    nav_history["nav"] > 0
]
# print(nav_history)

# print(nav_history.dtypes)

nav_history.to_csv(
    "data/processed/cleaned_nav_history.csv",
    index=False
)
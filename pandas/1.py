import pandas as pd 
d={
    "id":[1,2,3,4,5,6],"dept":[1,2,3,4,5,6],"name":["a","b","c","d","e","f"]

}
df=pd.DataFrame(d)
print(df)
print(df.groupby("dept").sum())
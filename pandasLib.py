import pandas as pd

df=pd.DataFrame({"Day":[1,2,3,4],"Visitor":[200,100,230,300],"BounceRate":[20,30,20,30]})
df2=pd.DataFrame({"Day":[5,6,7,8],"Visitor":[200,100,230,300],"BounceRate":[20,30,20,30]})

df.set_index("Day",inplace=True) #set day as the index of the dataframe
df=df.rename(columns={"Visitor":"Users"}) #changing visitor header to user
print(df)

concatenated=pd.concat([df,df2]); #this will concatenate the dataFrame
print(concatenated)

data=pd.read_csv(r"G:\devlopment\AI\DataSet\CSV\test.csv") #read a csv file
data.to_html("data.html") #covert that csv to html
newData=pd.read_csv(r"G:\devlopment\AI\DataSet\dialogs.txt",delimiter="\t") #read a txt file
data.to_csv("newData.csv") #convert txt to csv
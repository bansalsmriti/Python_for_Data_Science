import pandas as pd
uname=['userID','Gender','Age','Occupation','Zip']
users=pd.read_table('C:/Users/bansa/OneDrive/Documents/Python projects/Wes McKinney/users.dat', sep='::',header=None,names=uname)
rname=['userID','MovieID','Rating','Time_stamp']
uratings=pd.read_table('Python projects/Wes McKinney/ratings.dat', sep='::',header=None,names=rname)
mname=['MovieID','Title','Genres']
movies=pd.read_table('Python projects\Wes McKinney\movies.dat', sep='::',header=None,names=mname)
print(users[:5])
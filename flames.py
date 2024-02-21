import streamlit as st
st.title("welcome to the game")
s1=st.text_input("enter first name")
s2=st.text_input("enter second name")
s1=list(s1)
s2=list(s2)
for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i]==s2[j]:
            s1[i]='0'
            s2[j]='0'
            break
count=0
for i in s1+s2:
    if i!='0':
        count+=1
res=["friends","lovers","attraction","marriage","enemies","sister"]
while len(res)>1:
    splitindex=count%len(res)-1
    if splitindex>=0:
        right=res[splitindex+1:]
        left=res[:splitindex]
        res=right+left
    else:
        res=res[:len(res)-1]
if st.button("submit"):
    st.success(res[0])

import streamlit as st
import time

col1, col2 = st.columns([1,1])
with col1:
    st.image('骑车.jpg')
with col2:
    st.image('自行车.jpg')

col3, col4 = st.columns([2,1])
with col3:
    roading = st.progress(0, '开始加载')
    for i in range(1, 100, 1):
        time.sleep(0.02)
        roading.progress(i,'正在加载'+str(i)+'%')
        
    roading.progress(100, '加载完毕！')
    col5, col6 = st.columns([1,1])
    with col5:
        st.slider('加载1：', 1, 100, 50)
    with col6:
        st.slider('加载2：', 1, 100,[2,60])
with col4:
    st.image('a.jpg')

col7, col8, = st.columns([1,3])
with col7:
    st.image('b.jpg')
with col8:
    st.write('你喜欢啥运动捏?')
    col9, col10= st.columns([1,0.3])
    with col9:
        st.checkbox('A.跑步')
        st.checkbox('c.骑行')     
    with col10:
        st.checkbox('B.游泳')
        st.checkbox('D.其他')

col11, col12, = st.columns([1,3])
with col11:
    st.image('g.jpg')
with col12:
    go = st.selectbox('你的支持是我最大的动力，去支持一下up吧！', ['我的贴吧', '我的bilibili'])
    if go == '我的贴吧':
        st.link_button('帮我盖楼', 'https://www.baidu.com/')
    elif go == '我的bilibili':
        st.link_button('帮我一键三连', 'https://www.bilibili.com/')

col13, col14, = st.columns([1,3])
with col13:
    st.image('e.jpg')
with col14:
    st.markdown('# 非常感谢大家支持！！！') 
    st.markdown('### Thank you for you support！！！') 
    


import streamlit as st
from PIL import Image
import time

page = st.sidebar.radio('我的首页', ['兴趣推荐', '图片处理工具', '智能词典', '留言区'])

    
def page_1():
    '''兴趣推荐'''
    with open('河西走廊之梦.mp3','rb') as f:
        mymp3 = f.read()
    st.audio(mymp3, format='audio/mp3', start_time=0)
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
    
def img_change(img,rc,gc,bc):
    #改图
    width,height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            #RGB
            r = img_array[x,y][rc]
            g = img_array[x,y][gc]
            b = img_array[x,y][bc]
            img_array[x,y] = (r,g,b)
    return img

def page_2():
    '''图片处理工具'''
    st.write(":sunglasses:图片换色:sunglasses:")
    uploaded_file = st.file_uploader("上传图片",type=['png','jpeg','jpg'])
    if uploaded_file:
        #获取文件名称，类型，大小
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        st.image(img)
        #选择框
        tab1,tab2,tab3,tab4 = st.tabs(["原图","改色1","改色2","改色3"])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img,0,2,1))
        with tab3:
            st.image(img_change(img,1,2,0))
        with tab4:
            st.image(img_change(img,1,0,2))
        
def page_3():
    '''智能词典'''
    st.write('智能词典')

    with open('words_space.txt','r',encoding='utf-8') as f:
        words_list = f.read().split('\n')

    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')

    words_dict ={}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]),i[2]] 

    with open('check_out_times.txt','r',encoding='utf-8') as f:
        times_list = f.read().split('\n')
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')
    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])
    word = st.text_input('输入要查询的单词')

    if word in words_dict:
        st.write(words_dict[word])
        n = words_dict[word][0]

        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        with open('check_out_times.txt','w',encoding='utf-8') as f:
            message = ''
            for k,v in times_dict.items():
                message += str(k) + '#' + str(v) + '\n'
            message = message[:-1]
            f.write(message)

def page_4():
    '''留言区'''
    st.write('留言区')
    with open('leave_messages.txt','r',encoding='utf-8') as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')
    for i in messages_list:
        if i[1] == '阿短':
            with st.chat_message('🌞'):
                st.write(i[1],':',i[2])
        elif i[1] == '编程猫':
            with st.chat_message('🍥'):
                st.write(i[1],':',i[2])

    name = st.selectbox('我是......',['阿短','编程猫'])
    new_message = st.text_input('想要说的话......')
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1),name,new_message])
        with open('leave_messages.txt','w',encoding='utf-8') as f:
            message = ''
            for i in messages_list:
                message += i[0] + '#' + i[1] + '#' + i[2] + '\n'
            message = message[:-1]
            f.write(message)

 
if page == '兴趣推荐':
    page_1()
elif page == '图片处理工具':
    page_2()
elif page == '智能词典':
    page_3()
elif page == '留言区':
    page_4()



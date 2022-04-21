import streamlit as st
from time import time
from time import sleep

st.title("BASICS OF STREAMLIT APP")
st.image("download.png")
st.write('This app is developed as purpose of notes')
st.write("---")


st.header("st.header")
st.text("st.header used to write headings in app, just like bellow;")
st.header("This is a Header")
if st.checkbox('Show Code for st.header'):
    with st.echo():
        st.header("This is a Header")
st.write("---")

st.header("st.subheader")
st.text("st.subheader used to write subheadings in app, just like bellow;")
st.subheader("This is a subheader")
if st.checkbox('Show Code for st.subheader'):
    with st.echo():
        st.subheader("This is a subheader")
st.write("---")

st.header("st.markdown")
st.text("st.markdown used to write markdowns in app, just like bellow;")
st.markdown("This is a markdown text")
if st.checkbox('Show Code for st.markdown'):
    with st.echo():
        st.markdown("This is a markdown text")
st.write("---")

st.header("st.write")
st.text("st.write used to write simple text in app, just like bellow;")
st.write("This is a simple text")
if st.checkbox('Show Code for st.write'):
    with st.echo():
        st.write("This is a simple text")
st.write("---")

st.header("st.caption")
st.text("st.caption used to write captions in app, just like bellow;")
st.caption("This is a caption")
if st.checkbox('Show Code for st.caption'):
    with st.echo():
        st.caption("This is a caption")
st.write("---")

st.header('st.latex')
st.text("st.latex used to write equations in app, just like bellow;")
st.latex(r''' a+a r^1+a r^2+a r^3 ''')
if st.checkbox('Show Code for st.latex'):
    with st.echo():
        st.latex(r''' a+a r^1+a r^2+a r^3 ''')
st.write("---")

st.header('st.code')
st.text("st.code used to write codes in app, just like bellow;")
st.code("st.code()")
if st.checkbox('Show Code for st.code'):
    with st.echo():
        st.code("st.code()")
st.write("---")

st.header("st.image")
st.text("st.image used to add pictures in app,just like bellow;")
st.image("image.jpg")
if st.checkbox('Show Code for st.image'):
    with st.echo():
        st.image("image.jpg")
st.write("---")

st.header("st.audio")
st.text("st.audio used to add audio in app,just like bellow;")
st.audio("music.mp3")
if st.checkbox('Show Code for st.audio'):
    with st.echo():
        st.audio("music.mp3")
st.write("---")

st.header("st.video")
st.text("st.video used to add video in app,just like bellow;")
st.video("video.mp4")
if st.checkbox('Show Code for st.video'):
    with st.echo():
        st.video("video.mp4")
st.write("---")

# st.video("video.mp4")

st.header("st.checkbox")
st.text("st.checkbox used to add checkbox in app,just like bellow;")
# st.checkbox('yes')
if st.checkbox('Show Code for st.checkbox'):
    with st.echo():
        st.checkbox('yes')
st.write("---")

st.header("st.button")
st.text("st.button used to add button in app,just like bellow;")
st.button('Click')
if st.checkbox('Show Code for st.button'):
    with st.echo():
        st.button('Click')
st.write("---")

st.header("st.radio")
st.text("st.radio used to show options in app,just like bellow;")
st.radio('Pick your gender',['Male','Female'])
if st.checkbox('Show Code for st.radio'):
    with st.echo():
        st.radio('Pick your gender',['Male','Female'])
st.write("---")

st.header("st.selectbox")
st.text("st.selectbox used to select options in app, just like bellow;")
st.selectbox('Pick your gender',['Male','Female'])
if st.checkbox('Show Code for st.selectbox'):
    with st.echo():
        st.selectbox('Pick your gender',['Male','Female'])
st.write("---")

st.header("st.multiselect")
st.text("st.multiselect used to select multiple options in app, just like bellow;")
st.multiselect('choose a planet',['Jupiter', 'Mars', 'neptune'])
if st.checkbox('Show Code for st.multiselect'):
    with st.echo():
        st.multiselect('choose a planet',['Jupiter', 'Mars', 'neptune'])
st.write("---")

st.header("st.select_slider")
st.text("st.select_slider used to show slider for distinict gradient in app, just like bellow;")
st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
if st.checkbox('Show Code for st.select_slider'):
    with st.echo():
        st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
st.write("---")

st.header("st.slider")
st.text("st.slider used to show slider for continous numbers in app, just like bellow;")
st.slider('Pick a number', 0,50,2)
if st.checkbox('Show Code for st.slider'):
    with st.echo():
        st.slider('Pick a number', 0,50,2)
st.write("---")

st.header("st.number_input")
st.text("st.number_input used to show box to input numbers in app, just like bellow;")
st.number_input('Pick a number', 0,10)
if st.checkbox('Show Code for st.number_input'):
    with st.echo():
        st.number_input('Pick a number', 0,10)
st.write("---")

st.header("st.text_input")
st.text("st.text_input used to show box to input text in app, just like bellow;")
st.text_input('Email address')
if st.checkbox('Show Code for st.text_input'):
    with st.echo():
        st.text_input('Email address')
st.write("---")

st.header("st.date_input")
st.text("st.date_input used to show box with calender to input date in app, just like bellow;")
st.date_input('Travelling date')
if st.checkbox('Show Code for st.date_input'):
    with st.echo():
        st.date_input('Travelling date')
st.write("---")

st.header("st.time_input")
st.text("st.time_input used to show box to input date with suggestions in app, just like bellow;")
st.time_input('School time')
if st.checkbox('Show Code for st.time_input'):
    with st.echo():
        st.time_input('School time')
st.write("---")

st.header("st.text_area")
st.text("st.text_area used to show a big box to input long text in app, just like bellow;")
st.text_area('Description')
if st.checkbox('Show Code for st.text_area'):
    with st.echo():
        st.text_area('Description')
st.write("---")

st.header("st.file_uploader")
st.text("st.file_uploader used to show a drag and drop box to input files in app, just like bellow;")
st.file_uploader('Upload a photo or file')
if st.checkbox('Show Code for st.file_uploader'):
    with st.echo():
        st.file_uploader('Upload a photo or file')
st.write("---")

st.header("st.color_picker")
st.text("st.color_picker used to show a small box to pick color with HEX color suggesstions in app, just like bellow;")
st.color_picker('Choose your favorite color')
if st.checkbox('Show Code for st.color_picker'):
    with st.echo():
        st.color_picker('Choose your favorite color')
st.write("---")

st.header("st.balloons")
st.text("st.balloons used to show balloons in app whenever you make changes, just like you see;")
st.balloons()
if st.checkbox('Show Code for st.balloon'):
    with st.echo():
        st.balloons()
st.write("---")

st.header("st.progress")
st.text("st.progress used to show a progress bar in app, just like bellow;")
st.progress(10)
if st.checkbox('Show Code for st.progress'):
    with st.echo():
        st.progress(10)
st.write("---")

st.header("st.spinner")
st.text("st.spinner used to show a spinner with a input messege and losds/sleep the app for given seconds")
with st.spinner('Wait for it...'):
    sleep(1)
if st.checkbox('Show Code for st.spinner'):
    with st.echo():
        with st.spinner('Wait for it...'):
            sleep(5)
st.write("---")

st.header("st.success")
st.text("st.success used to show a green bar in app showing some success, just like bellow;")
st.success("You did it !")
if st.checkbox('Show Code for st.success'):
    with st.echo():
        st.success("You did it !")
st.write("---")

st.header("st.error")
st.text("st.error used to show a red bar in app showing some error, just like bellow;")
st.error("oops! you got some Error")
if st.checkbox('Show Code for st.errorr'):
    with st.echo():
        st.error("oops! you got some Error")
st.write("---")

st.header("st.warning")
st.text("st.warning used to show a yellow bar in app showing some warning, just like bellow;")
st.warning("Thers's a Warning")
if st.checkbox('Show Code for st.warning'):
    with st.echo():
        st.warning("Thers's a Warning")
st.write("---")

st.header("st.info")
st.text("st.info used to show a blue bar in app showing some important information message, just like bellow;")
st.info("It's easy to build a streamlit app")
if st.checkbox('Show Code for st.info'):
    with st.echo():
        st.info("It's easy to build a streamlit app")
st.write("---")

st.header("st.exception")
st.text("st.exception used to show a red bar in app showing some exception/error, just like bellow;")
st.exception(RuntimeError("RuntimeError exception"))
if st.checkbox('Show Code for st.execption'):
    with st.echo():
        st.exception(RuntimeError("RuntimeError exception"))
st.write("---")

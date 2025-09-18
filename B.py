import streamlit as st
import google.generativeai as genai

genai.configure(api_key = "AIzaSyB46ZXN6HfBHiJpqbdp81Wmg0IEn2y0mTA")

model = genai.GenerativeModel("gemini-1.5-flash")

def generate_response(prompt):
    try:
      response = model.generate_content(prompt)
      return response.text
    except Exception as e:
       print(e)
def setup():
  st.set_page_config(page_title="Teaching AI", page_icon="🧑‍🏫")
  st.title("Teaching AI")
  st.write("I am your teacher😠")
  if "history" not in st.session_state:
    st.session_state.history = []
  if st.button("Clear History"):
    st.session_state.history = []
    st.rerun()

  a=st.text_input("Ask me anything : ")
  if st.button("Ask"):
    if a.strip():
      with st.spinner("Thinking (•_•)💭"):
        response = generate_response(a.strip())
        st.session_state.history.append({"question":a.strip(),"answer":response})

        
    else:
      st.warning("Please enter a question👿")
  history_html="<div class='history'>"
  for idx,qa in enumerate(st.session_state.history,1):
    q=qa["question"]
    a=qa["answer"]
    history_html+=f"<div class='question'>Q{idx}:{q}</div>"
    history_html+=f"<div class='answer'>A{idx}:{a}</div>"
  history_html+="</div>"
  st.markdown(history_html,unsafe_allow_html=True)
setup()
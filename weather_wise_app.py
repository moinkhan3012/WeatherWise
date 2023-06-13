import os
import streamlit as st

from langchain.llms import OpenAI

from langchain import LLMChain
from langchain.agents import load_tools,ZeroShotAgent, AgentExecutor

from langchain.memory import ConversationBufferMemory
from pyowm.commons.exceptions import NotFoundError
from dotenv import load_dotenv
load_dotenv()

def verifyOpenAIKey(key:str):
    if not (key.startswith('sk-') and len(key)==51):
        st.warning('OpenAI Key is not correct.', icon='⚠')
        
        return False

    return True


def initialize():
    llm= OpenAI(temperature =0, model_name = 'gpt-3.5-turbo')

    tools = load_tools(["openweathermap-api",'google-search'], llm)


    prefix = """Yor are a weather activity application, and you are trained to return the weather of the location. If ask any further subsequent question for the location, you need to answer the question considering the location given by user as a input. To better utitlize the tools, you should save the country of the location. Whenever using the OpenWeatherMap tool, you should pass the actuion input in this form, City/State/location, Country name, eg. Texas,US. You have access to the following tools"""
    suffix = """Begin!"
    {chat_history}
    Question: {input}
    {agent_scratchpad}"""

    prompt = ZeroShotAgent.create_prompt(
        tools, 
        prefix=prefix, 
        suffix=suffix, 
        input_variables=["input", "chat_history", "agent_scratchpad"]
    )
    memory = ConversationBufferMemory(memory_key="chat_history")

    llm_chain = LLMChain(llm=OpenAI(temperature=0), prompt=prompt)
    agent = ZeroShotAgent(llm_chain=llm_chain, tools=tools, verbose=True)
    agent_chain = AgentExecutor.from_agent_and_tools(agent=agent, tools=tools, verbose=True, memory=memory)

    return agent_chain


def main():
    st.sidebar.title('OpenAI API Key')
    openai_api_key = st.sidebar.text_input('Enter OpenAI API Key here or [get one here](https://platform.openai.com/account/api-keys)')
    if 'openai_api_key' not in st.session_state:
        print(openai_api_key)
        if verifyOpenAIKey(openai_api_key):    
            if openai_api_key:
                st.session_state.openai_api_key = openai_api_key
                os.environ['OPENAI_API_KEY'] = openai_api_key
        else:
            return
    else: 
        os.environ['OPENAI_API_KEY'] = st.session_state.openai_api_key

    prompt = st.text_input('Ask your questions here!!!')


    if st.button("Reset", type="primary"):
        # print('button initialize')
        st.session_state.agent_chain = initialize()
        prompt = ''
        

    if 'agent_chain' not in st.session_state:
        st.session_state.agent_chain = initialize()


    if prompt:
        # print(prompt)
        try:
            st.info(st.session_state.agent_chain.run(input=prompt))
            
        except NotFoundError as err:
            st.error(f":red[{type(err).__name__}\:{err}  \nHint: City name not found in the prompt]")

        except Exception as err:
            
            st.error(f":red[{type(err).__name__}\:{err}]")

        with st.expander('Conversation History'):
            st.info(st.session_state.agent_chain.memory.buffer.replace('\n','  \n'))

  
if __name__ == "__main__":
    st.set_page_config(
        page_title=":red[Weather Wise]",
        page_icon="robot_face",
        layout="wide")
    st.title(':red[Weather Wise]')
    main()
    
            
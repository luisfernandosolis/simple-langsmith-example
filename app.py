from langchain.llms import OpenAI
from langchain import PromptTemplate, LLMChain
import os
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain
from dotenv import load_dotenv
import chainlit as cl

from langchain.schema import StrOutputParser


## create the chain

llm=OpenAI()

prompt_template_one=PromptTemplate.from_template("Give me a name of company that makes {product}"
)

prompt_template_two=PromptTemplate.from_template("give me a description of this kinds of company who names is like this: {company}"
)

{"company":LLMChain(llm=llm, prompt=prompt_template_one, output_parser=StrOutputParser())}


chain=(
    {"company":LLMChain(llm=llm, prompt=prompt_template_one, output_parser=StrOutputParser())}
    |prompt_template_two
    |llm 
    | StrOutputParser()
)
print(chain.invoke("Apple"))

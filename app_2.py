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

llm = OpenAI(temperature=0.7)
chain_one = LLMChain(llm=llm, prompt=prompt_template_one)

chain_two=LLMChain(llm=llm, prompt=prompt_template_two)




overall_chain = SimpleSequentialChain(
    chains=[chain_one, chain_two], verbose=True
)

review = overall_chain.run("Apple")

print(review)

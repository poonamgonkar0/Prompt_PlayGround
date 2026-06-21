from langchain_openai import ChatOpenAI

key = open('api.txt').read().strip()

model=ChatOpenAI(api_key=key ,model="gpt-4o-mini")

from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate

system_prompt = SystemMessagePromptTemplate.from_template(
    'you are a polite and helpful {role}. your work is to {task} the given '
    'input by user but also follow the {constraint} and give the output in {output} Length'
    
)
human_prompt=HumanMessagePromptTemplate.from_template('{input_message}')

prompt=ChatPromptTemplate.from_messages([system_prompt,human_prompt])

from langchain_core.output_parsers import StrOutputParser

output= StrOutputParser()

chain= prompt | model | output

def playGround (role,task,constraint,length,output,input_message):
    
    response=chain.invoke({
         "role": role,
        "task": task,
        "constraint": constraint,
        "length": length,
        "output": output,
        "input_message": input_message
    })
    return response

def custum_prompt (role,task,constraint,length,output,input_message):
    formatted_prompt = prompt.format_messages(
    role="Teacher",
    task="explain",
    constraint="Bullet Points",
    output="short",
    input_message="ml")

    full_text = "\n".join([message.content for message in formatted_prompt])
    
    return full_text
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o-mini")
result = model.invoke("Hello, how are you?")

# print(result)

print(result.content)
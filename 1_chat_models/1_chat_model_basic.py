from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o-mini")
result = model.invoke("Hello, how are you?")

print("Full response:")
print(result)

print("************")

print("Content only:")
print(result.content)
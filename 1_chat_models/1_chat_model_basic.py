# Import the ChatOpenAI class from the langchain_openai module
from langchain_openai import ChatOpenAI

# Initialize the ChatOpenAI model with the specified model name
model = ChatOpenAI(model="gpt-4o-mini")

# Invoke the model with a sample input and store the result
result = model.invoke("Hello, how are you?")

# Print the full response from the model
print("Full response:")
print(result)

print("************")

# Print only the content part of the response
print("Content only:")
print(result.content)
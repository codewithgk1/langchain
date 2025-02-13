from langchain.chat_models import init_chat_model

# pass any model along with the model provider
# follow link to check list of models and model providers : https://python.langchain.com/docs/integrations/chat/#featured-providers
model = init_chat_model(model="gpt-4o-mini", model_provider="openai")
result = model.invoke("Hello, how are you?")

print("Full Response")
print(result)

print("Only Content")
print(result.content)
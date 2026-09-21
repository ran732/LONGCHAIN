from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    temperature=0.5
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("Tell me the name of 5 indian girl name")

print(result.content)
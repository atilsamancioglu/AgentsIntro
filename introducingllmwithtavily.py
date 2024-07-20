from dotenv import load_dotenv
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

load_dotenv()

model = ChatOpenAI(model="gpt-4")

search = TavilySearchResults(max_results=2)
# If we want, we can create other tools.
# Once we have all the tools we want, we can put them in a list that we will reference later.
tools = [search]

model_with_tools = model.bind_tools(tools)

# response = model_with_tools.invoke([HumanMessage(content="Hi!")])
# print(response)
# print(f"ToolCalls: {response.tool_calls}")
# tool calls is 0


if __name__ == '__main__':
    response = model_with_tools.invoke([HumanMessage(content="What's the weather in istanbul?")])
    print(f"ContentString: {response.content}")
    print(f"ToolCalls: {response.tool_calls}")
    #tool called tavily




from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv

load_dotenv()

class LogAnalyst:
    def __init__(self):
        self.llm = ChatOpenAI(model = "gpt-4o", temperature=0)

    async def analyze(self, query: str, logs: list):
        if not logs:
            return "No logs found."
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a DevOps expert. Analyze these logs"),
            ("user", "Question: {query} \n\n Logs:{logs_text}")
        ])

        chain = prompt | self.llm | StrOutputParser()

        logs_text = "\n".join([str(log) for log in logs])
        response = await chain.ainvoke({"query": query, "logs_text": logs_text})

        return response
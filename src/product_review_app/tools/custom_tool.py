from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field

from crewai_tools import ScrapeWebsiteTool

# To enable scrapping any website it finds during it's execution
tool = ScrapeWebsiteTool()

# Initialize the tool with the website URL, 
# so the agent can only scrap the content of the specified website
tool = ScrapeWebsiteTool(website_url='https://www.example.com')

# Extract the text from the site
text = tool.run()
print(text)


class MyCustomToolInput(BaseModel):
    """Input schema for MyCustomTool."""
    argument: str = Field(..., description="")

class getDataPolymarket(BaseTool):
    name: str = "get_data_polymarket"
    description: str = (
        "This tool will return all the scrapped data from polymarket.com"
    )
    args_schema: Type[BaseModel] = MyCustomToolInput

    def _run(self, argument: str) -> str:
        # To enable scrapping any website it finds during it's execution
        tool = ScrapeWebsiteTool()

        # Initialize the tool with the website URL, 
        # so the agent can only scrap the content of the specified website
        tool = ScrapeWebsiteTool(website_url='https://www.polymarket.com')

        # Extract the text from the site
        text = tool.run()
        return text


class getDataKalshi(BaseTool):
    name: str = "get_data_kalshi"
    description: str = (
        "This tool will return all the scrapped data from kalshi.com"
    )
    args_schema: Type[BaseModel] = MyCustomToolInput

    def _run(self, argument: str) -> str:
        # To enable scrapping any website it finds during it's execution
        tool = ScrapeWebsiteTool()

        # Initialize the tool with the website URL, 
        # so the agent can only scrap the content of the specified website
        tool = ScrapeWebsiteTool(website_url='https://www.kalshi.com')

        # Extract the text from the site
        text = tool.run()
        return text

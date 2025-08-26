from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from crewai_tools import ScrapeWebsiteTool
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

scrape_polymarket = ScrapeWebsiteTool(website_url='https://www.polymarket.com')
scrape_kalshi = ScrapeWebsiteTool(website_url='https://www.kalshi.com')

@CrewBase
class ProductReviewApp():
    """ProductReviewApp crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def data_collector(self) -> Agent:
        return Agent(
            config=self.agents_config['data_collector'], # type: ignore[index]
            verbose=True,
            tools = [scrape_polymarket, scrape_kalshi]
        )

    @agent
    def data_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['data_analyst'], # type: ignore[index]
            verbose=True
        )
    
    @agent
    def data_formatter(self) -> Agent:
        return Agent(
            config=self.agents_config['data_formatter'], # type: ignore[index]
            verbose=True
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def data_collection_task(self) -> Task:
        return Task(
            config=self.tasks_config['data_collection_task'], # type: ignore[index]
            output_file = 'raw_data.json'
        )

    @task
    def data_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['data_analysis_task'], # type: ignore[index]
            output_file='unified.json'
        )
    
    @task
    def data_formatting_task(self) -> Task:
        return Task(
            config=self.tasks_config['data_formatting_task'], # type: ignore[index]
            output_file='final.csv'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the ProductReviewApp crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )

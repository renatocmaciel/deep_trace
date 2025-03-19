from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from .tools.linkedin import LinkedInTool
from .tools.image_analyzer import ImageAnalysisTool
from .models import BasicInfo, DeepSearchInfo, ImageCollection, ImageAnalysis, Profile

@CrewBase
class DeepTraceCrew():
    """Profile Tracing crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def basic_info_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['basic_info_agent'],
            tools=[LinkedInTool(max_calls=1)],
            allow_delegation=False,
            verbose=True,
            max_iter=1
        )

    @agent
    def deep_search_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['deep_search_agent'],
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            allow_delegation=False,
            verbose=True,
        )

    @agent
    def image_fetch_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['image_fetch_agent'],
            tools=[ScrapeWebsiteTool(max_calls=10)],
            allow_delegation=False,
            verbose=True,
            max_iter=2
        )

    @agent
    def image_analysis_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['image_analysis_agent'],
            tools=[ImageAnalysisTool(max_calls=1)],
            allow_delegation=False,
            verbose=True,
            max_iter=2
        )

    @agent
    def consolidation_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['consolidation_agent'],
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            allow_delegation=False,
            verbose=True,
        )


    @task
    def basic_info_task(self) -> Task:
        return Task(
            config=self.tasks_config['basic_info_task'],
            agent=self.basic_info_agent(),
            output_pydantic=BasicInfo,
            max_retries=1
        )

    @task
    def deep_search_task(self) -> Task:
        return Task(
            config=self.tasks_config['deep_search_task'],
            agent=self.deep_search_agent(),
            context=[self.basic_info_task()],
            output_pydantic=DeepSearchInfo,
            max_retries=1
        )

    @task
    def image_collection_task(self) -> Task:
        return Task(
            config=self.tasks_config['image_collection_task'],
            agent=self.image_fetch_agent(),
            context=[self.basic_info_task(), self.deep_search_task()],
            output_pydantic=ImageCollection,
            max_retries=1
        )

    @task
    def image_processing_task(self) -> Task:
        return Task(
            config=self.tasks_config['image_processing_task'],
            agent=self.image_analysis_agent(),
            context=[self.basic_info_task(), self.image_collection_task()],
            output_pydantic=ImageAnalysis,
            max_retries=1
        )

    @task
    def data_consolidation_task(self) -> Task:
        return Task(
            config=self.tasks_config['data_consolidation_task'],
            agent=self.image_analysis_agent(),
            context=[self.basic_info_task(), self.deep_search_task(), self.image_collection_task(), self.image_processing_task()],
            output_pydantic=Profile,
            max_retries=1
        )


    @crew
    def crew(self) -> Crew:
        """Creates the DeepTrace crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
            output_pydantic=Profile
        )

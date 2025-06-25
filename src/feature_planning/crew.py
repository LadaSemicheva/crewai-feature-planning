from crewai import Agent
from crewai import Crew
from crewai import Process
from crewai import Task
from crewai.memory import LongTermMemory
from crewai.memory import ShortTermMemory
from crewai.memory.storage.ltm_sqlite_storage import LTMSQLiteStorage
from crewai.memory.storage.rag_storage import RAGStorage
from crewai.project import agent
from crewai.project import crew
from crewai.project import CrewBase
from crewai.project import task
from crewai_tools import SerperDevTool


@CrewBase
class FeaturePlanning:
    """FeaturePlanning crew"""

    @agent
    def tech_spec_extractor_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["tech_spec_extractor_agent"],  # type: ignore[index]
            verbose=True,
            tools=[SerperDevTool()],
        )

    @agent
    def feature_extraction_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["feature_extraction_agent"],  # type: ignore[index]
            verbose=True,
        )

    @task
    def tech_spec_extraction_task(self) -> Task:
        return Task(
            config=self.tasks_config["tech_spec_extraction_task"],  # type: ignore[index]
        )

    #
    @task
    def feature_extraction_task(self) -> Task:
        return Task(
            config=self.tasks_config["feature_extraction_task"],  # type: ignore[index]
        )

    @crew
    def crew(self) -> Crew:
        """Creates the FeaturePlanning crew"""

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
            memory=True,
            long_term_memory=LongTermMemory(
                storage=LTMSQLiteStorage(db_path="./memory/long_term_memory_storage.db")
            ),
            short_term_memory=ShortTermMemory(
                storage=RAGStorage(
                    embedder_config={
                        "provider": "openai",
                        "config": {"model": "text-embedding-3-small"},
                    },
                    type="short_term",
                    path="./memory/",
                )
            ),
        )

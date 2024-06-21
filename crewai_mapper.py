import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process
from langchain_openai import AzureOpenAI
from pathlib import Path

#environment variable setup
load_dotenv()


GPT35 = AzureOpenAI(
    azure_endpoint=os.environ.get("AZURE_ENDPOINT"),
    openai_api_version="2023-07-01-preview",
    azure_deployment=os.environ.get("GPT_DEPLOYMENT_NAME"),
    openai_api_key=os.environ.get("OPENAI_API_KEY"),
    openai_api_type="azure",
    max_tokens= -1
)

# use path variables to define input and output directories
INPUT_PATH = Path("./input_data")
OUTPUT_PATH = Path("./output_data")

data_analyst = Agent(
  role='Senior Data Analyst',
  goal='Analyse accounting data from an input format and figure out which columns can be mapped to a set output format.',
  verbose=True,
  memory=True,
  backstory=(
  """You have over 10 years of experience as a data analyst and engineer.
  You are able to look at an input dataset and a list of output columns and see which input dataset 
  columns correspond to what output column names. You respond only with the useful information and in English.
  """
  ),
  tools=[],
  allow_delegation=True,
  llm=GPT35
)

analyse_output = Task(
  description=(
  """
  Analyse the following column names: {expected}. 
  What potential columns from {dataset} could they correspond to? 
  Give a concise answer only with the potential matches, do not give explanations.
  """
  ),
  expected_output="Return only the potential matches to the {expected} columns in this format: {format}",
  tools=[],
  agent=data_analyst,
  async_execution=False,
  output_file = str(OUTPUT_PATH / 'outputReport.md')
)

mapping_crew = Crew(
  agents=[data_analyst], 
  tasks=[analyse_output], 
  process=Process.sequential
)

format = "-->expected_column -->dataset_column"

    
def get_mapping(expected: list, input: str):
    result = mapping_crew.kickoff(inputs={'dataset': input, 'expected': expected, 'format': format})
    return result
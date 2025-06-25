import warnings

from feature_planning.crew import FeaturePlanning

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

user_stories = [
    "As a recruiter, I want to upload resumes, so that I can add candidates to the system.",
    "As a recruiter, I want to extract skills from resumes, so that I can screen quickly.",
    "As a recruiter, I want to search by skill, so that I can find candidates faster.",
    "As a recruiter, I want to view summaries, so that I can present profiles to managers.",
]


def run():
    for i, user_story in enumerate(user_stories, start=1):
        inputs = {
            "user_story": user_story,
            "tech_spec_output_path": f"output/tech_specs/tech_spec_{i}.md",
            "feature_output_path": f"output/features/features_{i}.md",
        }

        crew = FeaturePlanning().crew()
        crew.kickoff(inputs=inputs)

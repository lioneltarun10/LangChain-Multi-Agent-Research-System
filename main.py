from src.pipelines.pipeline import run_research_pipeline

if __name__ == "__main__":
    topic = "The impact of AI on job market in 2026"
    result = run_research_pipeline(topic)
    # print("\nFinal Result:\n", result)
from deep_trace.crew import DeepTraceCrew
from deep_trace.models import Profile
from deep_trace.database.database import search_profile_in_db, save_profile_to_db


def run_deep_search(inputs) -> Profile:
    deep_trace_crew = DeepTraceCrew()
    crew = deep_trace_crew.crew()
    return crew.kickoff(inputs=inputs)



async def run_deep_search_async(inputs) -> Profile:
    deep_trace_crew = DeepTraceCrew()
    crew = deep_trace_crew.crew()
    results = await crew.kickoff_async(inputs=inputs)
    # save_profile(results.pydantic)
    return results.pydantic




async def deep_trace(inputs) -> Profile:
    if search_results := search_profile_in_db_async(inputs):
        return search_results
    profile = run_deep_search_async(inputs)
    save_profile_to_db_async(profile)
    return profile


async def deep_trace(inputs) -> Profile:
    if search_results :=  search_profile_in_db(inputs):
        return search_results

    profile = await run_deep_search_async(inputs)
    save_profile_to_db(profile, inputs)

    return profile

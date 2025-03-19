import logging
from crewai.tools import BaseTool

from deep_trace.tools.client import LinkedinClient


class LinkedInTool(BaseTool):
    name: str = "Retrieve LinkedIn profiles"
    description: str = (
        "Retrieve LinkedIn profiles given a name. Comma separated"
    )

    def _run(self, name: str) -> str:
        try:
            linkedin_client = LinkedinClient()
            people = linkedin_client.find_people(name)
            people = self._format_publications_to_text(people)
            linkedin_client.close()
            return people
        except Exception as e:
            logging.error(f'LinkedInTool error: {e}')
            return []

    def _format_publications_to_text(self, people):
        result = ["\n".join([
            "Person Profile",
            "-------------",
            p['profile_photo'],
            p['name'],
            p['position'],
            p["location"],
            p["profile_link"],
        ]) for p in people]
        result = "\n\n".join(result)

        return result

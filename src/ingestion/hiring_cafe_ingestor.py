from ingestion.base_ingestor import BaseIngestor
from ingestion.logger import logger


class HiringCafeIngestor(BaseIngestor):
    def __init__(self):
        super().__init__(source_name="hiring_cafe")

    def fetch_jobs(self):
        """
        Placeholder for Hiring Cafe ingestion logic.
        """
        logger.info("Fetching jobs from Hiring Cafe (stub)")
        return []

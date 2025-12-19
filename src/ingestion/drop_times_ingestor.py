from ingestion.base_ingestor import BaseIngestor
from ingestion.logger import logger


class DropTimesIngestor(BaseIngestor):
    def __init__(self):
        super().__init__(source_name="the_drop_times")

    def fetch_jobs(self):
        """
        Placeholder for The Drop Times ingestion logic.
        Actual fetching will be implemented next.
        """
        logger.info("Fetching jobs from The Drop Times (stub)")
        return []

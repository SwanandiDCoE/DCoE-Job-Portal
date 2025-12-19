from abc import ABC, abstractmethod
from datetime import datetime


class BaseIngestor(ABC):
    """
    Base class for all job data ingestors.
    Each source-specific ingestor must implement this interface.
    """

    def __init__(self, source_name: str):
        self.source_name = source_name

    @abstractmethod
    def fetch_jobs(self):
        """
        Fetch raw job data from the source.
        Must be implemented by subclasses.
        """
        pass

    def build_raw_job_record(self, job: dict) -> dict:
        """
        Wrap a raw job payload into the standard ingestion schema.
        """
        return {
            "source": self.source_name,
            "source_job_id": job.get("id"),
            "title": job.get("title"),
            "company_name": job.get("company"),
            "location": job.get("location"),
            "employment_type": job.get("employment_type", "unknown"),
            "job_url": job.get("url"),
            "posted_date": job.get("posted_date"),
            "ingested_at": datetime.utcnow().isoformat(),
            "raw_payload": job,
        }

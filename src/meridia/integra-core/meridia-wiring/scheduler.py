# scheduler.py — Meridia Feed Scheduler
# Runs all six data sources on their natural cadences
# Run: python scheduler.py
# Runs as a background process on the NAS

import asyncio
import sys
from pathlib import Path
from loguru import logger
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

sys.path.insert(0, str(Path(__file__).parent))
from feeds.pull_all import pull_fred, pull_census, pull_ffiec, pull_hmda, pull_fdic, pull_cfpb

scheduler = AsyncIOScheduler()

def setup_jobs():
    """
    Schedule each feed on its natural cadence.
    All times are UTC.
    """

    # FRED — Monthly on the 1st at 2:00 AM
    scheduler.add_job(
        pull_fred, CronTrigger(day=1, hour=2, minute=0),
        id="fred_monthly", name="FRED Macro Pull",
        max_instances=1, replace_existing=True
    )

    # Census ACS — Annually on Jan 15 (data released Q1)
    scheduler.add_job(
        pull_census, CronTrigger(month=1, day=15, hour=3, minute=0),
        id="census_annual", name="Census ACS Pull",
        max_instances=1, replace_existing=True
    )

    # FFIEC — Quarterly (Jan, Apr, Jul, Oct 10th)
    scheduler.add_job(
        pull_ffiec, CronTrigger(month="1,4,7,10", day=10, hour=3, minute=30),
        id="ffiec_quarterly", name="FFIEC Census Flat Files",
        max_instances=1, replace_existing=True
    )

    # HMDA — Annually on Mar 1 (prior year data released)
    scheduler.add_job(
        pull_hmda, CronTrigger(month=3, day=1, hour=4, minute=0),
        id="hmda_annual", name="HMDA Loan Data Pull",
        max_instances=1, replace_existing=True
    )

    # FDIC — Annually on Sep 1 (Summary of Deposits released)
    scheduler.add_job(
        pull_fdic, CronTrigger(month=9, day=1, hour=4, minute=30),
        id="fdic_annual", name="FDIC Summary of Deposits",
        max_instances=1, replace_existing=True
    )

    # CFPB Complaints — Daily at 2:30 AM
    scheduler.add_job(
        pull_cfpb, CronTrigger(hour=2, minute=30),
        id="cfpb_daily", name="CFPB Complaint Pull",
        max_instances=1, replace_existing=True
    )

    logger.info("Feed scheduler configured:")
    for job in scheduler.get_jobs():
        logger.info(f"  {job.name} — next run: {job.next_run_time}")

async def main():
    setup_jobs()
    scheduler.start()
    logger.info("Meridia Feed Scheduler running. Ctrl+C to stop.")
    try:
        while True:
            await asyncio.sleep(3600)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
        logger.info("Scheduler stopped.")

if __name__ == "__main__":
    asyncio.run(main())

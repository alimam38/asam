#!/usr/bin/env python3
"""
load_tract_centroids.py — Load Census Bureau Gazetteer tract centroids into PostgreSQL.

Downloads the 2023 national tract gazetteer, parses INTPTLAT/INTPTLONG,
adds centroid_lat/centroid_lng columns to census_tracts, and batch-updates
every row that matches a GEOID in the file.

Usage:
    python load_tract_centroids.py [path/to/2023_Gaz_tracts_national.txt]

Default path: C:/Users/alima/Downloads/2023_Gaz_tracts_national/2023_Gaz_tracts_national.txt
"""

import csv
import os
import sys
import logging
from pathlib import Path
from dotenv import load_dotenv
import psycopg2
import psycopg2.extras

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger(__name__)

DEFAULT_GAZ_PATH = Path(
    r"C:\Users\alima\Downloads\2025_Gaz_tracts_national\2025_Gaz_tracts_national.txt"
)

BATCH_SIZE = 500


def db_connect():
    load_dotenv(Path(__file__).parent / ".env")
    return psycopg2.connect(
        host=os.environ["DB_HOST"],
        port=int(os.environ.get("DB_PORT", 5432)),
        dbname=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
    )


def add_columns(cur):
    cur.execute("""
        ALTER TABLE census_tracts
            ADD COLUMN IF NOT EXISTS centroid_lat  DECIMAL(10,7),
            ADD COLUMN IF NOT EXISTS centroid_lng  DECIMAL(11,7)
    """)
    log.info("centroid_lat / centroid_lng columns ready")


def load_gazetteer(path: Path) -> dict[str, tuple[float, float]]:
    """Parse tab-delimited gazetteer → {geoid: (lat, lng)}."""
    coords: dict[str, tuple[float, float]] = {}

    # Peek at raw bytes to detect BOM or unexpected encoding
    with open(path, "rb") as f:
        raw_header = f.readline()
    log.info(f"Raw header (first 120 bytes): {raw_header[:120]}")

    # utf-8-sig strips BOM automatically; Census files sometimes include it
    with open(path, encoding="utf-8-sig") as f:
        reader = csv.DictReader(f, delimiter="|")
        # Materialise and normalise field names before iteration
        raw_fields = reader.fieldnames or []
        reader.fieldnames = [h.strip() for h in raw_fields]
        log.info(f"Detected columns: {reader.fieldnames}")

        for row in reader:
            geoid = row.get("GEOID", "").strip()
            lat   = row.get("INTPTLAT", "").strip()
            lng   = row.get("INTPTLONG", "").strip()
            if geoid and lat and lng:
                try:
                    coords[geoid] = (float(lat), float(lng))
                except ValueError:
                    pass

    log.info(f"Gazetteer parsed — {len(coords):,} tracts total")
    return coords


def update_tracts(cur, coords: dict[str, tuple[float, float]]) -> int:
    """Batch-update census_tracts with real centroids. Returns updated row count."""
    cur.execute("SELECT geoid FROM census_tracts")
    db_geoids = {row[0] for row in cur.fetchall()}
    log.info(f"census_tracts has {len(db_geoids):,} rows")

    matched = [(lat, lng, geoid) for geoid, (lat, lng) in coords.items() if geoid in db_geoids]
    log.info(f"Matched {len(matched):,} GEOIDs to gazetteer entries")

    if not matched:
        log.warning("No matches — check that GEOID formats align (should be 11 digits)")
        return 0

    updated = 0
    for i in range(0, len(matched), BATCH_SIZE):
        batch = matched[i : i + BATCH_SIZE]
        psycopg2.extras.execute_batch(
            cur,
            "UPDATE census_tracts SET centroid_lat = %s, centroid_lng = %s WHERE geoid = %s",
            batch,
        )
        updated += len(batch)
        log.info(f"  Updated {updated:,} / {len(matched):,} rows …")

    return updated


def verify(cur):
    cur.execute("""
        SELECT
            COUNT(*)                                             AS total,
            COUNT(centroid_lat)                                  AS has_centroid,
            ROUND(AVG(centroid_lat)::numeric, 4)                AS avg_lat,
            ROUND(AVG(centroid_lng)::numeric, 4)                AS avg_lng
        FROM census_tracts
    """)
    row = cur.fetchone()
    log.info(
        f"Verification — total={row[0]}, with centroid={row[1]}, "
        f"avg_lat={row[2]}, avg_lng={row[3]}"
    )


def main():
    gaz_path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_GAZ_PATH

    if not gaz_path.exists():
        log.error(f"Gazetteer file not found: {gaz_path}")
        log.error("Download from: https://www2.census.gov/geo/docs/maps-data/data/gazetteer/2025_Gazetteer/2025_Gaz_tracts_national.zip")
        sys.exit(1)

    log.info(f"Loading from: {gaz_path}")
    coords = load_gazetteer(gaz_path)

    log.info("Connecting to PostgreSQL …")
    conn = db_connect()
    conn.autocommit = False

    try:
        with conn.cursor() as cur:
            add_columns(cur)
            updated = update_tracts(cur, coords)
            verify(cur)
        conn.commit()
        log.info(f"Done — {updated:,} census_tracts rows updated with real centroids")
    except Exception:
        conn.rollback()
        log.exception("Load failed — rolled back")
        sys.exit(1)
    finally:
        conn.close()


if __name__ == "__main__":
    main()

# AIA Corpus — NAS Deployment

## What You're Deploying

Three things:
1. **Corpus schema** — PostgreSQL tables that store and index all institutional knowledge
2. **Cataloger** — Python script that watches your Dropbox folder and auto-registers new files
3. **Docker packaging** — Everything runs as containers on the Synology alongside your existing PostgreSQL

## Prerequisites

- Synology DS925+ with DSM (already running)
- PostgreSQL container (already running)
- Docker and Docker Compose available on NAS
- SSH access to the NAS

## Step-by-Step

### 1. Create the AIA folder on the NAS

```bash
ssh your-nas-ip
mkdir -p /volume1/docker/aia-corpus
mkdir -p /volume1/AIA_Corpus
```

### 2. Copy files to the NAS

Transfer these files to `/volume1/docker/aia-corpus/`:
- `aia_corpus_schema.sql`
- `aia_cataloger.py`
- `Dockerfile`
- `docker-compose.yml`
- `.env.template`

You can use SCP, Synology File Station, or SMB share:
```bash
scp aia_corpus_schema.sql aia_cataloger.py Dockerfile docker-compose.yml .env.template your-nas-ip:/volume1/docker/aia-corpus/
```

### 3. Configure environment

```bash
cd /volume1/docker/aia-corpus
cp .env.template .env
nano .env
```

Update these values:
- `DB_HOST` — Your existing PostgreSQL container name (find with `docker ps`)
- `DB_PASSWORD` — Your actual PostgreSQL password
- `DROPBOX_PATH` — Where Cloud Sync puts Dropbox files (set up in Step 5)

### 4. Deploy the corpus schema

**Option A: Docker Compose (recommended)**
```bash
cd /volume1/docker/aia-corpus
docker-compose up aia-cataloger-init
```
This runs the schema SQL against your PostgreSQL, then exits.

**Option B: Direct SQL (if you prefer)**
```bash
docker exec -i your-postgres-container psql -U postgres -d meridia < aia_corpus_schema.sql
```

If the `meridia` database doesn't exist yet:
```bash
docker exec -i your-postgres-container psql -U postgres -c "CREATE DATABASE meridia;"
docker exec -i your-postgres-container psql -U postgres -d meridia < aia_corpus_schema.sql
```

### 5. Set up Dropbox Cloud Sync

In DSM:
1. Open **Cloud Sync** (install from Package Center if needed)
2. Add **Dropbox** connection
3. Create a new sync task:
   - **Cloud folder:** The new folder you'll create for AIA corpus material
   - **Local path:** `/volume1/Dropbox` (or whatever you set in .env)
   - **Sync direction:** Download only (Dropbox → NAS)
   - **Schedule:** Real-time or every 5 minutes

### 6. Start the cataloger

```bash
cd /volume1/docker/aia-corpus
docker-compose up -d aia-cataloger
```

The cataloger will:
- Watch `/volume1/Dropbox` every 120 seconds
- When new files appear, extract text and register them in `corpus.documents` with status `raw`
- Skip duplicates via SHA-256 checksum
- Log activity to Docker logs

Check logs:
```bash
docker logs -f aia-cataloger
```

### 7. Verify

```bash
docker exec -i your-postgres-container psql -U postgres -d meridia -c "
  SELECT COUNT(*) as total_docs FROM corpus.documents;
  SELECT status, COUNT(*) FROM corpus.documents GROUP BY status;
  SELECT * FROM corpus.naming_registry;
  SELECT title, domain, decided_at FROM corpus.decisions WHERE status = 'active';
"
```

## How Ingestion Works After Deployment

1. **You move files to your Dropbox AIA folder** — from any device, anywhere
2. **Cloud Sync pulls them to the NAS** — automatic, real-time
3. **Cataloger registers them** — text extracted, checksum computed, `raw` record created
4. **We classify in sessions** — open Claude, query raw documents, classify together
5. **Corpus grows** — every session adds structure, lineage, extracts

## Manual Scan (One-Time Batch)

To scan a folder that's already on the NAS without watch mode:

```bash
docker run --rm \
  -v /volume1/some-folder:/data/input:ro \
  --network aia-network \
  aia-cataloger \
  --scan /data/input \
  --db-host your-postgres-container \
  --db-name meridia \
  --db-user postgres \
  --db-pass yourpassword \
  --origin dropbox \
  --verbose
```

Or generate SQL without database connection:

```bash
docker run --rm \
  -v /volume1/some-folder:/data/input:ro \
  -v /volume1/docker/aia-corpus:/data/output \
  aia-cataloger \
  --scan /data/input \
  --sql-output /data/output/batch_inserts.sql \
  --verbose
```

## Folder Structure on NAS (After Deployment)

```
/volume1/
├── docker/
│   └── aia-corpus/           ← Deployment files
│       ├── aia_corpus_schema.sql
│       ├── aia_cataloger.py
│       ├── Dockerfile
│       ├── docker-compose.yml
│       └── .env
├── Dropbox/                  ← Cloud Sync from Dropbox (auto)
│   └── AIA/                  ← Your new Dropbox folder
│       ├── architecture/
│       ├── products/
│       └── ...
├── AIA_Corpus/               ← Local corpus storage
└── docker/                   ← Existing Docker volumes
    └── postgres/             ← Existing PostgreSQL data
```

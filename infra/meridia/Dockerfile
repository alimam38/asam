FROM python:3.11-slim

WORKDIR /app

# Install dependencies
RUN pip install --no-cache-dir \
    PyPDF2 \
    python-docx \
    openpyxl \
    psycopg2-binary

# Copy cataloger
COPY aia_cataloger.py .

# Default: scan mode (override with docker run args)
ENTRYPOINT ["python", "aia_cataloger.py"]

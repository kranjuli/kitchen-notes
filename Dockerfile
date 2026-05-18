FROM ghcr.io/astral-sh/uv:0.11.16-python3.14-trixie-slim@sha256:56378b6ff601fc05ed4d0ef0de5772171427e5b8eff7b2045ac5d0c6db633616

WORKDIR /app

# copy only the files needed for dependency installation to leverage Docker caching
COPY pyproject.toml uv.lock ./

# install dependencies without dev packages, using the lock file for reproducibility
RUN uv sync --no-dev --frozen --no-cache

# now copy the rest of the application code
COPY . .

# set the PATH to include the virtual environment's bin directory
ENV PATH="/app/.venv/bin:$PATH"

ENV PYTHONPATH="/app/src"

# expose the port the app runs on
EXPOSE 5000

# set the default command to run the application
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:5000", "wsgi:application"]

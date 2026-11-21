import os
# One place to change the model. Set WORKSHOP_MODEL in .env to override.
MODEL = os.getenv("WORKSHOP_MODEL", "gemini-3.6-flash")
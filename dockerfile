# 1. Use a lightweight base image
FROM python:3.12-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy only the requirements first to leverage Docker cache
COPY requirements.txt .

# 4. Install dependencies (this layer is cached unless requirements.txt changes)
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of your application files (app.py, static/, templates/, etc.)
COPY . .

# 6. Expose the port your Flask app runs on
EXPOSE 5001

# 7. Run the application
# host 0.0.0.0 is critical so the container can talk to your laptop
CMD ["python", "app.py"]
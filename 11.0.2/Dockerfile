FROM gurobi/python:11.0.2_3.10

# Set the application directory
WORKDIR /app

# Install additional dependencies
RUN python3 -m pip install numpy scipy

# Copy the application code
ADD matrix1.py /app

# Execute the code
CMD ["python", "/app/matrix1.py"]
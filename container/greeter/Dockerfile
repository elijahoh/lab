FROM ubuntu:24.04

WORKDIR /app

# Set default environment variables
ENV GREETING="Hello"
ENV NAME="World"

COPY greet .

RUN chmod +x greet

ENTRYPOINT ["./greet"]

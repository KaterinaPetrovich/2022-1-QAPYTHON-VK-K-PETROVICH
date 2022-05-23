FROM python:3.8
RUN pip install Flask
COPY . /mock

WORKDIR /mock

CMD ["python", "mock_vk_id.py"]
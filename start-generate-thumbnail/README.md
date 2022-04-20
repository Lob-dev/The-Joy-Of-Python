
### Project Settings

```shell
conda create -n generate-thumbnail
conda activate generate-thumbnail
pip install uvicorn fastapi PyYAML opencv-python httpie
```

<br/>

### Project Test
```shell
http -v -j GET http://127.0.0.1:8080/api/video/thumbnail?second=9 filename="sample.mp4" file_store_path="/data" thumbnail_name="sample_image.jpg" thumbnail_store_path="/data"
```
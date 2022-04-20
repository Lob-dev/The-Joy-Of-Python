import cv2


# current_fps = video_capture.get(cv2.CAP_PROP_FPS)  # 초당 프레임 수
# current_frame_count = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))  # 총 프레임의 개수
# target_frame = target_second * current_fps  # 뽑아올 프레임 위치
# current_duration = current_frame_count / current_fps  # 총 프레임의 개수 / 초당 프레임 수 = 초
def generate_thumbnail(
        filename: str,
        file_store_path: str,
        thumbnail_name: str,
        thumbnail_store_path: str,
        target_second: int
) -> None:
    video_capture = cv2.VideoCapture(f'{file_store_path}/{filename}')
    video_capture.set(cv2.CAP_PROP_POS_MSEC, (round(target_second) * 1000))  # target ms의 frame 시점으로 설정
    success, image = video_capture.read()

    cv2.imwrite(f'{thumbnail_store_path}/{thumbnail_name}', image)
    video_capture.release()

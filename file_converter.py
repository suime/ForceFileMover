import fire
import os


def get_unique_filename(file):
    base, extension = os.path.splitext(file)
    counter = 1
    new_file = f"{base}_{counter}{extension}"
    while os.path.exists(new_file):
        counter += 1
        new_file = f"{base}_{counter}{extension}"
    return new_file


def main(filepath: str):
    # 파일 경로가 유효한지 확인
    if not os.path.isfile(filepath):
        return f"{filepath} 파일이 존재하지 않거나 경로가 잘못되었습니다."

    # ^ 1. 파일이름 읽어오기
    if filepath is not None:
        ext = filepath.rsplit(".", 1)[-1]

    # ^ 2. 인코딩인지 디코딩 판별
        with open(filepath, 'rb') as f:  # 바이트로 읽기
            text = f.read()

            # * 앞의 첫 두글자가 따옴표이고 확장자가 csv 이고 .의 개수가 2개 이상이라면 -> 해독
            if text[0:1] == b"\"" and ext == "csv" and filepath.count(".") > 1:
                text = text[1:]
                new = filepath.rsplit(".", 1)[0]

                if new.rsplit(".", 1)[-1] == "pdf":
                    text = b"%" + text

                if os.path.exists(new):
                    new_file = get_unique_filename(new)

                try:
                    with open(new_file, 'wb') as new_f:  # 바이트로 쓰기
                        new_f.write(text)
                except ValueError as e:
                    return f"{e} 오류가 발생했습니다."

                return f"{new_file}로 파일을 해독하였습니다."

            else:
                new_file = f"{filepath}.csv"

                if os.path.exists(new_file):
                    new_file = get_unique_filename(new_file)

                with open(filepath, 'rb') as f:  # 바이트로 읽기
                    text = f.read()
                    if ext == "pdf":
                        text = text[1:]

                    with open(new_file, 'wb') as csv:  # 바이트로 쓰기
                        text = b"\"" + text  # 바이트로 변환
                        csv.write(text)

                return f"{new_file}로 파일을 저장했습니다.."


if __name__ == "__main__":
    fire.Fire(main)

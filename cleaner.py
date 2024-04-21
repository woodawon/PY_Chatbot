import re # 정규표현식 라이브러리

def remove_chat_metadata(chat_export_file):
    data_time = r"(\d+\/\d+\/\d+, \s\d+:\d+)" # e.g. "9/16/22, 06:34"
    dash_whitespace = r"\s-\s" # " - "
    username = r"([\w\s])" # e.g. "Martin"
    metadata_end = r":\s" # ": "
    # 정규표현식 pattern 변수 완성
    pattern = data_time + dash_whitespace + username + metadata_end

    with open(chat_export_file, "r") as corpus_file:
        # txt file open
        content = corpus_file.read()

    # 데이터 전처리
    cleaned_corpus = re.sub(pattern, "", content)

    return tuple(cleaned_corpus.split("\n"))

if __name__ == "__main__":
    print(remove_chat_metadata("chat.txt"))




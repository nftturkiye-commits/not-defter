import pathlib

class FileManager:
    @staticmethod
    def read(file_path: str) -> str:
        """Dosyayı UTF-8 olarak okur, hata olursa fallback."""
        try:
            return pathlib.Path(file_path).read_text(encoding="utf-8")
        except UnicodeDecodeError:
            return pathlib.Path(file_path).read_text(encoding="latin-1")

    @staticmethod
    def write(file_path: str, content: str) -> None:
        """UTF-8 olarak yazar, klasör yoksa oluşturur."""
        p = pathlib.Path(file_path)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content, encoding="utf-8")

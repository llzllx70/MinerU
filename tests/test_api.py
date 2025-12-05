
import requests

def test_this():

    url = "http://172.16.2.49:8888/file_parse"

    data = {
        "return_middle_json": "false",
        "return_model_output": "false",
        "return_md": "true",
        "return_images": "false",
        "parse_method": "auto",
        "start_page_id": "0",
        "lang_list": "ch",
        "output_dir": "./output",
        "backend": "pipeline",
        "table_enable": "true",
        "formula_enable": "true"
    }

    files = {
        "files": ("【正文】中共浙江省委全面深化改革委员会关于印发《浙江省数字化改革总体方案》的通知.pdf", open("/home/double/vsproject/MinerU/demo/pdfs/【正文】中共浙江省委全面深化改革委员会关于印发《浙江省数字化改革总体方案》的通知.pdf", "rb"), "application/pdf")
    }

    resp = requests.post(url, data=data, files=files)
    print(resp.text)


test_this()

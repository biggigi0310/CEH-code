import pdfplumber

# 開啟 PDF 檔
with pdfplumber.open("2024CEH.pdf") as pdf:
    # 初始化一個空字串來存儲所有頁面的文字
    text = ""

    # 迭代每個頁面
    for page in pdf.pages:
        # 讀取每個頁面的文字並附加到text變量中
        text += page.extract_text()

# 將提取的文本內容寫入到output.txt檔案中
with open("output.txt", "w", encoding="utf-8") as f:
    f.write(text)

print("Text has been saved to output.txt")

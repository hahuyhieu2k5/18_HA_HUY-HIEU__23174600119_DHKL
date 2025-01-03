{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Gửi yêu cầu tới https://www.example.com\n",
      "Gửi yêu cầu tới https://www.google.com\n",
      "Gửi yêu cầu tới https://www.wikipedia.org\n",
      "Gửi yêu cầu tới https://www.python.org\n",
      "Gửi yêu cầu tới https://www.github.com\n",
      "Phản hồi từ https://www.google.com: 200\n",
      "Phản hồi từ https://www.wikipedia.org: 200\n",
      "Phản hồi từ https://www.example.com: 200\n",
      "Phản hồi từ https://www.github.com: 200\n",
      "Phản hồi từ https://www.python.org: 200\n",
      "Tất cả yêu cầu HTTP đã hoàn thành.\n"
     ]
    }
   ],
   "source": [
    "import threading\n",
    "import requests\n",
    "\n",
    "def gui_yeu_cau(url):\n",
    "    try:\n",
    "        print(f\"Gửi yêu cầu tới {url}\")\n",
    "        response = requests.get(url)\n",
    "        print(f\"Phản hồi từ {url}: {response.status_code}\")\n",
    "    except requests.RequestException as e:\n",
    "        print(f\"Lỗi với {url}: {e}\")\n",
    "\n",
    "def main():\n",
    "    cac_url = [\n",
    "        \"https://www.example.com\",\n",
    "        \"https://www.google.com\",\n",
    "        \"https://www.wikipedia.org\",\n",
    "        \"https://www.python.org\",\n",
    "        \"https://www.github.com\"\n",
    "    ]\n",
    "\n",
    "    cac_luong = []\n",
    "\n",
    "    for url in cac_url:\n",
    "        luong = threading.Thread(target=gui_yeu_cau, args=(url,))\n",
    "        cac_luong.append(luong)\n",
    "\n",
    "    for luong in cac_luong:\n",
    "        luong.start()\n",
    "\n",
    "    for luong in cac_luong:\n",
    "        luong.join()\n",
    "\n",
    "    print(\"Tất cả yêu cầu HTTP đã hoàn thành.\")\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
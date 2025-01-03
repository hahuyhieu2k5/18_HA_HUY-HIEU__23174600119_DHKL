{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Starting download: file1.zip\n",
      "Starting download: file2.zip\n",
      "Starting download: file3.zip\n",
      "Starting download: file4.zip\n",
      "Starting download: file5.zip\n",
      "Completed download: file1.zip\n",
      "Completed download: file2.zip\n",
      "Completed download: file3.zip\n",
      "Completed download: file4.zip\n",
      "Completed download: file5.zip\n",
      "All downloads completed!\n"
     ]
    }
   ],
   "source": [
    "import threading\n",
    "import time\n",
    "\n",
    "def download_file(file_name):\n",
    "    print(f\"Starting download: {file_name}\")\n",
    "    time.sleep(2)  \n",
    "    print(f\"Completed download: {file_name}\")\n",
    "\n",
    "def main():\n",
    "    files_to_download = [\"file1.zip\", \"file2.zip\", \"file3.zip\", \"file4.zip\", \"file5.zip\"]\n",
    "    threads = []\n",
    "\n",
    "    for file_name in files_to_download:\n",
    "        thread = threading.Thread(target=download_file, args=(file_name,))\n",
    "        threads.append(thread)\n",
    "\n",
    "    for thread in threads:\n",
    "        thread.start()\n",
    "\n",
    "    for thread in threads:\n",
    "        thread.join()\n",
    "\n",
    "    print(\"All downloads completed!\")\n",
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
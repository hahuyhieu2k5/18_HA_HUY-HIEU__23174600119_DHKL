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
      "Even numbers:\n",
      "30\n",
      "32\n",
      "34\n",
      "36\n",
      "38\n",
      "40\n",
      "42\n",
      "44\n",
      "46\n",
      "48\n",
      "50\n",
      "Odd numbers:\n",
      "31\n",
      "33\n",
      "35\n",
      "37\n",
      "39\n",
      "41\n",
      "43\n",
      "45\n",
      "47\n",
      "49\n",
      "Both threads have finished.\n"
     ]
    }
   ],
   "source": [
    "import threading\n",
    "\n",
    "def print_even_numbers(start, end):\n",
    "    print(\"Even numbers:\")\n",
    "    for num in range(start, end + 1):\n",
    "        if num % 2 == 0:\n",
    "            print(num)\n",
    "\n",
    "def print_odd_numbers(start, end):\n",
    "    print(\"Odd numbers:\")\n",
    "    for num in range(start, end + 1):\n",
    "        if num % 2 != 0:\n",
    "            print(num)\n",
    "\n",
    "# Hàm chính\n",
    "def main():\n",
    "    start = 30\n",
    "    end = 50\n",
    "\n",
    "    # Tạo các luồng\n",
    "    even_thread = threading.Thread(target=print_even_numbers, args=(start, end))\n",
    "    odd_thread = threading.Thread(target=print_odd_numbers, args=(start, end))\n",
    "\n",
    "    # Khởi chạy các luồng\n",
    "    even_thread.start()\n",
    "    odd_thread.start()\n",
    "\n",
    "    # Đợi các luồng hoàn tất\n",
    "    even_thread.join()\n",
    "    odd_thread.join()\n",
    "\n",
    "    print(\"Both threads have finished.\")\n",
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
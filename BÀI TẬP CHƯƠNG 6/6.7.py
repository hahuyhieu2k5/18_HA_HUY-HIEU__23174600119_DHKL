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
      "Starting Main Thread\n",
      "Starting Google\n",
      "Google: Web Fri Jan 03 16:08:03 2025\n",
      "Starting Yahoo\n",
      "Yahoo: Web Fri Jan 03 16:08:03 2025\n",
      "Starting Facebook\n",
      "Facebook: Web Fri Jan 03 16:08:03 2025\n",
      "Google: Web Fri Jan 03 16:08:04 2025\n",
      "Yahoo: Web Fri Jan 03 16:08:04 2025\n",
      "Facebook: Web Fri Jan 03 16:08:04 2025\n",
      "Google: Web Fri Jan 03 16:08:05 2025Yahoo: Web Fri Jan 03 16:08:05 2025\n",
      "\n",
      "Facebook: Web Fri Jan 03 16:08:05 2025\n",
      "Exiting GoogleExiting Yahoo\n",
      "Exiting Facebook\n",
      "\n",
      "Exiting Main Thread\n"
     ]
    }
   ],
   "source": [
    "import threading\n",
    "import time\n",
    "from datetime import datetime\n",
    "\n",
    "def task(name):\n",
    "    print(f\"Starting {name}\")\n",
    "    for _ in range(3):\n",
    "        print(f\"{name}: Web {datetime.now().strftime('%a %b %d %H:%M:%S %Y')}\")\n",
    "        time.sleep(1)\n",
    "    print(f\"Exiting {name}\")\n",
    "\n",
    "def main():\n",
    "    print(\"Starting Main Thread\")\n",
    "\n",
    "    threads = []\n",
    "    services = [\"Google\", \"Yahoo\", \"Facebook\"]\n",
    "\n",
    "    for service in services:\n",
    "        thread = threading.Thread(target=task, args=(service,))\n",
    "        threads.append(thread)\n",
    "        thread.start()\n",
    "\n",
    "    for thread in threads:\n",
    "        thread.join()\n",
    "\n",
    "    print(\"Exiting Main Thread\")\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()"
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
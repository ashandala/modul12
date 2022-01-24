{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9225762d",
   "metadata": {},
   "outputs": [],
   "source": [
    "ticket = int(input(\"Введите количество билетов:\",))\n",
    "price = []\n",
    "for i in range(1, ticket + 1):\n",
    "    age_ticket = int(input(f\"Введите возраст {i} участника:\"))\n",
    "    if age_ticket < 18:\n",
    "        price.append(0)\n",
    "    elif age_ticket > 25:\n",
    "        price.append(1390)\n",
    "    else:\n",
    "        price.append (990)\n",
    "if ticket < 3:\n",
    "    print(\"Сумма покупки:\", sum(price))\n",
    "else:\n",
    "    print(\"Сумма покупки со скидкой 10%:\", sum( price) - sum(price) / 10)\n",
    "\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

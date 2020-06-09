{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "def lnZ(theta, M):\n",
    "    alpha, M_c = theta\n",
    "    lin_M_c= 10**M_c\n",
    "    def f(M):\n",
    "        return (M**alpha)*exp(-M/lin_M_c)\n",
    "    ans, err = quad(f, 1000, np.inf)\n",
    "    return np.log(ans)"
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
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import math\n",
    "\n",
    "# Coordonnées des points de départ et de destination\n",
    "lat1 = input('latitude du 1er point : ')\n",
    "lon1 = input('Longitude du 1er point : ')\n",
    "lat2 = input('latitude du 2eme point : ')\n",
    "lon2 = input('longitude du 2eme point : ' )\n",
    "\n",
    "# Différence de longitude\n",
    "dLon = math.radians(lon2 - lon1)\n",
    "\n",
    "# Calcul de la déclinaison magnétique pour la position de départ\n",
    "d_dep = input('valeur de la déclinaison magnétique au point de départ : ')\n",
    
 
    "declination = math.radians(d_dep)\n",
    "\n",
    "# Calcul de l'angle d'orientation magnétique\n",
    "y = math.sin(dLon) * math.cos(math.radians(lat2))\n",
    "x = math.cos(math.radians(lat1)) * math.sin(math.radians(lat2)) - math.sin(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.cos(dLon)\n",
    "bearing = math.degrees(math.atan2(y, x)) + math.degrees(declination)\n",
    "\n",
    "# Si l'angle est supérieur à 360 degrés, soustrayez 360 degrés pour obtenir l'angle final\n",
    "if bearing > 360:\n",
    "    bearing -= 360\n",
    "\n",
    "print(\"L'angle d'orientation magnétique est : \", round(bearing, 2), \"degrés.\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "env39",
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
   "version": "3.9.16"
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

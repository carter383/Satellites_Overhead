import ephem
import datetime
import pygeodesy
from math import cos, radians, sin, sqrt
import math
import os
import subprocess
import yaml

class Sats_Overhead:
    def __init__(self):
        self.read_config()
        self.readfile()

    def read_config(self):
        filename = 'config.yaml'
        with open(filename, 'r') as file:
            config = yaml.safe_load(file)
        self.username = config['Credentials']['Username']
        self.password = config['Credentials']['Password']
        self.Within_Miles = config['Within_Miles']
        self.Ellipsiod = config['Ellipsiod']
        self.Base_Lat = config['Lat']
        self.Base_Long = config['Lon']

    def file_download(self):
        if self.username == "" or self.password == "":
            print('No Username Or Password found in the config for https://www.space-track.org')
            self.username = str(input('Please enter your username: '))
            self.password = str(input('Please enter your password: '))
            print(self.username)
        os.system(f"curl -c cookies.txt -b cookies.txt https://www.space-track.org/ajaxauth/login -d \'identity={self.username}&password={self.password}\'")
        os.system("curl --cookie cookies.txt --limit-rate 100K https://www.space-track.org/basicspacedata/query/class/gp/EPOCH/%3E%5Cnow%2D30/orderby/NORAD%5FCAT%5FID%2CEPOCH/format/3le > Sats_TLE.3le")
        print("Downloaded Files")

    def haversine(self, lat1, lon1, lat2, lon2):
        lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
        dlat = lat2 - lat1 
        dlon = lon2 - lon1 
        a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
        c = 2 * math.asin(math.sqrt(a)) 
        r = 3956 
        return c * r

    def is_within_distance(self, lat1, lon1):
        distance = self.haversine(lat1, lon1, self.Base_Lat, self.Base_Long)
        return distance <= self.Within_Miles

    def readfile(self):
        file_path = 'Sats_TLE.3le'
        if not os.path.exists(file_path):
            self.file_download()
        Sats = []  
        with open(file_path, 'r') as file:
            if len(file.readlines()) == 0:
                print('Invalid TLE file Check Credentials for https://www.space-track.org')
                os.system('rm Sats_TLE.3le')
                exit()
        with open(file_path, 'r') as file:               
            while True:
                lines = [file.readline().strip() for _ in range(3)]
                if not any(lines):
                    break
                Sats.append(lines)
        self.Sats = Sats

    def geodetic_to_geocentric(self, latitude, longitude, height):
        φ = radians(latitude)
        λ = radians(longitude)
        sin_φ = sin(φ)
        a, rf = self.Ellipsiod        
        e2 = 1 - (1 - 1 / rf) ** 2  
        n = a / sqrt(1 - e2 * sin_φ ** 2) 
        r = (n + height) * cos(φ)   
        x = r * cos(λ)
        y = r * sin(λ)
        z = (n * (1 - e2) + height) * sin_φ
        return x, y, z


    def Check_overhead(self):
        self.Overhead = []
        while True:
            for sat in self.Sats:
                try:    
                    tle_rec = ephem.readtle(sat[0], sat[1], sat[2]);
                    tle_rec.compute()
                    Lat, Lon, Height = self.geodetic_to_geocentric( tle_rec.sublong, tle_rec.sublat, tle_rec.elevation)
                except RuntimeError :
                    self.Sats.remove(sat)
                    print(f"Cannot Calculate Sat {sat[0]}")
                    continue
                try:
                    within_distance = self.is_within_distance(Lat, Lon)
                except:
                    continue
                if within_distance:
                    if sat[0] in self.Overhead:
                        continue
                    self.Overhead.append(sat[0])
                    print(f"{sat[0]}, is overhead")
                elif sat[0] in self.Overhead:
                    self.Overhead.remove(sat[0])


if __name__ == "__main__":
    Sats_Over = Sats_Overhead()
    Sats_Over.Check_overhead()


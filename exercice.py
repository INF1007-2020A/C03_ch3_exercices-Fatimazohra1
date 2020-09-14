#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math


def average(a: float, b: float, c: float) -> float:
    return (a+b+c)/3
    


def to_radians(angle_degs: float, angle_mins: float, angle_secs: float) -> float:
    angle_rads = (angle_degs*(π/180)+angle_mins*(π/180*60)+angle_secs*(π/180*3600))
    return angle_rads


def to_degrees(angle_rads: float) -> tuple:
     angle_degrees = angle_rads * (180/π) + angle_mins*(180*60/π)+angle_secs*(180*3600/π))
    return angle_degrees


def to_celsius(temperature: float) -> float:
    deg_celsius=(temperature*9/5) + 32
    return 0.0


def to_farenheit(temperature: float) -> float:
    deg_farenheit=(temperature − 32) * 5/9
    return 0.0


def main() -> None:
    print(f"Moyenne des nombres 2, 4, 6: {average(2.1, 4.3, 6.5)}")

    print(f"Conversion de 100 degres, 2 minutes et 45 secondes en radians: {to_radians(180, 2, 45)}")
    
    degrees, minutes, seconds = to_degrees(1.0)
    print(f"Conversion de 1 radian en degres: {degrees} degres, {minutes} minutes et {seconds} secondes")

    print(f"Conversion de 100 Celsius en Farenheit: {to_farenheit(100.0)}")
    print(f"Conversion de 451 Farenheit en Celsius: {to_celsius(451.0)}")


if __name__ == '__main__':
    main()

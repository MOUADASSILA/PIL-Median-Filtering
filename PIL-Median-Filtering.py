#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  6 10:51:16 2024

@author: mac
"""

from PIL import Image, ImageFilter

image_path = "/Users/mac/Downloads/original.png"
original_image = Image.open(image_path)

median_filtered_image = original_image.filter(ImageFilter.MedianFilter(size=5))

median_filtered_image_path = "pil_median_filtered_image.png"
median_filtered_image.save(median_filtered_image_path)


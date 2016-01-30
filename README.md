# imagep
This class help you to calculate all posibility of permutation of repetitive colors in pixels of an image and generate all posibility images.

Imagine we generate all posibility of 16 pixels permutation as images, so we have all 16 pixels images that possible. In RGB system we have 255 red,255 green and 255 blue values. 255^3 = 16,581,375 colors. so for all 2*2 pixels images we have 16,581,375^4 posibility (7.559310165E28).

Yup, It's very huge. But think if we create a server for using this processes in could processing and show results to people in their mobile as an app, we can rating images in rarity. so we have some chance to find images that we coludn't even imagine.

## Permutation
In mathematics, the notion of permutation relates to the act of arranging all the members of a set into some sequence or order, or if the set is already ordered, rearranging (reordering) its elements, a process called permuting. [Read more in Wikipedia](https://en.wikipedia.org/wiki/Permutation)


## Using
Just pull or download repository, install `pillow` from `pip`, cd to directory and start with command:
```python
python imagep.py
```

It will ask about count of pixel rows and columns and generate all images in tmp directory next to the file. As default it will generate images with black and white color,for using all colors you can initiate `Imagep` class with True as last parameter:
```python
Imagep(x, y, True)
```


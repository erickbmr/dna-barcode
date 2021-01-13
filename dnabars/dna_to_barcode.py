from PIL import Image

#func for create each bar
def plotBar(image, width, color, heigth=100):
    return image.new("RGB", (width, heigth), color)

#main function
def dna_to_barcode(path):
    with open(path) as file:
        dna_sequence = file.read()

    #separating each nitrogenous bases
    dna = [char for char in dna_sequence]

    #setting the colors of each base
    adenine_color = "rgb(0,248,0)"  #green
    thymine_color = "rgb(255,0,0)"  #red
    guanine_color = "rgb(0,0,0)"    #black
    cytosine_color = "rgb(0,0,248)" #blue

    #create the full image
    barcode = Image.new("RGB", ((len(dna) * 2), 50))

    #variable for save the next drawable point in canvas
    pixels_counter = 0

    for b in dna:
        if pixels_counter < (len(dna) * 2):
            if b == 'a':
                bar = plotBar(Image, pixels_counter, adenine_color)
            elif b == 't':
                bar = plotBar(Image, pixels_counter, thymine_color)
            elif b == 'c':
                bar = plotBar(Image, pixels_counter, cytosine_color)
            elif b == 'g':
                bar = plotBar(Image, pixels_counter, guanine_color)
            
            barcode.paste(bar, (pixels_counter, 0))

            pixels_counter += 2

    barcode.show()
    barcode.save('../output/barcode.png', 'PNG')


path = '../docs/dna_sequence.txt'
dna_to_barcode(path)

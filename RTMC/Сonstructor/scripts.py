from psd_tools import PSDImage


psd_file = './documents/сертификат.psd'
layer_name = 'ФИО'
new_text = 'aboba'

image = PSDImage.open(psd_file)

for layer in image._layers:
    if layer.name == layer_name:
        

image.save('./documents/mod_сертификат.pdf')
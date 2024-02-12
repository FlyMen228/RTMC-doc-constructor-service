from psd_tools import PSDImage

file = PSDImage.open('documents/сертификат.psd')

layer_name = 'ФИО'

for layer in file:
    
    if layer.name == layer_name and layer.kind == 'type':
        
        engine_data = layer._engine_data

        editor = engine_data.get_editor()

        editor.set_text('aboba')

        layer.engine_data = editor.build()
        
        break
    
file.save('documents/modif_сертификат.psd')

file.close()

file = PSDImage.open('documents/сертификат.psd')

for layer in file:

    print(layer)
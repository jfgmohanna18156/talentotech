import json
import os

def update_json_images(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    for producto in data['productos']:
        _, ext = os.path.splitext(producto['imagen'])
        producto['imagen'] = f"./imgProductos/{producto['id_unico']}.jfif"
    
    with open(json_file, 'w') as f:
        json.dump(data, f, indent=2)

# Example usage
json_file = 'productos.json'
update_json_images(json_file)
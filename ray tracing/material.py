from color import Color


class Material:
    """Material has color and properties which tells us how it reacts to light"""

    def __init__(
        self, color=Color.from_hex("#FFFFFF"), 
        ambient=0.05, 
        diffuse=1.0, 
        specular=1.0, 
        reflection=0.5
    ):
        self.color = color
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.reflection = reflection

    def color_at(self, position):
        return self.color

class ChequeredMaterial:
    """" Create a chequboard pattern with two colors."""
    # The color of the material is determined by the position of the object.
    def __init__(self, 
                 color1=Color.from_hex("#FFFFFF"), 
                 color2=Color.from_hex("#000000"), 
                 ambient=0.05, 
                 diffuse=1.0, 
                 specular=1.0, 
                 reflection=0.5):
        
        self.color1 = color1
        self.color2 = color2
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.reflection = reflection

    def color_at(self, position):
        # Alternate between two colors based on the position.
        if int((position.x + 0.5) * 3.0) % 2 == int(position.z * 3.0) % 2:
            return self.color1
        else:
            return self.color2
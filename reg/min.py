import re
class minVoc:
    def __init__(self) -> None:
        pass


    @staticmethod
    def buscar(texto:str)-> list:
        # Patron de busqueda para vocales
        patron = "\\b[aeiuo][^\\s.,]*"
        result = re.findall(patron, texto)
        return result


if __name__ == "__main__":
    texto = """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin accumsan laoreet lacus non semper. Suspendisse potenti. Sed eget erat eu eros malesuada 
        venenatis in a elit. Donec malesuada convallis vehicula. Quisque iaculis neque lacus, nec dictum neque placerat ut. Aliquam consectetur metus erat, sit amet mollis 
        leo imperdiet at. Nam neque dui, vestibulum sit amet pulvinar vel, dignissim a quam. Aliquam varius maximus malesuada. Ut eros turpis, efficitur quis finibus ut, 
        auctor sagittis tortor. Etiam dui est, iaculis sed ullamcorper varius, vehicula venenatis quam. Proin tincidunt velit et magna facilisis, porttitor viverra nisi 
        viverra. Maecenas commodo magna quam. Proin porttitor sem ut nibh consectetur efficitur. Donec ut lacus id ex congue ornare vitae at ex. Vestibulum dictum nisi nunc.
        Sed convallis velit enim. Praesent quis quam nisl. Nullam sit amet congue tellus. Suspendisse sodales nisi at nunc semper varius. Morbi faucibus bibendum consectetur.
        Phasellus auctor odio vel tempor imperdiet. Suspendisse pretium leo magna. In tempus massa sit amet fringilla bibendum. Vivamus dictum sed nulla ac tempor. 
        Nam efficitur commodo ligula congue rhoncus. Vestibulum vulputate dui tortor, quis dignissim dui ornare ut. Maecenas ornare sapien in dui pellentesque, a 
        lacinia lacus ultricies. Curabitur vehicula leo at ultricies aliquam. Integer erat eros, consequat sed convallis ac, maximus ut arcu. Nulla turpis sem, 
        iaculis id sodales eu, efficitur sed lorem. Pellentesque tincidunt tincidunt odio vel rhoncus. In faucibus augue odio, ac bibendum purus mattis ac. Nunc 
        vestibulum magna in porttitor rutrum. Praesent malesuada ut metus et feugiat. Nulla eu ipsum justo.
        """
    print(minVoc.buscar(texto))

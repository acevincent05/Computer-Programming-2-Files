class Blender:
    def blend(self, fruit1: str = None, fruit2: str = None, n: int = 1):
        if fruit1 == None and fruit2 == None:
            print("There's nothing to blend here, boss.")
        else:
            blend = f'Blending {fruit1} and {fruit2}, boss.'
            if n > 1:
                for i in range(1, 1+n):
                    print(blend)
            else:
                print(blend)
class Ray:
    def __init__(self,origin, direction):
        self.origin = origin
        self.direction = direction.normalize()
    def position(self, time: float):
        return self.origin + self.direction * time
    def __str__(self):
            return f"Ray: Origin: {self.origin}, Direction: {self.direction}"

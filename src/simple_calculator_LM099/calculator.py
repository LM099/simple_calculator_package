class Calculator:
    """Una semplice classe calcolatrice con operazioni di base."""
    
    def add(self, x: float, y: float) -> float:
        """Somma due numeri."""
        return x + y
    
    def subtract(self, x: float, y: float) -> float:
        """Sottrae due numeri."""
        return x - y
    
    def multiply(self, x: float, y: float) -> float:
        """Moltiplica due numeri."""
        return x * y
    
    def divide(self, x: float, y: float) -> float:
        """Divide due numeri."""
        if y == 0:
            raise ValueError("Non è possibile dividere per zero!")
        return x / y
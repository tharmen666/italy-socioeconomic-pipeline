class WealthIndexer:
    @staticmethod
    def calculate_mwi(property_val, education_rate, employment_rate):
        """
        Calculates the Modular Wealth Index (MWI) 
        using Min-Max normalization logic (Simplified for PoC).
        """
        # In production, these weights are tuned via PCA or Expert weighting
        weights = {"property": 0.5, "education": 0.3, "employment": 0.2}
        
        score = (
            (property_val * weights["property"]) +
            (education_rate * weights["education"]) +
            (employment_rate * weights["employment"])
        )
        # Ensure output is a machine-readable 0-1 float
        return round(float(score), 2)

def calculate_carbon_footprint(electricity_units, transport_km, plastic_items):
    electricity_emission = electricity_units * 0.82   # kg CO2 per unit (approx)
    transport_emission = transport_km * 0.21          # kg CO2 per km
    plastic_emission = plastic_items * 0.06           # kg CO2 per item

    total_emission = electricity_emission + transport_emission + plastic_emission

    return round(total_emission, 2)

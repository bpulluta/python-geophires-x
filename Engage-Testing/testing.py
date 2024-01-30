all_results = {
    'POWER GENERATION PROFILE': [
        [
            'YEAR',
            'THERMAL DRAWDOWN',
            'GEOFLUID TEMPERATURE (deg C)',
            'PUMP POWER (MW)',
            'NET POWER (MW)',
            'NET HEAT (MW)',
            'FIRST LAW EFFICIENCY (%)',
        ],
        [0, 1.0, 227.0, 0.1791, 20.9816, 11.9018, 16.7075],
    ]
}

# Using a similar format to your original code
profile_data = all_results.get('POWER GENERATION PROFILE', [])
header = profile_data[0] if len(profile_data) > 0 else []
data = profile_data[1] if len(profile_data) > 1 else []

# Find the index for 'FIRST LAW EFFICIENCY (%)' in the header
efficiency_index = header.index('FIRST LAW EFFICIENCY (%)') if 'FIRST LAW EFFICIENCY (%)' in header else None

# Get the efficiency value using the index
first_law_eff = data[efficiency_index] if efficiency_index is not None else None

print(first_law_eff)

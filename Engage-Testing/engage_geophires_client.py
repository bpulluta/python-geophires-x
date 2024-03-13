import pandas as pd

from geophires_x_client import GeophiresXClient
from geophires_x_client.geophires_input_parameters import GeophiresInputParameters


class geophires_parametrization_analysis:
    def __init__(self, plant, prod_temp_min, prod_temp_max):
        self.client = GeophiresXClient()
        self.df_results = []
        self.parameter_list = []
        self.plant = plant
        self.prod_min = prod_temp_min
        self.prod_max = prod_temp_max  # Corrected this line to properly set prod_max
        self.results_cache = {}  # Cache for storing results

    def get_value(self, results, keys):
        for key in keys:
            results = results.get(key, {})
            if not isinstance(results, dict):
                return None
        return results.get('value', None)

    def calculate_ratios(self, data_row):
        # Make sure the required data is present
        required_keys = [
            'Average Reservoir Heat Extraction (MWth)',
            'Average Heat Production (MWth)',
            'Average Electricity Production (MWe)',
        ]

        if not all(key in data_row for key in required_keys):
            print('Required data is missing to calculate ratios.')
            return None

        # Calculate ratios
        heat_extraction = data_row['Average Reservoir Heat Extraction (MWth)']
        heat_production = data_row['Average Heat Production (MWth)']
        electricity_production = data_row['Average Electricity Production (MWe)']

        ratios = {
            'Ratio Avg Reservoir Heat Extraction to Ratio Avg Reservoir Heat Extraction': heat_extraction
            / heat_extraction
            if heat_extraction
            else 0.0,
            'Ratio Avg Heat Production to Avg Reservoir Heat Extraction': heat_production / heat_extraction
            if heat_extraction
            else 0.0,
            'Ratio Avg Electricity Production to Avg Reservoir Heat Extraction': electricity_production
            / heat_extraction
            if heat_extraction
            else 0.0,
        }

        return ratios

    def process_multiple(self, input_params):
        # Initialize data_row at the beginning of the method
        data_row = {}

        param_key = str(input_params)
        if param_key in self.results_cache:
            return self.results_cache[param_key]

        result = self.client.get_geophires_result(GeophiresInputParameters(input_params))
        all_results = result.result

        # Define paths for the values we're interested in
        paths = {
            'Depth (km)': ['ENGINEERING PARAMETERS', 'Well depth (or total length, if not vertical)'],
            'Number of Prod Wells': ['ENGINEERING PARAMETERS', 'Number of Production Wells'],
            'Number of Inj Wells': ['ENGINEERING PARAMETERS', 'Number of Injection Wells'],
            'Flow Rate per Prod Well (kg/sec)': ['ENGINEERING PARAMETERS', 'Flowrate per production well'],
            'Maximum Reservoir Temperature (deg.C)': ['RESOURCE CHARACTERISTICS', 'Maximum reservoir temperature'],
            'Surface Plant Cost ($M)': ['CAPITAL COSTS (M$)', 'Total surface equipment costs'],
            'Exploration Cost ($M)': ['CAPITAL COSTS (M$)', 'Exploration costs'],
            'Drilling and completion cost ($MUSD)': ['CAPITAL COSTS (M$)', 'Drilling and completion costs'],
            'Wellfield maintenance costs ($MUSD/yr)': [
                'OPERATING AND MAINTENANCE COSTS (M$/yr)',
                'Wellfield maintenance costs',
            ],
            'Make-Up Water O&M Cost ($MUSD/year)': ['OPERATING AND MAINTENANCE COSTS (M$/yr)', 'Water costs'],
            'Average Reservoir Heat Extraction (MWth)': [
                'RESERVOIR SIMULATION RESULTS',
                'Average Reservoir Heat Extraction',
            ],
            'Average Heat Production (MWth)': ['SURFACE EQUIPMENT SIMULATION RESULTS', 'Average Net Heat Production'],
            'Average Cool Production (MW)': ['SURFACE EQUIPMENT SIMULATION RESULTS', 'Average Cooling Production'],
            'Average Electricity Production (MWe)': [
                'SURFACE EQUIPMENT SIMULATION RESULTS',
                'Average Net Electricity Generation',
            ],
            'Lifetime': ['ECONOMIC PARAMETERS', 'Project lifetime'],
            'Total capital costs ($MUSD/yr)': ['CAPITAL COSTS (M$)', 'Total capital costs'],
            'Surface maintenance costs ($MUSD/yr)': [
                'OPERATING AND MAINTENANCE COSTS (M$/yr)',
                'Power plant maintenance costs',
            ],
            'Average Production Temperature (degC)': ['RESERVOIR SIMULATION RESULTS', 'Average Production Temperature'],
            'Maximum Total Electricity Generation (MWe)': [
                'SURFACE EQUIPMENT SIMULATION RESULTS',
                'Maximum Total Electricity Generation',
            ],
            'Maximum Cooling Production (MW)': ['SURFACE EQUIPMENT SIMULATION RESULTS', 'Maximum Cooling Production'],
            'Maximum Net Heat Production (MWth)': [
                'SURFACE EQUIPMENT SIMULATION RESULTS',
                'Maximum Net Heat Production',
            ],
        }

        # Extract values using the defined paths and update data_row
        for label, path in paths.items():
            value = self.get_value(all_results, path)

            if value is not None:
                data_row[label] = value

        data_row = {k: v for k, v in data_row.items() if v is not None}
        self.results_cache[param_key] = data_row

        ratios = self.calculate_ratios(data_row)
        if ratios:
            data_row.update(ratios)

        return data_row

    def run_iterations(self):
        for params in self.parameter_list:
            data_row = self.process_multiple(params)
            # Check if Average Production Temperature is within the specified range
            avg_prod_temp = data_row.get('Average Production Temperature (degC)', None)
            if avg_prod_temp is not None and self.prod_min <= avg_prod_temp <= self.prod_max:
                self.df_results.append(data_row)
            elif avg_prod_temp is not None and avg_prod_temp > self.prod_max:
                break  # Stop processing once the maximum temperature is reached

    def prepare_parameters(self, new_params_list):
        self.parameter_list = new_params_list

    def get_final_dataframe(self):
        return pd.DataFrame(self.df_results)

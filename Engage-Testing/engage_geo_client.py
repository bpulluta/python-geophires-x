import pandas as pd

from geophires_x_client import GeophiresXClient
from geophires_x_client.geophires_input_parameters import GeophiresInputParameters


class EngageAnalysis:
    def __init__(self, plant):
        self.client = GeophiresXClient()
        self.df_results = []
        self.parameter_list = []
        self.plant = plant
        self.results_cache = {}  # Cache for storing results

    # def process_multiple(self, input_params):
    #     # Generate a unique key for the input parameters (e.g., a string representation)
    #     param_key = str(input_params)

    #     # Check if results for these parameters are already in the cache
    #     if param_key in self.results_cache:
    #         return self.results_cache[param_key]

    #     # def process_multiple(self, input_params):
    #     result = self.client.get_geophires_result(GeophiresInputParameters(input_params))
    #     all_results = result.result

    #     # Extracting specific values from all_results
    #     depth_m = (
    #         all_results.get('ENGINEERING PARAMETERS', {})
    #         .get('Well depth (or total length, if not vertical)', {})
    #         .get('value', None)
    #     )
    #     number_of_prod_wells = (
    #         all_results.get('ENGINEERING PARAMETERS', {}).get('Number of Production Wells', {}).get('value', None)
    #     )
    #     number_of_inj_wells = (
    #         all_results.get('ENGINEERING PARAMETERS', {}).get('Number of Injection Wells', {}).get('value', None)
    #     )
    #     max_reservoir_temp = (
    #         all_results.get('RESOURCE CHARACTERISTICS', {}).get('Maximum reservoir temperature', {}).get('value', None)
    #     )

    #     # CAPITAL COSTS
    #     wellfield_cost = (
    #         all_results.get('CAPITAL COSTS (M$)', {}).get('Drilling and completion costs', {}).get('value', None)
    #     )
    #     surface_plant_cost = (
    #         all_results.get('CAPITAL COSTS (M$)', {}).get('Surface power plant costs', {}).get('value', None)
    #     )
    #     exploration_cost = all_results.get('CAPITAL COSTS (M$)', {}).get('Exploration costs', {}).get('value', None)
    #     gathering_cost = (
    #         all_results.get('CAPITAL COSTS (M$)', {}).get('Field gathering system costs', {}).get('value', None)
    #     )

    #     # OPERATING AND MAINTENANCE COSTS
    #     wellfield_OM_cost = (
    #         all_results.get('OPERATING AND MAINTENANCE COSTS (M$/yr)', {})
    #         .get('Wellfield maintenance costs', {})
    #         .get('value', None)
    #     )
    #     surface_plant_OM_cost = (
    #         all_results.get('OPERATING AND MAINTENANCE COSTS (M$/yr)', {})
    #         .get('Power plant maintenance costs', {})
    #         .get('value', None)
    #     )
    #     water_OM_cost = (
    #         all_results.get('OPERATING AND MAINTENANCE COSTS (M$/yr)', {}).get('Water costs', {}).get('value', None)
    #     )

    #     # RESERVOIR SIMULATION RESULTS
    #     avg_reservoir_extraction = (
    #         all_results.get('RESERVOIR SIMULATION RESULTS', {})
    #         .get('Average Reservoir Heat Extraction', {})
    #         .get('value', None)
    #     )

    #     # SURFACE EQUIPMENT SIMULATION RESULTS
    #     avg_total_heat_gen = (
    #         all_results.get('SURFACE EQUIPMENT SIMULATION RESULTS', {})
    #         .get('Average Net Heat Production', {})
    #         .get('value', None)
    #     )

    #     avg_total_electricity_gen = (
    #         all_results.get('SURFACE EQUIPMENT SIMULATION RESULTS', {})
    #         .get('Average Net Electricity Generation', {})
    #         .get('value', None)
    #     )

    #     # ECONOMIC PARAMETERS RESULTS
    #     lifetime = all_results.get('ECONOMIC PARAMETERS', {}).get('Project lifetime', {}).get('value', None)

    #     # Constructing the dictionary for DataFrame row
    #     data_row = {
    #         'Depth (m)': depth_m,
    #         'Number of Prod Wells': number_of_prod_wells,
    #         'Number of Inj Wells': number_of_inj_wells,
    #         'Maximum Reservoir Temperature (deg.C)': max_reservoir_temp,
    #         'Wellfield Cost ($M)': wellfield_cost,
    #         'Surface Plant Cost ($M)': surface_plant_cost,
    #         'Exploration Cost ($M)': exploration_cost,
    #         'Field Gathering System Cost ($M)': gathering_cost,
    #         'Wellfield O&M Cost ($M/year)': wellfield_OM_cost,
    #         'Surface Plant O&M Cost ($M/year)': surface_plant_OM_cost,
    #         'Make-Up Water O&M Cost ($M/year)': water_OM_cost,
    #         'Average Reservoir Heat Extraction (MWth)': avg_reservoir_extraction,
    #         'Average Heat Generation (MWth)': avg_total_heat_gen,
    #         'Average Electricity Generation (MWe)': avg_total_electricity_gen,
    #         'Lifetime': lifetime,
    #     }

    #     # Save the processed data in the cache
    #     self.results_cache[param_key] = data_row

    #     return data_row

    def process_multiple(self, input_params):
        # Generate a unique key for the input parameters (e.g., a string representation)
        param_key = str(input_params)

        # Check if results for these parameters are already in the cache
        if param_key in self.results_cache:
            return self.results_cache[param_key]

        # def process_multiple(self, input_params):
        result = self.client.get_geophires_result(GeophiresInputParameters(input_params))
        all_results = result.result

        # Extracting specific values from all_results
        depth_m = (
            all_results.get('ENGINEERING PARAMETERS', {})
            .get('Well depth (or total length, if not vertical)', {})
            .get('value', None)
        )
        number_of_prod_wells = (
            all_results.get('ENGINEERING PARAMETERS', {}).get('Number of Production Wells', {}).get('value', None)
        )
        number_of_inj_wells = (
            all_results.get('ENGINEERING PARAMETERS', {}).get('Number of Injection Wells', {}).get('value', None)
        )
        max_reservoir_temp = (
            all_results.get('RESOURCE CHARACTERISTICS', {}).get('Maximum reservoir temperature', {}).get('value', None)
        )

        # CAPITAL COSTS
        surface_plant_cost = (
            all_results.get('CAPITAL COSTS (M$)', {}).get('Total surface equipment costs', {}).get('value', None)
        )

        exploration_cost = all_results.get('CAPITAL COSTS (M$)', {}).get('Exploration costs', {}).get('value', None)
        drill_completion_cost = (
            all_results.get('CAPITAL COSTS (M$)', {}).get('Drilling and completion costs', {}).get('value', None)
        )

        # OPERATING AND MAINTENANCE COSTS
        surface_plant_OM_cost = (
            all_results.get('OPERATING AND MAINTENANCE COSTS (M$/yr)', {})
            .get('Power plant maintenance costs', {})
            .get('value', None)
        )

        water_OM_cost = (
            all_results.get('OPERATING AND MAINTENANCE COSTS (M$/yr)', {}).get('Water costs', {}).get('value', None)
        )
        wellfield_OM_cost = (
            all_results.get('OPERATING AND MAINTENANCE COSTS (M$/yr)', {})
            .get('Wellfield maintenance costs', {})
            .get('value', None)
        )

        # SURFACE EQUIPMENT SIMULATION RESULTS
        avg_total_heat_gen = (
            all_results.get('SUMMARY OF RESULTS', {}).get('Average Direct-Use Heat Production', {}).get('value', None)
        )

        avg_total_electricity_gen = (
            all_results.get('SUMMARY OF RESULTS', {}).get('Average Net Electricity Production', {}).get('value', None)
        )

        # RESERVOIR SIMULATION RESULTS
        avg_reservoir_extraction = (
            all_results.get('RESERVOIR SIMULATION RESULTS', {})
            .get('Average Reservoir Heat Extraction', {})
            .get('value', None)
        )

        # ECONOMIC PARAMETERS RESULTS
        lifetime = all_results.get('ECONOMIC PARAMETERS', {}).get('Project lifetime', {}).get('value', None)

        # Constructing the dictionary for DataFrame row
        data_row = {
            'Depth (m)': depth_m,
            'Number of Prod Wells': number_of_prod_wells,
            'Number of Inj Wells': number_of_inj_wells,
            'Maximum Reservoir Temperature (deg.C)': max_reservoir_temp,
            'Surface Plant Cost ($M)': surface_plant_cost,
            'Surface maintenance costs ($MUSD/yr)': surface_plant_OM_cost,
            'Exploration Cost ($M)': exploration_cost,
            'Drilling and completion cost ($MUSD)': drill_completion_cost,
            'Wellfield maintenance costs ($MUSD/yr)': wellfield_OM_cost,
            'Make-Up Water O&M Cost ($MUSD/year)': water_OM_cost,
            'Average Reservoir Heat Extraction (MWth)': avg_reservoir_extraction,
            'Average Heat Production (MWth)': avg_total_heat_gen,
            'Average Electricity Production (MWe)': avg_total_electricity_gen,
            'Lifetime': lifetime,
        }

        # Save the processed data in the cache
        self.results_cache[param_key] = data_row

        return data_row

    def run_iterations(self):
        for params in self.parameter_list:
            data_row = self.process_multiple(params)
            self.df_results.append(data_row)

    def prepare_parameters(self, new_params_list):
        self.parameter_list = new_params_list

    def get_final_dataframe(self):
        return pd.DataFrame(
            self.df_results,
            columns=[
                'Depth (m)',
                'Number of Prod Wells',
                'Number of Inj Wells',
                'Maximum Reservoir Temperature (deg.C)',
                'Surface Plant Cost ($M)',
                'Surface maintenance costs ($MUSD/yr)',
                'Exploration Cost ($M)',
                'Drilling and completion cost ($MUSD)',
                'Wellfield maintenance costs ($MUSD/yr)',
                'Make-Up Water O&M Cost ($MUSD/year)',
                'Average Reservoir Heat Extraction (MWth)',
                'Average Heat Production (MWth)',
                'Average Electricity Production (MWe)',
                'Lifetime',
            ],
        )

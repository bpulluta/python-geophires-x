function calculate_cost(geotherm_cost_prod_cost_curve_welldiam, geotherm_cost_prod_cost_curve_welltype, resource_depth)
    if geotherm_cost_prod_cost_curve_welldiam == 0 #Small Diameter
        if geotherm_cost_prod_cost_curve_welltype == 0 #vertical
            return [ 
                0.281801107 * resource_depth^2 + 1275.521301 * resource_depth + 632315.1264,#baseline ?
                0.189267288 * resource_depth^2 + 293.4517365 * resource_depth + 1326526.313, #intermediate1 ?
                0.003145418 * resource_depth^2 + 782.70 * resource_depth + 983620.25, #intermediate2 ?
                -0.002397497 * resource_depth^2 + 752.94 * resource_depth + 524337.65#Ideal ?
            ]
        else
            return [ #horizontal
                0.2528 * resource_depth^2 + 1716.72 * resource_depth + 500866.89, #baseline
                0.19950 * resource_depth^2 + 296.13 * resource_depth + 1697867.71, #intermediate1
                0.0038019 * resource_depth^2 + 838.90 * resource_depth + 1181947.04, #intermediate2
                0.0037570 * resource_depth^2 + 762.53 * resource_depth + 765103.08 #Ideal
            ]
        end
    else
        if geotherm_cost_prod_cost_curve_welltype == 1 #Large Diameter
            if geotherm_cost_prod_cost_curve_welltype == 0 #vertical
                return [ 
                    0.30212 * resource_depth^2 + 584.91 * resource_depth + 751368.47, #baseline
                    0.13710 * resource_depth^2 + 129.61 * resource_depth + 1205587.57, #intermediate1
                    0.0080395 * resource_depth^2 + 455.61 * resource_depth + 921007.69, #intermediate2
                    0.0025212 * resource_depth^2 + 439.45 * resource_depth + 590611.90 #Ideal
                ]
            else
                return [ #horizontal
                    0.28977 * resource_depth^2 + 882.15 * resource_depth + 680562.50, #baseline
                    0.15340 * resource_depth^2 + 120.32 * resource_depth + 1431801.54, #intermediate1
                    0.0085389 * resource_depth^2 + 506.08 * resource_depth + 1057330.39, #intermediate2
                    0.0071869 * resource_depth^2 + 455.85 * resource_depth + 753377.73 #Ideal
                ]
            end
        end
    end
end

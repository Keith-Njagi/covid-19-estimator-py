import pprint

def estimator(data):
    input_data = data

    time_factor = int(input_data['timeToElapse']/3)
    
    impactCurrentlyInfected = input_data['reportedCases'] * 10
    impactInfectionsByRequestedTime = impactCurrentlyInfected * (2 ** time_factor)
    impactSevereCasesByRequestedTime = int(impactInfectionsByRequestedTime * 0.15)
    impactHospitalBedsByRequestedTime = int(input_data['totalHospitalBeds'] * 0.35) - impactSevereCasesByRequestedTime
    impactCasesForICUByRequestedTime = int(impactInfectionsByRequestedTime * 0.05)
    impactCasesForVentilatorsByRequestedTime = int(impactInfectionsByRequestedTime * 0.02)
    impactDollarsInFlight = round((impactInfectionsByRequestedTime * input_data['region']['avgDailyIncomePopulation']) * input_data['region']['avgDailyIncomeInUSD'] * sample_data['timeToElapse'], 2)

    severeImpactCurrentlyInfected = input_data['reportedCases'] * 50
    severeImpactInfectionsByRequestedTime = severeImpactCurrentlyInfected * (2 ** time_factor)
    severeImpactSevereCasesByRequestedTime = int(severeImpactInfectionsByRequestedTime * 0.15)
    severeImpactHospitalBedsByRequestedTime = int(input_data['totalHospitalBeds'] * 0.35) - severeImpactSevereCasesByRequestedTime
    severeImpactCasesForICUByRequestedTime = int(severeImpactInfectionsByRequestedTime * 0.05)
    severeImpactCasesForVentilatorsByRequestedTime = int(severeImpactInfectionsByRequestedTime * 0.02)
    severeImpactDollarsInFlight = round((severeImpactInfectionsByRequestedTime * input_data['region']['avgDailyIncomePopulation']) * input_data['region']['avgDailyIncomeInUSD'] * sample_data['timeToElapse'], 2)

    output = {'data': input_data,
            'impact': {
                'currentlyInfected': impactCurrentlyInfected,
                'infectionsByRequestedTime': impactInfectionsByRequestedTime,
                'severeCasesByRequestedTime': impactSevereCasesByRequestedTime,
                'hospitalBedsByRequestedTime': impactHospitalBedsByRequestedTime,
                'casesForICUByRequestedTime': impactCasesForICUByRequestedTime,
                'casesForVentilatorsByRequestedTime': impactCasesForVentilatorsByRequestedTime,
                'dollarsInFlight': impactDollarsInFlight,   
            },
            'severeImpacct': {
                'currentlyInfected': severeImpactCurrentlyInfected,
                'infectionsByRequestedTime': severeImpactInfectionsByRequestedTime,
                'severeCasesByRequestedTime': severeImpactSevereCasesByRequestedTime,
                'hospitalBedsByRequestedTime': severeImpactHospitalBedsByRequestedTime,
                'casesForICUByRequestedTime': severeImpactCasesForICUByRequestedTime,
                'casesForVentilatorsByRequestedTime': severeImpactCasesForVentilatorsByRequestedTime,
                'dollarsInFlight': severeImpactDollarsInFlight,
            }
        }
    my_printer = pprint.PrettyPrinter(depth=3)
    my_printer.pprint(output)
    return output
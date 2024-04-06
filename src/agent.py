import numpy as np
# notes Well-Riley model/need to add accomodation for airflow and consumption 
def simulate(I, q, p,t, V, p_vaccine):
    ventilation_rate = 3 
    social_distancing_effectiveness = 0.8 
    effective_volume = V * ventilation_rate
    P_unadjusted = 1 - np.exp(-I * q * p * t / effective_volume)
    P_adjusted = P_unadjusted * (1 - social_distancing_effectiveness) * (1 -p_vaccine)
    print(f"Unadjusted Probability of infection: {P_unadjusted*100:.2f}%")
    print(f"Adjusted Probability of infection with social distancing: {P_adjusted*100:.2f}%")

def main():
    I = 1  
    q = 10 
    p = 0.32  
    t = 8  
    V = 60  
    simulate(I,q,p,t,V,0.2)

if __name__ == '__main__':
    main()
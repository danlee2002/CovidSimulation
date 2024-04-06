import numpy as np
# notes Well-Riley model/need to add accomodation for airflow and consumption 
def simulate(I, q, p,t, V, p_mask):
    ventilation_rate = 3 
    social_distancing_effectiveness = 0.1
    effective_volume = V * ventilation_rate
    P_unadjusted = 1 - np.exp(-I * (q * 0.28 *(1- p_mask)) * p * t / effective_volume)
    print(f"Unadjusted Probability of infection: {P_unadjusted*100:.2f}%")

def main():
    I = 1  
    q = 100 
    p = 0.32  
    V = 45 
    simulate(I,q,p,7.52,V,0.94)
    simulate(I,q,p,4.93,V,0.09)

if __name__ == '__main__':
    main()
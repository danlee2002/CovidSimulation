import numpy as np
import matplotlib.pyplot as plt 
# notes Well-Riley model/need to add accomodation for airflow and consumption 
def simulate(I, q, p,t, V, p_mask):

    social_distancing_effectiveness = 0.1
    p_mask = np.random.choice([0, p_mask], p = [1 - p_mask, p_mask])
    P_unadjusted = (1 - np.exp(-I * (q * 0.28 *(1- p_mask)) * p * t /V)) * 0.9
    print(f"Unadjusted Probability of infection: {P_unadjusted*100:.2f}%")
    return P_unadjusted 
  

def main():
    I = 1  
    q = 100 
    p = 0.32  
    V = 253.5
    x_1 = []
    y_1 = []
    x_2 = []
    y_2 = []
    iterations = 5000
    for i in range(12):
        y_accum = 0
        y_accum = 1
        for j in range(iterations):
            y_accum+=simulate(I,q,p,i,V,0.09)
            y_accum+=simulate(I,q,p,i,V,0.94)
        y_1.append(y_accum/5000 * 100)
        y_2.append(y_accum/5000 * 100)
        x_1.append(i)
        x_2.append(i)
    plt.xlabel('Hours Passed')
    plt.ylabel('Probability of infection')
    plt.plot(x_1,y_1)
    plt.title('Korean vs American Policies')
    plt.show()
if __name__ == '__main__':
    main()
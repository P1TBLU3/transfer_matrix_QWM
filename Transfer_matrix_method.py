import numpy as np


#CONSTANTS DEFINITION

hbar = 1.0545718e-34  # Reduced Planck's constant in J·s
m = 9.10938356e-31    # Electron mass in kg (We assume we are working with electrons)



#FUNCTIONS 


# Get propagation coefficient k for a wave given E and V
def get_k(E, V): 
    if E >= V:
        return np.sqrt(2 * m * (E - V)) / hbar
    else:
        # For E < V, return an imaginary k
        return 1j * np.sqrt(2 * m * (V - E)) / hbar
    
    
# Transfer matrix associated to propagation through a region with constant potential V of length L.
def propagation_matrix(k, L):
    phi = k * L
    M = np.array([
        [np.exp(1j * phi), 0],
        [0, np.exp(-1j * phi),]
    ],dtype=complex)
    return M


# Transfer  associated to change between to 
def step_matrix(k_left, k_right):
    k_ratio = k_left / k_right
    M_step = 0.5 *np.array([[1 + k_ratio     ,    1 - k_ratio],
                       [1 - k_ratio     ,    1 + k_ratio]],dtype=complex)
    return M_step


def calculate_total_matrix(E,V0,VF):
    
    Transfer_matrix = np.array([[1, 0],
                         [0, 1]], dtype=complex)

    k_left = get_k(E,V0)

    for tuple in potential_profile:
        V, L= tuple
        k_right = get_k(E,V)
        
        M = step_matrix(k_left, k_right)
        Transfer_matrix = M @ Transfer_matrix
        
        M = propagation_matrix(k_right, L)
        Transfer_matrix = M @ Transfer_matrix
        
        k_left = k_right
        
        print(Transfer_matrix)

    k_right = get_k(E,VF)

    M = step_matrix(k_left, k_right)
    Transfer_matrix = M @ Transfer_matrix

    return Transfer_matrix



def get_coefficients(M):
    r = M[1,0]/M[1,1]
    t = ((M[0,0]*M[1,1])-(M[0,1]*M[1,0]))/M[1,1]
    T = np.abs(t) ** 2
    R = np.abs(r) ** 2 
    
    print("Total reflectance: " + str(R))
    print("Total transmittance: " + str(T))
    
    return r, t, R, T






#MODIFY THESE VALUES TO CALCULATE THE VALUES OF THE WAVE


# V is potential energy in each region, x defines the start of each region
V0 = 0
#Each step [Voltage , Length of interface]
#Length should be >= 0

potential_profile = [(0.9e-20, 0.5e-9), (0.7e-20, 0.5e-9), (1.3e-20,0.5e-9)]
VF = 0

#Energy in joules
E = 1.0e-20  # Example energy of incoming wave

A0 = 1e-9
print((np.abs(A0) ** 2))
#MAIN

M = calculate_total_matrix(E,V0,VF)

r, t, R, T = get_coefficients(M) 


if (V0 > E):
    #Decaying exponential coming from -inf -> intensity = 0
    A0= 0
    

print("Amplitude of the reflected wave:" + str(A0*r))
print("Amplitude of the transmitted  wave: " + str(A0*t))
print("Reflected energy: "+ str((np.abs(A0) ** 2)*R) + " J")
print("Transmitted enegy: " +str((np.abs(A0) ** 2)*T) + " J")

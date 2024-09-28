
# Filename: vqe_klein_gordon_qiskit.py

from qiskit import Aer, QuantumCircuit
from qiskit.utils import QuantumInstance
from qiskit.circuit.library import TwoLocal
from qiskit.algorithms import VQE
from qiskit.algorithms.optimizers import COBYLA
from qiskit.opflow import Z, X, Y, I, PauliSumOp
import numpy as np

def create_klein_gordon_hamiltonian():
    """
    Creates a simplified Hamiltonian representing scalar field configurations
    under gravitational influence. This is an analog for demonstration purposes.
    """
    # Example Hamiltonian: H = a*Z + b*X + c*Y + d*I
    a = 1.0  # Coefficient for Z term
    b = 0.5  # Coefficient for X term
    c = 0.3  # Coefficient for Y term
    d = 0.2  # Coefficient for Identity term

    hamiltonian = a * Z + b * X + c * Y + d * I
    return PauliSumOp.from_list([("Z", a), ("X", b), ("Y", c), ("I", d)])

def run_vqe():
    # Create the Hamiltonian
    hamiltonian = create_klein_gordon_hamiltonian()
    
    # Define the quantum instance
    quantum_instance = QuantumInstance(backend=Aer.get_backend('statevector_simulator'))
    
    # Define the ansatz (variational form)
    ansatz = TwoLocal(rotation_blocks='ry', entanglement_blocks='cz', reps=3)
    
    # Define the optimizer
    optimizer = COBYLA(maxiter=1000)
    
    # Initialize VQE
    vqe = VQE(ansatz=ansatz, optimizer=optimizer, quantum_instance=quantum_instance)
    
    # Run VQE to find the ground state energy
    result = vqe.compute_minimum_eigenvalue(hamiltonian)
    
    # Extract and print the results
    ground_state_energy = result.eigenvalue.real
    print(f"Computed Ground State Energy: {ground_state_energy:.6f} Hartree")
    print("Optimized Parameters:", result.optimal_point)

if __name__ == "__main__":
    run_vqe()

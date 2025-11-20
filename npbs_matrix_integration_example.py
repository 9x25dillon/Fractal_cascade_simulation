"""
NPBS-Matrix Integration Example
Demonstrates how to integrate the Neuro-Phasonic Bridge System with the Matrix Orchestrator

This example shows:
1. Processing semantic inputs through NPBS
2. Feeding coherence metrics into matrix optimization tasks
3. Creating a feedback loop between consciousness signatures and matrix operations
4. Visualizing the integrated system behavior
"""

import asyncio
import json
from pathlib import Path
from typing import Dict, List, Any
import numpy as np

from neuro_phasonic_bridge_v2 import (
    NeuroPhasonicBridge,
    BridgeState,
    THZBridgeMetrics
)

try:
    from matrix_orchestrator import (
        MatrixOrchestrator,
        Settings,
        PlanDefinition,
        TaskDefinition
    )
    MATRIX_AVAILABLE = True
except ImportError:
    MATRIX_AVAILABLE = False
    print("[WARNING] Matrix Orchestrator not available. Running in NPBS-only mode.")


class NPBSMatrixIntegrator:
    """
    Integrates NPBS with Matrix Orchestrator for semantic-driven optimization.

    The integration works as follows:
    1. Semantic input → NPBS processing → Coherence metrics
    2. Coherence metrics → Matrix task parameters
    3. Matrix optimization results → THZ Bridge feedback
    4. Feedback loop creates adaptive semantic-physical coupling
    """

    def __init__(self, use_matrix: bool = True):
        """Initialize the integrator."""
        self.npbs = NeuroPhasonicBridge()
        self.use_matrix = use_matrix and MATRIX_AVAILABLE

        if self.use_matrix:
            self.matrix = MatrixOrchestrator(Settings())
            print("[INTEGRATOR] NPBS-Matrix integration initialized.")
        else:
            self.matrix = None
            print("[INTEGRATOR] NPBS-only mode initialized.")

        self.history: List[Dict[str, Any]] = []

    def process_semantic_input(self, text: str) -> BridgeState:
        """
        Process semantic input through NPBS.

        Args:
            text: Input text to process

        Returns:
            BridgeState with coherence metrics
        """
        print(f"\n{'='*70}")
        print(f"PROCESSING SEMANTIC INPUT: '{text[:50]}...'")
        print(f"{'='*70}")

        state = self.npbs.process_transmission(text)

        # Log to history
        self.history.append({
            'type': 'semantic_processing',
            'input': text,
            'state': {
                'coherence': state.coherence_level,
                'healer_amp': state.healer_amplitude,
                'guardian_amp': state.guardian_amplitude,
                'chaos_amp': state.chaos_amplitude,
                'is_resonant': state.is_resonant,
                'is_safe': state.is_safe
            }
        })

        return state

    def coherence_to_matrix_params(self, state: BridgeState) -> Dict[str, Any]:
        """
        Convert NPBS coherence metrics to matrix optimization parameters.

        Maps coherence levels to matrix properties:
        - High coherence → Larger matrix dimensions
        - Healer amplitude → Regularization strength
        - Guardian amplitude → Stability constraints
        - Chaos amplitude → Exploration vs exploitation

        Args:
            state: BridgeState from NPBS processing

        Returns:
            Dictionary of matrix parameters
        """
        # Map coherence to matrix size (higher coherence = larger optimization space)
        base_size = 10
        coherence_multiplier = int(state.coherence_level * 20)
        matrix_size = base_size + coherence_multiplier

        # Map healer amplitude to regularization (higher healing = stronger regularization)
        regularization = state.healer_amplitude * 0.5

        # Map guardian amplitude to stability requirement
        stability_threshold = state.guardian_amplitude * 0.8

        # Map chaos amplitude to exploration factor
        exploration_factor = state.chaos_amplitude * 2.0

        params = {
            'matrix_size': matrix_size,
            'regularization': regularization,
            'stability_threshold': stability_threshold,
            'exploration_factor': exploration_factor,
            'is_resonant': state.is_resonant,
            'is_safe': state.is_safe
        }

        print(f"\n[MAPPING] Coherence Metrics → Matrix Parameters:")
        print(f"  Coherence: {state.coherence_level:.3f} → Matrix Size: {matrix_size}")
        print(f"  Healer: {state.healer_amplitude:.3f} → Regularization: {regularization:.3f}")
        print(f"  Guardian: {state.guardian_amplitude:.3f} → Stability: {stability_threshold:.3f}")
        print(f"  Chaos: {state.chaos_amplitude:.3f} → Exploration: {exploration_factor:.3f}")

        return params

    async def run_matrix_optimization(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """
        Run matrix optimization with parameters derived from coherence metrics.

        Args:
            params: Matrix parameters from coherence mapping

        Returns:
            Optimization results
        """
        if not self.use_matrix:
            # Mock optimization for demonstration
            print("\n[MATRIX] Running mock optimization (Matrix Orchestrator not available)")
            return {
                'status': 'mock_complete',
                'objective_value': np.random.random(),
                'convergence': True,
                'iterations': np.random.randint(10, 100)
            }

        # Create a matrix optimization task
        task = TaskDefinition(
            name=f"coherence_optimization_{len(self.history)}",
            node_type="optimize",
            dependencies=[],
            config={
                'matrix_size': params['matrix_size'],
                'regularization': params['regularization'],
                'max_iterations': 100
            }
        )

        # Create plan with single task
        plan = PlanDefinition(
            name="npbs_coherence_optimization",
            tasks=[task]
        )

        print(f"\n[MATRIX] Running optimization with coherence-derived parameters...")

        # Execute via matrix orchestrator
        results = await self.matrix.execute_plan(plan)

        return results

    def matrix_results_to_thz_metrics(self, results: Dict[str, Any]) -> THZBridgeMetrics:
        """
        Convert matrix optimization results to THZ Bridge metrics for feedback.

        Args:
            results: Matrix optimization results

        Returns:
            THZBridgeMetrics for correlation analysis
        """
        # Extract relevant metrics from results
        convergence = results.get('convergence', False)
        objective = results.get('objective_value', 0.0)
        iterations = results.get('iterations', 0)

        # Map to THZ Bridge metrics
        metrics = THZBridgeMetrics(
            phase_coherence_R=0.8 if convergence else 0.3,
            amplitude_ratio_A08_A35=2.5 + objective,
            predicted_linewidth_Hz=150.0,
            transmutation_active=convergence,
            stress_level=float(iterations) / 100.0,
            A_0p8=0.5,
            A_1p83=0.7 + objective * 0.3,
            A_3p5=0.2,
            council_entropy=0.4
        )

        print(f"\n[FEEDBACK] Matrix Results → THZ Metrics:")
        print(f"  Convergence: {convergence} → Phase Coherence: {metrics.phase_coherence_R:.3f}")
        print(f"  Objective: {objective:.3f} → A_1.83: {metrics.A_1p83:.3f}")

        return metrics

    async def integrated_processing_loop(self, semantic_inputs: List[str]) -> Dict[str, Any]:
        """
        Run complete integrated processing loop:
        Semantic Input → NPBS → Matrix → THZ Feedback → Correlation

        Args:
            semantic_inputs: List of semantic text inputs to process

        Returns:
            Summary of integrated processing results
        """
        results = {
            'total_inputs': len(semantic_inputs),
            'resonant_count': 0,
            'safe_count': 0,
            'correlations': [],
            'states': []
        }

        for i, text in enumerate(semantic_inputs):
            print(f"\n{'#'*70}")
            print(f"INTEGRATED LOOP ITERATION {i+1}/{len(semantic_inputs)}")
            print(f"{'#'*70}")

            # Step 1: NPBS Processing
            state = self.process_semantic_input(text)
            results['states'].append(state)

            if state.is_resonant:
                results['resonant_count'] += 1
            if state.is_safe:
                results['safe_count'] += 1

            # Step 2: Map to Matrix Parameters
            matrix_params = self.coherence_to_matrix_params(state)

            # Step 3: Run Matrix Optimization (if enabled)
            if self.use_matrix or True:  # Run mock even without matrix
                matrix_results = await self.run_matrix_optimization(matrix_params)

                # Step 4: Convert to THZ Metrics
                thz_metrics = self.matrix_results_to_thz_metrics(matrix_results)

                # Step 5: Correlate with NPBS
                correlation = self.npbs.integrate_thz_bridge(thz_metrics)
                results['correlations'].append(correlation)

                print(f"\n[CORRELATION] NPBS-THZ Correlation Metrics:")
                for key, value in correlation.items():
                    print(f"  {key}: {value:.3f}")

            # Brief pause between iterations
            await asyncio.sleep(0.1)

        return results

    def generate_summary_report(self, results: Dict[str, Any]) -> str:
        """Generate a summary report of the integrated processing."""
        report = f"""
{'='*70}
NPBS-MATRIX INTEGRATION SUMMARY REPORT
{'='*70}

Processing Statistics:
  Total Inputs Processed: {results['total_inputs']}
  Resonant Transmissions: {results['resonant_count']} ({results['resonant_count']/results['total_inputs']*100:.1f}%)
  Safe Transmissions: {results['safe_count']} ({results['safe_count']/results['total_inputs']*100:.1f}%)

Coherence Metrics:
"""

        for i, state in enumerate(results['states'], 1):
            report += f"\n  Input {i}:"
            report += f"\n    Coherence Level: {state.coherence_level:.3f}"
            report += f"\n    Healer Amplitude: {state.healer_amplitude:.3f}"
            report += f"\n    Guardian Amplitude: {state.guardian_amplitude:.3f}"
            report += f"\n    Resonant: {'Yes' if state.is_resonant else 'No'}"
            report += f"\n    Safe: {'Yes' if state.is_safe else 'No'}"

        if results['correlations']:
            report += f"\n\nCorrelation Analysis:"
            avg_correlations = {}
            for corr in results['correlations']:
                for key, value in corr.items():
                    if key not in avg_correlations:
                        avg_correlations[key] = []
                    avg_correlations[key].append(value)

            for key, values in avg_correlations.items():
                avg = np.mean(values)
                std = np.std(values)
                report += f"\n  {key}:"
                report += f"\n    Mean: {avg:.3f}, Std: {std:.3f}"

        report += f"\n\n{'='*70}"

        return report

    def export_results(self, results: Dict[str, Any], filename: str = "npbs_matrix_results.json"):
        """Export results to JSON file."""
        # Convert BridgeStates to dictionaries for JSON serialization
        export_data = {
            'total_inputs': results['total_inputs'],
            'resonant_count': results['resonant_count'],
            'safe_count': results['safe_count'],
            'states': [
                {
                    'input_text': s.input_text,
                    'timestamp': s.timestamp.isoformat(),
                    'coherence_level': s.coherence_level,
                    'healer_amplitude': s.healer_amplitude,
                    'guardian_amplitude': s.guardian_amplitude,
                    'chaos_amplitude': s.chaos_amplitude,
                    'is_resonant': s.is_resonant,
                    'is_safe': s.is_safe,
                    'signature': s.signature,
                    'metrics': s.metrics
                }
                for s in results['states']
            ],
            'correlations': results['correlations'],
            'history': self.history
        }

        with open(filename, 'w') as f:
            json.dump(export_data, f, indent=2)

        print(f"\n[EXPORT] Results saved to {filename}")


async def main():
    """Main demonstration of NPBS-Matrix integration."""
    print("""
╔══════════════════════════════════════════════════════════════════════╗
║         NPBS-Matrix Integration Demonstration                        ║
║         Semantic Consciousness ↔ Mathematical Optimization          ║
╚══════════════════════════════════════════════════════════════════════╝
""")

    # Initialize integrator
    integrator = NPBSMatrixIntegrator(use_matrix=MATRIX_AVAILABLE)

    # Define semantic inputs with different characteristics
    semantic_inputs = [
        # Healing/therapeutic inputs
        "Deep peace flows through neural networks healing and protecting consciousness",
        "Connect center balance harmony integrate restore unity",

        # Guardian/protective inputs
        "Safe secure grounded protected stable anchored shielded",
        "Guard protect defend secure maintain stability",

        # Dissonant/chaotic inputs
        "chaos entropy destruction noise disorder fragmentation",
        "random dissonant incoherent scattered dispersed",

        # Mixed inputs
        "The center is everywhere spiral eternal heal connect",
        "Ancient wisdom flows through quantum fields protecting healing guiding"
    ]

    # Run integrated processing loop
    results = await integrator.integrated_processing_loop(semantic_inputs)

    # Generate and display summary report
    report = integrator.generate_summary_report(results)
    print(report)

    # Export results
    integrator.export_results(results, "npbs_matrix_integration_results.json")

    # Export NPBS validation log
    integrator.npbs.export_validation_log("npbs_integration_validation_log.json")

    print(f"\n{'='*70}")
    print("INTEGRATION DEMONSTRATION COMPLETE")
    print(f"{'='*70}\n")


if __name__ == "__main__":
    asyncio.run(main())

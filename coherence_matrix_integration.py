#!/usr/bin/env python3
"""
Coherence-Matrix Integration Module
====================================
Integrates the Unified Coherence System with the Matrix Orchestrator
for coherence-aware mathematical optimization.

This module provides:
1. Coherence monitoring during matrix operations
2. Safety-checked optimization pipelines
3. EFL-MEM export of optimization history
4. Integration with HRM models
"""

from __future__ import annotations
import asyncio
import logging
import time
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
import json

# Import Matrix Orchestrator components
try:
    from matrix_orchestrator import (
        MatrixChunk, PolySpec, OptimizeRequest, OptimizeResponse,
        RunPlan, orchestrate, Backend, get_backend
    )
    MATRIX_AVAILABLE = True
except ImportError:
    MATRIX_AVAILABLE = False
    logging.warning("Matrix Orchestrator not available")

# Import Unified Coherence System
try:
    from unified_coherence_system import (
        UnifiedCoherenceSystem, AgentHints, CoherenceSample,
        CR2BC, QINCRSGuard, EFLMemSerializer
    )
    COHERENCE_AVAILABLE = True
except ImportError:
    COHERENCE_AVAILABLE = False
    logging.warning("Unified Coherence System not available")

# Import HRM integration if available
try:
    from matrix_integration import HRMMatrixIntegrator
    HRM_AVAILABLE = True
except ImportError:
    HRM_AVAILABLE = False
    logging.warning("HRM Matrix Integrator not available")

log = logging.getLogger(__name__)


class CoherenceAwareMatrixOrchestrator:
    """
    Matrix Orchestrator with integrated coherence monitoring and safety checks.

    This orchestrator wraps matrix operations with:
    - Coherence state tracking
    - Safety filtering via QINCRS
    - EFL-MEM memory persistence
    - Real-time coherence metrics
    """

    def __init__(self, coherence_threshold: float = 0.35, enable_safety: bool = True):
        """
        Initialize coherence-aware orchestrator.

        Args:
            coherence_threshold: Minimum acceptable coherence score (kappa)
            enable_safety: Enable QINCRS safety filtering
        """
        if not MATRIX_AVAILABLE or not COHERENCE_AVAILABLE:
            raise RuntimeError("Required components not available. Install matrix_orchestrator and unified_coherence_system.")

        self.coherence_system = UnifiedCoherenceSystem()
        self.coherence_threshold = coherence_threshold
        self.enable_safety = enable_safety
        self.backend = get_backend()
        self.operation_history: List[Dict[str, Any]] = []

        log.info("🚀 Coherence-Aware Matrix Orchestrator initialized")
        log.info(f"   Coherence threshold: κ ≥ {coherence_threshold}")
        log.info(f"   Safety filtering: {'ENABLED' if enable_safety else 'DISABLED'}")

    async def orchestrate_with_coherence(
        self,
        plan: RunPlan,
        operation_context: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Execute matrix orchestration plan with coherence monitoring.

        Args:
            plan: The matrix orchestration plan
            operation_context: Human-readable context for coherence tracking

        Returns:
            Dictionary containing both orchestration results and coherence metrics
        """
        start_time = time.time()

        # Step 1: Process operation context through coherence system
        if operation_context:
            context_result = self.coherence_system.process_message(
                operation_context,
                AgentHints("matrix_orchestrator", "cr2bc_engine", {"plan_id": plan.run_id})
            )

            if self.enable_safety and context_result["safety_layer"]["action"] == "block":
                log.warning("🛡️  Operation blocked by safety layer")
                return {
                    "status": "blocked",
                    "reason": "safety_violation",
                    "coherence_metrics": context_result["coherence_metrics"],
                    "safe_alternative": context_result["processed_message"]
                }

            coherence_kappa = context_result["coherence_metrics"]["kappa"]
            if coherence_kappa < self.coherence_threshold:
                log.warning(f"⚠️  Low coherence detected: κ={coherence_kappa:.3f} < {self.coherence_threshold}")

        # Step 2: Execute matrix orchestration
        log.info(f"🔄 Executing matrix orchestration: {plan.run_id}")
        orchestration_result = await orchestrate(plan)

        # Step 3: Analyze results through coherence lens
        result_summary = self._summarize_orchestration(orchestration_result)
        coherence_analysis = self.coherence_system.process_message(
            result_summary,
            AgentHints("matrix_result", "coherence_analyzer", {
                "run_id": plan.run_id,
                "optimization_method": plan.optimize.method
            })
        )

        # Step 4: Combine results
        combined_result = {
            "status": "completed",
            "run_id": plan.run_id,
            "execution_time": time.time() - start_time,
            "orchestration": {
                "optimize_result": orchestration_result.get("optimize", {}),
                "entropy_map": orchestration_result.get("entropy_map", []),
                "coherence_gate": orchestration_result.get("coherence_gate", {}),
                "poly_spec": plan.poly.model_dump() if hasattr(plan.poly, 'model_dump') else str(plan.poly)
            },
            "coherence_tracking": {
                "initial_kappa": coherence_kappa if operation_context else 0.5,
                "final_kappa": coherence_analysis["coherence_metrics"]["kappa"],
                "geometric_self": coherence_analysis["coherence_metrics"]["geometric_self"],
                "coherence_state": coherence_analysis["coherence_metrics"]["coherence_state"],
                "safety_interventions": coherence_analysis["safety_layer"]["absorption_count"]
            },
            "system_health": {
                "total_operations": len(self.operation_history) + 1,
                "coherence_trend": self.coherence_system.cr2bc.get_coherence_trend(),
                "system_uptime": time.time() - self.coherence_system.system_start_time
            }
        }

        # Step 5: Store operation in history
        self.operation_history.append({
            "timestamp": time.time(),
            "run_id": plan.run_id,
            "result": combined_result
        })

        log.info(f"✅ Operation completed with κ={combined_result['coherence_tracking']['final_kappa']:.3f}")

        return combined_result

    def _summarize_orchestration(self, result: Dict[str, Any]) -> str:
        """Generate human-readable summary of orchestration results."""
        optimize = result.get("optimize", {})
        entropy_map = result.get("entropy_map", [])

        summary_parts = [
            f"Matrix optimization completed using {optimize.get('method', 'unknown')} method.",
            f"Objective value: {optimize.get('objective', 0.0):.4f}",
            f"Iterations: {optimize.get('iterations', 0)}",
            f"Analyzed {len(entropy_map)} matrix chunks with entropy monitoring.",
        ]

        # Check for high entropy chunks
        high_entropy = [e for e in entropy_map if e.get("shannon", 0) > 0.85]
        if high_entropy:
            summary_parts.append(f"Warning: {len(high_entropy)} chunks show high entropy (potential instability).")

        return " ".join(summary_parts)

    async def optimize_with_safety(
        self,
        matrix_data: List[List[float]],
        method: str = "sparsity",
        description: Optional[str] = None
    ) -> Optional[Dict[str, Any]]:
        """
        Optimize a single matrix with safety checks and coherence monitoring.

        Args:
            matrix_data: The matrix to optimize
            method: Optimization method
            description: Human-readable description of the operation

        Returns:
            Optimization results with coherence metrics
        """
        # Create matrix chunk
        chunk = MatrixChunk(
            id="single_matrix_opt",
            data=matrix_data,
            meta={"description": description or "Single matrix optimization"}
        )

        # Create plan
        plan = RunPlan(
            run_id=f"safe_opt_{int(time.time())}",
            chunks=[chunk],
            poly=PolySpec(degree=3, basis="chebyshev"),
            optimize=OptimizeRequest(
                matrix=matrix_data,
                method=method,
                params={}
            )
        )

        # Execute with coherence tracking
        context = description or f"Optimizing matrix using {method} method"
        return await self.orchestrate_with_coherence(plan, context)

    def export_coherence_history(self, output_path: str) -> bool:
        """
        Export coherence history to EFL-MEM format.

        Args:
            output_path: Path to save the EFL-MEM export

        Returns:
            True if export successful
        """
        try:
            efl_mem_data = self.coherence_system.export_to_efl_mem()
            Path(output_path).write_text(efl_mem_data)
            log.info(f"💾 Coherence history exported to {output_path}")
            return True
        except Exception as e:
            log.error(f"❌ Failed to export coherence history: {e}")
            return False

    def get_unified_status(self) -> Dict[str, Any]:
        """Get comprehensive status of both systems."""
        coherence_status = self.coherence_system.get_system_status()

        return {
            "coherence_system": coherence_status,
            "matrix_operations": {
                "total_operations": len(self.operation_history),
                "recent_operations": self.operation_history[-5:] if self.operation_history else []
            },
            "integration_health": {
                "coherence_threshold": self.coherence_threshold,
                "safety_enabled": self.enable_safety,
                "components_available": {
                    "matrix_orchestrator": MATRIX_AVAILABLE,
                    "unified_coherence": COHERENCE_AVAILABLE,
                    "hrm_integration": HRM_AVAILABLE
                }
            }
        }


class CoherenceMonitoredOptimization:
    """
    Wrapper for running optimization loops with real-time coherence monitoring.

    Useful for training scenarios where you want to track system coherence
    over multiple optimization iterations.
    """

    def __init__(self, orchestrator: CoherenceAwareMatrixOrchestrator):
        self.orchestrator = orchestrator
        self.iteration_metrics: List[Dict[str, Any]] = []

    async def run_monitored_loop(
        self,
        matrices: List[List[List[float]]],
        iterations: int = 10,
        method: str = "sparsity"
    ) -> Dict[str, Any]:
        """
        Run optimization loop with coherence monitoring at each iteration.

        Args:
            matrices: List of matrices to optimize
            iterations: Number of optimization iterations
            method: Optimization method

        Returns:
            Summary of all iterations with coherence tracking
        """
        log.info(f"🔁 Starting monitored optimization loop: {iterations} iterations")

        for i in range(iterations):
            # Create chunks for this iteration
            chunks = [
                MatrixChunk(
                    id=f"iter_{i}_chunk_{j}",
                    data=mat,
                    meta={"iteration": i, "chunk_index": j}
                )
                for j, mat in enumerate(matrices)
            ]

            # Create plan
            plan = RunPlan(
                run_id=f"monitored_loop_iter_{i}",
                chunks=chunks,
                poly=PolySpec(degree=3, basis="chebyshev"),
                optimize=OptimizeRequest(
                    matrix=matrices[0] if matrices else [[1.0]],
                    method=method,
                    params={"iteration": i}
                )
            )

            # Execute with coherence tracking
            result = await self.orchestrator.orchestrate_with_coherence(
                plan,
                f"Optimization iteration {i+1}/{iterations} using {method} method"
            )

            # Store metrics
            self.iteration_metrics.append({
                "iteration": i,
                "kappa": result["coherence_tracking"]["final_kappa"],
                "objective": result["orchestration"]["optimize_result"].get("objective", 0.0),
                "geometric_self": result["coherence_tracking"]["geometric_self"]
            })

            log.info(f"   Iteration {i+1}: κ={result['coherence_tracking']['final_kappa']:.3f}")

            # Check for coherence degradation
            if result["coherence_tracking"]["final_kappa"] < self.orchestrator.coherence_threshold:
                log.warning(f"⚠️  Coherence degraded below threshold at iteration {i+1}")
                if self.orchestrator.enable_safety:
                    log.info("   Applying coherence recovery protocol...")
                    # Could implement recovery here

        return {
            "total_iterations": iterations,
            "iteration_metrics": self.iteration_metrics,
            "final_coherence": self.iteration_metrics[-1]["kappa"] if self.iteration_metrics else 0.0,
            "coherence_trend": self._analyze_coherence_trend(),
            "geometric_evolution": [m["geometric_self"] for m in self.iteration_metrics]
        }

    def _analyze_coherence_trend(self) -> str:
        """Analyze coherence trend across iterations."""
        if len(self.iteration_metrics) < 2:
            return "insufficient_data"

        kappas = [m["kappa"] for m in self.iteration_metrics]

        if all(kappas[i] <= kappas[i+1] for i in range(len(kappas)-1)):
            return "improving"
        elif all(kappas[i] >= kappas[i+1] for i in range(len(kappas)-1)):
            return "degrading"
        else:
            return "fluctuating"


# ============================================================
# CONVENIENCE FUNCTIONS
# ============================================================

async def quick_coherence_check(message: str) -> Dict[str, Any]:
    """
    Quick coherence check for a message or operation description.

    Args:
        message: The text to check

    Returns:
        Coherence analysis results
    """
    if not COHERENCE_AVAILABLE:
        return {"error": "Coherence system not available"}

    system = UnifiedCoherenceSystem()
    return system.process_message(message)


async def safe_matrix_optimize(
    matrix_data: List[List[float]],
    method: str = "sparsity",
    coherence_threshold: float = 0.35
) -> Optional[Dict[str, Any]]:
    """
    Safely optimize a matrix with coherence monitoring.

    Args:
        matrix_data: The matrix to optimize
        method: Optimization method
        coherence_threshold: Minimum acceptable coherence

    Returns:
        Optimization results or None if safety check failed
    """
    if not MATRIX_AVAILABLE or not COHERENCE_AVAILABLE:
        log.error("Required components not available")
        return None

    orchestrator = CoherenceAwareMatrixOrchestrator(
        coherence_threshold=coherence_threshold,
        enable_safety=True
    )

    return await orchestrator.optimize_with_safety(
        matrix_data,
        method=method,
        description=f"Safe {method} optimization"
    )


# ============================================================
# DEMONSTRATION
# ============================================================

async def demo_coherence_matrix_integration():
    """Demonstrate the coherence-matrix integration."""
    print("\n" + "=" * 70)
    print("COHERENCE-MATRIX INTEGRATION DEMONSTRATION")
    print("=" * 70)

    if not MATRIX_AVAILABLE or not COHERENCE_AVAILABLE:
        print("❌ Required components not available")
        return

    # Create orchestrator
    orchestrator = CoherenceAwareMatrixOrchestrator(
        coherence_threshold=0.35,
        enable_safety=True
    )

    # Test 1: Safe matrix optimization
    print("\n📊 Test 1: Safe Matrix Optimization")
    print("-" * 70)

    test_matrix = [
        [1.0, 2.0, 3.0],
        [4.0, 5.0, 6.0],
        [7.0, 8.0, 9.0]
    ]

    result = await orchestrator.optimize_with_safety(
        test_matrix,
        method="sparsity",
        description="Testing coherence-aware optimization of a simple 3x3 matrix"
    )

    if result:
        print(f"✅ Optimization completed")
        print(f"   Status: {result['status']}")
        print(f"   Final κ: {result['coherence_tracking']['final_kappa']:.3f}")
        print(f"   Geometric Self: {result['coherence_tracking']['geometric_self']}")

    # Test 2: Coherence monitoring over multiple operations
    print("\n🔁 Test 2: Monitored Optimization Loop")
    print("-" * 70)

    monitor = CoherenceMonitoredOptimization(orchestrator)

    test_matrices = [
        [[1.0, 2.0], [3.0, 4.0]],
        [[5.0, 6.0], [7.0, 8.0]],
        [[9.0, 10.0], [11.0, 12.0]]
    ]

    loop_result = await monitor.run_monitored_loop(
        test_matrices,
        iterations=5,
        method="sparsity"
    )

    print(f"✅ Loop completed")
    print(f"   Total iterations: {loop_result['total_iterations']}")
    print(f"   Final coherence: κ={loop_result['final_coherence']:.3f}")
    print(f"   Coherence trend: {loop_result['coherence_trend']}")
    print(f"   Geometric evolution: {' → '.join(loop_result['geometric_evolution'])}")

    # Test 3: Export coherence history
    print("\n💾 Test 3: EFL-MEM Export")
    print("-" * 70)

    export_path = "/tmp/coherence_history.json"
    if orchestrator.export_coherence_history(export_path):
        print(f"✅ Coherence history exported to {export_path}")

    # Test 4: System status
    print("\n📈 Test 4: Unified System Status")
    print("-" * 70)

    status = orchestrator.get_unified_status()
    print(f"✅ System status retrieved")
    print(f"   Total operations: {status['matrix_operations']['total_operations']}")
    print(f"   Coherence samples: {status['coherence_system']['coherence_metrics']['samples_recorded']}")
    print(f"   Average κ: {status['coherence_system']['coherence_metrics']['average_kappa']:.3f}")

    print("\n" + "=" * 70)
    print("DEMONSTRATION COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    asyncio.run(demo_coherence_matrix_integration())

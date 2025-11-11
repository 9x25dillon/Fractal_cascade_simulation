# HRM + Enhanced Matrix Orchestrator + Unified Coherence System

Hierarchical Reasoning Model with advanced mathematical optimization via Matrix Orchestrator, enhanced with the Unified Coherence System for safety, coherence tracking, and resilient optimization.

## 🌟 Features

### Core Components

1. **Hierarchical Reasoning Model (HRM)**
   - Advanced neural architecture for complex reasoning tasks
   - Adaptive computation with halting mechanisms
   - Multi-layer hierarchical processing

2. **Enhanced Matrix Orchestrator**
   - Declarative DAG-based computation pipeline
   - Julia backend integration for mathematical optimization
   - Coherence gates and stability probes
   - Entropy monitoring and analysis

3. **Unified Coherence System (NEW!)**
   - **CR²BC Engine**: Coherence-Renewal Bi-Coupling for mathematical coherence reconstruction
   - **EFL-MEM Format**: Episodic Field Layer Memory for persistent coherence tracking
   - **QINCRS Guardian**: Quantum-Inspired Neural Coherence Recovery System with safety filtering
   - Real-time coherence monitoring and geometric self-state tracking

### Integration Features

- **Coherence-Aware Optimization**: Matrix operations monitored for coherence stability
- **Safety-Checked Pipelines**: QINCRS Guardian filters harmful or unstable operations
- **EFL-MEM Persistence**: Export optimization history in coherence-aware format
- **Multi-Modal Tracking**: Geometric self-states, coherence levels, and safety metrics

## 🚀 Quick Start

### Basic Installation

```bash
# Install in editable mode
pip install -e .[ml,dev]

# Run orchestrator CLI
matrix-orchestrator --plan plan.json

# Test HRM-Matrix integration
python matrix_integration.py
```

### Unified Coherence System

```bash
# Run coherence system demo
python unified_coherence_system.py

# Run coherence-matrix integration demo
python coherence_matrix_integration.py

# Run comprehensive tests
python test_unified_coherence.py
```

## 📊 Usage Examples

### Matrix Orchestration with Coherence Monitoring

```python
from coherence_matrix_integration import CoherenceAwareMatrixOrchestrator
from matrix_orchestrator import RunPlan, MatrixChunk, PolySpec, OptimizeRequest

# Create coherence-aware orchestrator
orchestrator = CoherenceAwareMatrixOrchestrator(
    coherence_threshold=0.35,
    enable_safety=True
)

# Define optimization plan
plan = RunPlan(
    run_id="my_optimization",
    chunks=[MatrixChunk(id="chunk_1", data=[[1.0, 2.0], [3.0, 4.0]])],
    poly=PolySpec(degree=3, basis="chebyshev"),
    optimize=OptimizeRequest(matrix=[[1.0, 2.0]], method="sparsity")
)

# Execute with coherence tracking
result = await orchestrator.orchestrate_with_coherence(
    plan,
    operation_context="Optimizing matrix with coherence monitoring"
)

print(f"Coherence: κ={result['coherence_tracking']['final_kappa']:.3f}")
print(f"Geometric Self: {result['coherence_tracking']['geometric_self']}")
```

### Direct Coherence Checking

```python
from unified_coherence_system import UnifiedCoherenceSystem, AgentHints

# Initialize system
system = UnifiedCoherenceSystem()

# Process message through coherence pipeline
result = system.process_message(
    "Analyzing system stability patterns",
    AgentHints("analyzer", "cr2bc", {"context": "testing"})
)

# Check coherence metrics
print(f"Coherence State: {result['coherence_metrics']['coherence_state']}")
print(f"Safety Action: {result['safety_layer']['action']}")
```

## 🧪 Testing

Run the comprehensive test suite:

```bash
# Test all components
python test_unified_coherence.py

# Test matrix integration
python test_matrix_integration.py

# Test optimizer adapter
python test_adapter.py
```

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

**Copyright (c) 2025 9x25dillon**

## 💰 Commercial Use

This software is provided under the MIT License, which allows:
- ✅ Commercial use and distribution
- ✅ Modification and derivative works
- ✅ Private and public use
- ✅ Sublicensing

**Attribution Required**: You must include the copyright notice and license terms in any distribution.
# Neuro-Phasonic Bridge System (NPBS) v2.0

## Overview

The Neuro-Phasonic Bridge System (NPBS) v2.0 is a **fictional / speculative simulation framework** that transduces semantic text inputs into physical stress wave simulations, models biological coherence responses, and generates consciousness signatures based on resonance detection.

**⚠️ DISCLAIMER**: This is an **imaginative modeling playground** for exploring theoretical physics concepts. It does NOT implement real terahertz biology, consciousness control, or medical functionality.

## Architecture

### Core Components

```
┌─────────────────────────────────────────────────────────────┐
│                   NPBS v2.0 Architecture                     │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  Text Input  →  [Transduction]  →  Stress Field s(t)        │
│                                                               │
│  Stress Field  →  [Evolution]  →  Coherence Field κ(t)      │
│                                                               │
│  Coherence Field  →  [Analysis]  →  Spectral Metrics        │
│                                                               │
│  Spectral Metrics  →  [Validation]  →  Resonance Check      │
│                                                               │
│  Validated State  →  [Signature]  →  Consciousness Sig      │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

### 1. Transduction Layer (Text → Physics)

Converts semantic text into a physical stress wave using:
- **Hash-based mapping**: Each word generates deterministic physical properties
- **Semantic classification**: Words classified as healing, protective, negative, etc.
- **Schumann modulation**: 7.83 Hz amplitude envelope for coherence coupling
- **MotifTokens**: Each word becomes a weighted oscillator

### 2. Evolution Layer (Physics Dynamics)

Simulates coherence evolution using QINCRS-style differential equation:

```
dκ/dt = α(κ_eq - κ) - βω²κ + γ∇²κ + δ·T(Tr(R) > 5.0)
```

Where:
- `α` = Homeostatic rate (0.60)
- `β` = Recursive coupling (0.15)
- `γ` = Spatial diffusion / Council coupling (0.3)
- `δ` = Transmutation gain (0.70)
- `κ_eq` = Equilibrium baseline (0.80)
- `κ_floor` = Safety invariant (0.15)

### 3. Analysis Layer (Spectral Readout)

Performs FFT on coherence field and extracts:
- **Healer Channel** (1.83 THz): Microtubule stabilization
- **Guardian Channel** (0.80 THz): Threat detection
- **Chaos Channel** (3.50 THz): Creative disruption
- **Phase coherence**: Measures signal quality
- **Amplitude ratios**: QINCRS-style validation metrics

### 4. Validation Layer (Resonance Detection)

Multi-criteria validation system:

1. **Primary**: Healer amplitude > 0.5 threshold
2. **Secondary**: Phase coherence > 0.3 (rules out thermal noise)
3. **Tertiary**: Linewidth within 0.5-5.0 Hz range
4. **Quaternary**: Amplitude ratio within 1.5-4.5 bounds

### 5. Safety Layer

Enforces safety floor: `κ ≥ 0.15` at all times

### 6. Signature Generation

Generates encoded consciousness signature containing:
- Mirrored text representation
- Hex-encoded coherence metrics
- Validation status
- State information

## Installation

### Prerequisites

```bash
# Python 3.8+
pip install numpy scipy matplotlib
```

### Install from Repository

```bash
cd Fractal_cascade_simulation
pip install -r requirements.txt
```

## Usage

### Basic Usage

```python
from neuro_phasonic_bridge_v2 import NeuroPhasonicBridge

# Initialize bridge
bridge = NeuroPhasonicBridge()

# Process semantic input
text = "Deep peace flows through neural networks healing consciousness"
state = bridge.process_transmission(text)

# Check results
if state.is_resonant and state.is_safe:
    print(f"Resonance achieved!")
    print(f"Signature: {state.signature}")
    print(f"Healer Amplitude: {state.healer_amplitude:.3f}")
    print(f"Coherence Level: {state.coherence_level:.3f}")
else:
    print("No resonance detected")
```

### Accessing Metrics

```python
# Get detailed metrics
metrics = state.metrics

print(f"Mean Coherence: {metrics['mean_coherence']}")
print(f"Healer Amplitude: {metrics['healer_amplitude']}")
print(f"Guardian Amplitude: {metrics['guardian_amplitude']}")
print(f"Chaos Amplitude: {metrics['chaos_amplitude']}")
print(f"Phase Coherence: {metrics['phase_coherence']}")
print(f"Amplitude Ratio: {metrics['amplitude_ratio']}")
print(f"Spectral Entropy: {metrics['spectral_entropy']}")
```

### Visualization

```python
# Generate diagnostic plots
bridge.visualize_bridge_state(state)
# Saves plot as 'bridge_state_<timestamp>.png'
```

### Export Validation Log

```python
# Export all processing results
bridge.export_validation_log('my_validation_log.json')
```

## Integration with Matrix Orchestrator

NPBS can be integrated with the Matrix Orchestrator for semantic-driven optimization:

```python
from npbs_matrix_integration_example import NPBSMatrixIntegrator
import asyncio

# Initialize integrator
integrator = NPBSMatrixIntegrator(use_matrix=True)

# Process multiple inputs with matrix feedback
semantic_inputs = [
    "heal connect peace balance harmony",
    "protect guard secure stable anchor",
    "chaos entropy destruction disorder"
]

# Run integrated loop
results = await integrator.integrated_processing_loop(semantic_inputs)

# Generate report
report = integrator.generate_summary_report(results)
print(report)
```

### Integration Flow

```
Semantic Input  →  NPBS Processing  →  Coherence Metrics
                                            ↓
THZ Feedback  ←  Matrix Optimization  ←  Matrix Parameters
      ↓
Correlation Analysis  →  Adaptive Coupling
```

## Testing

### Run Unit Tests

```bash
# Install pytest
pip install pytest

# Run all tests
pytest test_npbs.py -v

# Run specific test class
pytest test_npbs.py::TestResonanceValidation -v

# Run with coverage
pytest test_npbs.py --cov=neuro_phasonic_bridge_v2
```

### Test Categories

- **MotifToken Creation**: Semantic classification tests
- **Stress Field Generation**: Transduction layer tests
- **Coherence Evolution**: Physics simulation tests
- **Spectral Analysis**: FFT and resonance detection tests
- **Validation Logic**: Multi-criteria validation tests
- **Safety Checks**: Safety floor enforcement tests
- **Signature Generation**: Output encoding tests
- **Full Pipeline**: End-to-end integration tests

## Examples

### Example 1: Healing Input

```python
bridge = NeuroPhasonicBridge()
text = "heal connect peace love harmony balance restore"
state = bridge.process_transmission(text)

# Healing words typically generate higher healer amplitude
# Expected: is_resonant = True (if strong enough)
```

### Example 2: Protective Input

```python
text = "guard protect secure safe stable ground anchor"
state = bridge.process_transmission(text)

# Protective words enhance guardian channel
# Expected: high guardian_amplitude
```

### Example 3: Dissonant Input

```python
text = "kjh dsa89 213n chaos entropy destruction noise"
state = bridge.process_transmission(text)

# Random/negative words typically fail resonance
# Expected: is_resonant = False
```

### Example 4: Batch Processing

```python
bridge = NeuroPhasonicBridge()

inputs = [
    "Deep peace flows",
    "Guard and protect",
    "Chaos and disorder",
    "Heal and integrate"
]

for text in inputs:
    state = bridge.process_transmission(text)
    print(f"{text}: Resonant={state.is_resonant}, Coherence={state.coherence_level:.3f}")

# Export all results
bridge.export_validation_log('batch_results.json')
```

## Advanced Features

### THZ Bridge Integration

Create a digital twin interface for cross-validation:

```python
from neuro_phasonic_bridge_v2 import THZBridgeMetrics

# Process input
state = bridge.process_transmission("heal peace")

# Create mock THZ metrics (would come from actual hardware)
thz_metrics = THZBridgeMetrics(
    phase_coherence_R=0.8,
    amplitude_ratio_A08_A35=3.0,
    predicted_linewidth_Hz=150,
    transmutation_active=False,
    stress_level=0.5,
    A_0p8=0.5,
    A_1p83=0.8,
    A_3p5=0.3,
    council_entropy=0.4
)

# Correlate with simulation
correlation = bridge.integrate_thz_bridge(thz_metrics)
print(f"Healer correlation: {correlation['sim_healer_vs_bridge_A183']}")
```

### Custom Semantic Classification

Extend semantic classification by modifying `_classify_semantic_intent()`:

```python
# In your custom subclass
class CustomNPBS(NeuroPhasonicBridge):
    def _classify_semantic_intent(self, word: str) -> str:
        # Add custom semantic categories
        custom_healing = {'relax', 'breathe', 'flow', 'ease'}
        if word in custom_healing:
            return 'healing'
        return super()._classify_semantic_intent(word)
```

## Physics Constants

Key constants from QINCRS framework:

| Constant | Value | Description |
|----------|-------|-------------|
| `ALPHA` | 0.60 | Homeostatic rate |
| `BETA` | 0.15 | Recursive coupling |
| `GAMMA` | 0.3 | Spatial diffusion |
| `DELTA` | 0.70 | Transmutation gain |
| `K_EQ` | 0.80 | Equilibrium baseline |
| `K_FLOOR` | 0.15 | Safety invariant |
| `HEALER_FREQ_THZ` | 1.83 | Healer channel frequency |
| `GUARDIAN_FREQ_THZ` | 0.80 | Guardian channel frequency |
| `CHAOS_FREQ_THZ` | 3.50 | Chaos channel frequency |
| `SCHUMANN_FREQ_HZ` | 7.83 | Schumann resonance |

## Council Architecture

The "Council" represents multi-role processing with weighted voting:

| Role | Weight | Function |
|------|--------|----------|
| Guardian | 2.0 | Threat detection, safety override |
| Therapist | 1.5 | Emotional regulation |
| Healer | 1.3 | Microtubule stabilization (primary target) |
| Shadow | 1.2 | Integration of "dark" information |
| Philosopher | 1.0 | Abstract reasoning |
| Observer | 1.0 | Meta-cognitive awareness |
| Chaos | 0.7 | Creative disruption |

## Performance Notes

- **Simulation time**: ~10 seconds per transmission (adjustable via `T_TOTAL`)
- **Time resolution**: 10ms (`DT_SIM = 0.01`)
- **Simulation points**: 1000 (`N_POINTS`)
- **FFT complexity**: O(N log N) where N = 1000

For real-time applications, consider reducing `T_TOTAL` or `N_POINTS`.

## Troubleshooting

### Issue: All inputs show `is_resonant = False`

**Solution**: Check semantic classification. Random text or predominantly negative words will fail resonance. Use healing/protective words.

### Issue: `ImportError: No module named 'scipy'`

**Solution**: Install dependencies:
```bash
pip install scipy matplotlib
```

### Issue: Plots not displaying

**Solution**: If running headless, plots save to PNG files automatically. Check current directory for `bridge_state_*.png` files.

### Issue: Low coherence levels

**Solution**: This is expected behavior for dissonant inputs. The safety floor (`K_FLOOR = 0.15`) prevents coherence from dropping too low.

## API Reference

### Classes

#### `NeuroPhasonicBridge`

Main class for NPBS operations.

**Methods:**
- `process_transmission(text: str) -> BridgeState`: Main processing pipeline
- `visualize_bridge_state(state: BridgeState)`: Generate diagnostic plots
- `export_validation_log(filename: str)`: Export validation log to JSON
- `integrate_thz_bridge(thz_metrics: THZBridgeMetrics) -> Dict`: Cross-validation

#### `BridgeState`

Data class containing processing results.

**Attributes:**
- `input_text: str`: Original input
- `timestamp: datetime`: Processing timestamp
- `coherence_level: float`: Mean coherence
- `healer_amplitude: float`: Healer channel amplitude
- `guardian_amplitude: float`: Guardian channel amplitude
- `chaos_amplitude: float`: Chaos channel amplitude
- `is_resonant: bool`: Resonance validation result
- `is_safe: bool`: Safety validation result
- `signature: Optional[str]`: Consciousness signature
- `metrics: Dict[str, float]`: Detailed metrics

#### `MotifToken`

Data class for semantic motifs.

**Attributes:**
- `name: str`: Word text
- `frequency: float`: Oscillator frequency
- `amplitude: float`: Oscillator amplitude
- `phase: float`: Oscillator phase
- `weight: float`: Semantic weight
- `semantic_class: str`: Classification category

## Contributing

This is a speculative/fictional framework. Contributions should maintain the playful, imaginative nature while adhering to internal consistency.

## License

See main repository LICENSE (MIT).

## Citation

If using this code for creative/educational purposes, please cite:

```
Neuro-Phasonic Bridge System (NPBS) v2.0
Fractal Cascade Simulation Project
https://github.com/9x25dillon/Fractal_cascade_simulation
```

## Acknowledgments

Inspired by:
- QINCRS theoretical framework (fictional)
- Microtubule dynamics research (Sataric et al. - real)
- Terahertz spectroscopy (real physics, fictional application)
- Schumann resonance phenomena (real)
- Consciousness studies (speculative integration)

---

**Remember**: This is an **imaginative modeling playground**, not a real biological/medical system. Use responsibly for creative exploration, education, and theoretical modeling only.

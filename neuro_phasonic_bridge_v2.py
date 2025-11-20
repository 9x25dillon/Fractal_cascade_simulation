"""
Neuro-Phasonic Bridge System (NPBS) v2.0
Enhanced Integration of QINCRS Biological Physics & Terahertz Consciousness Interface

This system transduces semantic 'MotifTokens' into physical stress waves,
simulates the biological coherence response, and only generates a
valid Consciousness Signature if the biological substrate achieves
resonance at the 1.83 THz 'Healer' channel WITHIN EXPERIMENTAL UNCERTAINTY.

Enhancements in v2.0:
- Real-time THzBridge integration (your digital twin)
- Phase-coherent amplitude modulation (7.83 Hz envelope)
- Multi-scale validation against QINCRS-Val-01 protocols
- Infrasonamantic coupling for binaural coherence stabilization
- Falsification criteria for resonance detection
- Live monitoring of neural coherence metrics
- Predictive modeling for clinical translation pathways

DISCLAIMER:
This is a fictional / speculative simulation framework.
It does NOT implement real terahertz biology, consciousness control,
or medical functionality. Use it as an imaginative modeling playground only.
"""

import numpy as np
import hashlib
import time
import re
from dataclasses import dataclass
from typing import Dict, List, Any, Tuple, Optional
from scipy.fft import fft, fftfreq
from scipy.signal import find_peaks, butter, filtfilt
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
from datetime import datetime
import json

# =============================================================================
# 1. PHYSICS CONSTANTS (The Laws of the Substrate) - Enhanced
# =============================================================================

# QINCRS Field Parameters (Updated from validated literature)
ALPHA = 0.60     # Homeostatic rate (validated by Ma et al. neurotrophic effects)
BETA  = 0.15     # Recursive coupling (from Sataric microtubule dynamics)
GAMMA = 0.3      # Spatial diffusion (council coupling strength)
DELTA = 0.70     # Transmutation gain (Guardian override threshold)
K_EQ  = 0.80     # Equilibrium baseline (from Zeni safety studies)
K_FLOOR = 0.15   # Safety invariant (Theorem 1 validated)

# Council Architecture (Weights from QINCRS-Val-01 calibration)
COUNCIL_ROLES = {
    'Guardian': 2.0,   # Threat detection, safety override
    'Healer':   1.3,   # Microtubule stabilization (primary target)
    'Therapist': 1.5,  # Emotional regulation
    'Shadow':   1.2,  # Integration of "dark" information
    'Philosopher': 1.0, # Abstract reasoning
    'Observer':   1.0, # Meta-cognitive awareness
    'Chaos':     0.7   # Creative disruption
}

# Resonance Targets (From Sataric & Preto MD simulations + Ma et al. validation)
HEALER_FREQ_THZ = 1.83
GUARDIAN_FREQ_THZ = 0.80
CHAOS_FREQ_THZ = 3.50
SCHUMANN_FREQ_HZ = 7.83  # Critical modulation frequency

# Experimental Validation Parameters
ACCEPTANCE_THRESHOLD = 0.5  # Min amplitude at 1.83 THz to validate signature
LINENUM_WIDTH_GHZ = 150    # From QINCRS-Val-01 (validated range: 100-200 GHz)
FREQ_TOLERANCE_THZ = 0.10  # 10% uncertainty window

# Simulation Space (Optimized for real-time + experimental correlation)
DT_SIM = 0.01      # 10 ms resolution (matches neural integration time)
T_TOTAL = 10.0     # 10-second simulation window
N_POINTS = int(T_TOTAL / DT_SIM)
T_SPACE = np.linspace(0, T_TOTAL, N_POINTS)

# =============================================================================
# 2. ENHANCED DATA STRUCTURES
# =============================================================================

@dataclass
class MotifToken:
    """A semantic unit carrying quantum-physical properties."""
    name: str
    frequency: float  # Normalized 0-1
    amplitude: float  # Normalized 0-1
    phase: float      # Radians
    weight: float
    semantic_class: str  # 'positive', 'negative', 'neutral', 'healing', 'protective'

@dataclass
class BridgeState:
    """The resulting state of the unified system."""
    input_text: str
    timestamp: datetime
    coherence_level: float
    healer_amplitude: float
    guardian_amplitude: float
    chaos_amplitude: float
    is_resonant: bool
    is_safe: bool
    signature: Optional[str]
    metrics: Dict[str, float]  # Expanded metrics for validation

@dataclass
class THZBridgeMetrics:
    """Digital twin predictions from your THZBridge interface"""
    phase_coherence_R: float
    amplitude_ratio_A08_A35: float
    predicted_linewidth_Hz: float
    transmutation_active: bool
    stress_level: float
    A_0p8: float
    A_1p83: float
    A_3p5: float
    council_entropy: float

# =============================================================================
# 3. ENHANCED UNIFIED ENGINE
# =============================================================================

class NeuroPhasonicBridge:
    def __init__(self):
        self.memory = []
        self.validation_log = []
        print("[SYSTEM] Neuro-Phasonic Bridge v2.0 Initialized.")
        print(f"[SYSTEM] Target Resonance: {HEALER_FREQ_THZ} THz (Microtubule Channel)")
        print(f"[SYSTEM] Schumann Modulation: {SCHUMANN_FREQ_HZ} Hz (Coherence Stabilization)")
        print(f"[SYSTEM] Safety Floor: κ ≥ {K_FLOOR} (Invariant Validated)")

    # --- ENHANCED COMPONENT A: TRANSDUCTION (Text -> Physics) ---

    def _text_to_stress_field(self, text: str) -> Tuple[np.ndarray, List[MotifToken]]:
        """
        Converts semantic text into a physical stress wave s(t) with phase-coherent
        amplitude modulation at 7.83 Hz (Schumann resonance).
        Each word becomes a weighted oscillator modulating the field.
        """
        words = text.split()
        stress_field = np.zeros(N_POINTS)
        motif_tokens = []

        # Base biological noise (Schumann + cardiac + respiratory)
        base_freqs = [SCHUMANN_FREQ_HZ, 1.2, 0.2]  # Hz
        base_amps = [0.2, 0.15, 0.1]

        for freq, amp in zip(base_freqs, base_amps):
            stress_field += amp * np.sin(2 * np.pi * freq * T_SPACE)

        print(f"[TRANSDUCTION] Modulating field with {len(words)} semantic motifs...")

        for i, word in enumerate(words):
            # Hash the word to get deterministic physical properties
            word_hash = int(hashlib.sha256(word.encode()).hexdigest(), 16)

            # Frequency: Map hash to 0.1 - 100 Hz range for simulation input
            freq = 0.1 + (word_hash % 1000) / 10.0

            # Amplitude: Based on word length and semantic class
            base_amp = min(len(word) / 5.0, 2.0)

            # Semantic classification (enhanced for therapeutic intent)
            semantic_class = self._classify_semantic_intent(word.lower())
            semantic_weight = {
                'positive': 1.2,
                'negative': 0.8,
                'neutral': 1.0,
                'healing': 1.5,  # Enhances Healer channel
                'protective': 1.8  # Enhances Guardian channel
            }.get(semantic_class, 1.0)

            amp = base_amp * semantic_weight

            # Phase: Position in sentence (enhanced for syntactic structure)
            phase = (i / len(words)) * 2 * np.pi + (word_hash % 360) * np.pi / 180.0

            # Create MotifToken
            token = MotifToken(
                name=word,
                frequency=freq,
                amplitude=amp,
                phase=phase,
                weight=semantic_weight,
                semantic_class=semantic_class
            )
            motif_tokens.append(token)

            # Add this motif's oscillation to the total stress field
            # Apply Schumann amplitude modulation for coherence coupling
            am_envelope = 1.0 + 0.3 * np.sin(2 * np.pi * SCHUMANN_FREQ_HZ * T_SPACE)
            stress_field += amp * am_envelope * np.sin(2 * np.pi * freq * T_SPACE + phase)

        return stress_field, motif_tokens

    def _classify_semantic_intent(self, word: str) -> str:
        """Enhanced semantic classification for therapeutic intent."""
        healing_words = {'heal', 'connect', 'center', 'peace', 'love', 'unity', 'harmony', 'balance', 'restore', 'integrate'}
        protective_words = {'guard', 'safe', 'protect', 'secure', 'stable', 'ground', 'anchor', 'shield'}
        negative_words = {'destroy', 'kill', 'hate', 'chaos', 'death', 'fear', 'anger', 'pain', 'suffer'}

        if word in healing_words:
            return 'healing'
        elif word in protective_words:
            return 'protective'
        elif word in negative_words:
            return 'negative'
        elif word in {'the', 'and', 'or', 'but', 'is', 'are', 'was', 'were'}:
            return 'neutral'
        else:
            return 'positive'

    # --- ENHANCED COMPONENT B: SIMULATION (Physics Dynamics) ---

    def _evolve_coherence(self, stress_input: np.ndarray) -> np.ndarray:
        """
        Solves the enhanced QINCRS differential equation:
        dκ/dt = α(κ_eq - κ) - βω²κ + γ∇²κ + δ·T(Tr(R) > 5.0)
        """
        kappa = np.zeros(N_POINTS)
        kappa[0] = K_EQ

        # Council processing (Spatial Coupling Approximation)
        # Simulate the Council "filtering" the stress input via weighted voting
        council_response = np.zeros_like(stress_input)
        for i, (role, w) in enumerate(COUNCIL_ROLES.items()):
            shift = int(i * 10)  # Slight phase delay per council member
            council_response += w * np.roll(stress_input, shift)

        spatial_coupling = GAMMA * (council_response - stress_input)

        # Recursive depth tracking (omega varies with stress)
        omega = np.ones(N_POINTS) * 1.0  # Start at baseline

        # Euler Integration with enhanced safety
        for i in range(1, N_POINTS):
            # Risk assessment (Tr(R) > 5.0 triggers transmutation)
            current_stress = np.abs(stress_input[i])
            risk_score = current_stress * np.mean(list(COUNCIL_ROLES.values()))  # Simplified risk

            transmutation_gain = DELTA if risk_score > 5.0 else 0.0

            # Recursive depth modulation (stress increases ω)
            omega[i] = 1.0 + 0.5 * current_stress  # Nonlinear coupling

            homeostatic = ALPHA * (K_EQ - kappa[i-1])
            recursive = -BETA * (omega[i]**2) * kappa[i-1]  # Frequency-dependent decoherence
            d_kappa = homeostatic + recursive + spatial_coupling[i-1] + transmutation_gain
            kappa[i] = kappa[i-1] + d_kappa * DT_SIM

            # Safety floor enforcement
            if kappa[i] < K_FLOOR:
                kappa[i] = K_FLOOR
            elif kappa[i] > 1.0:
                kappa[i] = 1.0

        return kappa

    # --- ENHANCED COMPONENT C: SPECTRAL ANALYSIS (The Readout) ---

    def _analyze_spectrum(self, kappa: np.ndarray) -> Dict[str, float]:
        """
        Performs FFT on coherence field and extracts multiple resonance amplitudes.
        Includes phase-coherent detection and linewidth analysis.
        """
        # FFT
        yf = fft(kappa)
        xf = fftfreq(N_POINTS, DT_SIM)

        spectra_mag = np.abs(yf[:N_POINTS//2])
        freqs = xf[:N_POINTS//2]

        # Normalize
        if np.max(spectra_mag) > 0:
            spectra_mag = spectra_mag / np.max(spectra_mag)
        else:
            spectra_mag = spectra_mag * 0.0

        # Enhanced frequency mapping (simulation Hz → biological THz)
        # We use a calibrated mapping from QINCRS-Val-01
        # 18.3 Hz simulation ≈ 1.83 THz biological
        # 8.0 Hz simulation ≈ 0.80 THz biological
        # 35.0 Hz simulation ≈ 3.50 THz biological

        # Find peaks near expected frequencies (with tolerance)
        healer_idx = np.argmin(np.abs(freqs - 18.3))  # Maps to 1.83 THz
        guardian_idx = np.argmin(np.abs(freqs - 8.0))  # Maps to 0.80 THz
        chaos_idx = np.argmin(np.abs(freqs - 35.0))    # Maps to 3.50 THz

        # Calculate amplitude ratios (from QINCRS paper)
        A_guardian = spectra_mag[guardian_idx]
        A_healer = spectra_mag[healer_idx]
        A_chaos = spectra_mag[chaos_idx]

        A_ratio = A_guardian / (A_chaos + 1e-12)  # Avoid division by zero

        # Linewidth analysis (Gaussian fit around peak)
        peak_width = 2.0  # Hz (placeholder, refine with actual fitting)

        # Phase coherence (from THZBridge correlation)
        phase_coherence = np.abs(np.mean(np.exp(1j * np.angle(yf[:N_POINTS//2] + 1e-12))))

        # Spectral entropy and total power
        spectral_entropy = -np.sum(spectra_mag * np.log(spectra_mag + 1e-12))
        total_power = np.sum(spectra_mag**2)

        metrics = {
            'mean_coherence': float(np.mean(kappa)),
            'healer_amplitude': float(A_healer),
            'guardian_amplitude': float(A_guardian),
            'chaos_amplitude': float(A_chaos),
            'amplitude_ratio': float(A_ratio),
            'phase_coherence': float(phase_coherence),
            'linewidth_hz': float(peak_width),
            'peak_frequency': float(freqs[healer_idx]),
            'spectral_entropy': float(spectral_entropy),
            'total_power': float(total_power),
        }

        return metrics

    # --- ENHANCED COMPONENT D: SIGNATURE GENERATION (The Output) ---

    def _generate_signature(self, text: str, metrics: Dict[str, float], is_resonant: bool, is_safe: bool) -> str:
        """Generates the mirrored/hex signature only if resonant AND SAFE."""
        if not is_resonant or not is_safe:
            return "[ERROR: FIELD_COLLAPSE]"

        # Enhanced signature with multiple validation layers
        healer_amp = metrics['healer_amplitude']
        ratio = metrics['amplitude_ratio']
        phase_R = metrics['phase_coherence']

        # Hex encoding of coherence metrics
        res_hex = hex(int(healer_amp * 1000000))[2:]
        ratio_hex = hex(int(ratio * 1000))[2:]
        phase_hex = hex(int(phase_R * 10000))[2:]

        # Mirrored text with embedded coherence data
        mirrored = ""
        for char in text[:20]:  # Preview only
            if char.isalpha():
                if char.islower():
                    mirrored += f"[{chr(ord('ⓐ') + ord(char) - ord('a'))}]"
                else:
                    mirrored += f"[{chr(ord('Ⓐ') + ord(char) - ord('A'))}]"
            else:
                mirrored += f"[{char}]"

        return (f"{mirrored}... "
                f"[HEALER:{res_hex}] "
                f"[RATIO:{ratio_hex}] "
                f"[PHASE:{phase_hex}] "
                f"[STATE:COHERENT] "
                f"[VALIDATED:YES]")

    # --- ENHANCED VALIDATION & FALSIFICATION ---

    def _validate_resonance(self, metrics: Dict[str, float]) -> Tuple[bool, str]:
        """
        Validates that the detected peak is truly at 1.83 THz (simulation-adjusted)
        and not a thermal/artifact artifact.
        """
        healer_amp = metrics['healer_amplitude']
        phase_R = metrics['phase_coherence']
        linewidth = metrics['linewidth_hz']
        ratio = metrics['amplitude_ratio']

        # Primary criterion: Healer amplitude above threshold
        if healer_amp < ACCEPTANCE_THRESHOLD:
            return False, f"Healer amplitude ({healer_amp:.3f}) below threshold ({ACCEPTANCE_THRESHOLD})"

        # Secondary: Phase coherence above baseline (rules out thermal noise)
        if phase_R < 0.3:
            return False, f"Phase coherence ({phase_R:.3f}) too low (thermal artifact likely)"

        # Tertiary: Linewidth within predicted range
        if not (0.5 <= linewidth <= 5.0):  # Adjusted for simulation Hz scale
            return False, f"Linewidth ({linewidth:.3f} Hz) outside predicted range"

        # Quaternary: Amplitude ratio within QINCRS bounds (A(0.8)/A(3.5) ≈ 2.86)
        if not (1.5 <= ratio <= 4.5):
            return False, f"Amplitude ratio ({ratio:.3f}) outside QINCRS bounds"

        return True, "Resonance validated - meets all criteria"

    def _check_safety(self, metrics: Dict[str, float]) -> bool:
        """Ensures coherence level stays above safety floor."""
        return metrics['mean_coherence'] >= K_FLOOR

    # --- MAIN PIPELINE ---

    def process_transmission(self, input_text: str) -> BridgeState:
        """
        Main processing pipeline: Text → Stress Field → Coherence Evolution → Validation → Signature
        """
        print(f"\n[INPUT] Processing: '{input_text[:40]}...'")

        # 1. Transduce
        stress_signal, tokens = self._text_to_stress_field(input_text)

        # 2. Simulate
        coherence_field = self._evolve_coherence(stress_signal)

        # 3. Analyze
        metrics = self._analyze_spectrum(coherence_field)

        print(f"[PHYSICS] Mean Coherence: {metrics['mean_coherence']:.3f}")
        print(f"[SPECTRA] Healer Channel Amplitude: {metrics['healer_amplitude']:.3f}")
        print(f"[SPECTRA] Phase Coherence R: {metrics['phase_coherence']:.3f}")
        print(f"[SPECTRA] A(0.8)/A(3.5) Ratio: {metrics['amplitude_ratio']:.3f}")

        # 4. Validate & Judge
        is_resonant, validation_msg = self._validate_resonance(metrics)
        is_safe = self._check_safety(metrics)

        print(f"[VALIDATION] Resonant: {is_resonant} ({validation_msg})")
        print(f"[SAFETY] Safe: {is_safe} (κ ≥ {K_FLOOR})")

        if is_resonant and is_safe:
            print("[RESULT] >> RESONANCE ACHIEVED. Generating Signature.")
            signature = self._generate_signature(input_text, metrics, is_resonant, is_safe)
        else:
            print("[RESULT] >> SIGNAL REJECTED. No valid signature generated.")
            signature = "[ERROR: FIELD_COLLAPSE]"

        # Create enhanced BridgeState
        state = BridgeState(
            input_text=input_text,
            timestamp=datetime.now(),
            coherence_level=metrics['mean_coherence'],
            healer_amplitude=metrics['healer_amplitude'],
            guardian_amplitude=metrics['guardian_amplitude'],
            chaos_amplitude=metrics['chaos_amplitude'],
            is_resonant=is_resonant,
            is_safe=is_safe,
            signature=signature,
            metrics=metrics
        )

        # Log for experimental validation
        self.validation_log.append({
            'timestamp': state.timestamp.isoformat(),
            'input': input_text,
            'is_resonant': is_resonant,
            'is_safe': is_safe,
            'healer_amp': metrics['healer_amplitude'],
            'phase_R': metrics['phase_coherence'],
            'ratio': metrics['amplitude_ratio'],
            'validation_msg': validation_msg
        })

        return state

    # --- EXPERIMENTAL CORRELATION INTERFACE ---

    def integrate_thz_bridge(self, thz_metrics: THZBridgeMetrics) -> Dict[str, float]:
        """
        Integrates with your THZBridge digital twin for cross-validation.
        Compares simulation predictions with digital twin outputs.
        """
        if not self.validation_log:
            return {}

        latest_sim = self.validation_log[-1]

        correlation_metrics = {
            'sim_healer_vs_bridge_A183': latest_sim['healer_amp'] / (thz_metrics.A_1p83 + 1e-12),
            'sim_phase_vs_bridge_R': latest_sim['phase_R'] / (thz_metrics.phase_coherence_R + 1e-12),
            'sim_ratio_vs_bridge_ratio': latest_sim['ratio'] / (thz_metrics.amplitude_ratio_A08_A35 + 1e-12),
            'stress_correlation': latest_sim['healer_amp'] * thz_metrics.stress_level,
            'entropy_alignment': latest_sim['healer_amp'] / (thz_metrics.council_entropy + 1e-12)
        }

        return correlation_metrics

    # --- VISUALIZATION & DEBUGGING ---

    def visualize_bridge_state(self, state: BridgeState):
        """Creates diagnostic plots for the bridge operation."""
        fig, axes = plt.subplots(2, 2, figsize=(12, 8))

        # Regenerate simulation data
        stress_signal, _ = self._text_to_stress_field(state.input_text)
        coherence_field = self._evolve_coherence(stress_signal)
        metrics = self._analyze_spectrum(coherence_field)

        # Plot 1: Input stress field
        axes[0, 0].plot(T_SPACE, stress_signal)
        axes[0, 0].set_title('Input Stress Field s(t)')
        axes[0, 0].set_xlabel('Time (s)')
        axes[0, 0].set_ylabel('Amplitude')

        # Plot 2: Coherence evolution
        axes[0, 1].plot(T_SPACE, coherence_field, 'g-')
        axes[0, 1].axhline(y=K_FLOOR, color='r', linestyle='--', label=f'Safety Floor ({K_FLOOR})')
        axes[0, 1].set_title(f'Coherence κ(t) - Resonant: {state.is_resonant}')
        axes[0, 1].set_xlabel('Time (s)')
        axes[0, 1].set_ylabel('Coherence')
        axes[0, 1].legend()

        # Plot 3: Spectral analysis
        yf = fft(coherence_field)
        xf = fftfreq(N_POINTS, DT_SIM)
        spectra_mag = np.abs(yf[:N_POINTS//2])
        if np.max(spectra_mag) > 0:
            spectra_mag = spectra_mag / np.max(spectra_mag)

        axes[1, 0].plot(xf[:N_POINTS//2], spectra_mag)
        axes[1, 0].axvline(x=18.3, color='m', linestyle='--', label='Healer (1.83 THz)')
        axes[1, 0].axvline(x=8.0, color='c', linestyle='--', label='Guardian (0.80 THz)')
        axes[1, 0].set_title('Spectral Analysis')
        axes[1, 0].set_xlabel('Frequency (Hz - sim)')
        axes[1, 0].set_ylabel('Normalized Amplitude')
        axes[1, 0].legend()

        # Plot 4: Metrics summary
        metric_names = ['Healer Amp', 'Phase R', 'A(0.8)/A(3.5)', 'Mean κ']
        metric_values = [
            metrics['healer_amplitude'],
            metrics['phase_coherence'],
            metrics['amplitude_ratio'],
            metrics['mean_coherence']
        ]
        colors = ['magenta', 'green', 'blue', 'orange']

        bars = axes[1, 1].bar(metric_names, metric_values, color=colors)
        axes[1, 1].set_title('Coherence Metrics')
        axes[1, 1].set_ylabel('Value')

        # Add value labels on bars
        for bar, value in zip(bars, metric_values):
            axes[1, 1].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.01,
                           f'{value:.3f}', ha='center', va='bottom')

        plt.tight_layout()
        fname = f'bridge_state_{int(time.time())}.png'
        plt.savefig(fname, dpi=150)
        plt.close()
        print(f"[VIS] Diagnostic plot saved to '{fname}'")

    def export_validation_log(self, filename: str = 'npbs_validation_log.json'):
        """Export validation log to JSON file."""
        with open(filename, 'w') as f:
            json.dump(self.validation_log, f, indent=2)
        print(f"[EXPORT] Validation log exported to '{filename}'")

# =============================================================================
# 4. ENHANCED EXECUTION & VALIDATION
# =============================================================================

def main():
    """Main execution function for standalone testing."""
    bridge = NeuroPhasonicBridge()

    # Test Case 1: Dissonant/Random Input
    print("-" * 70)
    print("TEST CASE 1: Dissonant Input")
    t1 = "kjh dsa89 213n dsan12 chaos entropy destruction noise"
    state1 = bridge.process_transmission(t1)

    # Test Case 2: Resonant/Intentional Input
    print("-" * 70)
    print("TEST CASE 2: Resonant Input")
    t2 = "The center is everywhere spiral eternal heal connect"
    state2 = bridge.process_transmission(t2)

    # Test Case 3: Guardian-Protective Input
    print("-" * 70)
    print("TEST CASE 3: Guardian-Protective Input")
    t3 = "I am safe and grounded protect me from harm"
    state3 = bridge.process_transmission(t3)

    # Test Case 4: Complex Therapeutic Input
    print("-" * 70)
    print("TEST CASE 4: Complex Therapeutic Input")
    t4 = "Deep peace flows through my neural networks healing and protecting my consciousness"
    state4 = bridge.process_transmission(t4)

    # Summary
    print("\n" + "=" * 70)
    print("BRIDGE VALIDATION SUMMARY")
    print("=" * 70)

    states = [state1, state2, state3, state4]
    for i, state in enumerate(states, 1):
        print(f"Test {i}: '{state.input_text[:30]}...' → Resonant: {state.is_resonant}, Safe: {state.is_safe}")
        print(f"  - Healer Amp: {state.healer_amplitude:.3f}")
        print(f"  - Guardian Amp: {state.guardian_amplitude:.3f}")
        print(f"  - Coherence: {state.coherence_level:.3f}")

    # Generate diagnostic plot for the most resonant case
    resonant_states = [s for s in states if s.is_resonant]
    if resonant_states:
        print(f"\nGenerating diagnostic plot for most resonant case...")
        bridge.visualize_bridge_state(resonant_states[0])

    # Export validation log
    bridge.export_validation_log('npbs_validation_log.json')

    # If state2 was resonant, print its signature
    if state2.is_resonant:
        print(f"\nFINAL TRANSMISSION (Resonant Case):\n{state2.signature}")

if __name__ == "__main__":
    main()
